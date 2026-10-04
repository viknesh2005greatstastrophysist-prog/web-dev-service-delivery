# Decisions

Decisions the operator made while the kit was built, and the ones still open. Each settled decision is
reflected in the prompt and the checklist; change them together if you reverse one.

## Settled

| Decision | What it means in the kit |
|---|---|
| Clone first, swap the client's content at the end | A private reference build proves the clone on the original's own content; the client's content goes in afterwards (prompt sections 4 to 6) |
| The inspired "close cousin" approach was dropped | The v5 edition is archived; v6 reproduces the design, layout, structure and motion |
| The run never blocks | Missing client material is filled from the content ladder; failed gates are reported, not hidden |
| Clients are not asked to find assets | Ladder: client, copy drafted from the brief, CC0 stock, marked placeholder |
| Testimonials, client names, statistics and awards are never drafted or stocked | Only the client's own, or a marked placeholder; an empty testimonial slot stays a placeholder |
| The agent never deploys | A human deploys and runs `npm run audit:live`; owner-only rows are confirmed in the launch checklist |
| Brand shift on by default | `design_shift` defaults to `palette+type`; a palette is derived if `brand.md` has none, holding WCAG relative luminance |
| Customers are in the United States | All deployed builds use `npm run build:deploy` and accessibility fixes on; `npm run build` remains a private fidelity comparison |
| Four priority tiers | Diamond is mandatory for launch; Gold adds experience quality; Silver/Bronze retain optional and specialist work. All 275 IDs remain; exceptions do not waive Diamond. |
| A reference that misses a published floor is a FAIL | Not an exception, even if the reference misses it too |
| CPU throttling is calibrated | Effective versioned profiles and any supported calibration are recorded; simulated and applied throttling are not stacked (checklist rule 3) |
| A11Y-21 and the touch-only hit areas stay | They change what some visitors see or feel; accepted |
| Observatory is a diagnostic quality gate | HOST-20 follows its assigned tier; a scanner grade is not proof of security. Actual security controls remain Diamond. |
| Real assistive-technology testing is mandatory | A11Y-18 requires an audience-based desktop/mobile matrix. Geography alone does not force a commercial tool; real required pairings stay unresolved until tested. |
| Lighthouse house targets control Gold completion | OPS-02, median of 3 runs; Diamond release safety is separate. |
| Two-part run is available | `RUN_PART=1` then `RUN_PART=2`; the default is one run |
| Derived type may keep a commercial original's open substitute | Least fidelity cost |
| A shift that changes little on a monochrome reference is accepted | Stated in the README (CNT-16) |
| The client approves the brand shift | `docs/ACCEPTANCE.md` (DEL-14) |

## Open

| Item | Owner | Notes |
|---|---|---|
| First end-to-end run of v6 | Operator | The evidence validator has fixture tests; a full client delivery through the prompt is still unverified |
| Permission or legal advice on the reference design | Operator | Recommended before any client launch; see `LEGAL_NOTES.md` |
| A licence for this kit | Operator | None chosen; internal use until then |
| Where the repository is hosted and who can see it | Operator | It contains analysis of third-party sites; prefer private |
| LICENSE grantor placeholder in each delivered project | Operator, per client | Completed before handover (SEC-10) |
| Qualified legal/rights review and takedown plan | Operator, per client | LEG-17, LEG-18; counsel for unclear applicability, disputed rights and regulated activity |
| Splitting the run if a model times out | Operator | Use the two-part run |
| Additional assistive-technology coverage | Operator | Add the tools required by the actual audience and support policy (A11Y-18) |
| Whether to delete the original's captured text and images from `WS` after client acceptance | Operator | Lowers exposure; keep hashes and measurements |

## Production audit decisions, 2026-10-02

Required production checks take precedence over fidelity in the deployed build. An incomplete handover may finish, but cannot pass launch. Owner-confirmation status can become PASS only from dated human evidence. Missing inputs do not prove a feature or duty absent. Field performance is separate from lab performance. The evidence validator checks records, not whether a claimed test is truthful.

## Priority revision, 2026-10-05

The tier policy supersedes historical references to all-row Gold gates. Required means Diamond for launch and Diamond plus Gold for Gold completion. Contractual scope is still enforceable regardless of generic tier.
