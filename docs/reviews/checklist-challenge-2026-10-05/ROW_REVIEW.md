# Complete row decisions

Compared with draft PR commit `d9ae192`. All 275 rows were inspected; changed criteria require reassessment, not automatic PASS. Historical results are unchanged.

| ID | Before | After | Changed | Reason |
|---|---|---|---|---|
| SPD-01 | Gold | Gold | requirement, verify | Measured loading and stability targets must be met, not merely recorded; lab and field claims remain separate. |
| SPD-02 | Gold | Bronze | tier | This is a reference-relative benchmark, so its score is fidelity bookkeeping; SPD-01 and SPD-13 protect actual shipped performance. |
| SPD-03 | Gold | Gold | Retained | The LCP asset’s discoverability and priority directly affect when users can see the main content, which fits Gold performance. |
| SPD-04 | Gold | Gold | Retained | Intrinsic dimensions prevent avoidable layout shifts and lazy loading avoids needless off-screen work, both measurable user-facing performance outcomes. |
| SPD-05 | Gold | Gold | Retained | Responsive image bytes and decoded dimensions affect mobile load time and visual quality, so the measured trade-off belongs in Gold. |
| SPD-06 | Diamond | Diamond | requirement, verify | A shared-cache leak can expose private user data, so Diamond applies only when private or personalized responses exist; public asset caching remains a performance optimization. |
| SPD-07 | Gold | Gold | Retained | Compressing large text responses reduces transfer bytes, while measured savings avoid making tiny responses slower or larger. |
| SPD-08 | Gold | Gold | requirement, verify | Loading unused or duplicate libraries adds bytes and execution cost, but population medians do not define a useful site-specific budget. |
| SPD-09 | Gold | Diamond | requirement, verify, tier | A blocking intro can keep users from the form or primary task when assets stall, a direct task failure; apply only when the shipped experience has an authored blocking intro. |
| SPD-10 | Silver | Silver | Retained | A poster and deferred video fetch reduce unnecessary bytes, which is a useful optional optimization rather than a release safety gate. |
| SPD-11 | Gold | Gold | Retained | Back/forward cache restoration reduces repeat waits and improves navigation reliability without weakening privacy-required cache policy. |
| SPD-12 | Silver | Silver | Retained | Speculation Rules are optional and must not trigger side-effect or private requests; ordinary navigation remains the supported fallback. |
| SPD-13 | Gold | Gold | requirement, verify | Gold needs falsifiable quality acceptance, with thresholds chosen before seeing results. |
| SPD-14 | Gold | Gold | requirement, verify | A p95 from only 20 sequential warm requests is unstable, and a universal 50 ms local-origin target does not map to visitor experience. |
| SPD-15 | Gold | Silver | requirement, verify, tier | Auditor-location TTFB and a fixed RTT formula are diagnostic signals, not stable user outcomes; SPD-20 and SPD-21 retain deployment and field performance evidence. |
| SPD-16 | Silver | Silver | requirement, verify | Fourteen KiB is a house transfer cap rather than a standard user threshold; SPD-17 protects the measured critical path. |
| SPD-17 | Gold | Gold | requirement, verify | The 170 KB caps are arbitrary without a supported-device budget, although identifying render-critical bytes is directly useful for performance. |
| SPD-18 | Gold | Gold | requirement, verify | Avoidable parser-blocking work delays rendering, but a one-stylesheet/30 KiB cap is an implementation constraint rather than a user outcome. |
| SPD-19 | Silver | Bronze | requirement, verify, tier | Requiring precompressed .br/.gz siblings and maximum compression levels is build-system bookkeeping; SPD-07 protects delivered bytes and negotiated compression behavior. |
| SPD-20 | Gold | Gold | Retained | Repeating lab measurements against the final HTTPS build catches content and deployment regressions before claiming shipped performance. |
| SPD-21 | Gold | Silver | requirement, verify, tier | Low-traffic sites may never reach an eligible field sample, so unavailable data cannot safely block release; SPD-01/13 retain lab checks and no field-pass claim is allowed. |
| TYP-01 | Gold | Silver | requirement, verify, tier | Self-hosting and WOFF2 subsetting are implementation optimizations; declared language coverage and visible fallback matter, while no remote/self-host rule is needed for comprehension. |
| TYP-02 | Gold | Gold | requirement, verify | A metric-matched fallback can prevent visible text shifts, but the 0.01 CLS cap and browser-support claim are not universal performance standards. |
| TYP-03 | Gold | Gold | requirement, verify | Preloading noncritical fonts competes with the page’s main content, so only assets proven to be render-critical should be prioritized. |
| TYP-04 | Gold | Silver | requirement, verify, tier | Synthetic weight or italics can be visually imperfect but do not by themselves block content; TYP-23 readability and TYP-11 contrast protect legibility. |
| TYP-05 | Diamond | Diamond | Retained | A valid document language helps assistive technology pronounce content correctly, preventing an avoidable accessibility barrier. |
| TYP-06 | Diamond | Diamond | Retained | Loss of text or controls at 200% enlargement directly excludes users who need magnification, so this is a Diamond access requirement. |
| TYP-07 | Silver | Bronze | requirement, verify, tier | Balancing and pretty wrapping are reference-dependent visual choices; TYP-23 protects readable body text and RSP-03 protects reflow. |
| TYP-08 | Silver | Silver | Retained | Tabular numerals prevent animated counters and aligned prices from shifting as digits change, a localized polish improvement. |
| TYP-09 | Gold | Silver | requirement, verify, tier | Forcing text-size-adjust to 100% can suppress helpful browser text inflation; TYP-06 protects user enlargement, so this remains optional tuning. |
| TYP-10 | Gold | Gold | Retained | Avoiding mobile input zoom reduces focus jumps during form completion, a measurable form-usability improvement when form controls exist. |
| TYP-11 | Diamond | Diamond | Retained | Insufficient text or control contrast can make core content and actions inaccessible, so the criterion-level contrast threshold belongs in Diamond. |
| TYP-12 | Gold | Silver | tier | Theme-color and overscroll flash are cosmetic polish; contrast and content access remain protected by TYP-11 and RSP-03. |
| TYP-13 | Gold | Silver | tier | A colored placeholder reduces a visual flash, while SPD-04 already prevents image-driven layout shifts that affect task stability. |
| TYP-14 | Silver | Silver | Retained | Avoiding visible gradient banding and ineffective fixed backgrounds improves visual finish but does not block the main task. |
| TYP-15 | Gold | Silver | requirement, verify, tier | A vendor prefix and visual fallback are optional implementation details; TYP-11 ensures readability if the blur effect is unavailable. |
| TYP-16 | Silver | Silver | Retained | On-brand selection, caret and accent colors are a low-cost polish improvement; default UI contrast remains governed by TYP-11. |
| TYP-17 | Gold | Gold | Retained | Stable scrollbar space prevents a small but measurable horizontal layout jump when a menu or modal locks scrolling. |
| TYP-18 | Diamond | Diamond | requirement, verify | Keyboard users can be excluded when focus disappears, but the current row incorrectly imports AAA focus geometry into AA. |
| TYP-19 | Gold | Silver | requirement, verify, tier | CSS media-query gating is implementation detail; RSP-07 keeps hover-only functionality available to touch and keyboard users. |
| TYP-20 | Silver | Silver | Retained | A print stylesheet is optional convenience for visitors who print the page, not a core web task or accessibility release gate. |
| TYP-21 | Gold | Diamond | requirement, verify, class, tier | When authored styling removes system cues, forced-colors users can lose controls or focus; test that conditional barrier. |
| TYP-22 | Bronze | Diamond | requirement, verify, class, tier | A control hidden by a cutout or browser chrome blocks the task; viewport-unit imitation has no safety value. |
| TYP-23 | Silver | Silver | requirement, verify | The row mixes useful readability guidance with AAA and house heuristics; only the spacing override is an AA criterion, covered by A11Y-16. |
| TYP-24 | Gold | Silver | requirement, verify, tier | The 2-family/4-file/100 KB caps are arbitrary and overlap SPD-17; measured critical-path performance is the stronger Gold protection. |
| RSP-01 | Diamond | Diamond | requirement, verify | Disabling zoom can remove a user’s magnification path, but the exact maximum-scale cutoff is not itself a WCAG criterion. |
| RSP-02 | Gold | Gold | requirement, verify | Its width list is a subset of RSP-08 and only checks rest state; keep it distinct by catching overflow introduced by interaction states. |
| RSP-03 | Diamond | Diamond | requirement, verify | WCAG 1.4.10 AA sets 320 CSS px reflow but allows content that requires two-dimensional layout; an absolute no-scroll rule would misclassify valid data. |
| RSP-04 | Diamond | Diamond | requirement, verify | Orientation lock can exclude users in one orientation, but WCAG 1.3.4 permits it where a specific orientation is essential. |
| RSP-05 | Diamond | Diamond | Retained | WCAG 2.5.8 protects pointer users from undersized controls and expressly allows its spacing, equivalent, inline, user-agent and essential exceptions. |
| RSP-06 | Gold | Gold | requirement, verify | Cross-engine smoke tests catch browser-specific breaks, but three named Playwright engines do not define every site’s supported audience or prove physical-device behavior. |
| RSP-07 | Diamond | Diamond | requirement, verify | A hover-only task can disappear for touch users; keyboard operability is separately protected by A11Y-05 and hover/focus content by A11Y-17. |
| RSP-08 | Gold | Gold | requirement, verify | The fixed 11-size sweep is mostly redundant viewport sampling; breakpoint edges, supported devices and extreme short/wide layouts reveal the actual failure modes. |
| RSP-09 | Diamond | Diamond | requirement, verify | A half-height Playwright viewport is not an iOS keyboard and a center-point hit test can fail valid layouts; a covered focused form field can still block submission. |
| RSP-10 | Gold | Gold | requirement, verify | Real devices expose browser chrome, keyboard and safe-area behavior that emulation misses, but media/form subchecks apply only when those features exist. |
| A11Y-01 | Diamond | Diamond | requirement, verify | Axe is useful for finding candidate WCAG failures but cannot establish conformance, and a fidelity branch must not ship known accessibility barriers. |
| A11Y-02 | Bronze | Bronze | requirement, verify | Population-frequency percentages do not identify harm on this site, and the six scan categories overlap A11Y-01, A11Y-08, A11Y-11, TYP-05 and TYP-11. |
| A11Y-03 | Diamond | Diamond | requirement, verify | A rigid one-main/header/nav/footer structure is not a WCAG requirement; lack of a way around repeated blocks is the actual keyboard barrier. |
| A11Y-04 | Diamond | Diamond | requirement, verify | WCAG requires meaningful structure to be programmatically determinable, not exactly one H1 or a ban on every skipped level. |
| A11Y-05 | Diamond | Diamond | requirement, verify | Keyboard access, focus containment and return are core barriers for implemented controls, while pattern requirements should follow the actual component rather than the reference. |
| A11Y-06 | Diamond | Diamond | requirement, verify | WCAG 2.4.11 AA fails only when author-created content entirely hides the focused component; requiring zero overlap asserts the AAA 2.4.12 outcome. |
| A11Y-07 | Diamond | Diamond | Retained | Where authored dragging is present, a click/tap alternative serves pointer users who cannot drag; keyboard access alone does not satisfy that separate need. |
| A11Y-08 | Diamond | Diamond | requirement, verify | Missing alternatives can hide image information, while a generic role/label on canvas cannot substitute for equivalent chart or stage content. |
| A11Y-09 | Diamond | Diamond | requirement, verify | Uncontrolled motion can harm or exclude people who request reduced motion, but this is an inclusive house behavior rather than a blanket WCAG 2.2 AA mandate. |
| A11Y-10 | Diamond | Diamond | requirement, verify | Qualifying auto-motion needs a usable control and flashes can cause seizure harm, but WCAG 2.2.2 and 2.3.1 are separate criteria with different tests. |
| A11Y-11 | Diamond | Diamond | Retained | Forms without visible instructions, associated names or usable error feedback can block the site’s core enquiry task for assistive-technology users. |
| A11Y-12 | Diamond | Diamond | requirement, verify | Client-side route changes can leave screen-reader users on stale context, but the title/focus/live-region triple is not a universal WCAG-mandated recipe. |
| A11Y-13 | Diamond | Diamond | requirement, verify | A hidden native pointer with a reference-matched custom cursor can make controls difficult to locate; visual fidelity does not justify removing pointer feedback. |
| A11Y-14 | Diamond | Diamond | requirement, verify | WCAG 1.4.2 governs automatically playing audio over three seconds, while the house no-autoplay-sound rule is a stricter protection against surprise and sensory disruption. |
| A11Y-15 | Diamond | Diamond | requirement, verify | When a current-page or selected state conveys information visually, users of assistive technology need equivalent state information. |
| A11Y-16 | Diamond | Diamond | Retained | WCAG 1.4.12 requires content to survive user-set spacing values, so clipping or lost control labels under the override can exclude users. |
| A11Y-17 | Diamond | Diamond | requirement, verify | Hover/focus-only content can disappear before users reach it; the reference is not an exception to WCAG 1.4.13 where that criterion applies. |
| A11Y-18 | Diamond | Gold | requirement, verify, tier | A documented screen-reader sample improves detection, but a fixed desktop/mobile pairing is not itself WCAG conformance; A11Y-22 retains the manual A/AA release gate. |
| A11Y-19 | Diamond | Diamond | requirement, verify | Repeated help placement and redundant data entry are separately addressed by WCAG 3.2.6 and 3.3.7, both Level A; the latter has explicit essential/security/stale-data exceptions. |
| A11Y-20 | Diamond | Diamond | requirement, verify | People unable to hear or see meaningful media need equivalent information; prerecorded captions are Level A, not AA. |
| A11Y-21 | Silver | Silver | requirement, verify | A contrast-preference enhancement is optional polish; default contrast failures remain Diamond under TYP-11 and cannot be waived by an alternate build. |
| A11Y-22 | Diamond | Diamond | Retained | An automated zero-violation scan cannot evaluate every applicable WCAG criterion or complete process, so a dated A/AA review protects against unexamined access barriers. |
| SEO-01 | Gold | Gold | Retained | Unique route metadata improves search-result identification; copy-length guidance is not a launch blocker. |
| SEO-02 | Diamond | Diamond | Retained | Unapproved or draft content must not become an indexable production release. |
| SEO-03 | Diamond | Gold | tier | Correct not-found status improves routing and search quality; required destination failures remain Diamond under SEO-08 and UXF-01. |
| SEO-04 | Diamond | Gold | requirement, verify, tier | Users and crawlers need readable content, but source-HTML rendering is not universally necessary. |
| SEO-05 | Silver | Silver | Retained | Share cards improve previews; image dimensions and payload are optimization details. |
| SEO-06 | Silver | Silver | Retained | Favicons improve recognition but do not determine whether the site works. |
| SEO-07 | Diamond | Gold | requirement, verify, tier | Canonical routing affects navigation and discoverability; HTTPS belongs to security controls. |
| SEO-08 | Diamond | Diamond | requirement, verify | Broken required destinations or inaccessible navigation prevent the promised journey; one literal HTML attribute is not the outcome. |
| SEO-09 | Silver | Silver | Retained | A security contact file is useful when the client supplies a responsible contact. |
| SEO-10 | Gold | Gold | Retained | Accurate crawl directives and sitemap entries improve discovery without guaranteeing indexing. |
| SEO-11 | Diamond | Diamond | requirement, class | Machine-readable claims must be truthful when published; installing schema markup is optional. |
| SEO-12 | Gold | Gold | Retained | Real image elements and fallbacks improve image discovery and rendering reliability. |
| SEO-13 | Gold | Gold | Retained | Owner evidence prevents an indexing report from being mistaken for a guarantee. |
| SEO-14 | Gold | Gold | Retained | Broken external references degrade real user paths; blocked bots need contextual handling. |
| SEO-15 | Silver | Silver | Retained | Search research is optional scope, not a universal launch task. |
| SEO-16 | Bronze | Bronze | Retained | Distribution needs owner approval and eligibility evidence; it is not build readiness. |
| SEO-17 | Bronze | Bronze | Retained | Crawler controls are optional discovery policy and never authenticate private content. |
| EDGE-01 | Bronze | Bronze | Retained | A captured baseline helps reproduce the reference’s error-page treatment. |
| EDGE-02 | Diamond | Gold | requirement, verify, tier | Visitors need a useful recovery path, but a well-styled 404 is not a security gate. |
| EDGE-03 | Gold | Gold | Retained | Clear, blame-free error text helps visitors recover without adding technical requirements. |
| EDGE-04 | Diamond | Gold | requirement, verify, tier | Missing resources should fail accurately; a universal 60-second cache ceiling has no user basis. |
| EDGE-05 | Diamond | Diamond | requirement, verify | A failed decorative resource must not hide essential content or block the main task. |
| EDGE-06 | Diamond | Gold | requirement, verify, tier | JavaScript-disabled support is quality engineering, not a universal legal condition. |
| EDGE-07 | Diamond | Gold | requirement, verify, tier | WebGL fallback is useful; MOT-05 owns the essential-task failure condition. |
| EDGE-08 | Gold | Gold | requirement, verify | Unexpected failures need correction; harmless warnings do not make a site unusable. |
| EDGE-09 | Diamond | Diamond | requirement, verify | False form success and URL exposure create direct task and privacy harms. |
| EDGE-10 | Gold | Gold | requirement, verify | History should remain usable when app navigation overrides browser behavior. |
| EDGE-11 | Gold | Gold | requirement, verify | Text extremes can hide controls or facts, especially on narrow screens. |
| EDGE-12 | Diamond | Gold | requirement, verify, tier | The banner’s usability is quality; legal consent obligations are owned by LEG-09. |
| EDGE-13 | Silver | Silver | requirement, verify | Offline support is optional unless promised; stale cached content can mislead. |
| EDGE-14 | Diamond | Gold | requirement, verify, tier | State coverage finds clipped controls; contrast and accessibility must use independent criteria. |
| EDGE-15 | Gold | Silver | requirement, verify, tier | A fixed 14 KB and 1-second target is an unsupported budget for every 404. |
| EDGE-16 | Silver | Silver | Retained | Path suggestions are optional convenience and must remain safely text-escaped. |
| EDGE-17 | Diamond | Gold | requirement, verify, tier | Historical-route migration matters when replacing an existing client site, not for every build. |
| EDGE-18 | Diamond | Diamond | requirement, verify, class | Present server handlers must fail honestly and safely without exposing internals; static sites do not need an invented server endpoint. |
| UXF-01 | Diamond | Diamond | requirement, verify | A dead primary control blocks the task; 400 ms and cursor-pointer heuristics are arbitrary. |
| UXF-02 | Diamond | Diamond | Retained | Honest pending, failure and recovery states prevent duplicate or lost submissions. |
| UXF-03 | Diamond | Gold | requirement, verify, tier | CTA placement is quality; broken destinations remain Diamond under interaction and route checks. |
| UXF-04 | Diamond | Gold | requirement, verify, tier | Correct client contact details are critical elsewhere; link ergonomics belong at Gold. |
| UXF-05 | Diamond | Diamond | Retained | Form minimization, labeling and recoverable errors protect privacy and the primary task. |
| UXF-06 | Gold | Gold | requirement, verify | Touch reliability matters, while AAA 44-pixel targets exceed the applicable minimum. |
| UXF-07 | Diamond | Diamond | requirement, verify | False claims, coercion and deceptive controls can directly manipulate user decisions. |
| UXF-08 | Diamond | Diamond | requirement, verify | Essential text must work with assistive technology and text-based tools. |
| UXF-09 | Gold | Gold | requirement, verify | Clear business, service and next action improve conversion without invented audience claims. |
| UXF-10 | Gold | Gold | requirement, verify | Unexpected browser recoloring can make controls hard to use; the implementation tag is optional. |
| UXF-11 | Gold | Gold | requirement, verify | A reachable contact action matters; copying a poor reference path or fixed click cap does not. |
| MOT-01 | Gold | Gold | requirement, verify | Visible stalls hurt interaction; reference-relative frame counts and universal thresholds are unjustified. |
| MOT-02 | Gold | Silver | requirement, verify, tier | Animation property choices should follow measured cost, not a blanket CSS prescription. |
| MOT-03 | Gold | Silver | requirement, verify, tier | ScrollTrigger cleanup matters when used; the exact API is an implementation choice. |
| MOT-04 | Bronze | Bronze | Retained | Lenis wiring is conditional specialist fidelity work, not a general user requirement. |
| MOT-05 | Diamond | Diamond | requirement, verify | Essential content must survive graphics failure; DPR and heap thresholds are optimization choices. |
| MOT-06 | Diamond | Gold | requirement, verify, tier | Resize errors reduce quality but do not normally defeat the core site task. |
| MOT-07 | Bronze | Bronze | requirement, verify | Transition effects are reference details; focus and navigation outcomes are covered elsewhere. |
| MOT-08 | Silver | Silver | requirement, verify | Cursor effects are optional; reduced-motion access remains a separate required outcome. |
| MOT-09 | Bronze | Bronze | Retained | Scrubbed-video encoding is a specialized reference-matching technique. |
| MOT-10 | Bronze | Bronze | Retained | A ready signal makes capture tests reliable but does not affect visitors. |
| MOT-11 | Bronze | Bronze | requirement, verify | Frame-rate review is specialist fidelity evidence, not a reason to copy frame-dependent bugs. |
| MOT-12 | Gold | Gold | requirement, verify | Rejected autoplay should not strand media or disrupt surrounding content. |
| MOT-13 | Gold | Silver | requirement, verify, tier | GPU leak monitoring is optional diagnosis; user-visible context failure is handled by MOT-05. |
| MOT-14 | Gold | Silver | requirement, verify, tier | Passive listeners are a tuning choice unless they visibly block normal scrolling. |
| MOT-15 | Gold | Silver | requirement, verify, tier | Long-task observation is useful tuning, but a non-baseline browser API is not a launch gate. |
| SEC-01 | Diamond | Gold | requirement, verify, tier | The production-mode artifact must be exercised because development servers can hide routing and header failures. Requiring npm run start, compression, cache rules and a single audit command everywhere overstates the control; selected-host behavior is the evidence. |
| SEC-02 | Diamond | Gold | requirement, verify, tier | Several listed headers are useful hardening, but their absence alone is not an exploitable flaw on every site. COOP and CORP can break OAuth popups and cross-origin assets; an informative Server banner is low-value disclosure and HOST-16 already says a generic Server header is not a missing security control. |
| SEC-03 | Diamond | Diamond | requirement, verify | An HTTP-to-HTTPS downgrade can expose traffic to active interception, so deployed HTTPS enforcement matters. A fixed two-year lifetime, preload and includeSubDomains create lock-in and can break subdomains; they are not a universal minimum. |
| SEC-04 | Diamond | Gold | requirement, verify, tier | CSP can limit the impact of script injection, but a self-only policy is not a universal exploit fix and can break approved fonts, embeds, payments, CAPTCHA or analytics. The actual requirement is a least-privilege policy that fits the rendered site. |
| SEC-05 | Diamond | Diamond | requirement, verify | Unreviewed requests can disclose visitor IP, referrer or interaction data, and remote scripts can change after review. A literal zero-origin rule conflicts with legitimate approved providers and with CSP exceptions; approved, bounded providers are not inherently unsafe. |
| SEC-06 | Diamond | Diamond | requirement, verify | A committed token can enable account takeover or expose client data; detection must cover the delivered artifact and repository history, and a confirmed credential must be revoked. Requiring bespoke scanner rules or scanning unreachable Git objects on every hosting workflow is tool-specific. |
| SEC-07 | Diamond | Diamond | requirement, verify | A shipped exploitable dependency or unreviewed install hook can compromise the client site or build credentials. Severity labels alone are insufficient: the decision depends on reachability, exposure, exploitability and mitigation. SBOM/signature paperwork and broad license administration are not the same security control. |
| SEC-08 | Gold | Diamond | requirement, verify, tier | Actual confidential-data disclosure is a release blocker regardless of which debugging tool exposes it. |
| SEC-09 | Diamond | Diamond | requirement, verify | An insecure session cookie or unnecessary tracking storage can create account compromise or privacy exposure. The control must apply only to storage the site actually uses; blanket absence rules can conflict with owner-approved consent, preferences or authentication features. |
| SEC-10 | Diamond | Gold | requirement, verify, tier | Ignoring generated files and documenting setup support a reliable handover, but README and .gitignore checks do not prevent a tracked secret. The proposed AI-authorship/copyright assertions are legal conclusions and can falsely disclaim rights; rights belong in LEG-14, not a boilerplate license. |
| SEC-11 | Gold | Gold | requirement, verify | A repeatable verification entry point that fails on real build or journey failures improves release reliability. npm run verify, Playwright, axe and an offline audit are implementation choices, not universal foundations; accessibility is assessed in its own rows. |
| SEC-12 | Diamond | Diamond | requirement, verify, class | Unreviewed remote executable code can change independently and compromise visitors. SRI is useful for immutable cross-origin bytes when browser CORS rules permit it, but it is not applicable to every dynamic API or changing provider resource. |
| SEC-13 | Gold | Diamond | requirement, verify, tier | Client-side injection remains dangerous even when a site has no backend; a Trusted Types tool mandate is unnecessary. |
| SEC-14 | Silver | Silver | requirement | COOP/COEP can isolate browsing contexts and enable specific APIs, but blanket use can break OAuth popups, downloads and embeds. The row correctly makes adoption conditional on a real need and compatibility test. |
| SEC-15 | Diamond | Diamond | requirement, class | Where CI/deployment automation exists, untrusted jobs and third-party actions must not obtain production credentials or bypass artifact review. |
| BACK-00 | Diamond | Diamond | requirement, verify | An incomplete system/data inventory can hide applicable security and privacy duties; the format is optional. |
| BACK-01 | Diamond | Diamond | requirement | A contact form is the core enquiry journey. A successful local mail sink or a different serverless adapter does not establish that the chosen runtime sends the client’s message; missing credentials must fail visibly before launch. |
| BACK-02 | Diamond | Gold | requirement, verify, tier | Allowlisting methods/content types and returning clear status codes makes the endpoint predictable, but 405/415 semantics alone are not an exploitable failure. Unbounded bodies are a resource-exhaustion risk and remain Diamond controls in BACK-04 and BACK-17. |
| BACK-03 | Diamond | Diamond | requirement, verify | Client-side checks can be bypassed. Unsafe server parsing or output of submitted values can enable injection, resource abuse or disclosure; safe rejection must not leak internals. |
| BACK-04 | Diamond | Diamond | requirement, verify | An unauthenticated endpoint can be flooded or used to incur provider charges. A hard per-IP number is not universal: users share IPs, forwarded headers can be forged, and serverless instances do not share memory. |
| BACK-05 | Diamond | Diamond | requirement, verify | Cookie-authenticated state changes can be forged by cross-site requests. SameSite alone has sibling-domain and safe-method gaps; CAPTCHA does not establish request origin. The old rule also omits PATCH and overstates which APIs need CSRF defenses. |
| BACK-06 | Diamond | Diamond | requirement, verify | A credentialed permissive CORS response can expose private browser-readable data, but CORS does not authenticate direct requests or stop CSRF by itself. Same-origin-only routes need no CORS grant; public resources may have a deliberate wider policy. |
| BACK-07 | Diamond | Diamond | requirement, verify | Caching an authenticated response under a shared key can leak private user data. Conversely, frame-ancestors is a document-framing control and has little meaning on ordinary JSON responses; requiring it on every API response is not a useful universal gate. |
| BACK-08 | Diamond | Diamond | requirement, verify | A form endpoint without its provider config cannot complete the core journey, while exiting the whole site because an optional integration is unconfigured creates unnecessary downtime. Diagnostics must not reveal credentials. |
| BACK-09 | Diamond | Gold | requirement, verify, tier | Request IDs and redacted failure records make incidents diagnosable, but absent structured logs do not themselves create an exploit. Input validation, throttling and authorization must prevent attacks independently; a static site has no server log to configure. |
| BACK-10 | Diamond | Diamond | requirement, verify | Unbounded provider waits can leave a visitor uncertain; blind retries can duplicate or lose an enquiry when a timeout is ambiguous. Retry safety depends on provider idempotency and actual side effects. |
| BACK-11 | Gold | Silver | requirement, verify, tier | A minimal health endpoint can help a chosen host monitor, but it is optional infrastructure and a universal route can expose unnecessary service detail. Serverless monitoring may use provider-native checks. |
| BACK-12 | Diamond | Diamond | requirement | The anti-abuse control must not reject legitimate keyboard, autofill or assistive-technology use. A false positive blocks the only enquiry route and can exclude a disabled visitor, while a challenge needs an accessible alternative. |
| BACK-13 | Diamond | Diamond | requirement | Newline injection into Reply-To or another email header can add attacker-controlled recipients or alter routing. A fixed authenticated From address and CR/LF rejection directly prevent that header path. |
| BACK-14 | Diamond | Diamond | requirement, verify | Storing unnecessary enquiry data or leaking it into URLs, logs or analytics creates privacy and legal exposure. A site that immediately forwards an enquiry has no application database deletion endpoint to invent; retention must cover actual processors and stores. |
| BACK-15 | Diamond | Silver | requirement, verify, tier | A shared atomic idempotency store across all contact handlers is an architecture tax and can suppress two legitimate identical enquiries. Exactly-once email delivery is unavailable without provider support. Duplicate charge/order side effects remain Diamond in BACK-22/23. |
| BACK-16 | Bronze | Bronze | requirement | The row is specialist supply-chain hygiene and is already Bronze; its meaningful lockfile/install-script risks are covered at Diamond by SEC-07/SEC-12. npm audit signatures is explicitly conditional on package-manager support, so it should not be a universal security claim. |
| BACK-17 | Diamond | Diamond | requirement, verify | Malformed or streamed input must not crash a public handler or consume unbounded memory; unsafe output can turn an enquiry into script/header injection. These are direct DoS and injection paths. |
| BACK-18 | Diamond | Diamond | requirement | If accounts or private tenant data exist, trusting body-supplied owner IDs permits direct object access and cross-tenant disclosure. The predicate correctly makes full authorization-matrix testing conditional. |
| BACK-19 | Gold | Gold | requirement | Database latency and query growth affect a real list/search journey, but budgets must use representative data and actual permissions. A production load test or a guessed p95 target would add risk without evidence. |
| BACK-20 | Diamond | Diamond | requirement | A cache key that omits identity, tenant, locale or permissions can serve one user’s private data to another. This row correctly activates only when application-data caching exists and tests logout and permission changes. |
| BACK-21 | Gold | Gold | requirement | When the application opens SQL connections, pool mode and aggregate replica limits determine whether bursts exhaust a shared database. A managed data API does not imply the application’s pool was tested; no SQL feature means N/A. |
| BACK-22 | Diamond | Diamond | requirement | Forged, replayed or out-of-order provider events can grant access or mark the wrong payment state. Signature verification over the raw body and atomic deduplication protect actual trusted webhook flows; absent webhooks are N/A. |
| BACK-23 | Diamond | Diamond | requirement | A sandbox cannot prove the real production merchant, final callback or receipt path, and payment status has financial and legal consequences. Owner authorization is necessary for any live financial action. |
| MAIL-01 | Diamond | Diamond | requirement, verify | Authentication and mailbox delivery are separate evidence. Google’s current rule is SPF or DKIM for all senders and SPF, DKIM and DMARC for bulk senders; it recommends all three generally. Requiring aligned DMARC enforcement for every low-volume transactional sender can break legitimate mail, especially when old senders or forwarding are missed. |
| MAIL-02 | Diamond | Diamond | requirement | Marketing mail can create direct statutory and provider-rule violations; the row correctly limits scope to actual marketing and notes that transactional mail is treated differently. The FTC’s 10-business-day processing and 30-day availability rules are verified; Gmail one-click is conditional on bulk promotional messages. |
| MAIL-03 | Silver | Silver | requirement | Separate identities/streams may reduce operational coupling, but provider reputation isolation is not guaranteed and there is no marketing stream on a transactional-only site. Keeping the monitored Reply-To and N/A predicate avoids overclaiming. |
| MAIL-04 | Silver | Silver | requirement | MTA-STS is a receiving-domain transport policy, not a requirement for every site’s outgoing form notification. RFC 8461 testing mode reports policy failures while allowing normal delivery; enforcement misconfiguration can delay mail. |
| MAIL-05 | Diamond | Gold | requirement, verify, tier | Readable mail and a validated reply route support the enquiry journey, but a local SMTP sink proves only formatting. CR/LF injection is the Diamond control in BACK-13, and actual inbox delivery is MAIL-06; a fixed subject prefix or timestamp is not universally required. |
| MAIL-06 | Diamond | Diamond | requirement | The purpose of a contact form is a delivered enquiry. Provider acceptance and a local sink do not show that the named client mailbox receives or can reply to it; the final-domain test closes the actual journey. |
| MAIL-07 | Diamond | Diamond | requirement | A missing reset, verification or billing message can lock an account or conceal a financial state. The requirement is conditional on real transactional flows and correctly rejects invented flows or fake provider-acceptance evidence. |
| HOST-01 | Diamond | Diamond | requirement, verify | A wrong or expired certificate breaks secure access; an HTTP path that serves content can expose users. A fixed 14-day remaining-life rule and exactly one 301 are arbitrary snapshots, while 301 versus 308 can change POST semantics. |
| HOST-02 | Diamond | Diamond | requirement, verify | TLS protects credentials and content in transit. TLS 1.0/1.1 are formally deprecated; test compatibility against the actual public server rather than relying on a brittle external badssl control host or a dated Mozilla profile label. |
| HOST-03 | Diamond | Diamond | requirement, verify | Certificate expiry breaks the site and undermines HTTPS. Renewal timing depends on CA and host; fixed 60-day cron or hardcoded two-thirds lifetime can become wrong as lifetimes and CA recommendations change. RFC 9773 defines dynamic ACME renewal windows. |
| HOST-04 | Diamond | Diamond | requirement, verify | Wrong authoritative records can take the site or business email offline; a dangling owner-controlled service record can permit takeover. CAA and a universal 300–3600 second TTL are hardening/operations choices, not universal security prerequisites. |
| HOST-05 | Silver | Silver | requirement | HTTP/2 or HTTP/3 can improve transport efficiency, but absence does not block a site journey and actual support depends on the selected host/client. This is correctly an optional delivery optimization. |
| HOST-06 | Silver | Silver | requirement | A cache hit on hashed static files can reduce latency and origin load, but CDN placement and provider cache headers differ. The row is optional optimization rather than core safety. |
| HOST-07 | Diamond | Gold | requirement, tier | A real 404 helps visitors and search engines distinguish missing routes, but soft-404 behavior is not an exploitable security failure or a reason to block the core enquiry journey. Gold fits predictable navigation. |
| HOST-08 | Diamond | Diamond | requirement, verify | Correct controls must reach the deployed document and function responses, but listing Cloudflare/Netlify/Vercel/nginx files, line limits and npm start is an architecture-specific implementation recipe. The response behavior, not filename, is the security gate. |
| HOST-09 | Diamond | Diamond | requirement, verify | An unauthenticated preview can expose client-only copy, assets or credentials. X-Robots-Tag reduces indexing but is not access control; public synthetic demos need not carry private preview credentials. |
| HOST-10 | Diamond | Diamond | requirement, verify | Releasing an artifact different from the reviewed build is an unsafe release. Requiring a particular Git tag and SHA-256 is unnecessary if the platform supplies an immutable deployment/commit identity; a tag alone does not establish what is live. |
| HOST-11 | Gold | Silver | requirement, verify, tier | Monitoring helps detect downtime, but five-minute polling and 30-day alerts have no stated service objective and do not prove that an enquiry reaches a mailbox. HOST-03 and MAIL-06 address the direct expiry and delivery evidence. |
| HOST-12 | Diamond | Diamond | requirement, verify, class | Compromised registrar/host/repository credentials can redirect the domain or deploy malicious content; account control is a direct security and availability path. DNSSEC is valuable in some domains but is provider/key-management dependent and misconfiguration can remove the domain from service. |
| HOST-13 | Silver | Silver | requirement, verify | Spend alerts and CDN routing are useful only when the provider plan, expected media and overage consequences justify them. An alert alone does not cap cost, and “large media” lacks a measurable threshold. |
| HOST-14 | Diamond | Diamond | requirement, verify | Loss of the only approved photos, source or mutable customer records can be irreversible. Restore scope should follow the data actually held: static rebuildable sites need recoverable source/content, while any database or customer state needs a tested isolated restore and agreed recovery objectives. |
| HOST-15 | Bronze | Bronze | requirement | A Green Web Foundation result is environmental reference data, not evidence that a core journey works or that security is adequate. Bronze correctly prevents an external badge from becoming a launch gate. |
| HOST-16 | Diamond | Diamond | requirement, verify | This deployment check correctly prioritizes directive semantics and explicitly permits a generic Server header, contradicting SEC-02’s blanket ban. The remaining controls matter only on response types where they apply; requiring CSP framing on every asset is meaningless. |
| HOST-17 | Gold | Gold | requirement, verify | A tested rollback supports reliable recovery, but five minutes is a guessed threshold: deployment rollback may be instant while DNS, certificates or data migrations can take longer. Record measured recovery and compare it with a stated objective. |
| HOST-18 | Gold | Silver | requirement, verify, tier | HTTP/3, Brotli and Early Hints are delivery optimizations; requiring a hint for three named assets across browsers/hosts does not prove a better user journey. The hardcoded support/version matrix will age. |
| HOST-19 | Diamond | Diamond | requirement | Changing DNS before the new host, TLS and business-mail routes work can interrupt the site or mail and make rollback slow. Retaining actual before-values and the old service until verification is a concrete unsafe-release control. |
| HOST-20 | Silver | Silver | requirement, verify | An Observatory grade is a dated scanner result, not overall security proof; a public scan also exposes history and may be unavailable. A+ and zero failed tests can reward scanner compatibility rather than actual risk reduction. |
| HOST-21 | Silver | Silver | requirement, verify | Internet.nl is a useful optional view of internet standards, but a mandatory 100% target bundles IPv6, DNSSEC, RPKI, security.txt and mail DANE/STARTTLS even where provider control or feature need differs. The score is not a user-journey proof. |
| HOST-22 | Diamond | Diamond | requirement | Replacing a DNS zone with website-only records can silently disable the owner’s existing mail, losing business messages even when the website works. Preserve current MX and sender/authentication records and verify both directions after cutover. |
| HOST-23 | Diamond | Gold | requirement, tier | Historical URL continuity is migration quality and contractual scope; core working routes and domain/mail safety retain Diamond protection. |
| OPS-01 | Gold | Gold | requirement, verify | Continuous build/test gates improve a predictable release, but npm audit is not a substitute for dependency triage in SEC-07 and a CI job that runs without deploy protection does not block an unsafe release. |
| OPS-02 | Gold | Gold | requirement, verify | Performance regressions can make the core experience materially slower, so approved budgets belong at Gold. A median of exactly three Lighthouse runs is a sampling choice that may still be noisy; compare enough equivalent runs to distinguish a real change from measurement variance and state the sample count. |
| OPS-03 | Gold | Gold | requirement, verify | A handover runbook prevents avoidable outages, but requiring manual certificate renewal or health checks when the selected host manages them creates false procedures. Steps must match the selected stack and assigned owner. |
| OPS-04 | Diamond | Silver | requirement, verify, tier | Real-user vitals collection is optional. Correct aggregation prevents duplicate or stale callback values, but implementing a pinned library, aggregation endpoint and bfcache lifecycle is instrumentation work; privacy controls remain mandatory if it is enabled. |
| OPS-05 | Diamond | Silver | requirement, verify, tier | First-party error/CSP reporting can shorten diagnosis, but requiring a new reporting service on every site adds collection of URLs, IPs and stack data. Reporting observes failures; it does not prevent them, and privacy minimization remains required if enabled. |
| OPS-06 | Diamond | Gold | requirement, verify, tier | Automated dependency alerts and a named owner improve maintenance, but a weekly bot or seven-day target cannot justify delaying a known exploited vulnerability and a static client handoff may assign maintenance to the client. SEC-07 owns the release-time security floor. |
| OPS-07 | Gold | Gold | requirement, verify | A browser policy lets the team test the actual user population, but “last two” changes continuously and is not grounded in the client’s service promise or analytics. The build should cover a declared supported range and actual critical paths. |
| OPS-08 | Gold | Silver | requirement, verify, tier | Timed support follow-ups are later service obligations; they cannot be observed before launch and do not establish initial quality. |
| OPS-09 | Silver | Silver | requirement, verify | HTML/CSS validation catches parser and conformance errors but does not prove accessibility or a working journey. Requiring a particular npm command/preset and charset as the literal first head element is narrower than the standard. |
| OPS-10 | Diamond | Diamond | requirement, class | Analytics is optional, but once enabled it can create privacy/legal harm by collecting form values, sensitive URLs or signals without required choice. Correctly distinguishing a phone click, form acceptance and inbox delivery prevents false conversion claims. |
| LEG-01 | Gold | Silver | requirement, verify, class, tier | Self-hosting is an implementation option; data-sharing review and font rights remain Diamond. |
| LEG-02 | Diamond | Diamond | requirement, verify | Unreviewed tracking can expose personal data and needs purpose, basis and consent review. |
| LEG-03 | Diamond | Silver | requirement, verify, tier | Provenance helps review; actual rights and permissions already have dedicated Diamond gates. |
| LEG-04 | Diamond | Diamond | Retained | Children’s data requires a condition-specific legal and collection review. |
| LEG-05 | Diamond | Diamond | Retained | Marketing email rules apply only when marketing messages are sent. |
| LEG-06 | Diamond | Diamond | Retained | Subscription terms affect financial decisions and must be clear before payment. |
| LEG-07 | Bronze | Bronze | Retained | This stable ID is explicitly superseded; preserving its N/A state preserves history. |
| LEG-08 | Diamond | Diamond | Retained | Privacy review must follow data across browser, server and processors. |
| LEG-09 | Diamond | Diamond | Retained | Required consent must actually block storage and remain rejectable and revocable. |
| LEG-10 | Diamond | Diamond | Retained | GPC behavior depends on current law and data flows, so applicability must be evidenced. |
| LEG-11 | Diamond | Diamond | requirement, verify | Published privacy disclosures must match collection; a draft label cannot replace approval. |
| LEG-12 | Diamond | Diamond | Retained | Required access disclosures must be truthful and cannot waive actual barriers. |
| LEG-13 | Diamond | Diamond | requirement, verify | Entity and commerce disclosures depend on the actual service and jurisdiction. |
| LEG-14 | Diamond | Diamond | requirement, verify | Licence conditions determine permitted use, modification, attribution and distribution. |
| LEG-15 | Diamond | Diamond | Retained | Safe-harbor duties depend on user-hosted content and a deliberate legal position. |
| LEG-16 | Diamond | Diamond | Retained | Uncleared content rights can create legal exposure and block a truthful launch. |
| LEG-17 | Diamond | Diamond | Retained | A qualified review resolves applicable legal and rights questions before publication. |
| LEG-18 | Bronze | Silver | requirement, verify, class, tier | General complaint runbooks are operational improvements; actual legal requirements remain in Diamond rather than duplicating a universal US workflow. |
| SUS-01 | Silver | Silver | requirement, verify | Weight is an optimization budget; a dated population median is not a universal requirement. |
| SUS-02 | Silver | Silver | Retained | Reduced-data behavior benefits battery and bandwidth but is an optional enhancement. |
| SUS-03 | Bronze | Bronze | Retained | A carbon estimate is an optional specialized measurement, not release evidence. |
| I18N-01 | Diamond | Gold | requirement, verify, tier | Locale navigation is quality; language tagging and pronunciation remain accessibility requirements. |
| I18N-02 | Gold | Gold | requirement, verify | Real translation fit matters; fixed expansion ratios can reject valid languages and layouts. |
| I18N-03 | Diamond | Diamond | requirement, verify | Unreadable glyphs or broken RTL can make a claimed supported language unusable. |
| I18N-04 | Diamond | Diamond | requirement, verify | Wrong dates, values or currencies can materially mislead users. |
| CNT-01 | Gold | Gold | Retained | Input gaps must be reported so a template run can continue without pretending content exists. |
| CNT-02 | Diamond | Diamond | requirement, verify | Unlicensed copied material is a rights risk; exact shingle counts create false positives. |
| CNT-03 | Diamond | Gold | requirement, verify, tier | An asset manifest improves traceability; legal rights and alt text are separately gated. |
| CNT-04 | Diamond | Diamond | requirement, verify | Incomplete approvals or rights must not be represented as final indexable content. |
| CNT-05 | Diamond | Diamond | requirement, verify | Invented facts, prices or testimonials directly deceive prospective customers. |
| CNT-06 | Gold | Gold | requirement, verify | Clipped content harms readability; exact reference line parity is only fidelity evidence. |
| CNT-07 | Diamond | Bronze | requirement, verify, tier | Contrast is a Diamond accessibility outcome; this row records optional visual treatment. |
| CNT-08 | Diamond | Diamond | requirement, verify | A valid commercial licence permits a reference font; unlicensed use remains a rights blocker. |
| CNT-09 | Diamond | Diamond | Retained | Image metadata can expose personal location or identifying information. |
| CNT-10 | Diamond | Gold | requirement, verify, tier | Locale completeness matters, while incorrect language tagging is handled as accessibility. |
| CNT-11 | Diamond | Diamond | requirement, verify | Drafts and unintended placeholders must not ship as final; intentional noindex routes can be valid. |
| CNT-12 | Silver | Silver | requirement, verify | Dynamic widgets should be truthful if used, but need not exist on every site. |
| CNT-13 | Gold | Gold | requirement, verify | Animations must preserve approved content; `data-slot` is an implementation detail. |
| CNT-14 | Diamond | Diamond | requirement, verify | Unlicensed reference assets and public comparison builds create rights and release risk. |
| CNT-15 | Diamond | Diamond | requirement, verify | Asset rights depend on the actual licence, permission and use, not categorical bans. |
| CNT-16 | Gold | Bronze | requirement, verify, tier | Brand mapping is useful fidelity documentation; comparator internals are specialist process. |
| CNT-17 | Diamond | Diamond | requirement, verify, class | Visitors need to understand a destination; banning particular phrases without context overstates WCAG. |
| DEL-01 | Diamond | Gold | requirement, verify, tier | Useful operating documentation enables reliable handover; filenames do not establish safety. |
| DEL-02 | Diamond | Gold | requirement, verify, tier | Audit automation reduces delivery errors, while the evidence and actual live outcomes remain Diamond. |
| DEL-03 | Diamond | Gold | requirement, verify, tier | Drafts must stay drafts; approved legal notices and applicability are governed by LEG-11/17. |
| DEL-04 | Diamond | Gold | requirement, verify, tier | Exception logs support review, but cannot substitute for actual accessibility results. |
| DEL-05 | Diamond | Gold | requirement, verify, tier | Factual provenance aids ownership review; fixed version tags and legal conclusions are unnecessary. |
| DEL-06 | Gold | Gold | Retained | A clean offline verification makes the package reproducible without contacting the reference site. |
| DEL-07 | Gold | Gold | Retained | Transactional content sync preserves the last good client content after invalid input or failure. |
| DEL-08 | Diamond | Diamond | requirement, verify | Deploying a different unverified artifact can restore known access barriers or expose private files. |
| DEL-09 | Diamond | Gold | requirement, verify, tier | Accurate linked docs and disclosed defects improve handover; release severity belongs to the gate. |
| DEL-10 | Diamond | Diamond | requirement, verify | A tested rollback path limits harm when an in-scope deployment or DNS change fails. |
| DEL-11 | Gold | Gold | Retained | Service, ownership and renewal records make the delivered site supportable. |
| DEL-12 | Silver | Gold | requirement, verify, tier | Editing instructions are part of this offer’s handover; page count and tool are arbitrary. |
| DEL-13 | Gold | Gold | requirement, verify | The client needs accurate runtime and support guidance, tailored to the actual agreement. |
| DEL-14 | Diamond | Diamond | requirement, verify | Approval must identify the released work and pending checks; commercial payment is a separate control. |
| DEL-15 | Diamond | Diamond | requirement, verify | Evidence integrity prevents missing, stale or failed requirements from being called release-ready. |
| DEL-16 | Gold | Gold | Retained | A scoped brief and acceptance checks reduce invented facts, privacy gaps and unverified claims. |
