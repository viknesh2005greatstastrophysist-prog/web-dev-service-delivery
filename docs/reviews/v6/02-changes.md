# Change log: review of the gold pass (2026-10-01)

Files: C = `PRODUCTION_CHECKLIST_clone_swap.md`, P = `PROMPT_awwwards_clone_swap_v6.md`, both in `/Users/vik/Downloads/scrollcraft (2)/`. The state I received is saved here as `ck.original.md` and `v6.original.md`; full diffs are `lab/checklist.review2.diff` and `lab/prompt.review2.diff`. Every edit is an exact-match replacement asserted to occur once (`lab/applylib.py`; batches `lab/apply_ck.py`, `apply_ck2.py` to `apply_ck4.py`, `apply_p.py`, plus C60 run inline from the same library). Severity: B = blocker, M = major, m = minor (see `opus-gold-review.md`). Sources fetched are saved under `lab/src/`.

Counts: checklist 67 edits (C01 to C67) touching the rules, 44 existing rows and the status notes, 6 rows added, 0 removed, 0 class changes; prompt 6 edits.

## Checklist: rules of application

1. **C01** (M-1). Rule 1: a published floor (rule 9) that the clone still misses stays `FAIL`. Why: rule 1 let a floor miss that the original shares be "logged", while new rule 9 says floors are never waived; the two disagreed on the status. Evidence: rule 1 and rule 9 text; prompt gate 10 accepts only PASS, N/A or FIDELITY-EXCEPTION for G rows.
2. **C02, C60** (B-2). Rule 3: CPU calibration and request-level throttling. Record `benchmarkIndex`, set `--throttling.cpuSlowdownMultiplier` from Lighthouse's own calculator (3 + (index - 1300) / 233 from 1,300; 2 + (index - 800) / 500 from 800), use the same multiplier for every "4x CPU" Playwright throttle; Playwright network throttling uses Lighthouse's request-level Slow 4G (562.5 ms, 1,474.6 Kbps, 675 Kbps). Why: the default 4x assumes a 1,500 to 2,000 host; a current laptop at 4x emulates a high-end phone, so every CPU-bound gold figure (TBT, INP proxy, MOT, UXF-02) was softer than it reads; and "CDP Slow 4G" with 150 ms latency is not Lighthouse-comparable. Evidence: `lab/src/lh-throttling.md` (benchmark table, calibration section), calculator bundle (`lab/calc-index-*.js`, formula above), `@paulirish/trace_engine` Lantern `Constants.js` (`DEVTOOLS_RTT_ADJUSTMENT_FACTOR = 3.75`, throughput 0.9), Lighthouse 13.5.0 `cli-flags.js` (`throttling.cpuSlowdownMultiplier`), `runner.js` (`benchmarkIndex` in `environment`).
3. **C03** (m). Rule 7 feature list gains A11Y-20.
4. **C04** (B-4, M-1). Rule 9: scoped to SPD, UXF, MOT and EDGE-15; gold at or beyond the top tenth of the 2025 HTTP Archive population where measured; the published floor is never waived (`FAIL`, design still not changed); a judgment floor (MOT-01) may be a FIDELITY-EXCEPTION when the reference misses it too and the clone is equal or better; accessibility thresholds keep rule 2's FIDELITY-EXCEPTION and `A11Y_FIXES` path. Why: "each speed, interaction and experience row states a published floor (the good or AA threshold) ... the floor is never waived" could be read to forbid the contrast and target-size exceptions that rule 2, DEL-04 and DEL-08 are built on, and it would have failed any faithful clone of a WebGL site on a (J) frame-time floor that became stricter under C02. Evidence: rule 2 text ("for example a low-contrast colour ... FIDELITY-EXCEPTION"), DEL-04, DEL-08.

## Checklist: SPD

5. **C66** (M-8). SPD-11 verify: the Lighthouse `bf-cache` audit scores 0 on any reason, including `Not actionable` and `Pending browser support`, so the row passes when no `Actionable` reason is listed. Evidence: Lighthouse 13.5.0 `core/audits/bf-cache.js` (`score: results.length ? 0 : 1` over all three failure types). Also checked: web.dev says `beforeunload` no longer blocks bfcache, so no change there.
6. **C05** (m). SPD-12 verify: a control page must prerender first, else `NOT_RUN`. Why: Playwright's automation flags may disable preloading; without a control a correct site fails. Not run here (browser launch blocked, see report).
7. **C06, C61** (B-1). SPD-13 recomputed. Mobile TBT 50 to 100 ms, desktop LCP 0.9 to 0.8 s, desktop SI 1.0 to 0.95 s, score 97 to 98, CPU calibrated, 0.98 points listed, population context, plain-http caveat, score bar follows a recorded metric exception. Why: the row claimed every figure scores "about 0.98 or better"; recomputation with Lighthouse 13.5.0's own scoring code shows desktop LCP 0.9 s = 0.96 and SI 1.0 s = 0.97 (below), mobile TBT 50 ms = 1.00 (its 0.98 point is 100 ms). 100 ms mobile TBT is still beyond the 2025 population's top decile (127 ms) and, with C02's calibration, stricter in practice than 50 ms at uncalibrated 4x. The score bar of 98 is what the per-metric targets imply. Evidence: `lab/lhscore.mjs` and `lab/lhscore.out.txt`; Almanac 2025 performance chapter (TBT percentiles); control-point comments in `core/audits/metrics/*.js` (FCP p10 = 8th percentile 2021, LCP p10 = 13th percentile 2020).
8. **C07** (M-3). SPD-15 rewritten: median TTFB at most 3 round trips plus 50 ms (round trip measured as `time_connect - time_namelookup`), never above 800 ms; redirect rule aligned with SEO-07. Why: the fixed 200 ms median depended on where the person running `audit:live` sits, so a correct deployment could fail; "at most one redirect" from `http://` conflicted with HSTS preload and the Observatory, which require `https` on the same host first. Evidence: web.dev TTFB (0.8 s good, includes DNS, connection, TLS), hstspreload.org requirements ("Redirect from HTTP to HTTPS on the same host"), Observatory `redirection.js` (`RedirectionOffHostFromHttp` fails).
9. **C08** (m). SPD-16: QUIC's initial window stated (RFC 9002 section 7.2: 10 datagrams, 14,720 bytes cap) and population (mobile HTML 14 KB at p25, 33 KB median).
10. **C09** (M-4). SPD-17: the budget excludes the LCP image itself and names what counts; JavaScript budget is everything before `load`; verify moved to the Lighthouse JSON (`network-requests` `transferSize`, `render-blocking-insight`, `metrics` `observedLargestContentfulPaint` and `observedLoad`); population and Russell's 2024 budget cited. Why: "bytes needed before the LCP element paints" could include the hero image (170 KB then unreachable with any image), and "every request that finishes before the LCP entry" with unthrottled Playwright is not reproducible. Evidence: Lighthouse 13.5.0 `network-requests.js` and `timing-summary.js` field names; Almanac 2025 page weight (JS p10 89 KB, p25 270 KB); infrequently.org 2024 (365 KiB JS for 3 s at P75); web.dev performance-budgets-101 (170 KB examples).
11. **C10** (M-5). SPD-18: late discovery is forbidden only for the LCP image and first-viewport fonts. Why: "no font or image found only after CSS or JavaScript runs unless it is preloaded" contradicted TYP-03 (preload only 1 or 2 fonts), TYP-24 (up to 4 files) and lazy loading (SPD-04): every non-critical font is discovered through CSS. Population added (15% pass the render-blocking audit; CSS p25 34 KB).
12. **C11** (gold gap). New SPD-20 (R-L): `audit:live` repeats Lighthouse on the deployed URL. Why: SPD-13 is measured over plain http on localhost, which saves Lantern's TLS round trip; the live run catches edge, TLS and compression regressions. PSI API rejected with evidence (keyless call returned 429, shared daily quota; `lab/psi.json`).

## Checklist: A11Y, RSP

13. **C12, C13** (M-6). A11Y-18: JAWS added (where the tester has a licence); the survey's primary-reader figures stated. Why: the row omitted the most common primary desktop reader (JAWS 40.5%, NVDA 37.7%) while citing JAWS's 60.5% "commonly used" share. Evidence: WebAIM screen reader survey 10 (`lab/src/webaim-sr10.txt`).
14. **C14** (m). A11Y-19: WCAG wording ("same order relative to other page content", "in the same process"), Level A stated; verify by DOM order. Evidence: W3C Understanding 3.2.6 and 3.3.7.
15. **C15** (gold gap). New A11Y-20 (C): captions for video with meaningful audio (WCAG 1.2.2), off by default, client-supplied or listed as a content gap; a missing captions control is a FIDELITY-EXCEPTION. New A11Y-21 (R): `prefers-contrast: more` applies the `A11Y_FIXES` contrast fixes, default rendering unchanged. Evidence: Front-End Checklist (captions item), web-features 3.40.0 (`prefers-contrast` Baseline high), Almanac 2025 accessibility (prefers-contrast on about 1% of pages), Playwright 1.63 `contrast` option.
16. **C16** (m). RSP-09: the half-height viewport is recorded as an approximation (iOS shrinks the visual, not the layout, viewport).

## Checklist: SEO

17. **C17** (M-3). SEO-07: `http` on a non-canonical host goes to `https` on the same host first (two hops). Evidence as entry 8.
18. **C18** (m). SEO-10: no `noindex`, redirecting or 4xx URL in the sitemap (Front-End Checklist items "Noindex in Sitemap", "4XX Pages in Sitemap").
19. **C19** (m). SEO-13: owner checks the share card in two platforms' preview tools.
20. **C20** (gold gap). New SEO-14 (R): external links answer 2xx; bot-blocked answers recorded, not failed; quarterly repeat in `docs/MAINTENANCE.md`.

## Checklist: EDGE

21. **C21, C22** (M-7). EDGE-02: built from the reference's components; a reference's custom 404 keeps its layout and motion; an item it lacks that only a visible addition would supply is a FIDELITY-EXCEPTION. Why: EDGE-01 says rebuild the reference's custom 404 "in the same style" and rule 2 protects every recorded state; EDGE-02's fixed content list (3 section links, contact route, no WebGL) contradicted both for any reference with its own 404.
22. **C23** (m). EDGE-04: the JSON 404 for `/api/*` applies only where server code exists (a static site has no `/api`).
23. **C24** (B-3). EDGE-15: verify by `npx lighthouse <url>/no-such-page --ignore-status-code`; the reference's own 404 features are kept with a FIDELITY-EXCEPTION. Why: the row said "Lighthouse stops with an error on a page that returns 404, so it cannot be used here" and fell back to "CDP Slow 4G and 4x CPU" in Playwright. Lighthouse 13.5.0 has `--ignore-status-code` ("Disables failing on all error status codes, and instead issues a warning", `cli/cli-flags.js` line 203; `core/lib/navigation-error.js`), and CDP throttling at Lighthouse's real request-level latency (562.5 ms per request) makes the 1.0 s LCP target unreachable for any page with one stylesheet, while 150 ms is not comparable to SPD-13. The G row was both wrongly sourced and not reliably executable.
24. **C25, C26, C62** (M-9). EDGE-18: a form posted without JavaScript (`Accept: text/html`) gets a page, never raw JSON (503 page when unconfigured, else the form's message); `fetch` still gets JSON; verify both. Why: the row served `500.html` with 503 for the unconfigured contact endpoint, which conflicted with BACK-07 (JSON API responses) for the normal `fetch` path and left the no-JavaScript path undefined.
25. **C63** (m). BACK-01: "No `mailto:` fallback" now reads "no `mailto:` form action in place of the endpoint (the error message may still show the client's address, UXF-05)". Why: UXF-05 offers the client's email address after a failed send.

## Checklist: UXF

26. **C27** (m). UXF intro: Doherty threshold attributed to its secondary source (Laws of UX); Chrome's tap-delay note added.
27. **C28, C29** (m). UXF-01: an inherited dead click is a FIDELITY-EXCEPTION (INHERITED is not a row status in the Statuses list); activation after the ready flag.
28. **C30, C42** (M-10). UXF-02 and BACK-10: the endpoint's outbound timeout is 8 s (J), below the form's 10 s limit, and the timeout message says the message may not have arrived; verify names Chromium and rule 3's throttle. Why: with BACK-10's 10 s server timeout the client's 10 s limit fired first, so a visitor saw a timeout while the server might still send, with no honest wording required.
29. **C31** (M-11). UXF-05: required fields carry `required` plus a visually hidden word where the reference marks them only with a symbol; paste never blocked; no `autofocus`. Why: "marked in words" is a visible change outside rule 2's closed list.
30. **C32** (M-2). UXF-06 rewritten. Why: its G requirement, `touch-action: manipulation` on every control "so a tap fires its click without the double-tap-zoom delay (MDN)", is obsolete: Chrome's own note says `width=device-width` (already required by RSP-01) removed the delay in Chrome 32, Firefox, Edge and iOS 9.3, and `touch-action` was only a fallback; adding it also changes felt gesture behaviour. The 44 px hit areas were not scoped to coarse pointers, so on desktop they would move hover zones (a felt change, rule 2), and WCAG 2.5.5's exceptions (equivalent control, inline link, user-agent size, essential) were missing, which made a G row fail correct inline links. Evidence: `lab/src/tapdelay.txt`, `lab/src/wcag-255.txt`.
31. **C33, C34** (M-12). UXF-07: an overlay the reference itself shows is kept as a FIDELITY-EXCEPTION, never added (rule 10); verify no longer flags a fixed full-screen background canvas (common on award sites) and only counts new elements above the content.

## Checklist: MOT, SEC, MAIL, HOST, OPS, LEG, SUS, I18N, DEL

32. **C35** (m). MOT-01: p95 within one 60 Hz frame (≤ 17 ms) to absorb rAF timestamp rounding; 16.7 ms exactly failed on 0.1 ms jitter.
33. **C36** (m). SEC-02: correct `Content-Type` with `charset=utf-8` on text (Front-End Checklist "MIME type validation"; `nosniff` makes a wrong type fatal).
34. **C37** (m). SEC-04: `form-action 'self'` (Observatory CSP test reads `form-action`; restricts form hijacking).
35. **C38, C39** (m). SEC-06: scan every repository object (`git cat-file --batch-all-objects`, as CNT-14; `git log --all -p` misses unreachable objects, which the previous review fixed elsewhere) and names ending in `PASSWORD`.
36. **C40** (gold gap). SEC-07: CycloneDX SBOM via `npm sbom`.
37. **C64, C41** (M-13). SEC-13 rewritten: report-only run first, enforce only with zero violations, never a pass-through `default` policy; Baseline date made precise. Why: "if a vendor library cannot be [routed], the row is R" was meaningless in an R row, and enforcing `require-trusted-types-for` with an unrouted library sink throws at runtime and breaks the page. Evidence: web-features 3.40.0 (`trusted-types` Baseline low 2026-02-24, Firefox 148).
38. **C67** (m). SEC-14: HANDOVER notes that a later third-party embed needs `credentialless` or the header removed (COEP `require-corp` blocks cross-origin subresources without CORP). Checked: no conflict with the same-origin contact form, self-hosted media or fonts.
39. **C43** (gold). MAIL-01: `p=none` with reports at launch, `p=quarantine` or stricter by the 30-day review (Internet.nl and the Google and Yahoo guidance treat `none` as monitoring only).
40. **C44** (m). MAIL-04: `testing` passes at launch, `enforce` by the 30-day review.
41. **C45** (M-3). HOST-01: same-host 301 (as SEO-07).
42. **C46** (m). HOST-19: a domain with no previous site records that instead of a cutover.
43. **C47, C65** (gold gap). New HOST-20 (G-L): Mozilla HTTP Observatory A+ with 0 failed tests, run by `audit:live` through the keyless API v2, NOT_RUN when unreachable, never called for a local host. New HOST-21 (R-O): Internet.nl website and email tests (free, manual; the batch API needs a membership account). Evidence: Observatory FAQ and API (`lab/obs.json` probe: mdn.dev A+ 115, algorithm 6, 12 tests; a first call returned 503), score table `src/grader/charts.js`, pass logic in `src/analyzer/tests/*.js` (COEP absent passes; off-host first redirect fails); Internet.nl API access page (restricted).
44. **C48** (m). OPS-02: Lighthouse CI uses the median of 3 and the rule 3 multiplier.
45. **C49** (gold gap). OPS-05: CSP and Trusted Types violation reports go to the first-party endpoint where server code exists.
46. **C50** (M-14). OPS-09: html-validate with `standard` and `document` presets (validity) instead of the default `recommended` (best practice and style); stylelint `config-recommended` instead of "the standard rule set" (stylistic); `<meta charset>` first. Why: 0 errors under the style presets is a code-style requirement, not validity, and would fail a correct build. Evidence: html-validate presets page, stylelint-config-recommended README.
47. **C51** (gold gap). LEG-12: the statement's preparation and review dates and the test method (DEL-13's yearly check already referred to an "accessibility statement date" that no row required).
48. **C52** (gold). SUS-01: median kept as floor, 25th percentile (1,127 KB, 42 requests) as gold. Evidence: Almanac 2025 page weight.
49. **C53** (m). I18N-02: a pseudo-localisation clip is reported as a translator budget, never fixed by redesign (rule 2).
50. **C54** (m). DEL-10: commands run where they can or print "needs the live URL" (a `dig` command cannot run "against the local server").
51. **C55, C56, C57** (m). DEL-12 and DEL-13 name `docs/EDITING.md` and `docs/MAINTENANCE.md` (the prompt lists them; the rows did not); DEL-13 adds the quarterly link check (SEO-14).

## Checklist: verification status

52. **C58** (m). The gold paragraph cited WCAG Understanding 3.3.8; the row it supports (A11Y-19) is 3.3.7 Redundant Entry, which I fetched and verified.
53. **C59** (m). New paragraph "Independent review of the gold pass" listing what was recomputed, fetched and found unusable unattended.

## Prompt

54. **P01** (M-1). Ground rule 8: "a missed published floor is `FAIL`".
55. **P02** (B-2). Preflight: record `benchmarkIndex` and the rule 3 multiplier, used for every run on both sites.
56. **P03** (m). Preflight: `html-validate` and `stylelint` (OPS-09).
57. **P04** (M-7). §4 production build: the 404 skips the intro unless the original's own 404 plays one.
58. **P05** (m). §8 `docs/DNS.md`: the cutover and rollback plan (HOST-19, DEL-10), which DEL-10 requires there.
59. **P06** (m). §8 `audit:live`: names the Lighthouse run (SPD-20) and the public Observatory scan (HOST-20).

Prompt length: 14,587 to 14,654 words (+0.5%). Checklist: 18,814 to 21,015 words (+11.7%: about 560 words are the six new rows, 230 the review note, and the rest the rewritten rows and rules).
