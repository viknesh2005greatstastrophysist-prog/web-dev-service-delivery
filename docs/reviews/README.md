# Reviews

Every review was done by a separate Opus agent that read the files, fetched sources, ran small experiments and
fixed what it found in place. They are static reviews: nobody has run the prompt end to end yet. Paths inside the
reports point at the scratchpad where they were produced, and some mention files that are not in this repository;
the findings and verdicts are what matter.

| Folder or file | Edition | Verdict | Main findings |
|---|---|---|---|
| `v3-comparison-edition/` (4 rounds) | v3, comparison-video edition | GREEN after round 4 | Gate honesty, comparator reproductions, tool contracts |
| `v4-client-edition/` | v4 client deliverables | GREEN | Template mode, 122 changes, non-blocking input |
| `v6/01-*` | v6 clone-and-swap | GREEN after 2 blockers | Brand shift broke the fidelity gates; legal footer links deadlocked the reference build; 18 rows orphaned from the prompt |
| `v6/02-*` | Gold-standard pass | GREEN after 4 blockers | Targets scored below 0.98 on Lighthouse's own curve; CPU throttling too soft; Lighthouse can audit a 404 with `--ignore-status-code`; rule 9 clashed with rule 2 |
| `v6/03-run-parts-changes.md` | Run parts section | GREEN after 2 blockers | Handoff could never verify (dirty tree); part 1 statuses contradicted Finish. Change log only |
| `v6/04-*` | US legal edits | GREEN after 1 blocker | "Shipped build" had two meanings; derived palette lost contrast; one-line deploy switch was four places |

See `docs/research/gold-benchmark-table.md` for the table that checks each gold target against field data and
external checklists.
