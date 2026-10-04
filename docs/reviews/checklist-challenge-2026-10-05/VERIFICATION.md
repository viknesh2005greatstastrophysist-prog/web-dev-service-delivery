# Verification, 2026-10-05

- All 275 stable IDs retained in the original order, across 18 sections; all 275 row decisions reconciled to the final catalogue.
- 70 tier changes; 210 requirement texts revised. Final priorities: 117 Diamond, 86 Gold, 54 Silver, 18 Bronze.
- `python3 scripts/check-kit.py`: 64 checks passed. [Log](check-kit.txt).
- `python3 -m unittest discover -s tests -v`: 54 tests passed in 3.348 seconds. [Log](tests.txt).
- The suite individually fails every one of the 117 Diamond rows and verifies launch is blocked. It also tests contracted lower-tier work, missing/tampered evidence, policy demotion, unknown/duplicate markers, original tiered snapshots and legacy four-column snapshots.
- A field-data fixture verifies UNAVAILABLE cannot be called a field pass and does not block Gold under risk-v2; it still blocks Silver completion.
- Renderer run twice: catalogue and operating-view hashes unchanged on the second run.
- `git diff --check`: passed before staging. Final staged diff also inspected for whitespace and unintended files.

The first verification run caught a heading-parser collision, generated dash characters forbidden by the kit, a stale literal command-name guard, and a reset bug in the new multi-row test fixture. These were corrected and the relevant checks rerun; the final logs above contain the successful run.

Primary review also corrected an advisory caption-level error and rejected unsafe or inadequately justified demotions. The new policy does not certify a deployed website, verify legal clearance or convert historical failures to passes. No live site was changed. The update remains on draft PR #2, not main.

Account usage observations: 86% used at the start, 90% at completion verification. The four-point change is account-wide and rounded, not an exact task cost. Work was bounded to the user's under-five-point limit.
