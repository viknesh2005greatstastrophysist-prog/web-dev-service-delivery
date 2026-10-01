# Verified notes already gathered (2026-10-01). Do not re-fetch these; cite them if useful.

All fetched from the primary page named, in this session.

## Response time and perceived speed
- Nielsen (nngroup.com/articles/response-times-3-important-limits): 0.1 s = feels instantaneous, no special feedback; 1 s = flow of thought uninterrupted; 10 s = limit of attention, feedback with expected completion time is essential.
- Doherty threshold (lawsofux.com/doherty-threshold): give system feedback within 400 ms.
- Business case (web.dev/case-studies/milliseconds-make-millions, Deloitte/Google, 37 brands, 30M sessions): a 0.1 s mobile speed improvement raised retail conversion 8.4%, travel 10.1%, lead-gen form progression 21.6%.

## Lighthouse scoring (source: GoogleChrome/lighthouse core/audits/metrics/*.js, main branch; p10 = the value that scores 0.9)
- Mobile: FCP p10 1800 ms / median 3000; LCP 2500 / 4000; TBT 200 / 600; Speed Index 3387 / 5800; CLS 0.1 / 0.25.
- Desktop: FCP 934 / 1600; LCP 1200 / 2400; TBT 150 / 350; SI 1311 / 2300; CLS 0.1 / 0.25.
- Weights (Lighthouse 10+): FCP 10, SI 10, LCP 25, TBT 30, CLS 25.
- Desktop preset (secondary source): RTT 40 ms, 10,240 Kbps, CPU slowdown 1. Mobile preset: RTT 150 ms, 1.6 Mbps, 750 Kbps up, 4x CPU (from the earlier review of Lighthouse 13.5 source).
- My computed scores (log-normal formula): mobile FCP 1.2 s = 0.989, LCP 1.8 s = 0.985, TBT 50 ms = 0.998, SI 2.0 s = 0.994, CLS 0.02 = 1.0; desktop FCP 0.6 s = 0.99, LCP 0.9 s ~0.96, SI 1.0 s = 0.971, TBT 50 ms = 0.998.

## Web performance guidance
- web.dev/optimize-lcp: ideal LCP split about TTFB 40%, load delay <10%, load duration 40%, render delay <10%.
- web.dev/ttfb: good <= 0.8 s, poor > 1.8 s; includes redirects, DNS, TLS, request. 103 Early Hints mentioned.
- developer.chrome.com/docs/web-platform/early-hints: 103 Early Hints; supported by Cloudflare, Fastly, Akamai; preconnect Chrome/Edge 103+, Firefox 120+, Safari 17+; preload Chrome 103+, Firefox 123+, not Safari; needs HTTP/2 or 3; "several hundred ms" LCP gains reported.
- web.dev/optimize-inp: INP good <= 200 ms, poor > 500; phases input delay, processing, presentation delay.
- web.dev/optimize-long-tasks: long task = over 50 ms; scheduler.yield() (Chrome/Edge 129+, Firefox 142+, not Safari) with setTimeout fallback; isInputPending() not recommended.
- web.dev/performance-budgets-101: example budgets: critical-path resources under 170 KB compressed, TTI under 5 s on slow 3G, JS under 170 KB on mobile; enforce with Lighthouse CI.
- web.dev/bfcache: instant back/forward; blockers: unload listeners, Cache-Control: no-store, open IndexedDB/fetch/WebSocket; all major browsers support; Lighthouse 10+ has a bfcache audit.
- Speculation Rules (developer.chrome.com/docs/web-platform/prerender-pages): eagerness immediate/eager/moderate/conservative; moderate = 200 ms hover or pointerdown; Chrome/Edge 109+, Firefox no, Safari flag; prerendered pages report zero LCP/CLS to analytics.
- web.dev/content-visibility: content-visibility:auto can cut rendering cost 7x in their example; needs contain-intrinsic-size; caveats with DOM APIs that force layout.
- TCP initial window 10 segments ~14 KB (RFC 6928): first-round-trip budget for the HTML (secondary sources).
- MDN touch-action: manipulation disables double-tap-zoom so browsers no longer delay click events.
- MDN color-scheme: `only light` opts out of Chrome's Auto Dark Theme; meta color-scheme before any CSS prevents a flash and sets canvas, scrollbar and form-control colours.
- MDN enterkeyhint and inputmode: Baseline widely available since Nov 2021.
- Cloudflare default cache: HTML and JSON not cached by default; 404/410 edge TTL 3 minutes; 200/301 120 minutes when no cache headers.

## Attention and layout
- NN/g scrolling-and-attention (2018): 57% of viewing time above the fold (80% in 2010); 74% in first two screenfuls; keep major CTAs above the fold.

## Errors, 404s and forms
- Google Search Central (crawling docs): 404 and 410 treated the same; content of 4xx pages is ignored; soft 404 = 2xx that looks like an error; Google's custom-404 help page is retired (no current guidance on wording).
- GOV.UK page-not-found pattern: H1 "Page not found", title "Page not found - service - GOV.UK"; do not blame the user; avoid jargon such as "404", avoid "oops" and humour, no red warning text; give contact details.
- NN/g (search summary, secondary): suggest popular pages, homepage, search; casual conversational tone can help brand perception; generic 404s lose visitors.
- NN/g error-message-guidelines: adjacent to the field, plain language, specific, constructive, positive and non-judgmental tone, preserve user input, never colour alone.
- NN/g errors-forms-design-guidelines: inline validation after the field is done (not while typing), message next to the field, not tooltip-only, not summary-only, not modal; if the same error repeats 3+ times, redesign and offer a support contact.
- Google intrusive interstitials: full-page overlays that obscure content are problematic; legal consent and age gates exempt; small banners acceptable.

## Targets
- web.dev/accessible-tap-targets: 48x48 CSS px target, about 8 px spacing; enlarge with padding without changing visuals; `@media (any-pointer: coarse)`.
- WCAG 2.5.5 Target Size (Enhanced): 44x44 CSS px, Level AAA; exceptions: equivalent targets, inline in text, user-agent controls, essential.
- WCAG 2.5.8 (AA) minimum 24x24 is already in RSP-05.
