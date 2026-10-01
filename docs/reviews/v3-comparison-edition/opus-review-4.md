GREEN

# Round 4 re-review of PROMPT_awwwards_clone_v3.md and PRODUCTION_CHECKLIST.md

Date 2026-09-30. No round-3 copies were in the scratchpad, so I checked every edit in place at its location in the current files. No file under `/Users/vik/Downloads/scrollcraft (2)/` was edited.

Result: 0 HIGH, 0 MEDIUM, 2 LOW.

## 1. Status of round-3 findings

| ID | Status | Evidence (current text) |
|---|---|---|
| M1 | FIXED | Gate 6 now reads: "single declarations and blocks of fewer than 3 declarations are exempt ...; blocks and runs that also appear verbatim in the `dist` files of an open-source package in the clone's lockfile are exempt, with each exemption listed by package and file". |
| S1 | FIXED | Rule 4: "do not ship its images, video, fonts or logo, and download none of them except images into `WS/evidence` as described below." |
| S2 | FIXED | Gate 2: "excluding states marked `state-changing on a live site`: 0 failures." The §5 sentence has the same clause. |
| S3 | FIXED | Gate 6: "(one declaration per line) ... appears in both the shipped CSS and the evidence stylesheets". The JS half is gone. |
| S4 | FIXED | §2: "Dismissing a consent banner with its Reject or essential-only choice is allowed, and is done identically on both sites." |
| S5 | FIXED, with a residual | Rule 7: "`curl -s <url>/build-id.txt` equals the random id that `npm run build` writes into the served output". See T1 and T2. |
| S6 | FIXED | HOST-12 Verify: "`dig +dnssec`; owner-only items are listed as open in the README". |

## 2. Mechanical re-checks

- Em dashes (U+2014) and en dashes (U+2013): 0 in both files.
- Checklist tables: 195 rows, every one with 4 columns.
- Row IDs: 167, no duplicates, no gaps. Every row ID cited in either file exists.
- Finish gates are numbered 1 to 12, matching the text "twelve".
- Upstream `assert-styles.mjs` at the pinned commit still passes the four smoke mismatches and `400px` vs `400.9px`, and fails the missing selector (5/6 passed). `transform-origin` `10px 20px` vs `10px 60px` still passes upstream.

## 3. Remaining findings (LOW only)

| ID | Sev | Location (exact text) | Problem | Fix (exact text) |
|---|---|---|---|---|
| T1 | LOW | P rule 7: "Start dev and preview servers ... confirm the port is serving your build before trusting a capture (`curl -s <url>/build-id.txt` equals the random id that `npm run build` writes into the served output)" | The dev server never runs `npm run build`, so this check cannot pass for `npm run dev`. | Replace the parenthesis with: "(`curl -s <url>/build-id.txt` equals the random id that `npm run build` writes into the build output, or, for the dev server, the id the dev script writes to `public/build-id.txt` at start)". |
| T2 | LOW | P §4 Production build bullet (no mention of `build-id.txt`) | The artifact appears only in rule 7, so a model could miss it until capture time. It is LOW, not MEDIUM: rule 7 already says `npm run build` writes it, the file is harmless to ship, and no gate depends on it. | Append to the §4 Production build bullet: "`npm run build` writes a random `build-id.txt` to the output root (used by ground rule 7)." |

## 4. Could not verify (unchanged, not blocking)

- Whether GSAP's ticker idles on its own, which affects how achievable MOT-05's "0 own rAF calls" check is.
- Playwright's default autoplay policy, which A11Y-14 depends on.
- The current SIL OFL FAQ position on subsetting and Reserved Font Names.
