# Review 4 report: four US-legal edits

**Verdict: GREEN after fixes.** Before the fixes it was NOT GREEN. The two-builds edit left "shipped build" meaning two different things, and several gates would have run on the wrong build. Those problems are fixed. What remains is in the residual risks and in the decisions for the operator.

## Blocker (fixed)
- **B1. "Shipped build" had two meanings (prompt §4 to §7 and Finish; checklist rules 2 and 9).**
  - What was wrong:
    - §7 said "shipped build (`app`, built with the flag off)", while edit 2 made the shipped build the accessibility build.
    - Read literally, §6 step 4 (comparator), §6 step 6 (production loop), gate 4 (motion) and §7 invariant 2 would have run the fidelity comparisons on the accessibility build. A contrast, target-size or motion fix would then fail them.
    - Both builds write `dist`, with no way to tell which one is being served (a leaked flag would go unnoticed).
    - Gate 5 never built `build:a11y`.
    - The leak checks covered only one output.
  - What I changed:
    - Added one definition in §4 and a one-line pointer in checklist rule 2: the shipped build is the deployed build, except that the comparator and motion gate on `app`, the swap probe, copy-fit and polish use the fidelity build. The reference build is always built with `A11Y_FIXES` unset.
    - `build-id.txt` now records `a11y=on` or `a11y=off`.
    - The leak checks (gates 6 and 13, CNT-14) now run on both outputs.
    - Named the build explicitly in §6 steps 4 and 6, §7 (intro, invariant 2, Method 3), gates 4, 5 and 8, and the step 4 heading.

## Major (fixed)
- **M1. Derived palette lost contrast (§6 step 2).**
  - Wrong: keeping OKLCH lightness lost contrast in 4 to 6 of 16 pairs, by up to 11.6% (table below). At 60° one pair fell below 4.5:1. The fallback kept the result safe, but it froze exactly the colours that lost contrast. So on a site whose only chromatic colour is an accent (acid lime, signal red), the default did nothing.
  - Fix: after the rotation, set lightness so WCAG relative luminance equals the original's, and lower chroma only as far as sRGB needs.
  - Also: CNT-16 and §6 allow 1% for 8-bit rounding (J), because even exact luminance holding loses up to 0.4% to rounding, and a strict "no lower" rule would trigger the fallback everywhere. The direction (plus or minus) is the one that keeps more chroma: at +45° red #E10600 becomes olive #986608, at -45° it becomes magenta #CE1A99. The signed angle is recorded.
- **M2. The "one-line" switch was really four places.** The Netlify config, `vercel.json`, the Cloudflare Pages dashboard and the CI job each held the build command. Fix: they, plus `npm run verify` and DEPLOY.md, all run `npm run build:deploy`, a single `package.json` line. `content:sync` rebuilds with it. DEL-08 checks it. `audit:live` records which build is live.
- **M3. Derived type had no rule for choosing among qualifying faces.** It also did not say what happens with a commercial original. Fix: pick the closest face by the §4 measures. A commercial original's §4 substitute qualifies, so that family stays as built (see Decision 1). Open-licensed originals now get a different family, as edit 1 intended. CNT-08 now covers derived faces. The no-candidate fallback already existed: the family is not shifted and the reason is logged.
- **M4. Parts of the page the shift could not reach.**
  - `--brand-map` rewrote only `rgb()` and `rgba()`. An original whose computed colours are `oklch()` or `color(srgb ...)` would fail gate 15 now that the shift is on by default. Fix: convert those for the lookup and write them back in their own function.
  - Hard-coded WebGL, canvas and SVG-attribute colours would not shift. Fix: §4 now makes them read the tokens at runtime.
  - Colours inside images, video, placeholders, `filter` functions and third-party defaults are now logged as unshifted in `brand-map.json` and CONTENT_NOTES.
  - Already fine: `currentColor`, blend modes, gradients, shadows and overlays follow the tokens.
- **M5. SEC-10 LICENSE.**
  - It had no grantor. Fix: a developer placeholder that the operator completes.
  - It granted "every right in the delivered code", which included OFL fonts, GSAP and other third-party parts. That contradicted LEG-14 and THIRD_PARTY_NOTICES. Fix: third-party parts are carved out.
  - The AI point is now hedged as the Copyright Office's view and cites the report by title.

## Minor (fixed)
- **DOJ wording.** The ADA web guidance (ada.gov, fetched) names WCAG and the Section 508 Standards as "helpful guidance" and leaves businesses flexibility. The old text said DOJ "sets no other standard", which overclaimed. Corrected.
- **LEG-18, checked against 17 U.S.C. 512 (Cornell LII statutory text).**
  - Changed: removing the material is the host's condition for keeping its safe harbour, not a duty (512(c)(1)(C) and 512(l)).
  - Changed: restoration is "not less than 10, nor more than 14, business days following receipt of the counter notice". It does not happen if the claimant first tells the host's agent it has filed an action (512(g)(2)(C)).
  - Changed: the counter-notice consents to a federal district court's jurisdiction (512(g)(3)(D)).
  - Changed: a registrar acts under its own terms, not section 512. The row did not conflate registrars and does not mention payment processors.
  - Already correct: LEG-18 is in the launch-checklist step. As a `G-O` row it is handled by gate 10's `OWNER-CONFIRM` rule and by checklist rule 8's line for every row.
  - I did not fetch copyright.gov/512; I used the statute itself.
- **AI authorship, checked against the report PDF (pypdf).** The report says:
  - "Copyright does not extend to purely AI-generated material".
  - "prompts do not alone provide sufficient control".
  - Humans can be entitled to copyright in "selection, coordination, or arrangement ... or creative modifications".

  The edits did not overclaim: "may limit" is correctly hedged. DEL-05 and PROVENANCE now use the report's terms (who directed the work, and who selected, arranged, modified or reviewed what) and cite Part 2.
- **Stale wording fixed:**
  - The README, CONTENT_NOTES and final message said "if one was applied" or "if any". They now report the shift (client's or derived, the angle, the families, or `none`) and which build is deployed and why.
  - The README gate table has a build column.
  - Gate 10, rule 9 and the footer note now cover LEG-12 clients as well as US-facing ones.
  - A11Y-21 is limited to the fidelity build; `build:a11y` meets it through DEL-08.
  - DEL-04 and FIDELITY_EXCEPTIONS now say which build is deployed and how to switch.
  - Rule 7 now says CNT-16's predicate comes from `brand.md`.
- **Run parts:** one phrase changed. The handoff needs nothing new:
  - The font route is already recorded.
  - Part 2 works out the US-facing decision again from the `CLIENT_INPUT` files, whose hashes the handoff checks. A changed `legal.md` already triggers a redo of the checklist map and the production build.

## Contrast experiment
Script: `lab/hue_rotation.py`. 16 award-style pairs, 13 of them with a chromatic colour (OKLCH chroma 0.02 or more).

| Rule | 30° | 45° | 60° |
|---|---|---|---|
| As written: keep L and C, clip channels | 6/16 lose, worst 10.8%, 0 drop below the threshold | 5/16, 8.6%, 0 | 5/16, 11.6%, **1 below 4.5** (red 4.97 to 4.39) |
| As written: keep L, reduce chroma into gamut | 5/16, 7.2%, 0 | 5/16, 9.3%, 0 | 4/16, 10.8%, 1 below |
| Fixed: hold relative luminance | 3/16 lose 0.4% or less (8-bit rounding), 0 | 6/16, 0.3% or less, 0 | 7/16, 0.3% or less, 0 |

The pairs that lost contrast under the rule as written were acid lime and black (both ways round), signal red on white, cream on forest green, and pastel peach on white. Under the fallback each of those colours would stay the original's.

**Honest limits of the default:**
- A mostly neutral reference (black, white and greys, common among winners) gets no palette change.
- If that reference also uses a commercial font, the derived type is the §4 substitute it already ships, so the default shift changes nothing beyond §4.
- An accent-only site now changes only its accent.

## Which build each gate or step runs on (after fixes)

| Gate or step | Build |
|---|---|
| §5: comparator, target validation, line parity, motion, eyeball, state walk; gates 1 and 2 | Reference build (`brand.css` emptied, `A11Y_FIXES` unset) and the original |
| §6 step 3 swap probe; step 5 copy-fit; gate 15 | Fidelity |
| §6 step 4 comparator and motion gate on `app`; gate 4 (shipped side) | Fidelity |
| §6 steps 4 and 6 state walk; gate 8 (shipped side); EDGE-14 | Deployed |
| §6 step 6 production audit; gates 10 and 11 (beat-or-match); gold targets (rule 9); SPD-13; A11Y-18 | Deployed |
| §6 step 6 checks after each batch | Comparator and motion: reference and fidelity. State walk: deployed. Rest frames: reference |
| §6 step 7 leak check; gates 6 and 13; CNT-14 | Output of both builds |
| §7 polish, invariants 1 and 3, gate 7 | Fidelity (invariant 2's production audit: deployed) |
| Gate 5 | `build` and `build:a11y` exit 0; `npm run dev` (flag unset) |
| `npm run verify`, CI deploy job, host build command, lighthouserc, `content:sync` | `build:deploy` (the deployed build) |
| `npm run start` | Whichever `dist` was built last; `build-id.txt` says which |
| `reference-build.mjs` | Copies app source, empties `brand.css`, flag unset |
| `audit:live`; gate 14 smoke test | Deployed (records `a11y` from the live `build-id.txt`) |
| A11Y-21 | Fidelity (`build:a11y` meets it through DEL-08) |

## Mechanical checks (`mechanical.txt`)
- 254 rows, no duplicate IDs, 4 cells and a valid class on every row, IDs sorted in all 18 sections.
- Every cited ID exists; every § reference, gate number, rule number and step number resolves.
- The prompt's section list equals the checklist's.
- 0 em dashes and 0 en dashes in both files.
- Prompt went from 16,144 to 16,472 words (+328); Run parts +1 word. Checklist went from 21,477 to 21,642 words (+165).

## Residual risks
- The derived palette has not been looked at by a person. Holding luminance can mute saturated warm hues (the direction rule mitigates this), and colours composited with alpha keep their contrast only approximately (the contrast table and the fallback catch this).
- The accessibility fixes must be written against the brand-shifted colours. The prompt does not say this, but DEL-08's axe run on the flag-on build enforces it.
- The 1% rounding allowance (J) slightly loosens CNT-16's "no lower" rule. The hard 4.5:1 and 3:1 floors are unchanged.
- A client who supplied licensed files of the original's own typeface still gets a different family under the default. They can avoid that by setting `design_shift: palette`.
- The LICENSE and section 512 wording is engineering hygiene, not legal advice. If the code cannot be copyrighted there may be little to grant, so the client contract matters more.
- This is a text review only. No live agent run was done, and the experiment uses 16 example pairs.

## Decisions for the operator
1. **Derived type when the original's font is commercial.** I applied the literal reading: the §4 substitute counts as "not the original's family", which costs the least fidelity. If you want more visual distance, exclude the substitute too. Recommendation: keep it as is.
2. **Holding luminance instead of "keep lightness".** This departs from the wording you approved, and is needed so that accent-only sites change at all. Recommendation: confirm it.
3. **The 1% rounding allowance and the direction rule.** Recommendation: keep both.
4. **Client sign-off.** Consider adding the derived palette and type to the client's approval fields in `docs/ACCEPTANCE.md` (not added). Recommendation: add them.
5. **Monochrome references.** The default shift is close to a no-op on them. Accept this, or prefer chromatic targets in §1. Recommendation: accept, and say so in the README, which the new README wording now does.
6. **LICENSE grantor.** The developer placeholder must be completed by the operator before handover.
