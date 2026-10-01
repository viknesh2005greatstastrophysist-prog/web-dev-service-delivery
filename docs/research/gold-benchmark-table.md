# Gold benchmark: is each gold target top-tier?

Method. Each target is compared with (a) the 2025 HTTP Archive population (Web Almanac 2025 chapters; the 2025 edition has no JavaScript, CSS, media or sustainability chapter, so those numbers come from its page-weight chapter), (b) Lighthouse 13.5.0's own scoring curve, recomputed with its source (`lab/lhscore.mjs`, output `lab/lhscore.out.txt`), and (c) the published standard behind the row. A gold target should sit at or beyond the top tenth of the population unless the floor is already near-universal. Verdicts: **top-tier** (top decile or a published top standard), **good** (top quartile or a recognised recommendation, not more), **too strict** (not reachable by a faithful build without an exception path), **unsupported** (the cited basis does not say it), **folklore** (a widely repeated rule the source contradicts).

Population sources: [performance](https://almanac.httparchive.org/en/2025/performance), [page weight](https://almanac.httparchive.org/en/2025/page-weight), [fonts](https://almanac.httparchive.org/en/2025/fonts), [accessibility](https://almanac.httparchive.org/en/2025/accessibility), [security](https://almanac.httparchive.org/en/2025/security), [third parties](https://almanac.httparchive.org/en/2025/third-parties), [CDN](https://almanac.httparchive.org/en/2025/cdn) (all fetched 2026-10-01, text in `lab/src/`). Lighthouse curve: `core/audits/metrics/*.js` and `shared/util.js` of Lighthouse 13.5.0 ([repository](https://github.com/GoogleChrome/lighthouse/tree/main/core/audits/metrics)).

## Speed (lab, Lighthouse curve and population)

| Target | Value in checklist (before → after) | Evidence | Verdict | Action |
|---|---|---|---|---|
| SPD-13 mobile FCP | ≤ 1.2 s | Scores 0.99; 0.98 point is 1.36 s. Lighthouse put its 0.9 point (1.8 s) at the 8th percentile of HTTP Archive mobile pages (2021, comment in `first-contentful-paint.js`). Field: 55% of mobile origins have good FCP. | top-tier | kept |
| SPD-13 mobile LCP | ≤ 1.8 s | Scores 0.98; 0.98 point 1.93 s. Lighthouse's 0.9 point (2.5 s) was the 13th percentile in 2020. Field: 62% of mobile origins good LCP. | top-tier | kept |
| SPD-13 mobile TBT | ≤ 50 ms → ≤ 100 ms | 50 ms scores 1.00, its claimed basis (0.98) is 100 ms. 2025 lab TBT, mobile: p10 127 ms, p25 679 ms, median 1,916 ms. With the new CPU calibration (rule 3) a fast laptop runs at about 5x to 10x, so 100 ms calibrated is stricter than 50 ms at plain 4x. | 50 ms: unsupported by its own basis; 100 ms: top-tier (beyond p10) | changed |
| SPD-13 mobile CLS | ≤ 0.02 | Scores 1.00; 0.98 point 0.06. Field: 81% of mobile origins good CLS (≤ 0.1). Layout shift is fixable invisibly (sizes, metric-matched fallbacks). | top-tier, deliberately tighter than the curve (J) | kept, reason stated |
| SPD-13 mobile Speed Index | ≤ 2.0 s | Scores 0.99; 0.98 point 2.52 s. Long intros and perpetual animation inflate SI, so award references often miss it: exception path (rule 9). | top-tier; reachable only for references without a long intro | kept |
| SPD-13 desktop FCP | ≤ 0.6 s | Scores 0.99; 0.98 point 0.69 s. | top-tier | kept |
| SPD-13 desktop LCP | ≤ 0.9 s → ≤ 0.8 s | 0.9 s scores 0.96, below the row's own "0.98 or better"; 0.98 point 0.82 s. Field: 74% of desktop origins good LCP. | 0.9 s: unsupported; 0.8 s: top-tier | changed |
| SPD-13 desktop TBT | ≤ 50 ms | Scores 1.00; desktop population p10 0 ms, p25 3 ms, median 92 ms. A page that meets 100 ms mobile at a calibrated 4x to 10x has near-zero desktop TBT. | good on its own (about p40), never binding | kept, noted |
| SPD-13 desktop Speed Index | ≤ 1.0 s → ≤ 0.95 s | 1.0 s scores 0.97; 0.98 point 0.96 s. | unsupported → top-tier | changed |
| SPD-13 Performance score | ≥ 97 → ≥ 98 on both | With every metric at its target the weighted score is 0.99 on both profiles; any metric at its 0.9 point drops it to 0.96 to 0.98 (`lhscore.out.txt`). 97 was looser than the metric targets it summarises. | 98 = what the targets imply | changed |
| SPD-13 INP proxy | ≤ 100 ms | Nielsen's 0.1 s limit for "instantaneous" (research notes, nngroup.com). Field: 77% of mobile origins good INP (≤ 200 ms), 63% of the top 1,000. No public distribution of p75 INP by percentile was found. Now measured at the calibrated CPU. | top-tier by principle, population unmeasured (J) | kept, CPU calibrated |
| Lab measurement itself | plain 4x CPU, local http | Lighthouse's throttling guide: 4x assumes a 1,500 to 2,000 `benchmarkIndex` host; its calculator gives 3 + (index - 1,300)/233 above that. Local http skips one TLS round trip in Lantern. | made every CPU-bound "gold" figure softer than it reads | rule 3 calibration (C02), SPD-20 live run |
| SPD-14 origin TTFB | p95 ≤ 50 ms (`/`), ≤ 20 ms (asset), local | Local self-check of server overhead; no population equivalent. | good sanity check, trivially reachable | kept |
| SPD-15 edge TTFB | median ≤ 200 ms, p75 ≤ 300 ms from the auditor → median ≤ 3 RTT + 50 ms, never > 800 ms | web.dev: good TTFB ≤ 0.8 s (field, includes DNS, connection, TLS). Field: 44% of mobile origins good TTFB. Almanac CDN chapter: HTTP/2 needs 3 round trips (TCP, TLS, HTTP) before content. A fixed 200 ms depends on the auditor's distance from the edge. | 200 ms: location-dependent, not reproducible; new: top-tier (edge wait ≤ 50 ms) with the published floor | changed |
| SPD-15 redirects | one redirect `http` → canonical `https` | hstspreload.org and the HTTP Observatory require `https` on the same host first. | contradicted the security standard | two hops allowed off-host (C07, C17, C45) |
| SPD-16 first flight | compressed HTML ≤ 14 KB | RFC 6928 (TCP IW10) and RFC 9002 §7.2 (QUIC 14,720 B cap). Population: mobile HTML p10 6 KB, p25 14 KB, median 33 KB. | good (top quartile), principled | kept, sources added |
| SPD-17 critical path | ≤ 170 KB compressed (critical) and ≤ 170 KB JS | web.dev budgets-101 uses 170 KB as its example for both. Population: mobile JS p10 89 KB, p25 270 KB, median 646 KB. Russell 2024: 365 KiB JS for 3 s at the 75th-percentile phone. three.js alone is about that size gzipped, so WebGL references need the exception. | top-tier (about the top 15% for JS); the critical figure was ambiguous (it could include the hero image) | scope and verify fixed |
| SPD-18 render blocking | 1 blocking stylesheet ≤ 30 KB | Population: total CSS mobile p10 7 KB, p25 34 KB, median 79 KB; only 15% of mobile pages pass Lighthouse's render-blocking audit. A hand-authored clone stylesheet is usually 10 to 25 KB compressed. | top-tier on blocking, good (about p25) on size | kept, discovery clause fixed |
| SPD-11 bfcache | G, no `unload`, no `no-store` | Population: `unload` on 10% of mobile pages (20% of the top 1,000), `no-store` on 23%. | good, near-universal floor | kept, verify fixed |
| SPD-12 speculation rules | R, `moderate` | Present on 35% of mobile pages (WordPress default). | good | kept, control added |
| SUS-01 page weight | ≤ median 2,164 KB / 72 requests → gold ≤ p25 1,127 KB / 42 | Population mobile: total p10 516 KB, p25 1,127 KB; requests p10 25, p25 42. The median was only "good". | median: good; p25: top quartile, reachable only where the reference allows | gold added |
| TYP-24 fonts | ≤ 2 families, ≤ 4 files, ≤ 100 KB before first paint | Population: font requests per page median 4, p75 6; font file median about 35 KB, p90 about 115 KB. | good (4 files is the median count; 100 KB is about the top third) | kept (R, J) |
| MOT-01 frames | p95 ≤ 16.7 ms unthrottled; floor p95 ≤ 25 ms at 4x | One 60 Hz frame; no population data. rAF timestamps are rounded, so exactly 16.7 ms failed on 0.1 ms jitter. Under calibrated CPU the (J) floor gets stricter. | top-tier by principle; floor is judgment | ≤ 17 ms; (J) floor may be an exception when the reference misses it |
| MOT-15 long animation frames | none over 50 ms after the intro | 50 ms is the LoAF and long-task threshold (web.dev). Chromium only (web-features: not Baseline). | top-tier, R | kept |

## Interaction and experience

| Target | Value | Evidence | Verdict | Action |
|---|---|---|---|---|
| UXF-01 dead clicks | visible effect within 400 ms | Doherty threshold (1982 IBM paper, as summarised by Laws of UX; secondary). | good, principled | kept, source labelled |
| UXF-02 feedback | 100 ms next-frame response; pending ≤ 400 ms; result or timeout ≤ 10 s | Nielsen 0.1 s, 1 s, 10 s limits; Doherty 400 ms. Server timeout (10 s) equalled the client limit. | top-tier; the timeout pair was inconsistent | server 8 s, honest message |
| UXF-06 touch | `touch-action: manipulation` + 44 px | Chrome blog: `width=device-width` removed the tap delay in Chrome 32, Firefox, Edge, iOS 9.3; `touch-action` is only a fallback. WCAG 2.5.5 (AAA) 44 px with four exceptions; web.dev 48 px. | `touch-action`: folklore; 44 px: top-tier (AAA) but must be coarse-pointer only and keep the exceptions | rewritten |
| UXF-07 deceptive design | no unprompted overlay > 30% | Google intrusive-interstitials guidance. Verify flagged fixed background canvases. | top-tier | verify fixed, reference's own overlay is an exception |
| EDGE-15 404 weight | LCP ≤ 1.0 s mobile, ≤ 14 KB | (J). My Lantern estimate, not run: about 0.8 s for a 14 KB page plus one stylesheet over http, about 0.95 s with TLS. Lighthouse can measure it with `--ignore-status-code`. | top-tier, tight but reachable for a light 404 | verify fixed (Lighthouse), reference's own 404 kept |
| EDGE-02/03 404 content | real 404, plain H1, causes, home plus 3 section links, contact, noindex, focus | GOV.UK page-not-found pattern; Google Search Central on soft 404s. | top-tier (matches GOV.UK) | kept; reference's custom 404 kept by rule 2 |
| EDGE-18 500 page | static 500, no leak | GOV.UK "There is a problem with the service" pattern; OWASP error handling. | top-tier | no-JavaScript form path added |
| TYP-23 reading | 45 to 80 cpl, line height 1.5, no justify, 16 px | WCAG 1.4.8 (AAA) 80 characters and 1.5 spacing; the rest (J). | top-tier where the reference allows (R) | kept |

## Accessibility

| Target | Value | Evidence | Verdict | Action |
|---|---|---|---|---|
| A11Y-01/02 automated | axe 0 violations, every route and state | Median Lighthouse accessibility score 85 (2025); only 30% of sites pass contrast. Automated tools find under half of WCAG issues (Almanac, citing GOV.UK). | top-tier | kept |
| A11Y-16, A11Y-17, A11Y-19 | 1.4.12, 1.4.13, 3.2.6, 3.3.7 | WCAG 2.2 Understanding pages; 3.3.7 is "same process", not "session". | top-tier (AA and A) | A11Y-19 wording fixed |
| A11Y-18 screen readers | NVDA, VoiceOver, TalkBack | WebAIM survey 10: primary JAWS 40.5%, NVDA 37.7%; JAWS was missing. | good → top-tier with JAWS | JAWS added |
| Captions | none | WCAG 1.2.2 (Level A); Front-End Checklist. | gap | A11Y-20 added |
| prefers-contrast | none | Baseline widely available; used by about 1% of pages. | gap (cheap, invisible by default) | A11Y-21 added (R) |
| Accessibility statement | content list, no date | GOV.UK and the EU model statement carry preparation and review dates and the test method; DEL-13 already checked a date no row required. | good → top-tier | LEG-12 extended |

## SEO, security, hosting, email, operations, handover

| Target | Value | Evidence | Verdict | Action |
|---|---|---|---|---|
| SEO-01, 05, 10, 11, 12 | titles, Open Graph, sitemap, Organization, images | Google Search Central (title links: no limit, truncated to device width; sitemaps: 50 MB or 50,000 URLs, accurate `lastmod`, `priority` and `changefreq` ignored; Organization logo ≥ 112×112 on white), ogp.me. Population: `robots.txt` answers 200 on 85% of sites. | top-tier | sitemap hygiene added (SEO-10) |
| External links | none | Front-End Checklist "broken external links". | gap | SEO-14 added (R) |
| SEC-02/04 headers | nosniff, Referrer-Policy, Permissions-Policy, COOP, CORP, `frame-ancestors`, strict CSP | Population: CSP on 21.9% of pages, Permissions-Policy 3.7%, HSTS 36%. Observatory v6 score table gives this set about 135 (A+ needs 100). | top-tier (a strict self-only CSP is top 1 to 2%) | `form-action`, content types added; HOST-20 makes it measurable |
| HSTS | `max-age=63072000` | Population p90 is 730 days; hstspreload.org minimum 1 year. | top-tier (top decile) | kept |
| SEC-05 third parties | zero | 90 to 92% of pages load at least one third party. | top-tier (top decile) | kept |
| SEC-13 Trusted Types | R | Baseline since 2026-02-24 (web-features); 12% of mobile pages carry one Android-related TT header. | top-tier; enforcement unsafe without a report-only run | rewritten |
| SEC-14 COEP | R | Observatory +10; no conflict with same-origin form and media. | top-tier | handover note |
| Objective graders | none | Mozilla HTTP Observatory API v2: keyless, 1 scan per host per minute, public history (probe: A+ 115). SSL Labs API v4: registration with an organisation email. Internet.nl: website test free, batch API members only. securityheaders.com: bot challenge. WebPageTest: key. PageSpeed Insights: keyless quota exhausted (429). | Observatory usable unattended; others not | HOST-20 (G-L), HOST-21 (R-O), SPD-20 (R-L) |
| TLS, HTTP/3, Early Hints | TLS 1.2+1.3, HTTP/2 or 3, Early Hints where offered | TLS 1.3 on 76% of pages; Early Hints on about 4%; HTTP/3 rising (Almanac CDN). Mozilla intermediate profile. | good to top-tier | kept |
| IPv6, DNSSEC, RPKI | AAAA "if supported", DNSSEC R-O | Internet.nl's 100% needs all three. | good | HOST-21 owner test |
| MAIL-01 DMARC | `p=none` minimum, quarantine "recommended" | Google and Yahoo minimum is `p=none`; Internet.nl wants quarantine or reject. | good → top-tier with a dated move | quarantine by 30 days |
| MAIL-04 MTA-STS | testing then enforce | RFC 8461. | top-tier | enforce by 30 days |
| OPS-02 budgets in CI | Lighthouse CI at gold | web.dev budgets-101 recommends Lighthouse CI. CI runners vary; median of 3 and the same multiplier. | top-tier, flake risk | runs and multiplier stated |
| OPS-09 validity | "standard rule set" for CSS, html-validate default | html-validate `recommended` and `stylelint-config-standard` are style presets, not validity. | wrong tool choice | validity presets |
| Handover docs | HANDOVER, EDITING, MAINTENANCE, ACCEPTANCE | Agency practice (J); SBOM is cheap (`npm sbom`). | top-tier | file names in rows, SBOM added |
| I18N-02 expansion | 1.4x and 2x pseudo-localisation | W3C text-size article (IBM table): up to 10 chars 200 to 300%, over 70 chars 130%. | top-tier; must not force redesign | report, never redesign |

## Answer to "is the gold actually gold?"

Mostly yes, after corrections. Of the numeric gold targets, four were not what they claimed (desktop LCP and SI below their stated 0.98 basis, mobile TBT 50 ms with no basis, the 97 score bar looser than the targets it summarises), one was folklore (`touch-action: manipulation` as the tap-speed fix), one was not reproducible (a fixed 200 ms edge TTFB from wherever the auditor sits), and one rested on a false tool claim (Lighthouse cannot audit a 404). The largest hidden softness was in the measurement, not the numbers: at Lighthouse's default 4x on a current laptop, every CPU-bound "gold" figure was measuring a high-end phone. With the CPU calibrated and the figures recomputed, the speed targets sit beyond the 2025 population's top decile, and the gaps a top agency or auditor would still flag (captions, JAWS, contrast preference, objective header grade, external links, sitemap hygiene, statement date, SBOM) are now rows.
