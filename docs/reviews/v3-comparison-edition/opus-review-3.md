NOT GREEN

# Round 3 re-review of PROMPT_awwwards_clone_v3.md and PRODUCTION_CHECKLIST.md

Date 2026-09-30. Both files were diffed against `v3.before-round2.md` and `checklist.before-round2.md`, and the changed text was read in context. No file under `/Users/vik/Downloads/scrollcraft (2)/` was edited.

Result: 0 HIGH, 1 MEDIUM (new, from the N5 wording), 6 LOW.

## 1. Mechanical checks

- Em dashes (U+2014) and en dashes (U+2013): 0 in both files.
- Checklist tables: 195 rows, every one with 4 columns.
- Row IDs: 167, no duplicates, no gaps. HOST now runs 01 to 17.
- Classes: 88 G, 13 G-L, 30 R, 1 R-L, 34 C, 1 C-L.
- Every cited row ID exists in both files.
- Finish gates are numbered 1 to 12, and the text "twelve" matches. The references "gate 6" and "gates 1 to 6" resolve.
- The pinned contract link returns 200.
- New smoke case run against upstream `assert-styles.mjs` at the pinned commit: `transform-origin` `10px 20px` vs `10px 60px` gives "1/1 passed", so upstream still passes the first four cases as the prompt states.

## 2. Status of round-2 findings

| ID | Status | Note |
|---|---|---|
| N1 | FIXED | New §2 bullet, plus "States that are state-changing on the original are exempt (see §2)". Wording residual in S2. |
| N2 | FIXED | "The sole exception is the demo form's post-submit message" is in P rule 5 and C rule 2. |
| N3 | FIXED | SEO-01: "The title matches the original's title with the brand name only ... notice goes in the meta description." |
| N4 | FIXED | MOT-11 now mirrors the original's 30-versus-60 fps dependence. |
| N5 | PARTIAL | Pretty-printed runs replace the verbatim-line check, but "no identical selector-plus-block" creates M1 below. |
| N6 | FIXED | Evidence images or slot crops are allowed, with at least one per slot. Wording residual in S3. |
| R1 | FIXED | |
| R2 | FIXED | |
| R3 | FIXED | |
| R4 | FIXED | |
| R5 | FIXED | |
| R6 | FIXED | |
| R7 | FIXED | |
| R8 | FIXED | |
| R9 | FIXED | |
| R10 | FIXED | |
| R11 | FIXED | |
| R12 | FIXED | |
| R13 | FIXED | |
| R14 | FIXED | |
| R15 | FIXED | |
| R16 | FIXED | |

## 3. Remaining findings

| ID | Sev | Location (exact text) | Problem | Fix (exact text) |
|---|---|---|---|---|
| M1 | MED | P gate 6: "no run of 5 or more consecutive identical declarations or statements, and no identical selector-plus-block, appears in both the shipped CSS or JS and the evidence stylesheets (single declarations are exempt ...)" | False positive by design. When the original and the clone use the same open-source package, the package's own CSS ships identically in both: Tailwind preflight, `lenis/dist/lenis.css` (which MOT-04 requires when the original uses Lenis), Swiper, normalize.css. Those identical blocks and runs fail gate 6 even though nothing was lifted from the original. Small resets such as `*,::before,::after{box-sizing:border-box}` also collide. Honest clones would then report FAIL, or dodge by rewriting selectors. | Append to gate 6: "Blocks and runs that also appear verbatim in the `dist` files of an open-source package in the clone's lockfile are exempt (list each exemption with the package and file), as are blocks of fewer than 3 declarations." |
| S1 | LOW | P ground rule 4: "Do not hotlink from the original, and do not ship or download its images, video, fonts or logo." Later in the same rule: "fetch its images into `WS/evidence` only" | The two sentences contradict each other literally, though the later one is specific. | "Do not hotlink from the original, do not ship its images, video, fonts or logo, and download none of them except images into `WS/evidence` as described below." |
| S2 | LOW | P §5: "Final state: the clone has 0 failures and the original has 0 failures on the same `rest` and `motion` set."; P gate 2: "The same assertions on the live original: 0 failures." | These do not repeat the §2 exclusion of state-changing states, so a literal reader would try to measure them on the original. | Gate 2: "The same assertions on the live original, excluding states marked `state-changing on a live site`: 0 failures." Add the same clause to the §5 sentence. |
| S3 | LOW | P gate 6: "appears in both the shipped CSS or JS and the evidence stylesheets" | Evidence holds only stylesheets (rule 4 allows reading stylesheets, not JS), so the JS half of the check has nothing to compare against. | "appears in both the shipped CSS and the evidence stylesheets". Drop "or JS" and "or statements". |
| S4 | LOW | P §2 new bullet: "Do not submit a form, subscribe, sign up, add to cart or send any other write" vs L57: "consent banners (handle them the same way on both sites when capturing)" | Clicking a consent button sends a consent write to the original's consent platform. Without a rule, models may split on whether that is allowed. | Append to the bullet: "Dismissing a consent banner with its Reject or essential-only choice is allowed and is done identically on both sites." |
| S5 | LOW | P ground rule 7: "confirm the port is serving your build (`curl -s <url> \| grep -o \"<title>.*</title>\"`)" | Since SEO-01 the clone's title equals the original's, so the title no longer identifies your build as distinct from, for example, an earlier build left running on the same port. | "confirm the port is serving your build by fetching a build marker (`curl -s <url>/build-id.txt` equals the id written by `npm run build`)". |
| S6 | LOW | C L3: "Every row below is checkable by an unattended agent"; C HOST-12: "Checklist confirmed by the owner" | This is an R row that cannot be done unattended. | HOST-12 Verify: "`dig +dnssec`; the owner items are listed as open in the README". |

## 4. Verified in this round

- All N1 to N6 and R1 to R16 edits are present at the quoted locations.
- Cross-references resolve: rule 7 lists existing rows, and `-L` rows now have a stated predicate.
- `POLISH` paths are consistent: `shots/before/*`, `shots/after/*` and `source-before`.
- HOST-08 is now local only, and HOST-16 and HOST-17 carry the live-only parts.
- The `transform-origin` smoke case behaves upstream as claimed.

## 5. Could not verify (unchanged)

- Whether GSAP's ticker idles on its own, which affects how achievable the MOT-05 "0 own rAF calls" check is.
- Playwright's default autoplay policy, which A11Y-14 depends on.
- The current SIL OFL FAQ position on subsetting and Reserved Font Names.
