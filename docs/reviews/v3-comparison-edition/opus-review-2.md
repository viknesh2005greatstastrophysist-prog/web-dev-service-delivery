NOT GREEN

# Re-review of PROMPT_awwwards_clone_v3.md and PRODUCTION_CHECKLIST.md after fixes

Date 2026-09-30. Both edited files were read in full and diffed against `v3.before-review-fixes.md` and `checklist.before-review-fixes.md`. No file under `/Users/vik/Downloads/scrollcraft (2)/` was edited.

Remaining or new: 1 HIGH, 5 MEDIUM, 16 LOW. Every original HIGH and MEDIUM is fixed; the remaining HIGH and MEDIUM items were introduced by the fixes or exposed by them.

## 1. Mechanical re-checks

- Em dashes (U+2014) and en dashes (U+2013): 0 in both files.
- Checklist tables: 193 rows, every one with 4 columns.
- Row IDs: 165, no duplicates, no gaps. A11Y now runs 01 to 14 and MOT 01 to 14; BACK still starts at 00.
- Classes: 89 G, 11 G-L, 29 R, 1 R-L, 34 C, 1 C-L.
- Every row ID cited in either file exists. The twelve gates and fifteen sections match the text.
- Strict smoke cases against upstream `assert-styles.mjs` (pinned commit), run in `review/fx/smoke-*.json`: padding, box-shadow, opacity and transition-duration all PASS upstream, confirming "The upstream script passes the first four". `400px` vs `400.9px` passes. The missing selector fails. The z-index 10 vs 11 and line count 3 vs 4 claims also PASS upstream, confirmed.
- RSP-05's new verify method works. On a 14x14 link, `elementFromPoint` sampling gave 9/49 hits with no hit area and 49/49 with an invisible `::before` expansion (`review/sc/efp.mjs`).
- MOT-05's hidden override works: the page receives `visibilityState` "hidden". The browser keeps firing rAF (31 callbacks in 500 ms), so the check must count the page's own `requestAnimationFrame` calls (see R12).
- Lighthouse 13.5.0 on `http://127.0.0.1`: `is-on-https` scores 1, so Best Practices is comparable; `lcp-breakdown-insight` exists. This resolves one earlier "could not verify".

## 2. Status of every earlier finding

| ID | Status | Note (quoted new text where not fully fixed) |
|---|---|---|
| H1 | FIXED | C rule 2 and P rule 8 now cover "anything a visitor can see or feel". Residuals are N3 and R10. |
| H2 | FIXED | LEG-03, LEG-11, LEG-12 and P rule 5 agree. R14 is a small wording ambiguity. |
| H3 | FIXED | Tablet and mobile rest states now come before the G rows. |
| H4 | FIXED | Allowed fixes only move toward the original's measured values. |
| H5 | FIXED | Wording matches the tested shoot.mjs behaviour. |
| H6 | FIXED | Baseline is `POLISH/shots/before/rest`, taken after `07-polish.md`, with a determinism check. |
| H7 | FIXED | No public deploy and no accounts; LEG-16 is G. HOST-08 and HOST-10 residuals are in R9. |
| H8 | FIXED | rAF recorder, completion time and deviation formula are all defined. |
| M1 | FIXED | |
| M2 | FIXED | |
| M3 | FIXED | Verified above. R5 is a nit about the fixture. |
| M4 | FIXED | |
| M5 | FIXED | |
| M6 | PARTIAL | The endpoint is now prescribed, but N1 and N2 follow from it. |
| M7 | FIXED | |
| M8 | FIXED | Tested. |
| M9 | FIXED | P L153's README list differs from rule 1 (R8). |
| M10 | FIXED | Rule 7's list is incomplete (R6). |
| M11 | PARTIAL | TYP-06, TYP-22, MOT-05 and OPS-01 are fixed. HOST-08 "confirmed on the deployed URL", HOST-10 "releases are tagged, and rollback to the previous deploy" and OPS-02 "CI run fails when a budget is exceeded" remain G but need a deploy or remote CI (R9). |
| M12 | FIXED | |
| M13 | FIXED | |
| M14 | FIXED | |
| M15 | FIXED | Invariant 5 wording nit (R4). |
| M16 | FIXED | Mask cap nit (R11). |
| M17 | FIXED | |
| M18 | FIXED | Firefox nit (R7). |
| M19 | FIXED | |
| M20 | FIXED | The new wording creates N1. |
| M21 | FIXED | Social-icon nit (R15). |
| M22 | FIXED | robots wording nit (R13). |
| L1 to L6, L8 to L15, L17 to L21 | FIXED | |
| L7 | PARTIAL | New TYP-12 text: "If `html`'s background is asserted, set the colour on `body` and `:root` via `color-scheme` only." `color-scheme` cannot set a colour, and `:root` is `html` (R1). |
| L16 | NOT DONE | Intentional; accepted. |

## 3. New or remaining findings

| ID | Sev | Location (exact text) | Problem | Fix (exact text) |
|---|---|---|---|---|
| N1 | HIGH | P L52: "Every interactive state"; P L38: "`unreached[]` ... is allowed only for states that cannot be triggered on the original ... Gate 8 fails if ... the clone reaches fewer states than the original"; P L98: "the original has 0 failures on the same `rest` and `motion` set" | Form success and error states, newsletter signups and similar states **can** be triggered on the original, so the new rule makes the agent submit the real business's forms, unattended, to avoid failing gate 8 and target validation. That means sending messages on the user's behalf to a third party. The M20 fix made this worse. | Add to P §2 (after L52): "Never submit a form, subscribe, sign up, add to cart or send any other state-changing request to the original. Record those post-submit states in `unreached[]` with the reason `state-changing on a live site` (allowed without a trigger attempt), take their styling from the authored rules in the original's stylesheets, and exclude them from target validation." Append to P L38: "States that are state-changing on the original are exempt (see §2)." |
| N2 | MED | C BACK-01 and P L84: "the form then shows the original's own success component with the text \"Demo rebuild: nothing was sent.\""; C rule 2: "No production item may change anything a visitor can see ... in any ... interaction"; P rule 5: "Add no visible text or link to any in-scope page for legal or production reasons" | This is a direct contradiction: the mandated demo text is a visible change in an interaction state. | Append to C rule 2 and P rule 5: "Sole exception: the demo form's post-submit message required by BACK-01." |
| N3 | MED | C SEO-01 (G): "Because this is an unofficial rebuild, the title says so." | This conflicts with P rule 5 ("Add no visible text ... for legal or production reasons") and with rule 2, because the tab title is visible browser UI. Models will split on it. | SEO-01: "Unique `<title>` and meta description. The title matches the original's title, with the brand name only and never the domain; the unofficial-rebuild notice goes in the meta description." |
| N4 | MED | C MOT-11 (G): "Lerps and inertia use elapsed time, not a per-frame constant, so 120 Hz and 30 Hz displays give the same result." | If the original uses per-frame lerp (common on award sites), a time-based clone feels different from it on a 120 Hz recording machine. That breaks rule 2's "scroll feel". This row came from my own earlier suggestion, and it was wrong as a G row. | "MOT-11: The clone has the same frame-rate dependence as the original. Run both traces at 60 fps and at 30 fps (rAF skipping every other frame); the clone's 30-versus-60 deviation stays within the motion-gate tolerances of the original's 30-versus-60 deviation." |
| N5 | MED | P gate 6: "no line of 60 or more characters of shipped CSS or JS appears verbatim in the evidence stylesheets" | Minified CSS is one line, so the check is either meaningless or a false positive. It also clashes with rule 4's "measured values are facts and stay identical": a long gradient or `transition` declaration copied from a measured value would trip it. This was also my earlier wording. | "After formatting both sides with the same pretty-printer (one declaration per line), no run of 5 or more consecutive identical declarations, and no identical selector-plus-block, appears in both shipped CSS and the evidence stylesheets. Single declarations are exempt (measured values stay identical). Shipped JS is compared the same way on formatted statements, runs of 5." |
| N6 | MED | P rule 4: "do not ship or download its images ... You may ... measure its images ... keep those evidence files in `WS/evidence`"; gate 6: "no shipped raster is within Hamming distance 10 (dHash) of any evidence image" | It is ambiguous whether downloading images into evidence is allowed. If it isn't, the dHash gate has nothing to compare against. Models will split between downloading and not, so the gate is either vacuous or treated as a rule break. | Rule 4: "You may fetch the original's images into `WS/evidence` only, for measurement and gate 6, never into the app. Alternatively, save a screenshot crop of each image slot to `WS/evidence`; gate 6 compares shipped rasters with whichever evidence images exist and must list at least one per image slot." |
| R1 | LOW | C TYP-12 (quoted in L7 above) | The new text is technically wrong. | "If `html` computes transparent and `body` has an opaque background, the canvas already takes `body`'s colour (CSS background propagation), which counts as PASS; otherwise, if `html`'s background is asserted, it is a `FIDELITY-EXCEPTION`." |
| R2 | LOW | C TYP-22: "only where that leaves the computed height unchanged at the four viewports" | In headless emulation `svh` equals `vh`, so this always holds and effectively mandates `svh`, which changes heights on real phones compared with an original that uses `vh`. | "Keep the original's viewport units exactly; record whether it uses `vh`, `svh` or `dvh`." Class R. |
| R3 | LOW | P L144: "re-run the harness (desktop, mobile, reduced)" | The key is now `laptop`, and no after-run path is given. | "(laptop, mobile, reduced) into `shots/after/{laptop,mobile,reduced}`". |
| R4 | LOW | P invariant 5: "the project is byte-identical to `POLISH/source-before`" | Should say `<name>/app`, since the project also contains WS. | "`<name>/app` is byte-identical to `POLISH/source-before`". |
| R5 | LOW | P L92 smoke case "a `padding` value" | `padding` is a shorthand, which §3 forbids ("never `padding`"), so a strict comparator could reject it for the wrong reason. | Use "`transform-origin` `10px 20px` against `10px 60px`"; upstream passes it the same way (first-number match). |
| R6 | LOW | C rule 7 list | It omits RSP-07, A11Y-10 and MOT-06 (which is always on). `-L` rows have no predicate. | Add RSP-07 and A11Y-10. Add: "`-L` rows use the predicate `README states not deployed (LEG-16)`." |
| R7 | LOW | P L40: "`{hasTouch: true, isMobile: true, deviceScaleFactor: 2}`" | Playwright does not support `isMobile` in Firefox, which RSP-06 runs. | Append: "(in Firefox omit `isMobile`)". |
| R8 | LOW | P L153: "(Lighthouse scores, LCP, CLS, TBT, bytes, requests, JS bytes)" | Differs from C rule 1's numeric list (MOT-01, SEO score without `is-crawlable`, LCP minus TTFB). | "(every numeric row listed in checklist rule 1)". |
| R9 | LOW | C HOST-08, HOST-10, OPS-02 (class G) | Each needs a deployed URL or a remote CI run. | Split into a local G part (config committed; clean-clone build; `lhci autorun` fails locally on a lowered budget) and a `-L` part (deployed confirmation, tags and rollback on the host). |
| R10 | LOW | C A11Y-06: "set `scroll-padding-top` at least the header height" | This moves anchor landing positions compared with the original, which rule 2 covers only implicitly. | Append: "unless the original lands anchors elsewhere (rule 2)". |
| R11 | LOW | P invariant 1: "infinite CSS animations paused at their rest value"; masks | "Rest value" of an infinite animation is undefined, and there is no cap on masked area. | "paused at `currentTime` 0; masks may cover at most 5% of each frame, and the README lists them." |
| R12 | LOW | C MOT-05 Verify: "assert the rAF count over 2 s is 0"; MOT-03 and MOT-05: "5 route changes" | The browser keeps firing rAF after the override (tested), so the check must count the page's own calls. Also, a single-route scope has no route changes. | "wrap `requestAnimationFrame` and count the page's own calls"; "5 route changes, or 5 unmount/remount cycles on a single-route scope". |
| R13 | LOW | P L59: "honour `robots.txt` `Disallow` for any automated path other than the scoped routes" | This reads as permission to crawl disallowed scoped routes. There is also no terminal state for a stop on 403 or 429. | "If `robots.txt` disallows a scoped route for all user agents, choose another target. A 403 or 429 is `HARD-BLOCKER` after one retry 10 minutes later." |
| R14 | LOW | C LEG-11: "and from any form; on in-scope pages only as visually hidden text" | "from any form" could be read as a visible link. | "and from any form, as visually hidden text". |
| R15 | LOW | P rule 4: "Icons count as images: redraw or substitute them." | Third-party brand icons (social networks) are logos, so this conflicts with "never a traced or redrawn copy". | Append: "Third-party brand icons come from an openly licensed icon set, with the licence recorded." |
| R16 | LOW | C MOT-14 Verify; MOT-13 `renderer.info.memory`; OPS-01 `actionlint` | Listing non-passive listeners cannot tell whether a listener calls `preventDefault`. `renderer.info` exists only in three.js. `actionlint` is not in preflight. | MOT-14: "dispatch a synthetic wheel event and flag non-passive listeners after which `defaultPrevented` is false". MOT-13: "(three.js: `renderer.info.memory`; otherwise count live textures and buffers)". Add `actionlint` to the P preflight list. |

## 4. Verified true in this round

- The six strict-smoke cases behave upstream exactly as the prompt now claims.
- The prompt's "Also reproduced" list (opacity, transition-duration, z-index, line count) is correct.
- `elementFromPoint` sees pseudo-element hit areas; the axe `target-size` blindness was confirmed earlier.
- Lighthouse 13.5.0 audit names `lcp-breakdown-insight`, `lcp-discovery-insight` and `bf-cache` exist; `largest-contentful-paint-element` does not.
- `is-on-https` passes on 127.0.0.1.
- The `flow` and `data-sc-verify-state` wording matches shoot.mjs L514 to L515.
- The contract link is pinned to the SHA.

## 5. Could not verify

- Whether GSAP's ticker idles on its own when nothing is animating; this affects how achievable MOT-05's "0 rAF" is.
- The Playwright default autoplay policy flag, which A11Y-14 depends on.
- The current SIL OFL FAQ position on subsetting and Reserved Font Names.
