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
import itertools
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
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
ids = [ROW.match(l).group(1) for l in rows]
dups = [i for i, n in Counter(ids).items() if n > 1]
check("checklist: no duplicate row IDs", not dups, str(dups))


def cells(line):
    return re.sub(r"`[^`]*`", "X", line).count("|")


bad_cells = [l[:16] for l in rows if cells(l) != 5]
check("checklist: every row has 4 cells", not bad_cells, str(bad_cells[:5]))
bad_class = [l[:16] for l in rows if not re.search(r"\| (G|R|C)(-L|-O)? \|$", l)]
check("checklist: every row ends in a valid class (G, R or C, optional -L or -O)", not bad_class, str(bad_class[:5]))

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

fin = pr[pr.index("## Finish"):]
gates = re.findall(r"^(\d+)\. ", fin, re.M)
check("Finish lists gates 1 to 15 in order", gates == [str(i) for i in range(1, 16)], str(gates))
check("Finish says 'all fifteen'", "all fifteen" in fin)

gr = pr[pr.index("## Ground rules"):pr.index("## Methodology")]
check("prompt has ground rules 1 to 10", re.findall(r"^(\d+)\. \*\*", gr, re.M) == [str(i) for i in range(1, 11)])
rules_block = ck[ck.index("**Rules of application**"): ck.index("## SPD")]
ck_rules = re.findall(r"^(\d+)\. ", rules_block, re.M)
check("checklist has rules of application 1 to 10", ck_rules == [str(i) for i in range(1, 11)], str(ck_rules))
rule_refs = {int(r) for r in re.findall(r"\brules? (\d+)\b", ck)}
check("checklist 'rule N' references exist", all(1 <= r <= 10 for r in rule_refs), str(sorted(rule_refs)))

# ---------- hygiene ----------
check("no em or en dashes in the prompt or the checklist", not re.search("[\u2014\u2013]", pr + ck))
check("no machine-specific absolute paths", "/Users/" not in pr + ck and "C:\\" not in pr + ck)
for rel in ("skills/scroll-craft/SKILL.md", "skills/scroll-craft/scripts/shoot.mjs", "skills/scroll-craft/references/verify.md",
            "skills/scroll-craft/LICENSE", "checklist/PRODUCTION_CHECKLIST_clone_swap.md", "examples/CLIENT_INPUT/brief.md"):
    check(f"kit file exists: {rel}", (ROOT / rel).exists())
sub = ROOT / "vendor" / "clone-app-pat-pro-public"
check("methodology submodule is checked out (run: git submodule update --init)", (sub / "SKILL.md").exists(),
      "empty: the agent will clone the repository itself")

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
