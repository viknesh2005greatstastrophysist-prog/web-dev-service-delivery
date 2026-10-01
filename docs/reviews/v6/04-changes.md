# Review 4 change log (exact-match replacements, each asserted to match once; script: apply.py, plus 4 follow-up single replacements)
Originals: v6.original.md, ck.original.md. Full diffs: v6.review4.diff, ck.review4.diff.

## Prompt (PROMPT_awwwards_clone_swap_v6.md)
1. §4 Which build ships: DOJ sentence corrected (ADA web guidance names WCAG and the Section 508 Standards as helpful guidance, no binding standard for private businesses); the README records which line decided "US-facing"; host build command, CI deploy job, `npm run verify` and DEPLOY.md run `npm run build:deploy` (one package.json line that runs `build:a11y`, else `build`), so "changes one line" is real; "state walk's contrast check" became "the state walk"; switch also recorded in the accessibility statement; NEW definition: "shipped build" = deployed build except comparator and motion gate on app, swap probe, copy-fit and polish (fidelity build); reference build always built with A11Y_FIXES unset; both builds write `build-id.txt` with `a11y=on|off`; leak checks run on both outputs.
2. §4 Build discipline: WebGL, canvas and SVG attribute colours read the colour tokens at runtime.
3. §5 Production gate: "shipped build (§6)" -> "deployed build (§4, §6)".
4. §5 Eyeball pass: §7 baseline is on app's fidelity build.
5. §6 step 2 derived palette: after the hue rotation, lightness is set so WCAG relative luminance equals the original's, chroma lowered only as far as sRGB needs; direction (plus or minus) chosen to keep more chroma; signed angle recorded.
6. §6 step 2: contrast pair rule allows 1% for 8-bit rounding (J).
7. §6 step 2 derived type: pick the closest face by the §4 measures; a commercial original's §4 substitute qualifies (family then stays as built).
8. §6 step 2 comparator: non-rgb expected colours (`oklch()`, `color(srgb ...)`) are converted for the map lookup and written back; colours the tokens cannot reach are listed as unshifted in brand-map.json and CONTENT_NOTES.
9. §6 step 4 heading "Strict comparator on `app`"; serves app's fidelity build.
10. §6 step 4: motion gate on the fidelity build, state walk on the deployed build.
11. §6 step 6: rebuild both builds after each batch; comparator and motion gate on app's fidelity build.
12. §7 intro, invariant 2 and Method 3: fidelity build named explicitly.
13. §8 README: brand shift (client or derived, angle, families, or none), which build is deployed and why, gate table with a build column.
14. §8 CONTENT_NOTES: brand shift and what it left unshifted.
15. §8 FIDELITY_EXCEPTIONS: which build is deployed and how to switch.
16. §8 PROVENANCE: cites the report as Part 2; records who directed the work and who selected, arranged, modified or reviewed what (the report's terms).
17. §8 content:sync rebuilds with `npm run build:deploy`.
18. §8 audit:live records the live `build-id.txt` `a11y` value.
19. Finish gate 4: shipped side is app's fidelity build. Gate 5: `npm run build:a11y` must also exit 0. Gate 8: shipped side is the deployed build. Gate 10: covers LEG-12 clients as well as US-facing ones. Gate 15: contrast tolerance points to §6 step 2.
20. Final message: brand shift (or none), the deployed build and why.
21. Run parts item 3: "shipped-build motion gate" -> "motion gate on `app`" (Run parts +1 word).

## Checklist (PRODUCTION_CHECKLIST_clone_swap.md)
22. Rule 2: "Elsewhere in this checklist the shipped build is the deployed build, except for the fidelity gates."
23. Rule 7: CNT-16's predicate comes from `brand.md`.
24. Rule 9: accessibility floors: FIDELITY-EXCEPTION in the fidelity build, met by the A11Y_FIXES fix in a deployed build:a11y build.
25. A11Y-21: applies to the fidelity build; build:a11y meets it through DEL-08; Verify on the fidelity build.
26. DEL-04: which build is deployed and how to switch.
27. DEL-08: build:deploy; production audit on the deployed build; build-id `a11y` value; Verify reads it.
28. CNT-08: covers the derived open-licensed faces under the default shift.
29. CNT-14: dist from each of the two builds.
30. CNT-16: 1% allowance for 8-bit rounding (J).
31. SEC-10: LICENSE has a grantor (developer placeholder), carves out third-party parts (LEG-14), hedges the AI point as the Copyright Office's view, cites the report by title.
32. DEL-05: report's terms (selected, arranged, modified or reviewed).
33. LEG-18: 512(c) safe-harbour framing (removal is the condition of the safe harbour, 512(c)(1)(C), 512(l)); registrar acts under its own terms; counter-notice consents to a federal court's jurisdiction; 512(g) restoration 10 to 14 business days after receipt unless the claimant first tells the host it has filed suit.
34. Footer note: the deployed build of a US-facing client carries the fixes.

Counts: 254 rows (unchanged by this review), 0 em or en dashes, prompt +328 words (16,144 -> 16,472), checklist +165 words (21,477 -> 21,642).
