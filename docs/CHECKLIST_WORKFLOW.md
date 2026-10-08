# Use the checklist in daily work

Keep all 275 stable IDs in one release record. Generate a short work queue from that record.
Diamond is the mandatory launch floor; Gold adds quality. Silver and Bronze never allow a weaker
Diamond floor. A lower-tier contract promise still blocks its due milestone. These are internal
standards, not official certificates.

## 1. Establish the actual service

Fill the operator's [private release profile](../examples/CLIENT_INPUT/release-profile.md) using
the existing brief, scope, rights and provider records. Agree pages/actions, audience, data flows,
access, ownership and contract promises. Include host logs and server-side sharing. No cookies
does not establish absence of personal information. Record unknown inputs early.

Review every ID for applicability. Unconditional G cannot be N/A except retired LEG-07;
conditional C/R needs observed absence and evidence. Unknown stays unresolved. Record new serious
risks even if the catalogue missed them. Do not create unnecessary features to satisfy a row.

## 2. Prepare tests and capture evidence in groups

The six [work bundles](../checklist/bundles.json) organize overlapping catalogue groups:

| Bundle | Main outcome |
|---|---|
| Navigation and essential actions | Routes, actions and recovery states work. |
| Enquiries and integrations | Validation and feedback are truthful; the intended result occurs. |
| Accessibility, responsive use and performance | Essential use and agreed quality hold under supported conditions. |
| Security and privacy | Actual data paths and appropriate defenses, notices and choices are verified. |
| Content, claims and rights | Facts and asset rights are supported; the client approves the actual version. |
| Deployment, ownership and recovery | The real destination works, owners have access and recovery is proven. |

Membership is organizational, not a test result. Map actual procedures to row IDs in the profile;
one run/report may support several rows only when each expected and observed result and coverage
is explicit. Show unmapped Diamond work. Prepared procedures, fixtures and capture setup can be
reused; client verdicts cannot. A provider accepting an enquiry does not prove mailbox receipt.

During development, run affected regression checks. At final freeze, revalidate claimed PASS/N/A
against the exact build and relevant configuration. Capture sanitized external settings privately;
code can remain unchanged while DNS, provider settings or mailbox rules change. The validator
does not automatically verify these external settings. Never stamp fresh identities onto old proof.

## 3. Use one daily queue

Create the full record using [the evidence contract](RELEASE_EVIDENCE.md), then generate a view:

```bash
python3 scripts/release_queue.py /path/to/private-evidence/release.json \
  --checklist checklist/PRODUCTION_CHECKLIST_clone_swap.md \
  --tiers checklist/tiers.json --bundles checklist/bundles.json \
  > /path/to/private-evidence/daily-queue.md
```

`--format json` produces the same advisory view as JSON. No network requests, deployments or
record writes occur. A zero exit code means the view was generated, never that a release passed.
Save output to a different file from the input. Keep real records, profiles and queue output private.

The queue preserves every open Diamond row first, including owner/live or later-timed rows.
It then shows due contracted work, owner inputs, final-domain checks, Gold work and follow-ups.
It shows recorded status counts for all 275 rows; PASS/N/A are omitted from the open list only
as recorded claims. They have not been validated by this tool. Invalid/duplicate/missing IDs,
wrong checklist hashes or incompatible metadata fail instead of silently shrinking the view.

Check the profile, unmapped procedures, actual evidence and new risks alongside the queue.
Do not mistake a blocked action for absence or a scheduled observation for completion. Each open
row needs a reason, owner, next action and review date. Time-box a stubborn issue, record its
specific dependency and continue other feasible work. Track active work separately from waiting.

## 4. Separate the release decisions

Record operator QA, exact-version client approval and authorization to cut over separately.
Finish applicable pre-cutover Diamond work, resolve known failures, prepare recovery and live
probes. Prefer protected final-domain verification where feasible; inherently live checks require
an authorized controlled cutover. Until all applicable live Diamond requirements pass, this is
a verification window, not Diamond completion. A failed critical path requires immediate
containment, repair and recheck or rollback. Approval cannot waive a required failure.

HOST-14 remains unconditional Diamond. Static sites require a clean rebuild/redeploy from retained
approved source/assets; mutable data requires the relevant tested restore. A backup assertion or
removing a support promise cannot replace this proof. Recheck affected evidence and approvals
after code, content, artifact or configuration changes.

## 5. Report delivery and later obligations honestly

Report Diamond verification, Gold completion and contractual delivery separately. Run the actual
`release_gate.py` phases and review evidence before claiming completeness. Full Gold requires every
applicable Diamond and Gold row. SEO-13 includes a review two weeks after launch; it cannot be
pre-passed. SPD-21 insufficient field data is Silver and does not alone block Gold. Recurring
control setup may pass when actually installed and tested; continuing duties remain assigned.

Separate the handover deadline from later observation dates in the agreed scope. A 14-day handover
cannot also promise full Gold at handover when a required review occurs two weeks after a later
launch. Future duties need accepted ownership, due dates, actions and escalation. Ongoing agency
maintenance is included only when agreed. Non-indexing alone does not prove an SEO-13 failure:
the requirement is the review and investigation, not guaranteed search inclusion.

Preserve missed dates, defects and remediation history. The current gate reports an overdue open
review date as a record error even for optional work. Reassess it honestly; never automatically
move dates to keep a result green. Timing does not waive Diamond or change the Gold gate.

## Rehearse and measure

First reconstruct saved historical accounting without rewriting old verdicts. Then rehearse a
controlled ordinary-site release: missing inbox receipt, hidden data processing, future Gold,
changed navigation/approval, due contracted Silver, missing recovery proof and non-indexing
without a technical defect must all produce honest decisions. A historical public site is not
recertified by importing its record or changing policy.

Measure active work, waiting, rework, evidence capture, procedure/map upkeep and coverage gaps.
Zero false completion decisions and complete mandatory coverage are the acceptance target.
Another reviewer must be able to recover the same decision. Net time savings and production
capacity remain unproven until measured; one rehearsal cannot prove scale. Use existing files
and scripts before considering dashboard infrastructure.

## Clone and media work

For commissioned clones, use [CLONE_WORKFLOW](CLONE_WORKFLOW.md) before expanding the build.
Close the pinned reference sample, validate original generated media and final crops, then close
the adapted sample. Full fidelity and production decisions remain separate. A finished private
handover can preserve blockers, but cannot become an accepted-clone or launch claim.
