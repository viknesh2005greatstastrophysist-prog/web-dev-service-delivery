# History

## 2026-10-08: implement the reviewed checklist operating workflow

Added the private release profile, six overlapping work bundles and a dependency-free advisory
queue generated from the complete release record. Documented grouped evidence, separate release
decisions, accepted future owners, recovery proof and later Gold observations. Corrected the
stale SPD-21 sentence: unavailable Silver field data does not alone block Gold under risk-v2.
All row IDs, tiers and release-gate semantics are retained. No client website is recertified.

## 2026-10-05: challenge the production tier assumptions

The second audit replaces implementation mandates and reference comparisons with scoped outcome criteria. It preserves all 275 IDs, records each decision, and versions the Diamond floor so historical snapshots retain their original meaning. See [review](reviews/checklist-challenge-2026-10-05/REVIEW.md) and [operating standard](../checklist/RELEASE_STANDARD.md). No website is recertified by this policy change.


How the prompt and checklist got to their current form. Append a line here for every change that matters.

## Lineage

| Edition | Date | What it was | Where it is | Status |
|---|---|---|---|---|
| Master prompts (general, precise, reviewed, accounting and tax) | 2026-09-28 to 09-30 | The first audit-and-tighten work: Awwwards pixel rebuilds plus a scroll-craft layer | `archive/earlier-master-prompts/` | Superseded |
| Clone with polish | 2026-09-30 | The operator's own short prompt ("rebuild it pixel for pixel") plus the scroll-craft polish pass as an additive last step | `archive/prompts/PROMPT_awwwards_clone_with_polish.md` | Superseded |
| v2 | 2026-09-30 | Whole-prompt rewrite for truthful gates, fidelity and motion, autonomy, the comparison video | `archive/prompts/PROMPT_awwwards_clone_v2.md` | Superseded |
| v3 and `PRODUCTION_CHECKLIST.md` | 2026-09-30 | Comparison-video edition: 167-row checklist, Opus-reviewed to GREEN in 4 rounds | `archive/prompts/PROMPT_awwwards_clone_v3.md`, `archive/checklists/PRODUCTION_CHECKLIST.md`, reviews in `docs/reviews/v3-comparison-edition/` | Superseded |
| v4 client edition | 2026-09-30 | Paid client deliverables: template mode, content sections, 188 rows; Opus-reviewed GREEN; made non-blocking after a HARD-BLOCKER complaint | `archive/prompts/PROMPT_awwwards_client_v4.md`, `archive/checklists/PRODUCTION_CHECKLIST_client.md`, reviews in `docs/reviews/v4-client-edition/` | Superseded; v6 is built on it |
| v5 inspired edition | 2026-09-30 | "Close cousin" approach to reduce legal exposure: a distance gate against the reference; GPT-run lessons added | `archive/prompts/PROMPT_awwwards_inspired_v5.md`, `archive/checklists/PRODUCTION_CHECKLIST_inspired.md` | Abandoned when the operator chose clone-then-swap |
| v6 clone-and-swap | 2026-10-01 | Reference build, content ladder, swap probe, brand shift, production loop; 196 rows; Opus-reviewed GREEN after 2 blockers | `prompt/`, `checklist/`; review in `docs/reviews/v6/01-*` | Current |
| v6 gold-standard pass | 2026-10-01 | Whole checklist raised to gold: 253 rows, 18 sections, new UXF section; Opus-reviewed GREEN after 4 blockers | `docs/reviews/v6/02-*`, `docs/research/` | Current |
| v6 run parts | 2026-10-01 | Optional `RUN_PART=1` and `RUN_PART=2`; Opus-reviewed GREEN after 2 blockers | `docs/reviews/v6/03-*` | Current |
| v6 US legal edits | 2026-10-01 | Brand shift default, two builds, AI-authorship wording, LEG-18; Opus-reviewed GREEN after 1 blocker | `docs/reviews/v6/04-*`, `docs/LEGAL_NOTES.md` | Current |

## What the GPT run taught (an earlier client edition, run with no client input)

The run built a working site, disclosed five failed gates and one unrun gate, and scored 100 on Lighthouse mobile
against 61 for the original. It also produced 260 geometry failures and visible defects that its checks missed:
an overlay backdrop that collapsed to zero height, menu and footer text that was dark on dark, a footer clock
replaced by an address, mobile contact buttons in the wrong layout, no mobile navigation with JavaScript off, and
animation code that overwrote placeholder markers. It had built audit machinery before the pages looked right.

Each defect became a rule or a gate in v6:
- Ground rule 9, "look before you measure": screenshots of every state next to the original before any number.
- Ground rule 10, rebuild the box tree: never paste sampled computed values onto a differently nested DOM.
- The state walk: every menu and overlay at five viewports, contrast measured on rendered pixels, backdrop area,
  and outside-click, Escape and close all dismissing.
- Per-element coverage and geometry asserted from the first cycle.
- Live widgets stay functional; animation code never writes slot markers (CNT-12, CNT-13).
- Ten broken-fixture smoke tests for the audit tool, so a check that cannot fail is not a check.
- `escalation.md` must list every remaining visible defect when a gate fails.

## Change log

- 2026-10-01: Repository created. The prompt's two absolute paths became `<KIT_DIR>` paths, and its methodology step
  now uses the pinned submodule first. `scripts/check-kit.py` added. Everything else is as reviewed.

- 2026-10-02: Production audit corrected performance comparisons, accessibility precedence, applicability, mail/DNS recovery and release claims. Preserved all 254 existing IDs and added eight checks. Added a dependency-free evidence validator, adversarial tests, stable ID inventory and an inactive CI template (workflow authorization pending); synchronized prompt/runbook/decisions. See `docs/reviews/production-audit-2026-10-02/AUDIT.md`. No website deployment is certified by this audit.

- 2026-10-03: Reviewed sampled frames and public post descriptions from nine supplied Instagram clips. Added the video lessons companion and eight source-linked rows (270 total), strengthened safe caching, GPU fallbacks, structured data and reference intake, and extended provenance checks. This changes the kit; it does not certify or deploy a client website. See `docs/reviews/instagram-addon-2026-10-03/REVIEW.md`.

- 2026-10-03 (second media batch): Integrated six further videos and one nine-slide carousel. Added five conditional/recommended checks for crawler policy, webhook verification, production payment evidence, transactional mail and URL migration (275 total); strengthened cost bounds, sending identities and audience-fit copy. See `docs/reviews/instagram-batch2-2026-10-03/REVIEW.md`.

- 2026-10-05: Reorganized all 275 stable IDs into Diamond/Gold/Silver/Bronze priorities, with a generated operating view and explicit rationale/timing register. Diamond is nonwaivable for launch; Gold adds quality requirements; Silver/Bronze add optional scope. Updated validator, prompt and contract together; legacy snapshots keep historical semantics. Corrected overprescriptive cache/compression, error-page, provider diagnostics and header comparisons; clarified current legal applicability and qualified review. No RIOA evidence is retroactively passed. See `docs/reviews/checklist-tiers-2026-10-05/`.

- 2026-10-08: Added pinned representative clone-stage closure and original generated-media validation/sync preparation after auditing RIOA/Visuvate and landscaping/Elite. Fail/unrun states stop expansion; hashes bind evidence to source and compiled files. Generated media has a typed source, scene briefs, exact slot/manifest inventory and honest model attribution. Preserved all 275 IDs, tiers and full-site/release gates. Three Fable loops and adversarial verification are in `docs/reviews/clone-workflow-2026-10-08/`. No client website is rebuilt or recertified.
