#!/usr/bin/env python3
"""Mechanical consistency check for the prompt and the checklist.

Run it after every edit to either file:

    python3 scripts/check-kit.py

It checks the things that broke during earlier reviews: duplicate or missing row
IDs, malformed table rows, section lists that disagree, references that point at
nothing, stray dashes, and paths that only work on one machine. Exit code 0 means
every check passed; 1 means at least one failed. It cannot judge whether a rule is
right, only whether the two files still agree with each other.
"""
import argparse
import itertools
import json
import subprocess
from release_gate import catalogue, specifications, priority_policy, TIERS
from release_queue import work_metadata
import pathlib
import re
import sys
from collections import Counter

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parent.parent)
ROOT = parser.parse_args().root.resolve()
PROMPT = ROOT / "prompt" / "PROMPT_awwwards_clone_swap_v6.md"
CHECKLIST = ROOT / "checklist" / "PRODUCTION_CHECKLIST_clone_swap.md"

ROW = re.compile(r"\| ([A-Z0-9]+-\d+)([A-Z-]*) \|")
results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))


pr = PROMPT.read_text()
ck = CHECKLIST.read_text()

# ---------- checklist rows ----------
rows = [l for l in ck.split("\n") if re.match(r"\| [A-Z0-9]+-\d+", l)]
ids = [ROW.match(l).group(1) for l in rows if ROW.match(l)]
try:
    parsed_rows = catalogue(CHECKLIST)
    check("checklist: strict row grammar and nonempty catalogue", True)
except ValueError as error:
    parsed_rows = {}
    check("checklist: strict row grammar and nonempty catalogue", False, str(error))
manifest = ROOT / "checklist/row-ids.txt"
expected_ids = manifest.read_text().splitlines() if manifest.exists() else []
check("checklist: IDs exactly match stable inventory", bool(expected_ids) and ids == expected_ids)
readme = (ROOT / "README.md").read_text()
check("README row count matches catalogue", f"({len(ids)} rows, 18 sections)" in readme)
dups = [i for i, n in Counter(ids).items() if n > 1]
check("checklist: no duplicate row IDs", not dups, str(dups))


def cells(line):
    return re.sub(r"`[^`]*`", "X", line).count("|")


bad_cells = [l[:16] for l in rows if cells(l) != 6]
check("checklist: every row has 5 cells", not bad_cells, str(bad_cells[:5]))
bad_class = [l[:16] for l in rows if not re.search(r"\| (G|R|C)(-L|-O)? \| (Diamond|Gold|Silver|Bronze) \|$", l)]
check("checklist: every row ends in a valid class (G, R or C, optional -L or -O)", not bad_class, str(bad_class[:5]))
try:
    tier_register = json.loads((ROOT / 'checklist/tiers.json').read_text())
    tier_rows = tier_register['rows']
    specs = specifications(CHECKLIST)
    check('tiers: complete ordered inventory, valid metadata and matching priorities',
          tier_register.get('policy_version') == priority_policy(ck) == 'risk-v2' and
          [r['id'] for r in tier_rows] == ids and
          all(r['tier'] in {tier.lower() for tier in TIERS} and specs[r['id']][1] == r['tier'].title()
              and r['rationale'].strip() and r['group'].strip()
              and r['timing'] in {'prelaunch', 'cutover', 'postlaunch', 'recurring'} for r in tier_rows))
except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
    check('tiers: complete ordered inventory, valid metadata and matching priorities', False, str(error))

try:
    _, work_rows = work_metadata(CHECKLIST, ROOT/'checklist/tiers.json', ROOT/'checklist/bundles.json')
    check('work bundles: every stable ID mapped without changing priorities', list(work_rows) == ids)
except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
    check('work bundles: every stable ID mapped without changing priorities', False, str(error))

unsorted = []
for sec, grp in itertools.groupby(ids, key=lambda i: i.split("-")[0]):
    nums = [int(x.split("-")[1]) for x in grp]
    if nums != sorted(nums):
        unsorted.append(sec)
check("checklist: IDs sorted within each section", not unsorted, str(unsorted))

# ---------- cross references ----------
idset = set(ids)
prefixes = ("SHA-", "UTF-", "TLS-", "ISO-", "WCAG-", "RFC-", "HTTP-", "X-", "CC-", "ES-")
cited = set(re.findall(r"\b([A-Z][A-Z0-9]{1,4}-\d{2})\b", ck + pr))
missing = [c for c in sorted(cited) if c not in idset and not c.startswith(prefixes)]
check("every row ID cited in either file exists", not missing, str(missing))

# The reviewed source set is fixed to the user's supplied clips; JSON is provenance,
# not a transcript or release proof. Validate errors as failed checks, never crash.
source_path = ROOT / "docs/reviews/instagram-addon-2026-10-03/lessons.json"
try:
    source_record = json.loads(source_path.read_text())
    sources = source_record["sources"]
    supplied = {"Dc-Ye_1zpcr", "DcKiRe3TvdB", "Dd36v-8s8O2", "Dd6qP9CRxax", "Dd35bp-q_Cv", "DduSPm2B3Lq", "DdsrRJpywBe", "Dd3ZGNeSvK5", "DdP1ySxAsxT"}
    check("video sources: exactly nine supplied IDs and matching URLs",
          len(sources) == 9 and {x["id"] for x in sources} == supplied and
          all(x["url"] == f"https://www.instagram.com/p/{x['id']}/" for x in sources))
    check("video sources: every mapped row exists",
          all(x["rows"] and all(row in idset for row in x["rows"]) for x in sources))
    check("video sources: sampled review scope and artifact identities",
          source_record["schema_version"] == 1 and bool(source_record["review_scope"]) and
          all(x["status"] == "REVIEWED_SAMPLED_VISUAL_AND_POST_TEXT" and
              x["audio_transcribed"] is False and x["frames"] and
              re.fullmatch(r"[a-f0-9]{64}", x["video_sha256"]) and
              re.fullmatch(r"[a-f0-9]{64}", x["post_metadata_sha256"]) and
              all(re.fullmatch(r"[a-f0-9]{64}", f["sha256"]) for f in x["frames"])
              for x in sources))
except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
    check("video sources: readable provenance record", False, str(error))
addon_path = ROOT / "checklist/VIDEO_LESSONS_ADDON.md"
addon = addon_path.read_text() if addon_path.exists() else ""
addon_refs = set(re.findall(r"\b([A-Z][A-Z0-9]{1,4}-\d{2})\b", addon))
check("video add-on: cited rows exist", addon_refs <= idset, str(sorted(addon_refs-idset)))

# The second batch includes a carousel. Require all supplied sources while
# keeping media kinds and their identity/coverage limits explicit.
try:
    batch = json.loads((ROOT / "docs/reviews/instagram-batch2-2026-10-03/lessons.json").read_text())
    entries = batch["sources"]
    expected = {"Db6mbRuyiik", "DbD6WQzDIk4", "Dd53_9IsfZ-", "DdS5oHtPvcA", "DcJ4skky39X", "DbdQQN3smX8", "Da1AU0nhCbI"}
    check("second batch: all seven source IDs and URLs",
          len(entries) == 7 and {x["id"] for x in entries} == expected and
          all(x["url"] == f"https://www.instagram.com/p/{x['id']}/" for x in entries))
    check("second batch: all mapped rows exist", all(x["rows"] and set(x["rows"]) <= idset for x in entries))
    check("second batch: media kinds and reviewed artifact identities",
          batch["schema_version"] == 1 and bool(batch["review_scope"]) and
          all(x["media_kind"] == ("carousel" if x["id"] == "DbD6WQzDIk4" else "video") and
              x["status"] == ("REVIEWED_CAROUSEL_AND_POST_TEXT" if x["media_kind"] == "carousel" else "REVIEWED_SAMPLED_VISUAL_AND_POST_TEXT") and
              x["audio_transcribed"] is False and x["artifacts"] and
              (x["media_kind"] != "carousel" or len(x["artifacts"]) == 9) and
              re.fullmatch(r"[a-f0-9]{64}", x["media_sha256"]) and
              re.fullmatch(r"[a-f0-9]{64}", x["post_metadata_sha256"]) and
              all(re.fullmatch(r"[a-f0-9]{64}", f["sha256"]) for f in x["artifacts"])
              for x in entries))
except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
    check("second batch: readable source record", False, str(error))
second_addon_path = ROOT / "checklist/VIDEO_LESSONS_BATCH2.md"
second_addon = second_addon_path.read_text() if second_addon_path.exists() else ""
second_refs = set(re.findall(r"\b([A-Z][A-Z0-9]{1,4}-\d{2})\b", second_addon))
check("second add-on: cited rows exist", second_refs <= idset, str(sorted(second_refs-idset)))

# sections: prompt list equals the checklist's headings
ck_sections = []
for h in re.findall(r"^## ([A-Za-z0-9 ]+?):", ck, re.M):
    ck_sections += [x.strip() for x in h.split(" and ")]
m = re.search(r"checklist has (\w+) sections \(([^)]*)\)", pr)
pr_sections = [x.strip() for x in m.group(2).split(",")] if m else []
check("prompt section list equals the checklist's headings", pr_sections == ck_sections, f"prompt={pr_sections} checklist={ck_sections}")
words = {"seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}
check("prompt section count word matches the list", m and words.get(m.group(1)) == len(pr_sections), m.group(1) if m else "not found")

# prompt section numbers 1..8 and the references to them
heads = re.findall(r"^## (\d+)\.", pr, re.M)
check("prompt has numbered sections 1 to 8", heads == [str(i) for i in range(1, 9)], str(heads))
refs = set(re.findall(r"(?<!contract )§(\d)\b", pr)) | set(re.findall(r"§(\d)\b", ck))
check("every § reference points at a section 1 to 8", all(1 <= int(r) <= 8 for r in refs), str(sorted(refs)))

def section(text, start, end=None):
    if start not in text or (end and end not in text):
        check(f"required section exists: {start}", False)
        return ""
    return text[text.index(start):text.index(end) if end else len(text)]


fin = section(pr, "## Finish")
gates = re.findall(r"^(\d+)\. ", fin, re.M)
check("Finish lists gates 1 to 15 in order", gates == [str(i) for i in range(1, 16)], str(gates))
check("Finish says 'all fifteen'", "all fifteen" in fin)

gr = section(pr, "## Ground rules", "## Methodology")
check("prompt has ground rules 1 to 10", re.findall(r"^(\d+)\. \*\*", gr, re.M) == [str(i) for i in range(1, 11)])
rules_block = section(ck, "**Rules of application**", "## SPD")
ck_rules = re.findall(r"^(\d+)\. ", rules_block, re.M)
check("checklist has rules of application 1 to 10", ck_rules == [str(i) for i in range(1, 11)], str(ck_rules))
rule_refs = {int(r) for r in re.findall(r"\brules? (\d+)\b", ck)}
check("checklist 'rule N' references exist", all(1 <= r <= 10 for r in rule_refs), str(sorted(rule_refs)))

# ---------- hygiene ----------
check("no em or en dashes in the prompt or the checklist", not re.search("[\u2014\u2013]", pr + ck))
check("no machine-specific absolute paths", "/Users/" not in pr + ck and "C:\\" not in pr + ck)
for rel in ("skills/scroll-craft/SKILL.md", "skills/scroll-craft/scripts/shoot.mjs", "skills/scroll-craft/references/verify.md",
            "skills/scroll-craft/LICENSE", "checklist/PRODUCTION_CHECKLIST_clone_swap.md", "examples/CLIENT_INPUT/brief.md",
            "scripts/release_gate.py", "tests/test_release_gate.py", "docs/RELEASE_EVIDENCE.md",
            "scripts/release_queue.py", "tests/test_release_queue.py", "docs/CHECKLIST_WORKFLOW.md",
            "examples/CLIENT_INPUT/release-profile.md", "checklist/bundles.json",
            "docs/ci/verify-kit.yml", "checklist/VIDEO_LESSONS_ADDON.md", "checklist/VIDEO_LESSONS_BATCH2.md"):
    check(f"kit file exists: {rel}", (ROOT / rel).exists())
sub = ROOT / "vendor" / "clone-app-pat-pro-public"
check("methodology submodule is checked out (run: git submodule update --init)", (sub / "SKILL.md").exists(),
      "empty: the agent will clone the repository itself")

# The presence of SKILL.md alone does not prove the correct upstream revision.
pin = "2c03e02d7e1849374739b576b9a0734e6d7e94ab"
head = subprocess.run(["git", "-C", str(sub), "rev-parse", "HEAD"], capture_output=True, text=True)
check("methodology checkout matches reviewed pin", head.returncode == 0 and head.stdout.strip() == pin)
check("prompt names the reviewed methodology pin", pin in pr)
check("prompt uses executable release record", "scripts/release_gate.py" in pr and "--phase launch" in pr and "--phase handover" in pr)
check("prompt uses advisory operating workflow", "docs/CHECKLIST_WORKFLOW.md" in pr and "scripts/release_queue.py" in pr)
# This guards accidental stale policy phrases, not arbitrary semantic contradictions.
for forbidden in ("LCP minus TTFB", "else `build`", "For any other client the fidelity build ships", "ready for a human to deploy"):
    check(f"prompt omits superseded policy: {forbidden}", forbidden not in pr)
check("deploy build is always accessible", "The deployed artifact must pass applicable accessibility checks in every geography." in ck)

# Validate actual Markdown file links in the active entry points, not example code paths.
for rel in ("checklist/RELEASE_STANDARD.md", "checklist/TIERS.md", "docs/CHECKLIST_WORKFLOW.md",
            "examples/CLIENT_INPUT/README.md",
            "docs/reviews/checklist-challenge-2026-10-05/REVIEW.md",
            "docs/reviews/checklist-challenge-2026-10-05/SOURCES.md",
            "docs/reviews/checklist-challenge-2026-10-05/VERIFICATION.md",
            "docs/reviews/checklist-tiers-2026-10-05/REVIEW.md",
            "docs/reviews/checklist-tiers-2026-10-05/INDEPENDENT_REVIEW.md",
            "README.md", "docs/HOW_TO_RUN.md", "docs/RELEASE_EVIDENCE.md", "checklist/PRODUCTION_CHECKLIST_clone_swap.md", "checklist/VIDEO_LESSONS_ADDON.md",
            "docs/reviews/instagram-addon-2026-10-03/REVIEW.md", "checklist/VIDEO_LESSONS_BATCH2.md",
            "docs/reviews/instagram-batch2-2026-10-03/REVIEW.md"):
    document = ROOT / rel
    if not document.exists():
        check(f"active Markdown file exists: {rel}", False)
        continue
    links = re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", document.read_text())
    broken = [link for link in links if not re.match(r"[a-z]+:|#", link) and not (document.parent / link.split("#")[0]).exists()]
    check(f"active Markdown file links resolve: {rel}", not broken, str(broken))

# ---------- report ----------
width = max(len(n) for n, _, _ in results)
failed = 0
for name, ok, detail in results:
    mark = "PASS" if ok else "FAIL"
    if not ok:
        failed += 1
    print(f"{mark}  {name.ljust(width)}" + (f"  [{detail}]" if (not ok and detail) else ""))
print(f"\nrows: {len(rows)}   prompt words: {len(pr.split())}   checklist words: {len(ck.split())}")
print("ALL CHECKS PASSED" if not failed else f"{failed} CHECK(S) FAILED")
sys.exit(1 if failed else 0)
