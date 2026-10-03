# Production checklist audit

Date: 2026-10-02. Baseline: `996113d84f406fb3a50fd1dcb2a210c25ebf9462`.

The previous checklist passed its mechanical check while permitting misleading readiness claims. This revision corrects the requirements and adds tested evidence validation. It does not certify a client website or establish that the full delivery prompt has run successfully.

## Verified scope and decision

Reviewed the active checklist, prompt, check script, runbook, decision log, legal notes and release instructions. All 254 original row IDs are retained; eight additions produce 262 rows across the existing 18 sections. The stricter numerical targets remain house policy. No site has been deployed by this audit.

The core failure was mixing four different facts: a run finished, a reference looked similar, an automated scan passed, and a client site was safe to launch. They now have separate evidence and decisions. Required production failures cannot pass because the reference shares them. Accessibility fixes are mandatory in every deployed build. Incomplete inputs can still produce a useful handover, with launch blocked.

## Findings and treatment

| Area | Finding | Correction and verification |
|---|---|---|
| Release rules and prompt | “Done” included honestly listed failures while implying deploy readiness. Owner rows could never become PASS. | Explicit handover/launch/gold phases; owner PASS needs dated manual evidence. Prompt and runbook synchronized. |
| SPD | LCP minus TTFB was used to compare localhost with a remote reference; lab timing stood in for field INP; strict scores implied population ranking. | Full LCP, comparable profiles, final HTTPS lab gate, separate field row, and house-budget labeling. |
| TYP | Changing a root font size and an axe result were overclaimed as complete resize/contrast proof. | Real zoom/text-size review and rendered-background/manual checks. |
| RSP | Full hit-box sampling rejected legitimate WCAG spacing exceptions; browser coverage was optional and emulation obscured physical-device gaps. | Criterion-specific alternatives, required three-engine smoke tests and separate owner device check. |
| A11Y | Keyboard was treated as sufficient for dragging; reduced motion could replace pause controls; visible labels and media alternatives were incomplete. | Pointer alternatives, on-page controls, labels, meaningful media alternatives and full A/AA manual worksheet. |
| SEO | CONTENT-PENDING could become indexable via an environment flag; indexing and reference-route redirects were overclaimed. | Content/approval guard, actual client migration map, and indexing status rather than a guarantee. |
| EDGE | Reference defects and dead actions could survive as exceptions. | Deployment safety precedence; unknown routes remain genuine errors; content-sync failures cannot be hidden as success. |
| UXF | Dead controls/deceptive reference mechanics could be retained. | Actual useful destinations and safe deployed behaviour, with fidelity differences recorded separately. |
| MOT | One set of timing figures could imply production quality. | Matched recorded environments, explicit house budgets and required production checks; motion fidelity remains separate. |
| SEC | .env.example was excluded from secret scanning; documented advisories could pass; cookie rules ignored script-readable preferences. | Scan examples/history/output, review build as well as runtime dependencies, context-appropriate cookies and CI trust controls. |
| BACK | No form implied no backend; Node SMTP stood in for edge/provider compatibility; per-process limits and deduplication were inadequate. | Actual endpoint inventory, selected-runtime tests, shared abuse/idempotency and malformed/ambiguous-failure cases. |
| MAIL | Sending/receiving applicability was confused; MTA-STS testing was described as enforcement; no final inbox proof existed. | Mail inventory, administrator-controlled policy, provider-specific rules and authorized final-domain receipt confirmation. |
| HOST | Generic mirror/rollback language and a website-only DNS plan omitted recovery and existing business email. | Isolated restore evidence, exact rollback steps, mail-preserving cutover and actual scanner metadata. |
| OPS | Repeated web-vitals reports could discard updated values; weekly bot cadence implied security response. | Retain latest/final metric value, incident-prioritized maintenance, exact artifact deployment and kit CI. Failed budgets cannot automatically raise their own thresholds. |
| LEG | Missing legal inputs and no third-party browser requests could imply N/A; upload registration was overstated. | Full data flow and reviewed applicability; no automatic legal inference or broad risk ranking. |
| SUS | Sustainability figures could look like certification. | Existing recommendations retained; gold distinguishes recommendation/field gaps and records limitations. |
| I18N | Feature absence and untranslated content needed explicit evidence. | Conditional applicability and unresolved gaps cannot be marked away by missing input. Existing locale checks retained. |
| CNT | File presence and zero placeholders could imply approved complete content. | Actual facts/rights/brand/content approval required; final release identity invalidates old evidence after changes. |
| DEL | Handover packaging, owner acceptance and production readiness were conflated. | Exact artifact identity, separate accessible output, owner acceptance and executable release record contract. |

## Executable control

`scripts/release_gate.py` checks every row exactly once, valid status/applicability, checklist fingerprint, release and evidence identities, timestamp ordering, relative nonempty evidence files, file hashes, manual owner records, public production DNS, complete content and a11y mode. It rejects malformed JSON, duplicate keys, evidence path escapes and unresolved required rows. Recommended misses need a named follow-up and cannot pass gold.

`scripts/check-kit.py` additionally enforces the stable ID inventory, documented count, strict row syntax, section/gate cross-references, active entry-point links and the exact methodology checkout pin. The prepared CI template runs consistency and fixture tests with read-only permissions and an immutable checkout action pin. It is inactive: GitHub rejected publishing an active workflow because the current OAuth token lacks the workflow scope. See [activation instructions](../../ci/README.md). No hosted CI result is claimed.

Evidence validation is intentionally not website certification. A fabricated screenshot can hash correctly. Scope inventories, applicability, actual observations, owner identity and deployed-artifact identity still require independent inspection. The tool does not establish copyright permission or WCAG conformance.

## Adversarial review and verification

The independent standards review identified stale Observatory metadata, overstated cross-origin isolation and a guaranteed-indexing implication; all were corrected. A separate implementation review reproduced a launch false-pass for `https://localhost.` and loopback DNS aliases. Host normalization plus a global-address DNS check and regression fixtures close that path. DNS is a point-in-time check, not a deployment test.

The test suite uses synthetic evidence only. It exercises complete records and mutations for missing/duplicate IDs, wrong checklist/build identity, altered/missing/empty files, symlink/path escapes, inappropriate N/A, unresolved required checks, owner automation, local/mixed DNS, unsupported statuses, stale timestamps and malformed input. Structural mutations cover silent row deletion, malformed table rows, missing sections, broken links and stale counts. The [verification log](VERIFICATION.md) records 42 passing consistency checks and 31 passing tests; no synthetic result is a client PASS.

## Council and reasoning review

Five independent advisors and five anonymized peer reviews challenged the release design. Consensus: prevent false readiness for an exact artifact, and keep file integrity separate from truth. The real tradeoff was a short critical-path list versus full row traceability. This revision keeps stable IDs and explicit feature predicates so requirements do not disappear, while recommendations need not block launch. Peer review identified budget scope and migration as omissions. The work was bounded to the existing kit, one source correction pass, a small standard-library validator, negative fixtures and final review; no unrelated site build or open-ended research was added.

The first concrete action was to reproduce the old checker passing despite its semantic release gaps. The next control was a passing synthetic record plus deliberately broken variants. The strongest remaining counterexample is a dishonest or incomplete audit with valid hashes. The explicit limitation, independent evidence review and actual-site rehearsal requirement address that without pretending software can prove every human claim.

## Remaining limits

- Hosted CI is awaiting workflow-authorized activation; local verification passed. The complete active-workflow proposal is also preserved on the local `codex/production-checklist-audit` branch.

- The entire v6 client delivery workflow has not been verified end to end by this audit.
- Actual deployment adapters, physical devices, screen readers, inbox delivery, DNS, restoration and legal approvals remain project-specific work.
- Some unchanged historical compatibility statements and statistics were not freshly executed or re-researched. They must not override current primary documentation for a release.
- No automatic tool can prove an owner attestation or that a screenshot covers every state. Missing evidence remains a blocker, and passing records still need review.

See [sources](SOURCES.md) and the [release evidence contract](../../RELEASE_EVIDENCE.md). The recommended next acceptance step is one controlled delivery rehearsal on the chosen host with actual user-journey, recovery and owner evidence. That is outside this checklist-repair claim.
