# Add-on verification, 2026-10-03

## Recorded scope

The catalogue has 270 rows in 18 sections. The stable inventory preserves all 262 IDs from commit 334b324b78aec2e330e0d3ec9c160de93c6d317d and adds eight rows. Nine supplied sources and 69 inspected sampled frames are indexed. No native captions or spoken-audio transcription were available. Source hashes identify the retained artifacts; the structural checks do not verify the truth of media or release claims.

## Checks

Initial local checks found the review linked this verification file before it existed. The valid-kit test rejected that missing link; it was corrected by adding this file. Final check results are recorded below after rerun.

- Structural checker: PASS, 49 checks, `python3 scripts/check-kit.py` (exit 0).
- Unit/mutation tests: PASS, 36 tests, `python3 -m unittest discover -s tests -v` (exit 0). Includes missing-source, source-URL mismatch, nonexistent-row mapping, malformed-JSON and missing-companion regressions.
- Git whitespace check: PASS (`git diff --check`). Primary integration review and independent bounded technical review completed. The independent reviewer identified overbroad query/UI applicability and a copyright-date mapping error; both were corrected before the final verification run.
- Hosted CI: inactive workflow template remains pending workflow authorization.
- Live website, database workload, account ownership and owner approvals: not tested by this toolkit change.

No website is cleared for production by these results.

Saved local output: [structural checks](structural-checks.txt), [unit tests](unit-tests.txt).

`structural-checks.txt` SHA-256: `be931b71d6440f8e4fbf3f129cb873521ba21d09bd427527f1d856e2c6f622d2`.

`unit-tests.txt` SHA-256: `4919f2341a5141beef18e095bd1ae28a3338729c9fdd7a34f7836c6115dcda72`.

Independent findings and corrections: [review](INDEPENDENT_REVIEW.md).

Saved text logs remove trailing alignment spaces only. Staging the logs exposed those spaces in the whitespace check; they were trimmed and the final staged check passed.
