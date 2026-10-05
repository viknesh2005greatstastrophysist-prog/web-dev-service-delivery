# Release evidence contract

The validator checks record completeness, artifact identity claims and file integrity. It does not run website audits, authenticate a human, interpret screenshots, prove legal compliance or discover omitted routes. A dishonest test can still produce a well-formed record. A reviewer must inspect the underlying evidence and compare the actual deployed artifact with the recorded identity.

Use the corrected checklist as the requirement source. All 275 row IDs remain present for every project; conditional rows can be N/A only with an observed absence predicate and evidence. Do not turn optional features into mandatory services just to satisfy the catalogue.

## Decisions

| Phase | Success label | What it establishes |
|---|---|---|
| handover | HANDOVER-READY | Diamond local records pass; live/owner rows may remain explicitly pending with an owner, action and review date. CONTENT-PENDING is allowed. This does not authorize deployment. |
| launch | LAUNCH-EVIDENCE-COMPLETE | Every applicable Diamond row has passing records for the production release, approved content and accessibility fixes enabled. Other tier misses have assigned follow-up. Actual test truth still requires review. |
| gold | GOLD-EVIDENCE-COMPLETE | Launch requirements plus every applicable Gold row pass. No Gold claim with unresolved Diamond/Gold or contracted rows, or missing required quality evidence. Longitudinal field sampling is Silver under risk-v2. |
| diamond | DIAMOND-EVIDENCE-COMPLETE | Alias of launch checks; Diamond is the mandatory safety floor. |
| silver | SILVER-SCOPE-EVIDENCE-COMPLETE | Diamond, Gold and Silver records complete; this is additional scope, not a lower safety level. |
| bronze | FULL-CATALOGUE-EVIDENCE-COMPLETE | All four tiers complete; Bronze never permits skipping Diamond. |
| any | BLOCKED | The output lists the exact missing or invalid requirements. A useful incomplete handover can still be delivered with this status. |

A build finish and the fifteen fidelity gates are separate from the production decision. The release validator covers checklist records, not visual fidelity. Report both. A live decision necessarily follows a controlled, approved deployment; before cutover, review local evidence and pre-launch owner obligations, and define the rollback triggers. Pending live checks never imply permission to launch. A temporary protected preview is not a completed client launch.

## Create and validate a record

Python 3.9 or newer; no package installation required. Production checks perform a system DNS lookup and reject unresolved or non-global addresses; no HTTP requests or form submissions are sent. Fixture tests inject DNS results and need no network.

```bash
python3 scripts/release_gate.py /path/to/private-evidence/release.json \
  --checklist checklist/PRODUCTION_CHECKLIST_clone_swap.md --init
python3 scripts/release_gate.py /path/to/private-evidence/release.json \
  --checklist checklist/PRODUCTION_CHECKLIST_clone_swap.md --phase handover
python3 scripts/release_gate.py /path/to/private-evidence/release.json \
  --checklist checklist/PRODUCTION_CHECKLIST_clone_swap.md --phase launch
python3 scripts/release_gate.py /path/to/private-evidence/release.json \
  --checklist checklist/PRODUCTION_CHECKLIST_clone_swap.md --phase gold
```

`--init` refuses to overwrite an existing record. Its output is deliberately unverified and fails validation until populated from actual observations. Successful validation exits 0; a blocked decision, malformed JSON or missing file exits 1. Save stdout as a decision artifact without replacing the input record. Evidence paths resolve relative to the record's directory, or an explicit `--evidence-root`. They must be nonempty files inside that directory, not absolute paths, parent traversals or symlinks escaping it.

In delivered apps, copy the validator to `scripts/release_gate.py` and the exact reviewed checklist to `docs/PRODUCTION_CHECKLIST.md`. Use that snapshot with `--checklist`. Keep the record, reports and redacted approvals private and outside the deployed artifact. Do not embed the final report in the archive it hashes. DEL-15 uses the validator test/integration log as evidence, not a recursive hash of its own decision output.

## Record fields

`schema_version` is 1. `checklist_sha256` is the exact UTF-8 checklist file hash. Review this snapshot against the approved kit commit; the validator cannot detect an operator deliberately replacing both checklist and fingerprint.

The `release` object contains:

- `revision`: full Git commit hash of the reviewed application source.
- `artifact_sha256`: SHA-256 of the immutable deployable archive, including public assets and necessary server/configuration files. Build once and deploy that artifact. An independent review must confirm the hash describes the actual output.
- `build_id`: the identity served by that artifact, including its accessibility mode. Do not overwrite the tested output with a fidelity build.
- `built_at`: UTC or offset-aware ISO timestamp, taken after the build completes.
- `url` and `environment`: the audited base URL and `local`, `staging` or `production`. Launch requires production HTTPS; the current DNS answer must contain only global addresses. This does not prove ownership, HTTP reachability, deployment identity or future DNS state; the live audit supplies that evidence.
- `a11y`: `on` for the deployed artifact; `content_status`: `CLIENT-COMPLETE` or `CONTENT-PENDING`.
- `required_rows`: an explicit list of additional contracted row IDs due by release, or `[]`. Future support/measurement duties stay in the full ledger with their actual due dates and owners; do not put a post-launch observation in a prelaunch completion list. Compare the timing with the actual contract and disclose outstanding obligations. These listed rows block readiness like required work even when their generic tier is Silver or Bronze. Contracted rows cannot use N/A; resolve an actual scope change before changing this inventory. Review the list against the signed scope; the validator cannot discover omitted promises.
- `routes`, `states`, `viewports`: nonempty unique string inventories. Derive routes from the built router, crawl, sitemap and approved scope; compare them independently. Derive states from the interaction inventory, including errors and reduced motion. The validator cannot infer omitted routes from these lists.

Each entry in `rows` has a stable `id`, boolean `applicable`, status, verification method (`automated` or `manual`) and coverage. For every observed result, also provide:

- `release_revision`, `artifact_sha256`, `build_id`, `environment`, `url`, matching the release being assessed.
- `tester`, `checked_at` after the build and no later than the current time.
- `coverage`: explicit route/state/viewport combinations or a concrete nonvisual scope such as the authoritative DNS zone. A reviewer checks completeness against the inventories; a generic “all tested” sentence is not sufficient evidence.
- `evidence`: nonempty objects with a relative `path` and exact `sha256`. Grouped logs are allowed when the artifact identifies every covered row and result. Hashes detect changed bytes, not genuine captures.

An N/A row needs `applicable: false`, `reason`, an observed `predicate`, and evidence. Every other row has `applicable: true`. Unconditional G rows cannot be excluded. Conditional C rows are required whenever applicable. `LEG-07` is retired and records N/A with its supersession reason.

Every unresolved result needs `reason`, `owner`, `next_action` and a future `review_by` ISO timestamp. `AWAITING-DEPLOY` is only for -L rows; `OWNER-CONFIRM` only for -O rows. Pending results need no fabricated capture. `UNAVAILABLE` is allowed only for SPD-21 with inadequate field data; it prevents Gold completion but not Diamond launch. `INHERITED` is never a production status. A Diamond FIDELITY-EXCEPTION blocks launch; a Gold exception also blocks Gold completion.

Owner PASS/N/A observations require `verification: manual` and a named human's evidence. A script cannot confirm mailbox receipt, legal rights, real devices or client approval on their behalf. The validator checks the record, not the person's identity.

## Freshness and review

Preserve one record per release and environment. Do not mix a localhost report with live confirmations in one launch record. Re-run applicable checks on the final artifact; if a prior isolated test remains relevant, the reviewer explicitly revalidates it against the final revision and records that later review with the original report attached. Changes to content, build output, dependencies, host settings, DNS or provider configuration invalidate affected results. Time ordering alone cannot prove freshness.

A reviewer independently checks at least the primary visitor journey, the actual deployed build id, the scope inventory, all critical security/accessibility failures and every N/A decision before signing. Evidence review is mandatory even when the JSON passes. Preserve the prior record and rollback artifact rather than editing old evidence into a new release.

## Test the control

```bash
python3 scripts/check-kit.py
python3 -m unittest discover -s tests -v
```

The fixture suite covers a passing synthetic record and rejected mutations. Synthetic records are not client evidence. The kit still needs an actual end-to-end client rehearsal, host testing, real-device/assistive-technology review and production delivery verification before it can demonstrate an entire working delivery process.


## Tier policy and migration

The five-column checklist embeds each row's Tier in the fingerprinted snapshot. `checklist/tiers.json` supplies the rationale and scheduling register; it cannot override the snapshot. Never strip the Tier column when packaging an app. `check-kit.py` rejects missing or inconsistent assignments. `--phase launch` and `--phase diamond` require applicable Diamond rows. Gold requires Diamond plus Gold. Silver adds Silver; Bronze adds Bronze. These are priority scopes, not external certifications. Always report the phase and remaining tier counts.

G/C/R remains only for applicability: unconditional G cannot use N/A; conditional C and absent R need an evidenced predicate. -L/-O retain live and manual-evidence semantics. Optional observations still require valid hashes, identity and coverage; unresolved optional rows need tracked follow-up. The metadata timing does not exempt Diamond from a launch decision. A handover decision can have pending live/owner evidence and grants no release authorization.

Before controlled cutover, all Diamond prelaunch obligations must be verified, the exact candidate approved, rollback rehearsed, and final-domain Diamond probes prepared. Execute those immediately after cutover; on failure roll back or disable the affected optional feature without breaking the agreed core journey. Until they pass, describe the cutover as provisional, never Diamond complete. Newly discovered safety or legal failures block release even if absent from the catalogue.

Legacy four-column snapshots retain their historical G/C launch and all-row Gold semantics. Mixed formats are rejected; new tier phases are rejected for legacy snapshots. Existing records are not rewritten, retagged as passed, or used with the new checklist hash. Create a new record and revalidate relevant evidence against the reviewed release. This policy revision cannot retroactively certify RIOA.

## Priority policy revisions

The current checklist declares `<!-- priority-policy: risk-v2 -->`. Its reviewed Diamond floor is pinned in the validator independently of the row register. Unknown or duplicate policy markers fail. Earlier tiered snapshots without a marker retain the original 150-row Diamond floor (`tiered-v1`); original four-column snapshots retain legacy behavior. Validate historical evidence against its actual approved snapshot, never a freshly substituted policy. A revision does not turn an old failure into a pass or authorize a live release. Reviewers must approve the actual policy version as well as the artifact.

The [challenge review](reviews/checklist-challenge-2026-10-05/REVIEW.md) records the causal reasons for reclassifying requirements and the controls retained after compound rows were narrowed. A shared evidence file may support multiple rows if its coverage is explicit; there is no requirement to run one separate test per ID.
