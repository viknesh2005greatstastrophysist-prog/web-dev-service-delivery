# Independent review and resolutions

Reviewed 2026-10-05 by a separate GPT-6 Luna agent, before final row-register integration. It inspected the uncommitted validator and policy diff; it did not rerun site tests or certify row placement. Primary review then inspected the assignments and resolved the following findings.

| Finding | Resolution |
|---|---|
| The renderer accepted only lowercase tiers but the consistency check accepted title case. | Both now require lowercase register values; malformed casing fails explicitly. |
| A coordinated downgrade in both table and register could evade a mismatch-only test. | The validator additionally pins the reviewed Diamond floor and rejects missing/demoted floor rows. A targeted mutation tests coordinated demotion. The code and approved snapshot remain trust boundaries; this does not defend against someone rewriting the validator itself. |
| Contracted Silver/Bronze obligations were prose-only. | Tiered records require an explicit release.required_rows inventory, and contracted unresolved checks block readiness. Tests cover this and missing/unknown scope. Reviewers still compare it to the real contract. |
| A11Y-18 reduced the former platform matrix. | Intentional: real desktop/mobile testing is now an audience-based minimum, still Diamond, with expansion for known needs and support commitments. It is not a conformance guarantee. |
| LEG-12 changed from universal drafting to conditional applicability. | Intentional: actual accessibility-statement duties and known limitations remain mandatory; DEL-03 was synchronized. |
| The review reported no history entry. | Primary inspection confirmed the 2026-10-05 entry in docs/HISTORY.md; no unresolved omission. |

The independent reviewer found no blanket legal waiver in LEG-17 and no explicit safety removal in compression, diagnostic-timing or deployed-header corrections. Primary integration additionally moved comparison-only UXF-11 to Gold, placed real assistive testing in Diamond, made self-hosted fonts Gold while retaining privacy controls in Diamond, and separated initial analytics/error-reporting safety from later recurring observations.

Final mechanical verification is recorded in VERIFICATION.md. Its scope is kit consistency and synthetic adversarial tests, not a website launch.
