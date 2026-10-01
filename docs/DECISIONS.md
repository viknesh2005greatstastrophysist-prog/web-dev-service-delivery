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
| Customers are in the United States | The deployed build for a US-facing client is `npm run build:a11y` (accessibility fixes on); `npm run build` stays the fidelity build |
| Gold standard across the whole checklist | Gold targets are the pass criteria for speed, interaction and experience rows; a miss needs a fidelity exception |
| A reference that misses a published floor is a FAIL | Not an exception, even if the reference misses it too |
| CPU throttling is calibrated | Lighthouse's 4x CPU slowdown is adjusted by the machine's benchmark index (checklist rule 3) |
| A11Y-21 and the touch-only hit areas stay | They change what some visitors see or feel; accepted |
| Observatory A+ is a must-pass live row | HOST-20; each scan is published |
| JAWS is required when the audience is North American | A11Y-18 (JAWS 55.5% vs NVDA 24.0% there, WebAIM survey 10) |
| Lighthouse CI blocks deploys at the gold targets | OPS-02, median of 3 runs |
| Two-part run is available | `RUN_PART=1` then `RUN_PART=2`; the default is one run |
| Derived type may keep a commercial original's open substitute | Least fidelity cost |
| A shift that changes little on a monochrome reference is accepted | Stated in the README (CNT-16) |
| The client approves the brand shift | `docs/ACCEPTANCE.md` (DEL-14) |

## Open

| Item | Owner | Notes |
|---|---|---|
| First end-to-end run of v6 | Operator | Nothing here has been run yet. Send the report back to tune the prompt |
| Permission or legal advice on the reference design | Operator | Recommended before any client launch; see `LEGAL_NOTES.md` |
| A licence for this kit | Operator | None chosen; internal use until then |
| Where the repository is hosted and who can see it | Operator | It contains analysis of third-party sites; prefer private |
| LICENSE grantor placeholder in each delivered project | Operator, per client | Completed before handover (SEC-10) |
| Counsel review of the draft legal pages and the takedown plan | Operator, per client | LEG-17, LEG-18 |
| Splitting the run if a model times out | Operator | Use the two-part run |
| Whether to buy a JAWS licence | Operator | Needed for North American audiences (A11Y-18) |
| Whether to delete the original's captured text and images from `WS` after client acceptance | Operator | Lowers exposure; keep hashes and measurements |
