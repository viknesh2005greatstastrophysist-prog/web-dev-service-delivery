# Policy tier review notes

## Sources

- `challenge/policy.json`: the 119 supplied requirements, tiers, class labels and verification proposals. Every row was reviewed once; IDs and class labels are preserved in `policy-proposal.json`.
- `/Users/vik/.codex/skills/fable-thinking/SKILL.md`: used to inspect actual rows, test candidate claims and look for failure cases.
- `/Users/vik/.codex/skills/accessibility/SKILL.md`: used only to keep accessibility outcomes distinct from implementation-specific state-walk and contrast tooling.
- No live site was tested and no legal or standards claim embedded in the packet was independently refreshed. Current legal applicability and standards need source checks when applied to a real release.

## Counterexamples that changed the proposal

- `SEO-03` and `EDGE-02` both address missing routes, but status and visitor recovery have different outcomes. A real 404 is useful search/route quality; broken links to required routes remain the release blocker in `SEO-08`.
- `UXF-01` treated a 400 ms response and every `cursor:pointer` node as an objective pass condition. A fast no-op is still broken; a legitimate network request may take longer while correctly reporting pending state in `UXF-02`.
- `EDGE-04`, `MOT-05`, and `EDGE-15` prescribe fixed cache, DPR, heap, byte and LCP limits without a user or project budget. The proposal retains missing-resource accuracy and graphics fallback, while moving tuning targets to optional or agreed performance budgets.
- `CNT-02` and `CNT-14` turn word-shingle and perceptual-hash matches into automatic rights failures. Common phrases, independent design similarity and valid shared licences can be false positives; matches should trigger review, while unlicensed reference content and public comparison builds remain blocked.
- `CNT-08`/`CNT-15` should follow the actual licence and permission. A legitimately licensed commercial font or permitted image use is not a defect; missing permission remains a rights blocker.
- `CNT-11` banned `noindex` on all production pages, which also rejects intentionally non-indexed routes. Route-level indexing policy can allow them while still blocking draft legal text and unintended placeholders.
- `DEL-08` required two builds and particular flags; the concrete release risk is deploying an unverified or private artifact. Identity and passed checks are required; a second build is not.
- `LEG-18` described a US safe-harbor workflow as a universal launch procedure. Its legal steps apply only when service content and legal reliance make them relevant; counsel determines scope.

No canonical checklist or production package was edited. This is a proposal for parent integration, not release evidence or legal approval.
