# Coordinator proposals, part 2: TYP, RSP, A11Y, MOT, SEO, I18N, CNT, SEC, MAIL, HOST, OPS, LEG, DEL, EDGE-13
# Sources: fetched this session (WCAG 2.2 Understanding pages, ARIA APG, Google Search Central, ogp.me, W3C i18n, WebAIM survey 10, MDN Trusted Types and LoAF, OWASP HTTP headers cheat sheet, RFC 8461, Node release page, Google Workspace sender guidelines, web.dev, Lighthouse source).

### REPLACE A11Y-05
| A11Y-05 | Every interactive element is reachable and operable by keyboard in a logical order; no traps. A modal (`role="dialog"`, `aria-modal="true"` only when everything outside is inert and visually obscured) is named by `aria-labelledby` or `aria-label`, moves focus into itself on open, wraps Tab and Shift+Tab inside, closes on Esc and returns focus to the control that opened it (ARIA Authoring Practices, modal dialog pattern). A menu, disclosure or tab set follows its APG pattern where the reference has one. | Playwright Tab walk plus a per-overlay test: open, assert focus inside, Tab past the last stop wraps to the first, Esc closes, `document.activeElement` is the opener | G |
**Why and sources:** w3.org/WAI/ARIA/apg/patterns/dialog-modal (Tab wrap, Esc, return focus, `aria-modal` only when outside is inert).

### NEW after A11Y-15
| A11Y-16 | Text spacing (WCAG 1.4.12, AA): with line height 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 (each a multiple of the font size) forced by an injected `!important` stylesheet, no text is clipped, hidden or overlapping and no control loses its label, at `desktop`, `tablet` and `mobile`. Containers that clip on purpose for a reveal mask are fixed invisibly (a mask that follows the text height); where only a visible change fixes it, it is a `FIDELITY-EXCEPTION` with its `A11Y_FIXES` fix. | Playwright: inject the override stylesheet, then the state walk's clip and overlap checks and a screenshot review of every text slot | G |
**Why and sources:** w3.org/WAI/WCAG22/Understanding/text-spacing (the four values, Level AA).
| A11Y-17 | Content on hover or focus (WCAG 1.4.13, AA), wherever a tooltip, preview, submenu or cursor-follow panel appears: it can be dismissed without moving the pointer or focus (Esc), the pointer can move over it without it vanishing, and it stays until the trigger is removed, it is dismissed or it is no longer valid. A reference that breaks this is a `FIDELITY-EXCEPTION`. | Playwright per interaction-map entry: show, press Esc, move the pointer onto the panel, wait 2 s | C |
**Why and sources:** w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.
| A11Y-18 | A real screen-reader pass by a person, on the shipped build: NVDA with Firefox or Chrome on Windows, VoiceOver with Safari on macOS and on iOS, and TalkBack with Chrome on Android. Landmarks, headings, the menu, any form and the 404 page are read in order, every control has a sensible name and state, and nothing is announced twice or left silent. The WebAIM screen reader survey 10 has NVDA (65.6%), JAWS (60.5%) and VoiceOver (43.9%) as the commonly used desktop readers and VoiceOver (70.6%) and TalkBack (34.7%) on mobile, so a pass with those covers most users. Findings are recorded and fixed before launch. | Owner: record the tester, the tools and versions, the date and the findings in `docs/LAUNCH_CHECKLIST.md` | G-O |
**Why and sources:** webaim.org/projects/screenreadersurvey10 (usage figures). Automated axe runs find only part of the issues; this row is the human check.
| A11Y-19 | Consistent help and no re-typing (WCAG 3.2.6 and 3.3.7): a help mechanism (contact details, the contact form, an FAQ link) that appears on several pages sits in the same place in the same order, and a form never asks for information the visitor has already given in the same session. | Playwright: compare the position and order of the help mechanism across built routes; submit the form and assert no repeated field | C |
**Why and sources:** w3.org/WAI/WCAG22/Understanding/consistent-help (Level A, four kinds of help mechanism). Single-route sites record `N/A` with the route-count predicate.

### NEW after TYP-22
| TYP-23 | Body copy is comfortable to read where the reference allows it: about 45 to 80 characters per line at `desktop` (WCAG 1.4.8 sets 80 as its AAA limit), body line height at least 1.5, no justified text, and no body copy set below 16 px on touch devices. Display and headline type is exempt, and any value the reference sets differently stays the reference's (rule 2) and is listed. | Playwright: for each body-copy slot compute characters per line from `Range.getClientRects()` and the text length; computed `line-height`, `text-align`, `font-size` | R |
**Why and sources:** w3.org/WAI/WCAG22/Understanding/visual-presentation (80 characters, line spacing, no justification). The 45 lower bound and the 16 px floor are (J).
| TYP-24 | Font budget: at most 2 families and 4 `woff2` files on the critical path, and at most 100 KB of font bytes before first paint (J); a variable font is preferred when 3 or more weights of one family are used. | Playwright response sizes of `font/woff2` requests before the LCP entry | R |
**Why and sources:** (J); W3C Web Sustainability Guidelines lean to fewer font downloads; complements TYP-01 to TYP-03 and SPD-17.

### NEW after RSP-07
| RSP-08 | Device matrix review: rest screenshots with no overlap, clipping or stretched layout at 320×568, 375×667, 430×932, 412×915, 768×1024, 1024×768, 1440×900, 1920×1080, 2560×1440 and 3440×1440, and at a short laptop height (1440×500). The layout holds the reference's max widths on very wide screens. | Playwright viewport sweep with screenshots; review the set | R |
**Why and sources:** (J) practice; extends RSP-02.
| RSP-09 | With the on-screen keyboard open, a focused form field is still visible and not covered by a fixed bar (forms only). | Playwright at 375×667: shrink the viewport height to 50% to imitate the keyboard, focus each field, and assert `elementFromPoint` at the field's centre returns the field | C |
**Why and sources:** (J); Playwright cannot raise a real keyboard, so this is an approximation recorded as such.

### REPLACE MOT-01
| MOT-01 | Smooth under load. Gold: in a scripted full-page scroll at 1440×900 with no CPU throttle, p95 frame time ≤ 16.7 ms (one 60 Hz frame) and no frame over 50 ms; floor: with 4x CPU throttle p95 ≤ 25 ms and at most 5% of frames over 33 ms (J). Never worse than the original's measured values. | Playwright rAF timing during scroll at both CPU settings; Performance trace | G |
**Why and sources:** 16.7 ms is the 60 Hz frame budget; 50 ms is the long-task threshold (web.dev/optimize-long-tasks). Earlier floor kept.

### NEW after MOT-14
| MOT-15 | No long animation frame (over 50 ms) after the intro during a scripted run of every interaction and a full scroll, at the mobile CPU profile. Chromium only: the Long Animation Frames API is not Baseline, so other engines are `NOT_RUN` for this row. Long tasks are broken up with `scheduler.yield()` where it exists and a `setTimeout` fallback otherwise. | Playwright in Chromium: `PerformanceObserver` with `type: 'long-animation-frame'`, `buffered: true`; count entries after the ready flag | R |
**Why and sources:** developer.mozilla.org PerformanceLongAnimationFrameTiming (over 50 ms, limited availability); web.dev/optimize-long-tasks (`scheduler.yield()` in Chrome and Edge 129, Firefox 142, not Safari).

### REPLACE SEO-01
| SEO-01 | Unique, descriptive `<title>` per route and a unique meta description, built from the client's copy, else the drafted copy, or from template copy while the content status is `CONTENT-PENDING`. Google sets no title length limit and truncates to the device width, so the key words come first and the whole title stays near 60 characters (J); the site name sits at the start or end after a delimiter; the description is about 70 to 160 characters (J). No boilerplate shared by all routes and no trace of the design reference's name. | grep head on every route; length and uniqueness report | G |
**Why and sources:** developers.google.com/search/docs/appearance/title-link (no limit, truncation, branding, uniqueness).

### REPLACE SEO-05
| SEO-05 | Open Graph and card tags: `og:title`, `og:type`, `og:url` (canonical, on `SITE_URL`), `og:description`, `og:site_name`, `og:locale` (language_TERRITORY), `og:image` (absolute URL on `SITE_URL`, 1200×630, from the client's or stock imagery, or, when neither fits, a generated placeholder with the logo or wordmark) with `og:image:width`, `og:image:height` and `og:image:alt`, and `twitter:card=summary_large_image`. The image returns 200 with an image content-type, is under 600 KB (J), and keeps its key content inside the central 60% so crops do not cut it. | curl the tags; fetch the image's path on the local server and check status 200, an image content-type, 1200×630, size, and that `og:url` and the image sit on `SITE_URL`'s host (the deployed URL is checked by CNT-11) | G |
**Why and sources:** ogp.me (required: title, type, image, url; optional: description, site_name, locale, image:width, image:height, image:alt). The size cap and the safe area are (J).

### REPLACE SEO-10
| SEO-10 | `robots.txt` (allows crawling in production and links the sitemap with an absolute `Sitemap:` line) and `sitemap.xml` (UTF-8, every indexable route, absolute URLs on `SITE_URL`, at most 50,000 URLs and 50 MB) are served with 200. `lastmod` is set only from a real content change date and never to the build time (Google uses it only when it is verifiably accurate); `priority` and `changefreq` are omitted (Google ignores them). | curl both files in production mode; every sitemap URL, with its `SITE_URL` origin replaced by the local server's, returns 200; parse `lastmod` against the content file's git date (the deployed URL is checked by CNT-11) | G |
**Why and sources:** developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap.

### REPLACE SEO-11
| SEO-11 | JSON-LD `Organization` (and `WebSite`) uses only facts from `CLIENT_INPUT` and validates; it carries `name`, `url`, a crawlable `logo` of at least 112×112 px that looks right on white, `sameAs` for real profiles, and `contactPoint`, `address`, `telephone` or `email` only when the client supplied them; `name` matches the visible site name. It is omitted while the content status is `CONTENT-PENDING`. No other structured-data types unless the client's content supports them. | Parse the JSON-LD; check every value occurs in `CLIENT_INPUT` and the visible page; fetch the logo and read its size | G |
**Why and sources:** developers.google.com/search/docs/appearance/structured-data/organization.

### NEW after SEO-11
| SEO-12 | Image search hygiene: content images are real `<img>` elements with descriptive file names (not `IMG_0023.jpg`), a `src` fallback inside any `srcset` or `<picture>`, and a format Google supports (AVIF, WebP, JPEG, PNG, SVG). | Playwright over `img` and `picture`: file-name pattern, presence of `src`, content types | R |
**Why and sources:** developers.google.com/search/docs/appearance/google-images.
| SEO-13 | The owner verifies the domain in Google Search Console and Bing Webmaster Tools, submits the sitemap, and checks after two weeks that the landing page is indexed and the coverage report shows no errors. | Owner: record the dates and the coverage status in `docs/LAUNCH_CHECKLIST.md` | R-O |
**Why and sources:** (J) launch practice; the agent cannot hold these accounts.

### REPLACE I18N-01
| I18N-01 | If the site has more than one language (`brief.md` or the copy): `hreflang` alternates that list every version including itself, return links between versions, valid language and region codes (language first, a region never alone) and an `x-default`, given in the head or in the sitemap; `lang` on the `<html>` and on any inline switch of language; `dir` for RTL; a language switcher that keeps the current page and is a real link; no automatic redirect by IP or browser language (J); no hardcoded strings in code. | grep head; Playwright per locale; parse the `hreflang` set for reciprocity | C |
**Why and sources:** developers.google.com/search/docs/specialty/international/localized-versions (self-reference, return links, x-default, code rules, three implementation methods).

### NEW after I18N-01
| I18N-02 | Text expansion: translated strings are longer than English, by 130% for sources over 70 characters up to 200 to 300% for sources under 10 characters (W3C, from IBM guidelines), so no fixed-width box, button or navigation item clips or overlaps when each slot is made 1.4 times longer, and labels under 20 characters 2 times longer (J); scripts such as Thai, Arabic and Chinese need more line height. | Playwright pseudo-localisation: rewrite each text slot with longer text in the browser and run the clip and overlap checks | C |
**Why and sources:** w3.org/International/articles/article-text-size.
| I18N-03 | Script coverage: each shipped font covers the glyphs of every shipped language (checked against its `cmap`), or a fallback for that script is declared with metric adjustments; RTL languages use logical CSS properties so the layout mirrors. | fontTools `cmap` coverage of each language's characters; Playwright with `dir="rtl"` screenshot | C |
**Why and sources:** (J) practice; complements TYP-01 and TYP-02.
| I18N-04 | Dates, numbers, currencies and lists come from `Intl` formatters for the page's locale, never hardcoded patterns. | grep for date and number format literals; Playwright per locale | C |
**Why and sources:** (J) practice.

### NEW after CNT-16
| CNT-17 | Link text says where the link goes: no "click here", bare "read more" or bare URL as the only text of a link, unless the surrounding text or an `aria-label` gives it the full purpose (WCAG 2.4.4 and 2.4.9). | Playwright: list link names, flag the generic phrases and any duplicate name with a different target | R |
**Why and sources:** W3C WCAG 2.2 (link purpose); axe `link-name` covers only empty names.

### REPLACE SEC-06
| SEC-06 | No secrets in the repo, the bundle or the git history; `.env` ignored; `.env.example` present. | grep `dist/` and the repo, and `git log --all -p`, `.env.example` excluded, for key-shaped values (`AKIA[0-9A-Z]{16}`, `sk-[A-Za-z0-9_-]{20,}`, `-----BEGIN`) and for non-empty string literals assigned to names ending in `KEY`, `SECRET`, `TOKEN` or `PASS`; a variable name alone is not a finding | G |
**Why and sources:** a secret committed and later deleted is still in history (J).

### REPLACE SEC-07
| SEC-07 | `npm audit --omit=dev` shows 0 high or critical (or each is documented); `npm audit signatures` reports no invalid or missing registry signatures for packages that publish them; lockfile committed; `engines` and `.nvmrc` set to a Node release line that is in Active or Maintenance LTS (nodejs.org release schedule); production dependency licences reviewed. | `npm audit`; `npm audit signatures`; license checker; read `.nvmrc` against the release schedule | G |
**Why and sources:** nodejs.org/en/about/previous-releases (production apps should use an Active or Maintenance LTS line).

### NEW after SEC-12
| SEC-13 | Trusted Types: the CSP carries `require-trusted-types-for 'script'` and a `trusted-types` allowlist with one named policy, so DOM-XSS sinks such as `innerHTML` accept only values that passed the policy. Trusted Types is Baseline 2026 (February 2026). Library code that uses a sink is routed through the policy or replaced; if a vendor library cannot be, the row is `R` and the reason is logged. | Playwright: 0 `securitypolicyviolation` events across the scripted run in Chromium; `grep` for `innerHTML` in authored source | R |
**Why and sources:** developer.mozilla.org Trusted_Types_API (directives, sinks, Baseline 2026).
| SEC-14 | Cross-origin isolation where it costs nothing: with no third-party requests (SEC-05) the response also carries `Cross-Origin-Embedder-Policy: require-corp`, which together with `Cross-Origin-Opener-Policy: same-origin` (SEC-02) makes `crossOriginIsolated` true and isolates the page from speculative side channels. | `curl -sI`; Playwright `self.crossOriginIsolated === true`; no blocked resource in the console | R |
**Why and sources:** OWASP HTTP Headers cheat sheet (COEP `require-corp`, COOP `same-origin`, CORP `same-site`).

### NEW after MAIL-03
| MAIL-04 | If the client's domain receives mail: MTA-STS is published (a `_mta-sts` TXT record and a policy at `https://mta-sts.<domain>/.well-known/mta-sts.txt`, mode `testing` first, then `enforce`, with a `max_age` of weeks) and TLS reporting (`_smtp._tls` TXT, RFC 8460) is on, so senders refuse to deliver to a host without a valid certificate. The records are in `docs/DNS.md`. | `dig +short TXT _mta-sts.<domain>`; `curl -s https://mta-sts.<domain>/.well-known/mta-sts.txt`; `dig +short TXT _smtp._tls.<domain>` | C-L |
**Why and sources:** RFC 8461 (record, policy location, three modes, max_age); RFC 8460 is named from prior knowledge and not fetched here.
| MAIL-05 | The notification mail to the client is well formed: sent from one fixed address on the authenticated domain, `Reply-To` set to the visitor's address only after it validated, a plain-text part with the message and a timestamp, no HTML from the visitor, a fixed subject prefix, and TLS to the provider. | Capture the message in the local SMTP sink and inspect headers and parts | C |
**Why and sources:** Google Workspace sender requirements (TLS, SPF or DKIM, alignment); (J) for the message shape. Complements BACK-13.

### REPLACE EDGE-13
| EDGE-13 | Slow 3G and offline: content is readable on slow 3G. An offline fallback page exists only through a minimal, versioned service worker that precaches the shell, the 404 and the offline page, updates on deploy and never serves stale HTML after one; otherwise no service worker is registered. | Playwright network emulation and `context.setOffline(true)`; after a rebuild the new HTML is served on the next load | R |
**Why and sources:** (J) practice: a service worker is a second cache that can hide a deploy, so the default is none.

### REPLACE OPS-02
| OPS-02 | Performance budgets are enforced in CI: Lighthouse CI assertions at the gold targets of SPD-13 for both profiles, plus transferred bytes, JS bytes and request count (SPD-17); where a `FIDELITY-EXCEPTION` records a miss, the assertion is the measured value plus 5%. | `lighthouserc` file; `lhci autorun` run locally exits non-zero when a budget is lowered below the measured value | G |
**Why and sources:** web.dev/articles/performance-budgets-101 (Lighthouse CI enforcement); targets from SPD-13.

### NEW after OPS-07
| OPS-08 | A post-launch review at 7 and 30 days: the contact form is tested end to end, the error log is read, Search Console coverage and Core Web Vitals field data (when traffic is enough) are checked, certificates and domain renewal dates are confirmed, and any issue is fixed or logged. | Owner: record each review date and outcome in `docs/LAUNCH_CHECKLIST.md` | R-O |
**Why and sources:** (J) launch practice.
| OPS-09 | HTML and CSS are valid: `npx html-validate` (or the W3C Nu checker) reports 0 errors on every built page, and a CSS linter with the standard rule set reports 0 errors. | Run the validators over `dist`; errors caused only by a vendor attribute the reference needs are listed | R |
**Why and sources:** (J) practice; invalid markup is a common cause of accessibility-tree errors.

### NEW after HOST-18
| HOST-19 | DNS cutover is planned: the TTL of the records that change is lowered to 300 s at least as long before cutover as the old TTL, the old host stays up until the new one passes `audit:live`, the rollback is one record change, and the TTL is raised again afterwards (HOST-04). The steps are in `docs/DNS.md` (DEL-10). | Owner: record the TTL change time, the cutover time and the `audit:live` result in `docs/LAUNCH_CHECKLIST.md` | G-O |
**Why and sources:** (J) standard cutover practice; no primary source fetched.

### NEW after LEG-16
| LEG-17 | Counsel has reviewed the legal drafts (privacy notice, accessibility statement, terms and cookie notice where they apply) and the question of the reference design's rights (PROVENANCE); the "DRAFT: requires legal review" headings are removed only after that review. | Owner: record the reviewer, the date and the outcome in `docs/LAUNCH_CHECKLIST.md` | G-O |
**Why and sources:** restates the engineering-hygiene-not-legal-advice limit of the LEG section as a launch step.

### NEW after DEL-09
| DEL-10 | `docs/DNS.md` and `docs/DEPLOY.md` hold the cutover and rollback plan (HOST-19): the order of steps, who does each, the TTL change, the expected propagation, the verification commands and the one-step rollback. | Read the files; every command in them runs against the local server or returns a clear "needs the live URL" message | G |
**Why and sources:** (J) launch practice.
| DEL-11 | `docs/HANDOVER.md` lists what the client's team needs to own the site: contacts and roles, every third-party service (none by default, or the named provider), every account someone must create and who owns it (never a credential), every environment variable and what it does, the domain and certificate renewal dates, the licence table, and the known limitations. | Read the file; compare its variable list with `.env.example` and its service list with the request-origin set (SEC-05) | G |
**Why and sources:** (J) handover practice.
| DEL-12 | A content-editing guide for someone who does not write code: how to change text and images (`content/site.json`, `npm run content:sync`, the image sizes in `docs/client-input-template/`), how to preview, rebuild and deploy, and what not to touch. It fits on two pages. | Read the file; run the documented steps in a scratch copy and confirm a text change reaches the built page | R |
**Why and sources:** (J) handover practice.
| DEL-13 | Maintenance and support are written down: the dependency update policy (OPS-06), the Node LTS line in use and when to move (an Active or Maintenance LTS line, per the Node release schedule), a yearly check (certificates, domain, legal pages, accessibility statement date, stock licences), and who to contact for a problem. | Read the file | R |
**Why and sources:** nodejs.org/en/about/previous-releases (LTS statuses).
| DEL-14 | An acceptance record, `docs/ACCEPTANCE.md`, with fields for the gate table, the client's approval of every `drafted` and `stock` slot, the operator's reading of `docs/FIDELITY_EXCEPTIONS.md`, the open `OWNER-CONFIRM` rows, and the names and dates of those who signed. | Read the file; its gate table matches `production.md` | G |
**Why and sources:** (J) handover practice.
