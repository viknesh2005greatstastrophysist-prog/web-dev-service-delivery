GREEN (after the fixes below). The gold standard holds up once four blockers are fixed, and the two files agree. Residual risks and operator decisions are listed at the end. The browser experiments could not run in this sandbox, so the browser-based verify methods were checked against source code and documentation only.

# Independent review of the gold pass: checklist and prompt v6

Reviewed and fixed 2026-10-01. C = `PRODUCTION_CHECKLIST_clone_swap.md`, P = `PROMPT_awwwards_clone_swap_v6.md`. The files as I received them are saved here as `ck.original.md` and `v6.original.md`. Every edit is logged in `changes.md` (59 entries, 67 checklist and 6 prompt replacements). The diffs are `lab/checklist.review2.diff` and `lab/prompt.review2.diff`, the mechanical checks are in `mechanical.txt`, the gold evidence table is `gold-benchmark.md`, and the scripts and fetched sources are in `lab/`.

Before my edits the pair was **NOT GREEN**, with four blockers (B-1 to B-4 below). All four are fixed in place. Totals: 4 blockers, 14 major and 25 minor findings, plus 11 gold-gap additions (6 new rows and 5 extended rows: the SBOM in SEC-07, CSP reports in OPS-05, the statement date in LEG-12, a 25th-percentile target in SUS-01, and a dated DMARC move in MAIL-01). Rows: 247 before, 253 after. 6 rows were added, 44 rows had their text changed, none were removed, and no row changed class. The prompt changed in 6 places and went from 14,587 to 14,654 words.

## 1. Is the gold actually gold?

Short answer: **yes for most rows, after corrections.** The main weakness was in how things were measured, not in the numbers. Area by area:

- **Speed (SPD-13 and its neighbours).** I recomputed the targets with Lighthouse 13.5.0's own scoring code (`lab/lhscore.mjs`). Two desktop targets scored below the "0.98 or better" the row claimed: LCP 0.9 s scores 0.96 and Speed Index 1.0 s scores 0.97. The mobile TBT target of 50 ms scores 1.00, but its 0.98 point is 100 ms, so the stated basis did not support it. The score bar of 97 was looser than the metric targets it sums up, which give 99. Now every figure sits at or inside its 0.98 point: desktop LCP 0.8 s, desktop SI 0.95 s, mobile TBT 100 ms, and a score of 98.

  The bigger problem was the CPU. Lighthouse's 4x CPU slowdown assumes a host with a `benchmarkIndex` of 1,500 to 2,000 (its throttling guide). A current laptop scores higher, so at 4x it emulates a high-end phone, and every CPU-bound "gold" figure (TBT, INP proxy, MOT, UXF-02) was softer than it read. Rule 3 now calibrates the multiplier with Lighthouse's own calculator formula.

  Against the 2025 population, mobile lab TBT is 127 ms at the 10th percentile and 1,916 ms at the median. Lighthouse set its FCP and LCP 0.9 points at the 8th and 13th percentiles of HTTP Archive pages. So the targets are beyond the top decile. They are reachable for a lean build, but not for a reference with a WebGL or video hero, which takes the FIDELITY-EXCEPTION path. Local runs are over plain http, which skips the TLS round trip, so a live Lighthouse run (SPD-20) was added.
- **Bytes.** The 170 KB JavaScript budget is about the top 15% of mobile pages (10th percentile 89 KB, 25th percentile 270 KB). It is also stricter than Russell's 2024 budget for a 3 s load (365 KiB): top-tier. The critical-path figure was ambiguous, because it could include the hero image; its scope is now fixed. The 30 KB blocking CSS file sits around the 25th percentile (34 KB) and only 15% of pages pass the render-blocking audit: good to top-tier. The 14 KB HTML first flight is the 25th percentile and is principled (RFC 6928 and RFC 9002): good. Page weight had the median as its target, which is only "good"; the 25th percentile (1,127 KB, 42 requests) is now the gold.
- **Edge and origin.** A fixed 200 ms edge TTFB measured from wherever the auditor sits could not be reproduced, so it now uses 3 round trips plus 50 ms with web.dev's 800 ms floor. The "one redirect" rule contradicted hstspreload.org and the Observatory, which both require `https` on the same host first.
- **Interaction and experience.** The 100 ms, 400 ms and 10 s limits are principled (Nielsen and Doherty). The 44 px target is AAA (WCAG 2.5.5), so top-tier, but it was missing 2.5.5's exceptions and was not limited to coarse pointers. `touch-action: manipulation` as the tap-speed fix is folklore: Chrome's own note says `width=device-width` removed the tap delay in 2014 to 2016. The 404 content matches GOV.UK's page-not-found pattern (top-tier), but it clashed with a reference's own custom 404 (EDGE-01, rule 2).
- **Accessibility.** Zero axe violations in every state, a human screen-reader pass, 1.4.12, 1.4.13 and 3.2.6 with 3.3.7 is top-tier, against a 2025 median Lighthouse accessibility score of 85 and a 30% contrast pass rate. The gaps a senior auditor would raise are now rows or row text: captions (WCAG 1.2.2), JAWS (the most common primary reader at 40.5%), `prefers-contrast` (Baseline, used on about 1% of pages), and the date and method in the accessibility statement.
- **Security.** The header set (strict self-only CSP, COOP, CORP, `frame-ancestors`, 2-year HSTS, zero third parties) is top-tier. CSP is on 21.9% of pages, the 90th-percentile HSTS max-age is 730 days, and 90 to 92% of pages load at least one third party. Until now the checklist had no objective grade. The Mozilla HTTP Observatory's keyless API gives this set about 135 (A+ starts at 100) and is now HOST-20. Trusted Types enforcement was unsafe as written, so it now runs report-only first.
- **SEO, i18n, email, hosting, operations, handover.** These are top-tier against Google's documentation and the W3C/IBM expansion table. I added sitemap hygiene, external-link checks, a dated DMARC move to quarantine and an MTA-STS move to enforce, the Internet.nl test (IPv6, DNSSEC, RPKI) as an owner step, validity presets that check standards rather than style, and an SBOM.

The full table, with each figure, its evidence and links, is in `gold-benchmark.md`.

## 2. Findings by severity

### Blockers (all fixed)

| ID | Where | What was wrong | Fix (changes.md) |
|---|---|---|---|
| B-1 | C SPD-13 | The gold row's stated basis ("each figure scores about 0.98 or better on Lighthouse's own curve") was false for desktop LCP (0.96) and Speed Index (0.97). Mobile TBT of 50 ms had no basis (its 0.98 point is 100 ms). The score bar (97) contradicted the metrics it summarises (99). | Recomputed targets, 0.98 points listed, score 98, population context (entry 7) |
| B-2 | C rule 3, every CPU-throttled row; P preflight | The CPU was not calibrated, so "4x" on a fast machine measured a high-end phone and every CPU-bound gold figure was weaker than claimed. Playwright "Slow 4G" had no defined latency, and Lighthouse's own request-level equivalent is 562.5 ms, not 150 ms. | Calibration from `benchmarkIndex` with Lighthouse's calculator formula; request-level network values; preflight records both (entries 2, 55) |
| B-3 | C EDGE-15 | A G row whose verify rested on a false claim ("Lighthouse stops with an error on a 404, so it cannot be used"; Lighthouse 13.5.0 has `--ignore-status-code`). The fallback (CDP Slow 4G in Playwright) made the 1.0 s LCP either unreachable (at Lighthouse's 562.5 ms request latency) or not comparable to SPD-13 (at 150 ms). It also contradicted EDGE-01 and rule 2 for a reference whose own 404 has WebGL or an intro. | Verify by Lighthouse with `--ignore-status-code`; the reference's own 404 features are kept with an exception (entry 23) |
| B-4 | C rule 9 (and rule 1, P rule 8) | "Each ... row states a published floor (the good or AA threshold) ... the floor is never waived" pulled AA accessibility thresholds under a no-exception rule. That contradicts rule 2's own example (a low-contrast reference colour is a FIDELITY-EXCEPTION), DEL-04 and DEL-08, so any reference with low contrast (83.9% of home pages) would deadlock gate 10. It also left rule 1's "row is logged" with no status. | Rule 9 scoped to SPD, UXF, MOT and EDGE-15. A published floor that is missed is `FAIL`. A (J) floor can take an exception when the reference misses it too. Accessibility keeps rule 2's path. Rule 1 and P rule 8 aligned (entries 1, 4, 54) |

### Major (all fixed)

| ID | Where | What was wrong | Fix |
|---|---|---|---|
| M-1 | C rule 1 | When the original missed a floor, rule 1 only said the row "is logged" and gave it no status, while rule 9 said floors are never waived. | `FAIL`, design unchanged (entry 1) |
| M-2 | C UXF-06 | The G row required `touch-action: manipulation` on every control as the tap-delay fix. That is obsolete given RSP-01's viewport, and it changes how gestures feel. The 44 px areas were not limited to coarse pointers, so desktop hover zones would move (rule 2). 2.5.5's exceptions were missing. | Rewritten (entry 30) |
| M-3 | C SPD-15, SEO-07, HOST-01 | The redirect rules contradicted HSTS preload and the Observatory, and edge TTFB depended on the auditor's location. | Same-host first; RTT-relative target (entries 8, 17, 41) |
| M-4 | C SPD-17 | The critical-path scope was ambiguous (it could include the LCP image), and the verify was not reproducible without throttling. | Scope fixed; verify from Lighthouse JSON (entry 10) |
| M-5 | C SPD-18 | "No font or image found only after CSS or JS unless preloaded" contradicted TYP-03, TYP-24 and lazy loading. | Limited to the LCP image and first-viewport fonts (entry 11) |
| M-6 | C A11Y-18 | JAWS, the most common primary reader, was left out. | Added (entry 13) |
| M-7 | C EDGE-02, P §4 | The fixed 404 content contradicted EDGE-01 and rule 2 for a reference with its own custom 404. | The reference's 404 is kept; items it lacks become exceptions (entries 21, 57) |
| M-8 | C SPD-11 | Lighthouse's bf-cache audit scores 0 on any reason, including `Not actionable` ones, so a G row could fail a correct site. | Pass on no `Actionable` reason (entry 5) |
| M-9 | C EDGE-18 | The unconfigured 503 served an HTML page where BACK-07 requires JSON for `fetch`, and the no-JS form post was undefined. | A page for `text/html` posts, JSON for `fetch` (entry 24) |
| M-10 | C UXF-02, BACK-10 | The server's 10 s timeout equalled the client's limit, so the visitor's timeout could fire while the mail was still sending. | Server 8 s; honest timeout message (entry 28) |
| M-11 | C UXF-05 | "Required marked in words" was a visible change outside rule 2's closed list. | Visually hidden word plus `required` (entry 29) |
| M-12 | C UXF-07 | The verify flagged fixed background canvases (common on award sites), and a reference's own overlay had no status. | Above-content test; the reference's overlay is an exception (entry 31) |
| M-13 | C SEC-13 | Enforcing Trusted Types with an unrouted library sink breaks the page, and "the row is R" in an R row meant nothing. | Report-only first; never a pass-through default (entry 37) |
| M-14 | C OPS-09 | "Standard rule set" and the html-validate default are style presets, so a valid build would fail. | Validity presets (entry 46) |

### Minor (all fixed, see changes.md)

SPD-12 control page; SPD-16 RFC 9002 and population; RSP-09 approximation; A11Y-19 WCAG wording (same order, same process); SEO-10 sitemap hygiene; SEO-13 share card; EDGE-04 `/api` only with server code; BACK-01 `mailto:` wording against UXF-05; UXF intro sources (Laws of UX as a secondary source); UXF-01 INHERITED is not a row status; MOT-01 timer rounding (≤ 17 ms); SEC-02 content types; SEC-04 `form-action`; SEC-06 all objects and `PASSWORD`; SEC-14 handover note; MAIL-04 enforce date; HOST-19 new domain; OPS-02 runs and multiplier; I18N-02 report, never redesign; DEL-10 wording; DEL-12 and DEL-13 file names; footer 3.3.8 corrected to 3.3.7. The P edits were §8 DNS.md cutover plan, §8 audit:live names, and the preflight validators.

## 3. Rows added, changed, removed

- **Added (6):** SPD-20 (R-L, Lighthouse on the deployed URL), A11Y-20 (C, captions), A11Y-21 (R, `prefers-contrast`), SEO-14 (R, external links), HOST-20 (G-L, Observatory A+ with 0 failed tests), HOST-21 (R-O, Internet.nl tests).
- **Changed text (44):** SPD-11, SPD-12, SPD-13, SPD-15, SPD-16, SPD-17, SPD-18, RSP-09, A11Y-18, A11Y-19, SEO-07, SEO-10, SEO-13, EDGE-02, EDGE-04, EDGE-15, EDGE-18, UXF-01, UXF-02, UXF-05, UXF-06, UXF-07, MOT-01, SEC-02, SEC-04, SEC-06, SEC-07, SEC-13, SEC-14, BACK-01, BACK-10, MAIL-01, MAIL-04, HOST-01, HOST-19, OPS-02, OPS-05, OPS-09, LEG-12, SUS-01, I18N-02, DEL-10, DEL-12, DEL-13. Also changed: rules 1, 3, 7 and 9, the UXF intro, and the verification-status notes.
- **Removed:** none. **Class changes:** none.
- **New rows not touched:** I reviewed every gold-pass row in the brief. SPD-06, SPD-14, SPD-19, TYP-23, TYP-24, RSP-08, A11Y-05, A11Y-16, A11Y-17, SEO-01, SEO-05, SEO-11, SEO-12, EDGE-03, EDGE-13, EDGE-16, EDGE-17, UXF-03, UXF-04, UXF-08 to UXF-11, MOT-15, I18N-01, I18N-03, I18N-04, CNT-17, MAIL-05, HOST-18, OPS-08, LEG-17, DEL-11 and DEL-14 needed no change. Their facts checked out against the sources below, or they are marked (J).

## 4. Coverage against external checklists and graders

| Source | Checked how | What ours lacked or stated weaker | Action |
|---|---|---|---|
| Front-End Checklist (thedaviddias, current README) | fetched, all items scanned (`lab/src/fec.md`) | captions; allow paste; avoid autofocus; noindex or 4xx URLs in the sitemap; MIME types; `meta charset` first; broken external links; screen-reader testing including JAWS | A11Y-20, UXF-05, SEO-10, SEC-02, OPS-09, SEO-14, A11Y-18 |
| web.dev (TTFB, bfcache, performance budgets, tap targets) | fetched bfcache and budgets; TTFB and tap targets from the research notes | `beforeunload` no longer blocks bfcache (no change needed); 170 KB is an example, not a standard | SPD-17 labelled (J) with population |
| Smashing front-end performance checklist (2021, the latest) | fetched | 170 KB JS budget (Russell's 130 to 170 KB), PRPL-30, IPv6, QUIC; OCSP stapling (not adopted: the agent controls no TLS stack) | IPv6 via HOST-21 |
| W3C WCAG 2.2 and WCAG-EM | fetched the Understanding pages for 2.5.5, 3.2.6, 3.3.7 and the WCAG-EM steps | 3.3.7 wording; 1.2.2 captions missing; WCAG-EM asks for the technologies relied on and the method, which the statement lacked | A11Y-19, A11Y-20, LEG-12 |
| GOV.UK Service Standard and patterns | fetched the standard; page-not-found from the research notes | points 5, 11 and 14 are covered (A11Y, OPS, HOST-11) | none |
| Google Search Essentials and Search Central | fetched title links, sitemaps, Organization | sitemap must not list noindex or 4xx URLs | SEO-10 |
| Mozilla HTTP Observatory | fetched the FAQ, API probe, score table and test source | no objective header grade; a first redirect off-host is a failed test | HOST-20, SEO-07 |
| securityheaders.com | blocked by a bot challenge (403) | not usable unattended (and no bypassing) | none |
| Qualys SSL Labs | API docs fetched | v4 needs registration with an organisation email | not added; testssl.sh stays optional in HOST-02 |
| Internet.nl | access page fetched | the batch API is for members only; the website and mail tests are free and manual | HOST-21 (R-O) |
| WebPageTest, PageSpeed Insights | probed | WPT needs a key; the keyless PSI quota was exhausted (429) | SPD-20 uses local Lighthouse instead |
| Hardenize | not checked (now a commercial product behind an account) | none | none |
| Awwwards Developer Award criteria | evaluation page fetched; guideline URLs return 404 | could not verify the jury's criteria text | none |

## 5. External facts: verified and not verified

**Verified this round** (fetched or read from source; text saved under `lab/src/`):
- Lighthouse 13.5.0 source (installed npm package): metric control points and their HTTP Archive percentile comments, the scoring boost and floor (`shared/util.js`), category weights (FCP 10, SI 10, LCP 25, TBT 30, CLS 25), `--ignore-status-code`, `--throttling.cpuSlowdownMultiplier`, `benchmarkIndex`, the scoring of the `bf-cache` audit, the field names of `network-requests` and `metrics`, and the Lantern Slow 4G constants including the request-level factors 3.75 and 0.9.
- The Lighthouse [throttling guide](https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md) and its [CPU calculator](https://lighthouse-cpu-throttling-calculator.vercel.app/) formula.
- Web Almanac 2025: [performance](https://almanac.httparchive.org/en/2025/performance), [page weight](https://almanac.httparchive.org/en/2025/page-weight), [fonts](https://almanac.httparchive.org/en/2025/fonts), [accessibility](https://almanac.httparchive.org/en/2025/accessibility), [security](https://almanac.httparchive.org/en/2025/security), [third parties](https://almanac.httparchive.org/en/2025/third-parties), [CDN](https://almanac.httparchive.org/en/2025/cdn). The 2025 edition has no JavaScript, CSS, media or sustainability chapter.
- [Mozilla HTTP Observatory](https://developer.mozilla.org/en-US/observatory/docs/faq): the API v2, the [score table and test logic](https://github.com/mdn/mdn-http-observatory), and a live probe of mdn.dev (A+ 115, algorithm 6).
- [hstspreload.org](https://hstspreload.org/) requirements.
- [WebAIM screen reader survey 10](https://webaim.org/projects/screenreadersurvey10/).
- [Chrome: 300ms tap delay, gone away](https://developer.chrome.com/blog/300ms-tap-delay-gone-away).
- WCAG 2.2 Understanding [2.5.5](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html), [3.2.6](https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html), [3.3.7](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html), and [WCAG-EM](https://www.w3.org/TR/WCAG-EM/).
- web-features 3.40.0 (Trusted Types Baseline 2026-02-24; LoAF, `scheduler` and speculation rules not Baseline; event timing and LCP Baseline 2025-12-12; `prefers-contrast` widely available).
- [html-validate presets](https://html-validate.org/rules/presets.html) and [stylelint-config-recommended](https://github.com/stylelint/stylelint-config-recommended).
- Google Search Central [title links](https://developers.google.com/search/docs/appearance/title-link), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) and [Organization](https://developers.google.com/search/docs/appearance/structured-data/organization).
- [W3C text size in translation](https://www.w3.org/International/articles/article-text-size).
- [web.dev bfcache](https://web.dev/articles/bfcache) and [performance budgets](https://web.dev/articles/performance-budgets-101).
- [Russell, Performance Inequality Gap 2024](https://infrequently.org/2024/01/performance-inequality-gap-2024/).
- [Smashing 2021 checklist](https://www.smashingmagazine.com/2021/01/front-end-performance-2021-free-pdf-checklist/).
- [Internet.nl API access](https://github.com/internetstandards/Internet.nl-API-docs).
- [SSL Labs API v4](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v4.md).
- PSI keyless quota (429 on 2026-10-01).

**Not verified:**
- Awwwards' Developer Award guidelines (404 or rendered by script).
- Hardenize.
- A public distribution of p75 INP by percentile, so the INP proxy target rests on Nielsen and is marked (J).
- The Doherty threshold, which comes only from a secondary summary.
- WhatsApp or LinkedIn share-image limits.
- The research-notes items I did not re-fetch (Nielsen, Deloitte study, Early Hints support list, Cloudflare 404 TTL, NN/g studies, GOV.UK page-not-found). I spot-checked the Almanac figures they rely on and found them consistent.
- The browser-side behaviour listed in section 6.

## 6. Experiments

Run:
1. **Lighthouse score recomputation** (`lab/lhscore.mjs` → `lab/lhscore.out.txt`). This imports Lighthouse 13.5.0's `Util.computeLogNormalScore` and gives the scores at each target, the 0.98, 0.95 and 0.90 points, the category score at the gold values (0.99 on both profiles), and the category score with one metric at its p10 (0.96 to 0.98).
2. **Lighthouse source reads.** The 404 handling (`navigation-error.js`, `ignoreStatusCode`), the CLI flags, the `bf-cache` audit scoring, the Lantern constants, and the JSON fields used by SPD-17.
3. **Observatory API probe.** The API is keyless; the first call returned 503 and the retry returned A+ 115 with 12 tests. I also read the redirection, CSP and COEP pass logic in the grader source.
4. **PSI keyless probe:** 429 (shared daily quota exhausted). **SSL Labs v3 `info`:** still answers anonymously (v4 needs registration). **securityheaders.com:** 403 bot challenge.
5. **Mechanical checks** (`lab/mech.py` → `mechanical.txt`). These were run before and after my edits, with 0 problems either way. They confirm 253 rows, each with 4 cells and a valid class, IDs sorted with no gaps, every cited ID resolving, the prompt's section list matching the checklist's 18 prefixes, every rule, § and gate reference resolving, no em or en dashes, and every doc the checklist names present in the prompt.

Not run, because the sandbox blocks them. Local port binding returned EPERM, and Chromium died at launch with a Mach-port permission error. Playwright 1.63 also wants Firefox and WebKit builds that are not cached.
- The SPD-12 prerender check with `activationStart`.
- The A11Y-16 text-spacing injection.
- The RSP-05 and UXF-06 hit-area grid.
- `crossOriginIsolated` under COEP.
- A Trusted Types report-only run.
- CDP throttling.
- curl timing against a local server.

For each of these I checked the API in Playwright's type definitions or the browser documentation instead. SPD-12 now carries a control page so that a browser which will not prerender gives `NOT_RUN` rather than a false `FAIL`.

## 7. Residual risks

- **Run size.** The checklist went from 196 rows (12,994 words) before the gold pass to 247, and is now 253 rows (21,015 words), alongside a 14,654-word prompt. Each new row is cheap, but the total is very large for one unattended session. The production loop allows 3 cycles, and many gold rows (SPD-13, SPD-17, UXF-06, A11Y-16) will need code changes in their own right. Expect several `FAIL` or `FIDELITY-EXCEPTION` outcomes on any WebGL or video reference, and consider the two-run split the previous review suggested.
- **Speed floors are now hard `FAIL`s.** A faithful clone of a slow reference (for example a 4 s WebGL hero) ends with SPD-01 `FAIL` and gate 10 `FAIL`, reported honestly. This follows from "floors are never waived" (decision 1 below).
- **Calibration makes CPU figures harder.** On a fast laptop the multiplier will be about 6x to 10x, so TBT, the INP proxy, MOT-01's (J) floor and MOT-15 become genuinely phone-like, and many award references will miss them. CI runners (OPS-02) add noise as well.
- **Browser-side verify methods** were reviewed but not executed here (section 6).
- **Observatory dependency.** HOST-20 depends on a third-party service that returned a transient 503. It is `NOT_RUN` when unreachable, and its scans are public.
- **A11Y-21 and UXF-06** change what visitors with a contrast preference or a touch screen see or feel. This is deliberate, but it is a reading of rule 2 (decision 3).
- **External figures change.** The Web Almanac figures are from 2025, and the Lighthouse curve is from 13.5.0. A different pinned Lighthouse version can move the 0.98 points.

## 8. Decisions for the operator

1. **Floors that the reference itself misses.** I kept your rule ("floors are never waived"): such a floor is `FAIL`, and the README says the miss is the reference's. The alternative is to accept it as a `FIDELITY-EXCEPTION` when the clone beats the original (rule 1). My recommendation is to keep `FAIL`, because it is honest and the run still finishes. Revisit this only if gate 10 failing on most motion-heavy references is unacceptable.
2. **CPU calibration.** It is on by default (rule 3). It makes the mobile figures reflect a mid-tier phone, but it also makes them harder to reach than the PageSpeed Insights numbers a client may quote. My recommendation is to keep it. The alternative is plain 4x, with the gold figures labelled "on a fast host".
3. **A11Y-21 (`prefers-contrast: more` turns on the contrast fixes) and UXF-06 (larger touch hit areas).** These change things only for visitors who asked for them or who use touch, in the same way reduced motion already does. My recommendation is to keep both. The safer alternative is to drop A11Y-21.
4. **HOST-20 is G-L.** It is an objective, free grade that the header rows already earn, but each scan is published on MDN. My recommendation is to keep it G-L. The alternative is R-L if publishing scans is a concern.
5. **JAWS in A11Y-18.** It is required only "where the tester has a licence". My recommendation is to budget a licence if the client's audience is in North America (55.5% primary JAWS use there).
6. **Lighthouse CI gating at gold (OPS-02).** CI noise can block deploys. My recommendation is to keep the gold assertions at `error` with the median of 3, and to loosen one to the measured value plus 5% only through a recorded exception, as the row already says.
7. **Run size.** Consider running clone and reference gates in one run, and swap, production and handover in a second.
