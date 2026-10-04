# Production priorities: Diamond, Gold, Silver, Bronze

These are agency priorities, not third-party certifications. Use this view to decide what to do next; use the linked full catalogue for the exact criterion and evidence method. All 275 IDs remain. A shorter operating view must not erase a failed check.

| Tier | Meaning | Gate |
|---|---|---|
| Diamond | Essential journeys, accessibility, security, privacy, legal duties, truthful content and safe release | Every applicable item must pass. No waiver. |
| Gold | Smooth, reliable experience, performance and delivery quality | Diamond plus Gold for Gold completion. |
| Silver | Useful enhancements, maintenance improvements and optional scope | Prioritized backlog; adds to Diamond and Gold. |
| Bronze | Specialist polish, reference comparisons and legacy bookkeeping | Retained when useful or contracted; never a weaker safety standard. |

## How to use it

Start with [the operating standard](RELEASE_STANDARD.md) for the decision in plain English. This catalogue is the traceability view, not 275 independent test sessions.

1. Inventory routes, data flows, providers, jurisdictions and contracted features. Unknown applicability is unresolved, not N/A. Privacy review includes hosting logs and processors even on a cookieless site.
2. Clear Diamond before claiming launch completeness. Review core navigation, readable mobile content, keyboard/assistive access, real form delivery, secrets, access controls, TLS, truthful claims, privacy and rights, recovery and exact deployment identity.
3. Prepare final-domain probes and rollback before controlled cutover; final-domain Diamond checks run immediately afterwards. Until then the cutover is provisional. Handover readiness is not launch approval.
4. Work through Gold next. Record optional misses with an owner, reason, next action and date. Contracted features remain delivery obligations even if their generic priority is Silver or Bronze.
5. Keep future field metrics, 7/30-day reviews and recurring checks pending until actually observed. Timing is scheduling metadata, never an exemption from Diamond.

Tier is separate from applicability and evidence status. `G` is always applicable, `C` conditional, `R` an enhancement whose absence needs evidence for N/A. `-L` requires production-domain evidence; `-O` needs named human evidence. No fake PASS, fabricated approval or downgrade to get a green dashboard. An uncovered critical defect or applicable legal duty is Diamond regardless of its row label. A lower-tier implementation preference never weakens the linked Diamond outcome. Reuse one evidence bundle across overlapping rows, but list exactly which controls and states it proves. Do not run duplicate tests merely to populate two rows.

The [release contract](../docs/RELEASE_EVIDENCE.md) explains phases and compatibility. The [current challenge audit](../docs/reviews/checklist-challenge-2026-10-05/REVIEW.md) records all decisions and their limits; [sources](../docs/reviews/checklist-tiers-2026-10-05/SOURCES.md) distinguish standards from house choices. Existing website evidence is not retroactively passed by this revision.


## Inventory

| Tier | Rows |
|---|---:|
| Diamond | 117 |
| Gold | 86 |
| Silver | 54 |
| Bronze | 18 |

## Diamond

| ID | Purpose and priority reason | When |
|---|---|---|
| [SPD-06](PRODUCTION_CHECKLIST_clone_swap.md#L44) | A shared-cache leak can expose private user data, so Diamond applies only when private or personalized responses exist; public asset caching remains a performance optimization. | prelaunch |
| [SPD-09](PRODUCTION_CHECKLIST_clone_swap.md#L47) | A blocking intro can keep users from the form or primary task when assets stall, a direct task failure; apply only when the shipped experience has an authored blocking intro. | prelaunch |
| [TYP-05](PRODUCTION_CHECKLIST_clone_swap.md#L69) | A valid document language helps assistive technology pronounce content correctly, preventing an avoidable accessibility barrier. | prelaunch |
| [TYP-06](PRODUCTION_CHECKLIST_clone_swap.md#L70) | Loss of text or controls at 200% enlargement directly excludes users who need magnification, so this is a Diamond access requirement. | prelaunch |
| [TYP-11](PRODUCTION_CHECKLIST_clone_swap.md#L75) | Insufficient text or control contrast can make core content and actions inaccessible, so the criterion-level contrast threshold belongs in Diamond. | prelaunch |
| [TYP-18](PRODUCTION_CHECKLIST_clone_swap.md#L82) | Keyboard users can be excluded when focus disappears, but the current row incorrectly imports AAA focus geometry into AA. | prelaunch |
| [TYP-21](PRODUCTION_CHECKLIST_clone_swap.md#L85) | When authored styling removes system cues, forced-colors users can lose controls or focus; test that conditional barrier. | prelaunch |
| [TYP-22](PRODUCTION_CHECKLIST_clone_swap.md#L86) | A control hidden by a cutout or browser chrome blocks the task; viewport-unit imitation has no safety value. | prelaunch |
| [RSP-01](PRODUCTION_CHECKLIST_clone_swap.md#L94) | Disabling zoom can remove a user’s magnification path, but the exact maximum-scale cutoff is not itself a WCAG criterion. | prelaunch |
| [RSP-03](PRODUCTION_CHECKLIST_clone_swap.md#L96) | WCAG 1.4.10 AA sets 320 CSS px reflow but allows content that requires two-dimensional layout; an absolute no-scroll rule would misclassify valid data. | prelaunch |
| [RSP-04](PRODUCTION_CHECKLIST_clone_swap.md#L97) | Orientation lock can exclude users in one orientation, but WCAG 1.3.4 permits it where a specific orientation is essential. | prelaunch |
| [RSP-05](PRODUCTION_CHECKLIST_clone_swap.md#L98) | WCAG 2.5.8 protects pointer users from undersized controls and expressly allows its spacing, equivalent, inline, user-agent and essential exceptions. | prelaunch |
| [RSP-07](PRODUCTION_CHECKLIST_clone_swap.md#L100) | A hover-only task can disappear for touch users; keyboard operability is separately protected by A11Y-05 and hover/focus content by A11Y-17. | prelaunch |
| [RSP-09](PRODUCTION_CHECKLIST_clone_swap.md#L102) | A half-height Playwright viewport is not an iOS keyboard and a center-point hit test can fail valid layouts; a covered focused form field can still block submission. | prelaunch |
| [A11Y-01](PRODUCTION_CHECKLIST_clone_swap.md#L109) | Axe is useful for finding candidate WCAG failures but cannot establish conformance, and a fidelity branch must not ship known accessibility barriers. | prelaunch |
| [A11Y-03](PRODUCTION_CHECKLIST_clone_swap.md#L111) | A rigid one-main/header/nav/footer structure is not a WCAG requirement; lack of a way around repeated blocks is the actual keyboard barrier. | prelaunch |
| [A11Y-04](PRODUCTION_CHECKLIST_clone_swap.md#L112) | WCAG requires meaningful structure to be programmatically determinable, not exactly one H1 or a ban on every skipped level. | prelaunch |
| [A11Y-05](PRODUCTION_CHECKLIST_clone_swap.md#L113) | Keyboard access, focus containment and return are core barriers for implemented controls, while pattern requirements should follow the actual component rather than the reference. | prelaunch |
| [A11Y-06](PRODUCTION_CHECKLIST_clone_swap.md#L114) | WCAG 2.4.11 AA fails only when author-created content entirely hides the focused component; requiring zero overlap asserts the AAA 2.4.12 outcome. | prelaunch |
| [A11Y-07](PRODUCTION_CHECKLIST_clone_swap.md#L115) | Where authored dragging is present, a click/tap alternative serves pointer users who cannot drag; keyboard access alone does not satisfy that separate need. | prelaunch |
| [A11Y-08](PRODUCTION_CHECKLIST_clone_swap.md#L116) | Missing alternatives can hide image information, while a generic role/label on canvas cannot substitute for equivalent chart or stage content. | prelaunch |
| [A11Y-09](PRODUCTION_CHECKLIST_clone_swap.md#L117) | Uncontrolled motion can harm or exclude people who request reduced motion, but this is an inclusive house behavior rather than a blanket WCAG 2.2 AA mandate. | prelaunch |
| [A11Y-10](PRODUCTION_CHECKLIST_clone_swap.md#L118) | Qualifying auto-motion needs a usable control and flashes can cause seizure harm, but WCAG 2.2.2 and 2.3.1 are separate criteria with different tests. | prelaunch |
| [A11Y-11](PRODUCTION_CHECKLIST_clone_swap.md#L119) | Forms without visible instructions, associated names or usable error feedback can block the site’s core enquiry task for assistive-technology users. | prelaunch |
| [A11Y-12](PRODUCTION_CHECKLIST_clone_swap.md#L120) | Client-side route changes can leave screen-reader users on stale context, but the title/focus/live-region triple is not a universal WCAG-mandated recipe. | prelaunch |
| [A11Y-13](PRODUCTION_CHECKLIST_clone_swap.md#L121) | A hidden native pointer with a reference-matched custom cursor can make controls difficult to locate; visual fidelity does not justify removing pointer feedback. | prelaunch |
| [A11Y-14](PRODUCTION_CHECKLIST_clone_swap.md#L122) | WCAG 1.4.2 governs automatically playing audio over three seconds, while the house no-autoplay-sound rule is a stricter protection against surprise and sensory disruption. | prelaunch |
| [A11Y-15](PRODUCTION_CHECKLIST_clone_swap.md#L123) | When a current-page or selected state conveys information visually, users of assistive technology need equivalent state information. | prelaunch |
| [A11Y-16](PRODUCTION_CHECKLIST_clone_swap.md#L124) | WCAG 1.4.12 requires content to survive user-set spacing values, so clipping or lost control labels under the override can exclude users. | prelaunch |
| [A11Y-17](PRODUCTION_CHECKLIST_clone_swap.md#L125) | Hover/focus-only content can disappear before users reach it; the reference is not an exception to WCAG 1.4.13 where that criterion applies. | prelaunch |
| [A11Y-19](PRODUCTION_CHECKLIST_clone_swap.md#L127) | Repeated help placement and redundant data entry are separately addressed by WCAG 3.2.6 and 3.3.7, both Level A; the latter has explicit essential/security/stale-data exceptions. | prelaunch |
| [A11Y-20](PRODUCTION_CHECKLIST_clone_swap.md#L128) | People unable to hear or see meaningful media need equivalent information; prerecorded captions are Level A, not AA. | prelaunch |
| [A11Y-22](PRODUCTION_CHECKLIST_clone_swap.md#L130) | An automated zero-violation scan cannot evaluate every applicable WCAG criterion or complete process, so a dated A/AA review protects against unexamined access barriers. | prelaunch |
| [SEO-02](PRODUCTION_CHECKLIST_clone_swap.md#L137) | Unapproved or draft content must not become an indexable production release. | prelaunch |
| [SEO-08](PRODUCTION_CHECKLIST_clone_swap.md#L143) | Broken required destinations or inaccessible navigation prevent the promised journey; one literal HTML attribute is not the outcome. | prelaunch |
| [SEO-11](PRODUCTION_CHECKLIST_clone_swap.md#L146) | Machine-readable claims must be truthful when published; installing schema markup is optional. | prelaunch |
| [EDGE-05](PRODUCTION_CHECKLIST_clone_swap.md#L162) | A failed decorative resource must not hide essential content or block the main task. | prelaunch |
| [EDGE-09](PRODUCTION_CHECKLIST_clone_swap.md#L166) | False form success and URL exposure create direct task and privacy harms. | prelaunch |
| [EDGE-18](PRODUCTION_CHECKLIST_clone_swap.md#L175) | Present server handlers must fail honestly and safely without exposing internals; static sites do not need an invented server endpoint. | prelaunch |
| [UXF-01](PRODUCTION_CHECKLIST_clone_swap.md#L183) | A dead primary control blocks the task; 400 ms and cursor-pointer heuristics are arbitrary. | prelaunch |
| [UXF-02](PRODUCTION_CHECKLIST_clone_swap.md#L184) | Honest pending, failure and recovery states prevent duplicate or lost submissions. | prelaunch |
| [UXF-05](PRODUCTION_CHECKLIST_clone_swap.md#L187) | Form minimization, labeling and recoverable errors protect privacy and the primary task. | prelaunch |
| [UXF-07](PRODUCTION_CHECKLIST_clone_swap.md#L189) | False claims, coercion and deceptive controls can directly manipulate user decisions. | prelaunch |
| [UXF-08](PRODUCTION_CHECKLIST_clone_swap.md#L190) | Essential text must work with assistive technology and text-based tools. | prelaunch |
| [MOT-05](PRODUCTION_CHECKLIST_clone_swap.md#L203) | Essential content must survive graphics failure; DPR and heap thresholds are optimization choices. | prelaunch |
| [SEC-03](PRODUCTION_CHECKLIST_clone_swap.md#L221) | An HTTP-to-HTTPS downgrade can expose traffic to active interception, so deployed HTTPS enforcement matters. A fixed two-year lifetime, preload and includeSubDomains create lock-in and can break subdomains; they are not a universal minimum. | cutover |
| [SEC-05](PRODUCTION_CHECKLIST_clone_swap.md#L223) | Unreviewed requests can disclose visitor IP, referrer or interaction data, and remote scripts can change after review. A literal zero-origin rule conflicts with legitimate approved providers and with CSP exceptions; approved, bounded providers are not inherently unsafe. | prelaunch |
| [SEC-06](PRODUCTION_CHECKLIST_clone_swap.md#L224) | A committed token can enable account takeover or expose client data; detection must cover the delivered artifact and repository history, and a confirmed credential must be revoked. Requiring bespoke scanner rules or scanning unreachable Git objects on every hosting workflow is tool-specific. | prelaunch |
| [SEC-07](PRODUCTION_CHECKLIST_clone_swap.md#L225) | A shipped exploitable dependency or unreviewed install hook can compromise the client site or build credentials. Severity labels alone are insufficient: the decision depends on reachability, exposure, exploitability and mitigation. SBOM/signature paperwork and broad license administration are not the same security control. | prelaunch |
| [SEC-08](PRODUCTION_CHECKLIST_clone_swap.md#L226) | Actual confidential-data disclosure is a release blocker regardless of which debugging tool exposes it. | prelaunch |
| [SEC-09](PRODUCTION_CHECKLIST_clone_swap.md#L227) | An insecure session cookie or unnecessary tracking storage can create account compromise or privacy exposure. The control must apply only to storage the site actually uses; blanket absence rules can conflict with owner-approved consent, preferences or authentication features. | prelaunch |
| [SEC-12](PRODUCTION_CHECKLIST_clone_swap.md#L230) | Unreviewed remote executable code can change independently and compromise visitors. SRI is useful for immutable cross-origin bytes when browser CORS rules permit it, but it is not applicable to every dynamic API or changing provider resource. | prelaunch |
| [SEC-13](PRODUCTION_CHECKLIST_clone_swap.md#L231) | Client-side injection remains dangerous even when a site has no backend; a Trusted Types tool mandate is unnecessary. | prelaunch |
| [SEC-15](PRODUCTION_CHECKLIST_clone_swap.md#L233) | Where CI/deployment automation exists, untrusted jobs and third-party actions must not obtain production credentials or bypass artifact review. | prelaunch |
| [BACK-00](PRODUCTION_CHECKLIST_clone_swap.md#L239) | An incomplete system/data inventory can hide applicable security and privacy duties; the format is optional. | prelaunch |
| [BACK-01](PRODUCTION_CHECKLIST_clone_swap.md#L240) | A contact form is the core enquiry journey. A successful local mail sink or a different serverless adapter does not establish that the chosen runtime sends the client’s message; missing credentials must fail visibly before launch. | prelaunch |
| [BACK-03](PRODUCTION_CHECKLIST_clone_swap.md#L242) | Client-side checks can be bypassed. Unsafe server parsing or output of submitted values can enable injection, resource abuse or disclosure; safe rejection must not leak internals. | prelaunch |
| [BACK-04](PRODUCTION_CHECKLIST_clone_swap.md#L243) | An unauthenticated endpoint can be flooded or used to incur provider charges. A hard per-IP number is not universal: users share IPs, forwarded headers can be forged, and serverless instances do not share memory. | prelaunch |
| [BACK-05](PRODUCTION_CHECKLIST_clone_swap.md#L244) | Cookie-authenticated state changes can be forged by cross-site requests. SameSite alone has sibling-domain and safe-method gaps; CAPTCHA does not establish request origin. The old rule also omits PATCH and overstates which APIs need CSRF defenses. | prelaunch |
| [BACK-06](PRODUCTION_CHECKLIST_clone_swap.md#L245) | A credentialed permissive CORS response can expose private browser-readable data, but CORS does not authenticate direct requests or stop CSRF by itself. Same-origin-only routes need no CORS grant; public resources may have a deliberate wider policy. | prelaunch |
| [BACK-07](PRODUCTION_CHECKLIST_clone_swap.md#L246) | Caching an authenticated response under a shared key can leak private user data. Conversely, frame-ancestors is a document-framing control and has little meaning on ordinary JSON responses; requiring it on every API response is not a useful universal gate. | prelaunch |
| [BACK-08](PRODUCTION_CHECKLIST_clone_swap.md#L247) | A form endpoint without its provider config cannot complete the core journey, while exiting the whole site because an optional integration is unconfigured creates unnecessary downtime. Diagnostics must not reveal credentials. | prelaunch |
| [BACK-10](PRODUCTION_CHECKLIST_clone_swap.md#L249) | Unbounded provider waits can leave a visitor uncertain; blind retries can duplicate or lose an enquiry when a timeout is ambiguous. Retry safety depends on provider idempotency and actual side effects. | prelaunch |
| [BACK-12](PRODUCTION_CHECKLIST_clone_swap.md#L251) | The anti-abuse control must not reject legitimate keyboard, autofill or assistive-technology use. A false positive blocks the only enquiry route and can exclude a disabled visitor, while a challenge needs an accessible alternative. | prelaunch |
| [BACK-13](PRODUCTION_CHECKLIST_clone_swap.md#L252) | Newline injection into Reply-To or another email header can add attacker-controlled recipients or alter routing. A fixed authenticated From address and CR/LF rejection directly prevent that header path. | prelaunch |
| [BACK-14](PRODUCTION_CHECKLIST_clone_swap.md#L253) | Storing unnecessary enquiry data or leaking it into URLs, logs or analytics creates privacy and legal exposure. A site that immediately forwards an enquiry has no application database deletion endpoint to invent; retention must cover actual processors and stores. | prelaunch |
| [BACK-17](PRODUCTION_CHECKLIST_clone_swap.md#L256) | Malformed or streamed input must not crash a public handler or consume unbounded memory; unsafe output can turn an enquiry into script/header injection. These are direct DoS and injection paths. | prelaunch |
| [BACK-18](PRODUCTION_CHECKLIST_clone_swap.md#L257) | If accounts or private tenant data exist, trusting body-supplied owner IDs permits direct object access and cross-tenant disclosure. The predicate correctly makes full authorization-matrix testing conditional. | prelaunch |
| [BACK-20](PRODUCTION_CHECKLIST_clone_swap.md#L259) | A cache key that omits identity, tenant, locale or permissions can serve one user’s private data to another. This row correctly activates only when application-data caching exists and tests logout and permission changes. | prelaunch |
| [BACK-22](PRODUCTION_CHECKLIST_clone_swap.md#L261) | Forged, replayed or out-of-order provider events can grant access or mark the wrong payment state. Signature verification over the raw body and atomic deduplication protect actual trusted webhook flows; absent webhooks are N/A. | prelaunch |
| [BACK-23](PRODUCTION_CHECKLIST_clone_swap.md#L262) | A sandbox cannot prove the real production merchant, final callback or receipt path, and payment status has financial and legal consequences. Owner authorization is necessary for any live financial action. | prelaunch |
| [MAIL-01](PRODUCTION_CHECKLIST_clone_swap.md#L268) | Authentication and mailbox delivery are separate evidence. Google’s current rule is SPF or DKIM for all senders and SPF, DKIM and DMARC for bulk senders; it recommends all three generally. Requiring aligned DMARC enforcement for every low-volume transactional sender can break legitimate mail, especially when old senders or forwarding are missed. | cutover |
| [MAIL-02](PRODUCTION_CHECKLIST_clone_swap.md#L269) | Marketing mail can create direct statutory and provider-rule violations; the row correctly limits scope to actual marketing and notes that transactional mail is treated differently. The FTC’s 10-business-day processing and 30-day availability rules are verified; Gmail one-click is conditional on bulk promotional messages. | prelaunch |
| [MAIL-06](PRODUCTION_CHECKLIST_clone_swap.md#L273) | The purpose of a contact form is a delivered enquiry. Provider acceptance and a local sink do not show that the named client mailbox receives or can reply to it; the final-domain test closes the actual journey. | cutover |
| [MAIL-07](PRODUCTION_CHECKLIST_clone_swap.md#L274) | A missing reset, verification or billing message can lock an account or conceal a financial state. The requirement is conditional on real transactional flows and correctly rejects invented flows or fake provider-acceptance evidence. | cutover |
| [HOST-01](PRODUCTION_CHECKLIST_clone_swap.md#L280) | A wrong or expired certificate breaks secure access; an HTTP path that serves content can expose users. A fixed 14-day remaining-life rule and exactly one 301 are arbitrary snapshots, while 301 versus 308 can change POST semantics. | cutover |
| [HOST-02](PRODUCTION_CHECKLIST_clone_swap.md#L281) | TLS protects credentials and content in transit. TLS 1.0/1.1 are formally deprecated; test compatibility against the actual public server rather than relying on a brittle external badssl control host or a dated Mozilla profile label. | cutover |
| [HOST-03](PRODUCTION_CHECKLIST_clone_swap.md#L282) | Certificate expiry breaks the site and undermines HTTPS. Renewal timing depends on CA and host; fixed 60-day cron or hardcoded two-thirds lifetime can become wrong as lifetimes and CA recommendations change. RFC 9773 defines dynamic ACME renewal windows. | prelaunch |
| [HOST-04](PRODUCTION_CHECKLIST_clone_swap.md#L283) | Wrong authoritative records can take the site or business email offline; a dangling owner-controlled service record can permit takeover. CAA and a universal 300–3600 second TTL are hardening/operations choices, not universal security prerequisites. | cutover |
| [HOST-08](PRODUCTION_CHECKLIST_clone_swap.md#L287) | Correct controls must reach the deployed document and function responses, but listing Cloudflare/Netlify/Vercel/nginx files, line limits and npm start is an architecture-specific implementation recipe. The response behavior, not filename, is the security gate. | cutover |
| [HOST-09](PRODUCTION_CHECKLIST_clone_swap.md#L288) | An unauthenticated preview can expose client-only copy, assets or credentials. X-Robots-Tag reduces indexing but is not access control; public synthetic demos need not carry private preview credentials. | prelaunch |
| [HOST-10](PRODUCTION_CHECKLIST_clone_swap.md#L289) | Releasing an artifact different from the reviewed build is an unsafe release. Requiring a particular Git tag and SHA-256 is unnecessary if the platform supplies an immutable deployment/commit identity; a tag alone does not establish what is live. | prelaunch |
| [HOST-12](PRODUCTION_CHECKLIST_clone_swap.md#L291) | Compromised registrar/host/repository credentials can redirect the domain or deploy malicious content; account control is a direct security and availability path. DNSSEC is valuable in some domains but is provider/key-management dependent and misconfiguration can remove the domain from service. | prelaunch |
| [HOST-14](PRODUCTION_CHECKLIST_clone_swap.md#L293) | Loss of the only approved photos, source or mutable customer records can be irreversible. Restore scope should follow the data actually held: static rebuildable sites need recoverable source/content, while any database or customer state needs a tested isolated restore and agreed recovery objectives. | prelaunch |
| [HOST-16](PRODUCTION_CHECKLIST_clone_swap.md#L295) | This deployment check correctly prioritizes directive semantics and explicitly permits a generic Server header, contradicting SEC-02’s blanket ban. The remaining controls matter only on response types where they apply; requiring CSP framing on every asset is meaningless. | cutover |
| [HOST-19](PRODUCTION_CHECKLIST_clone_swap.md#L298) | Changing DNS before the new host, TLS and business-mail routes work can interrupt the site or mail and make rollback slow. Retaining actual before-values and the old service until verification is a concrete unsafe-release control. | cutover |
| [HOST-22](PRODUCTION_CHECKLIST_clone_swap.md#L301) | Replacing a DNS zone with website-only records can silently disable the owner’s existing mail, losing business messages even when the website works. Preserve current MX and sender/authentication records and verify both directions after cutover. | cutover |
| [OPS-10](PRODUCTION_CHECKLIST_clone_swap.md#L317) | Analytics is optional, but once enabled it can create privacy/legal harm by collecting form values, sensitive URLs or signals without required choice. Correctly distinguishing a phone click, form acceptance and inbox delivery prevents false conversion claims. | prelaunch |
| [LEG-02](PRODUCTION_CHECKLIST_clone_swap.md#L326) | Unreviewed tracking can expose personal data and needs purpose, basis and consent review. | prelaunch |
| [LEG-04](PRODUCTION_CHECKLIST_clone_swap.md#L328) | Children’s data requires a condition-specific legal and collection review. | prelaunch |
| [LEG-05](PRODUCTION_CHECKLIST_clone_swap.md#L329) | Marketing email rules apply only when marketing messages are sent. | prelaunch |
| [LEG-06](PRODUCTION_CHECKLIST_clone_swap.md#L330) | Subscription terms affect financial decisions and must be clear before payment. | prelaunch |
| [LEG-08](PRODUCTION_CHECKLIST_clone_swap.md#L332) | Privacy review must follow data across browser, server and processors. | prelaunch |
| [LEG-09](PRODUCTION_CHECKLIST_clone_swap.md#L333) | Required consent must actually block storage and remain rejectable and revocable. | prelaunch |
| [LEG-10](PRODUCTION_CHECKLIST_clone_swap.md#L334) | GPC behavior depends on current law and data flows, so applicability must be evidenced. | prelaunch |
| [LEG-11](PRODUCTION_CHECKLIST_clone_swap.md#L335) | Published privacy disclosures must match collection; a draft label cannot replace approval. | prelaunch |
| [LEG-12](PRODUCTION_CHECKLIST_clone_swap.md#L336) | Required access disclosures must be truthful and cannot waive actual barriers. | prelaunch |
| [LEG-13](PRODUCTION_CHECKLIST_clone_swap.md#L337) | Entity and commerce disclosures depend on the actual service and jurisdiction. | prelaunch |
| [LEG-14](PRODUCTION_CHECKLIST_clone_swap.md#L338) | Licence conditions determine permitted use, modification, attribution and distribution. | prelaunch |
| [LEG-15](PRODUCTION_CHECKLIST_clone_swap.md#L339) | Safe-harbor duties depend on user-hosted content and a deliberate legal position. | prelaunch |
| [LEG-16](PRODUCTION_CHECKLIST_clone_swap.md#L340) | Uncleared content rights can create legal exposure and block a truthful launch. | prelaunch |
| [LEG-17](PRODUCTION_CHECKLIST_clone_swap.md#L341) | A qualified review resolves applicable legal and rights questions before publication. | prelaunch |
| [I18N-03](PRODUCTION_CHECKLIST_clone_swap.md#L354) | Unreadable glyphs or broken RTL can make a claimed supported language unusable. | prelaunch |
| [I18N-04](PRODUCTION_CHECKLIST_clone_swap.md#L355) | Wrong dates, values or currencies can materially mislead users. | prelaunch |
| [CNT-02](PRODUCTION_CHECKLIST_clone_swap.md#L362) | Unlicensed copied material is a rights risk; exact shingle counts create false positives. | prelaunch |
| [CNT-04](PRODUCTION_CHECKLIST_clone_swap.md#L364) | Incomplete approvals or rights must not be represented as final indexable content. | prelaunch |
| [CNT-05](PRODUCTION_CHECKLIST_clone_swap.md#L365) | Invented facts, prices or testimonials directly deceive prospective customers. | prelaunch |
| [CNT-08](PRODUCTION_CHECKLIST_clone_swap.md#L368) | A valid commercial licence permits a reference font; unlicensed use remains a rights blocker. | prelaunch |
| [CNT-09](PRODUCTION_CHECKLIST_clone_swap.md#L369) | Image metadata can expose personal location or identifying information. | prelaunch |
| [CNT-11](PRODUCTION_CHECKLIST_clone_swap.md#L371) | Drafts and unintended placeholders must not ship as final; intentional noindex routes can be valid. | cutover |
| [CNT-14](PRODUCTION_CHECKLIST_clone_swap.md#L374) | Unlicensed reference assets and public comparison builds create rights and release risk. | prelaunch |
| [CNT-15](PRODUCTION_CHECKLIST_clone_swap.md#L375) | Asset rights depend on the actual licence, permission and use, not categorical bans. | prelaunch |
| [CNT-17](PRODUCTION_CHECKLIST_clone_swap.md#L377) | Visitors need to understand a destination; banning particular phrases without context overstates WCAG. | prelaunch |
| [DEL-08](PRODUCTION_CHECKLIST_clone_swap.md#L390) | Deploying a different unverified artifact can restore known access barriers or expose private files. | prelaunch |
| [DEL-10](PRODUCTION_CHECKLIST_clone_swap.md#L392) | A tested rollback path limits harm when an in-scope deployment or DNS change fails. | prelaunch |
| [DEL-14](PRODUCTION_CHECKLIST_clone_swap.md#L396) | Approval must identify the released work and pending checks; commercial payment is a separate control. | cutover |
| [DEL-15](PRODUCTION_CHECKLIST_clone_swap.md#L397) | Evidence integrity prevents missing, stale or failed requirements from being called release-ready. | prelaunch |

## Gold

| ID | Purpose and priority reason | When |
|---|---|---|
| [SPD-01](PRODUCTION_CHECKLIST_clone_swap.md#L39) | Measured loading and stability targets must be met, not merely recorded; lab and field claims remain separate. | prelaunch |
| [SPD-03](PRODUCTION_CHECKLIST_clone_swap.md#L41) | The LCP asset’s discoverability and priority directly affect when users can see the main content, which fits Gold performance. | prelaunch |
| [SPD-04](PRODUCTION_CHECKLIST_clone_swap.md#L42) | Intrinsic dimensions prevent avoidable layout shifts and lazy loading avoids needless off-screen work, both measurable user-facing performance outcomes. | prelaunch |
| [SPD-05](PRODUCTION_CHECKLIST_clone_swap.md#L43) | Responsive image bytes and decoded dimensions affect mobile load time and visual quality, so the measured trade-off belongs in Gold. | prelaunch |
| [SPD-07](PRODUCTION_CHECKLIST_clone_swap.md#L45) | Compressing large text responses reduces transfer bytes, while measured savings avoid making tiny responses slower or larger. | prelaunch |
| [SPD-08](PRODUCTION_CHECKLIST_clone_swap.md#L46) | Loading unused or duplicate libraries adds bytes and execution cost, but population medians do not define a useful site-specific budget. | prelaunch |
| [SPD-11](PRODUCTION_CHECKLIST_clone_swap.md#L49) | Back/forward cache restoration reduces repeat waits and improves navigation reliability without weakening privacy-required cache policy. | prelaunch |
| [SPD-13](PRODUCTION_CHECKLIST_clone_swap.md#L51) | Gold needs falsifiable quality acceptance, with thresholds chosen before seeing results. | prelaunch |
| [SPD-14](PRODUCTION_CHECKLIST_clone_swap.md#L52) | A p95 from only 20 sequential warm requests is unstable, and a universal 50 ms local-origin target does not map to visitor experience. | prelaunch |
| [SPD-17](PRODUCTION_CHECKLIST_clone_swap.md#L55) | The 170 KB caps are arbitrary without a supported-device budget, although identifying render-critical bytes is directly useful for performance. | prelaunch |
| [SPD-18](PRODUCTION_CHECKLIST_clone_swap.md#L56) | Avoidable parser-blocking work delays rendering, but a one-stylesheet/30 KiB cap is an implementation constraint rather than a user outcome. | prelaunch |
| [SPD-20](PRODUCTION_CHECKLIST_clone_swap.md#L58) | Repeating lab measurements against the final HTTPS build catches content and deployment regressions before claiming shipped performance. | cutover |
| [TYP-02](PRODUCTION_CHECKLIST_clone_swap.md#L66) | A metric-matched fallback can prevent visible text shifts, but the 0.01 CLS cap and browser-support claim are not universal performance standards. | prelaunch |
| [TYP-03](PRODUCTION_CHECKLIST_clone_swap.md#L67) | Preloading noncritical fonts competes with the page’s main content, so only assets proven to be render-critical should be prioritized. | prelaunch |
| [TYP-10](PRODUCTION_CHECKLIST_clone_swap.md#L74) | Avoiding mobile input zoom reduces focus jumps during form completion, a measurable form-usability improvement when form controls exist. | prelaunch |
| [TYP-17](PRODUCTION_CHECKLIST_clone_swap.md#L81) | Stable scrollbar space prevents a small but measurable horizontal layout jump when a menu or modal locks scrolling. | prelaunch |
| [RSP-02](PRODUCTION_CHECKLIST_clone_swap.md#L95) | Its width list is a subset of RSP-08 and only checks rest state; keep it distinct by catching overflow introduced by interaction states. | prelaunch |
| [RSP-06](PRODUCTION_CHECKLIST_clone_swap.md#L99) | Cross-engine smoke tests catch browser-specific breaks, but three named Playwright engines do not define every site’s supported audience or prove physical-device behavior. | prelaunch |
| [RSP-08](PRODUCTION_CHECKLIST_clone_swap.md#L101) | The fixed 11-size sweep is mostly redundant viewport sampling; breakpoint edges, supported devices and extreme short/wide layouts reveal the actual failure modes. | prelaunch |
| [RSP-10](PRODUCTION_CHECKLIST_clone_swap.md#L103) | Real devices expose browser chrome, keyboard and safe-area behavior that emulation misses, but media/form subchecks apply only when those features exist. | prelaunch |
| [A11Y-18](PRODUCTION_CHECKLIST_clone_swap.md#L126) | A documented screen-reader sample improves detection, but a fixed desktop/mobile pairing is not itself WCAG conformance; A11Y-22 retains the manual A/AA release gate. | prelaunch |
| [SEO-01](PRODUCTION_CHECKLIST_clone_swap.md#L136) | Unique route metadata improves search-result identification; copy-length guidance is not a launch blocker. | prelaunch |
| [SEO-03](PRODUCTION_CHECKLIST_clone_swap.md#L138) | Correct not-found status improves routing and search quality; required destination failures remain Diamond under SEO-08 and UXF-01. | prelaunch |
| [SEO-04](PRODUCTION_CHECKLIST_clone_swap.md#L139) | Users and crawlers need readable content, but source-HTML rendering is not universally necessary. | prelaunch |
| [SEO-07](PRODUCTION_CHECKLIST_clone_swap.md#L142) | Canonical routing affects navigation and discoverability; HTTPS belongs to security controls. | cutover |
| [SEO-10](PRODUCTION_CHECKLIST_clone_swap.md#L145) | Accurate crawl directives and sitemap entries improve discovery without guaranteeing indexing. | prelaunch |
| [SEO-12](PRODUCTION_CHECKLIST_clone_swap.md#L147) | Real image elements and fallbacks improve image discovery and rendering reliability. | prelaunch |
| [SEO-13](PRODUCTION_CHECKLIST_clone_swap.md#L148) | Owner evidence prevents an indexing report from being mistaken for a guarantee. | postlaunch |
| [SEO-14](PRODUCTION_CHECKLIST_clone_swap.md#L149) | Broken external references degrade real user paths; blocked bots need contextual handling. | recurring |
| [EDGE-02](PRODUCTION_CHECKLIST_clone_swap.md#L159) | Visitors need a useful recovery path, but a well-styled 404 is not a security gate. | prelaunch |
| [EDGE-03](PRODUCTION_CHECKLIST_clone_swap.md#L160) | Clear, blame-free error text helps visitors recover without adding technical requirements. | prelaunch |
| [EDGE-04](PRODUCTION_CHECKLIST_clone_swap.md#L161) | Missing resources should fail accurately; a universal 60-second cache ceiling has no user basis. | prelaunch |
| [EDGE-06](PRODUCTION_CHECKLIST_clone_swap.md#L163) | JavaScript-disabled support is quality engineering, not a universal legal condition. | prelaunch |
| [EDGE-07](PRODUCTION_CHECKLIST_clone_swap.md#L164) | WebGL fallback is useful; MOT-05 owns the essential-task failure condition. | prelaunch |
| [EDGE-08](PRODUCTION_CHECKLIST_clone_swap.md#L165) | Unexpected failures need correction; harmless warnings do not make a site unusable. | prelaunch |
| [EDGE-10](PRODUCTION_CHECKLIST_clone_swap.md#L167) | History should remain usable when app navigation overrides browser behavior. | prelaunch |
| [EDGE-11](PRODUCTION_CHECKLIST_clone_swap.md#L168) | Text extremes can hide controls or facts, especially on narrow screens. | prelaunch |
| [EDGE-12](PRODUCTION_CHECKLIST_clone_swap.md#L169) | The banner’s usability is quality; legal consent obligations are owned by LEG-09. | prelaunch |
| [EDGE-14](PRODUCTION_CHECKLIST_clone_swap.md#L171) | State coverage finds clipped controls; contrast and accessibility must use independent criteria. | prelaunch |
| [EDGE-17](PRODUCTION_CHECKLIST_clone_swap.md#L174) | Historical-route migration matters when replacing an existing client site, not for every build. | prelaunch |
| [UXF-03](PRODUCTION_CHECKLIST_clone_swap.md#L185) | CTA placement is quality; broken destinations remain Diamond under interaction and route checks. | prelaunch |
| [UXF-04](PRODUCTION_CHECKLIST_clone_swap.md#L186) | Correct client contact details are critical elsewhere; link ergonomics belong at Gold. | prelaunch |
| [UXF-06](PRODUCTION_CHECKLIST_clone_swap.md#L188) | Touch reliability matters, while AAA 44-pixel targets exceed the applicable minimum. | prelaunch |
| [UXF-09](PRODUCTION_CHECKLIST_clone_swap.md#L191) | Clear business, service and next action improve conversion without invented audience claims. | prelaunch |
| [UXF-10](PRODUCTION_CHECKLIST_clone_swap.md#L192) | Unexpected browser recoloring can make controls hard to use; the implementation tag is optional. | prelaunch |
| [UXF-11](PRODUCTION_CHECKLIST_clone_swap.md#L193) | A reachable contact action matters; copying a poor reference path or fixed click cap does not. | prelaunch |
| [MOT-01](PRODUCTION_CHECKLIST_clone_swap.md#L199) | Visible stalls hurt interaction; reference-relative frame counts and universal thresholds are unjustified. | prelaunch |
| [MOT-06](PRODUCTION_CHECKLIST_clone_swap.md#L204) | Resize errors reduce quality but do not normally defeat the core site task. | prelaunch |
| [MOT-12](PRODUCTION_CHECKLIST_clone_swap.md#L210) | Rejected autoplay should not strand media or disrupt surrounding content. | prelaunch |
| [SEC-01](PRODUCTION_CHECKLIST_clone_swap.md#L219) | The production-mode artifact must be exercised because development servers can hide routing and header failures. Requiring npm run start, compression, cache rules and a single audit command everywhere overstates the control; selected-host behavior is the evidence. | prelaunch |
| [SEC-02](PRODUCTION_CHECKLIST_clone_swap.md#L220) | Several listed headers are useful hardening, but their absence alone is not an exploitable flaw on every site. COOP and CORP can break OAuth popups and cross-origin assets; an informative Server banner is low-value disclosure and HOST-16 already says a generic Server header is not a missing security control. | prelaunch |
| [SEC-04](PRODUCTION_CHECKLIST_clone_swap.md#L222) | CSP can limit the impact of script injection, but a self-only policy is not a universal exploit fix and can break approved fonts, embeds, payments, CAPTCHA or analytics. The actual requirement is a least-privilege policy that fits the rendered site. | prelaunch |
| [SEC-10](PRODUCTION_CHECKLIST_clone_swap.md#L228) | Ignoring generated files and documenting setup support a reliable handover, but README and .gitignore checks do not prevent a tracked secret. The proposed AI-authorship/copyright assertions are legal conclusions and can falsely disclaim rights; rights belong in LEG-14, not a boilerplate license. | prelaunch |
| [SEC-11](PRODUCTION_CHECKLIST_clone_swap.md#L229) | A repeatable verification entry point that fails on real build or journey failures improves release reliability. npm run verify, Playwright, axe and an offline audit are implementation choices, not universal foundations; accessibility is assessed in its own rows. | prelaunch |
| [BACK-02](PRODUCTION_CHECKLIST_clone_swap.md#L241) | Allowlisting methods/content types and returning clear status codes makes the endpoint predictable, but 405/415 semantics alone are not an exploitable failure. Unbounded bodies are a resource-exhaustion risk and remain Diamond controls in BACK-04 and BACK-17. | prelaunch |
| [BACK-09](PRODUCTION_CHECKLIST_clone_swap.md#L248) | Request IDs and redacted failure records make incidents diagnosable, but absent structured logs do not themselves create an exploit. Input validation, throttling and authorization must prevent attacks independently; a static site has no server log to configure. | prelaunch |
| [BACK-19](PRODUCTION_CHECKLIST_clone_swap.md#L258) | Database latency and query growth affect a real list/search journey, but budgets must use representative data and actual permissions. A production load test or a guessed p95 target would add risk without evidence. | prelaunch |
| [BACK-21](PRODUCTION_CHECKLIST_clone_swap.md#L260) | When the application opens SQL connections, pool mode and aggregate replica limits determine whether bursts exhaust a shared database. A managed data API does not imply the application’s pool was tested; no SQL feature means N/A. | prelaunch |
| [MAIL-05](PRODUCTION_CHECKLIST_clone_swap.md#L272) | Readable mail and a validated reply route support the enquiry journey, but a local SMTP sink proves only formatting. CR/LF injection is the Diamond control in BACK-13, and actual inbox delivery is MAIL-06; a fixed subject prefix or timestamp is not universally required. | prelaunch |
| [HOST-07](PRODUCTION_CHECKLIST_clone_swap.md#L286) | A real 404 helps visitors and search engines distinguish missing routes, but soft-404 behavior is not an exploitable security failure or a reason to block the core enquiry journey. Gold fits predictable navigation. | cutover |
| [HOST-17](PRODUCTION_CHECKLIST_clone_swap.md#L296) | A tested rollback supports reliable recovery, but five minutes is a guessed threshold: deployment rollback may be instant while DNS, certificates or data migrations can take longer. Record measured recovery and compare it with a stated objective. | prelaunch |
| [HOST-23](PRODUCTION_CHECKLIST_clone_swap.md#L302) | Historical URL continuity is migration quality and contractual scope; core working routes and domain/mail safety retain Diamond protection. | cutover |
| [OPS-01](PRODUCTION_CHECKLIST_clone_swap.md#L308) | Continuous build/test gates improve a predictable release, but npm audit is not a substitute for dependency triage in SEC-07 and a CI job that runs without deploy protection does not block an unsafe release. | recurring |
| [OPS-02](PRODUCTION_CHECKLIST_clone_swap.md#L309) | Performance regressions can make the core experience materially slower, so approved budgets belong at Gold. A median of exactly three Lighthouse runs is a sampling choice that may still be noisy; compare enough equivalent runs to distinguish a real change from measurement variance and state the sample count. | recurring |
| [OPS-03](PRODUCTION_CHECKLIST_clone_swap.md#L310) | A handover runbook prevents avoidable outages, but requiring manual certificate renewal or health checks when the selected host manages them creates false procedures. Steps must match the selected stack and assigned owner. | prelaunch |
| [OPS-06](PRODUCTION_CHECKLIST_clone_swap.md#L313) | Automated dependency alerts and a named owner improve maintenance, but a weekly bot or seven-day target cannot justify delaying a known exploited vulnerability and a static client handoff may assign maintenance to the client. SEC-07 owns the release-time security floor. | prelaunch |
| [OPS-07](PRODUCTION_CHECKLIST_clone_swap.md#L314) | A browser policy lets the team test the actual user population, but “last two” changes continuously and is not grounded in the client’s service promise or analytics. The build should cover a declared supported range and actual critical paths. | recurring |
| [I18N-01](PRODUCTION_CHECKLIST_clone_swap.md#L352) | Locale navigation is quality; language tagging and pronunciation remain accessibility requirements. | prelaunch |
| [I18N-02](PRODUCTION_CHECKLIST_clone_swap.md#L353) | Real translation fit matters; fixed expansion ratios can reject valid languages and layouts. | prelaunch |
| [CNT-01](PRODUCTION_CHECKLIST_clone_swap.md#L361) | Input gaps must be reported so a template run can continue without pretending content exists. | prelaunch |
| [CNT-03](PRODUCTION_CHECKLIST_clone_swap.md#L363) | An asset manifest improves traceability; legal rights and alt text are separately gated. | prelaunch |
| [CNT-06](PRODUCTION_CHECKLIST_clone_swap.md#L366) | Clipped content harms readability; exact reference line parity is only fidelity evidence. | prelaunch |
| [CNT-10](PRODUCTION_CHECKLIST_clone_swap.md#L370) | Locale completeness matters, while incorrect language tagging is handled as accessibility. | prelaunch |
| [CNT-13](PRODUCTION_CHECKLIST_clone_swap.md#L373) | Animations must preserve approved content; `data-slot` is an implementation detail. | prelaunch |
| [DEL-01](PRODUCTION_CHECKLIST_clone_swap.md#L383) | Useful operating documentation enables reliable handover; filenames do not establish safety. | prelaunch |
| [DEL-02](PRODUCTION_CHECKLIST_clone_swap.md#L384) | Audit automation reduces delivery errors, while the evidence and actual live outcomes remain Diamond. | prelaunch |
| [DEL-03](PRODUCTION_CHECKLIST_clone_swap.md#L385) | Drafts must stay drafts; approved legal notices and applicability are governed by LEG-11/17. | prelaunch |
| [DEL-04](PRODUCTION_CHECKLIST_clone_swap.md#L386) | Exception logs support review, but cannot substitute for actual accessibility results. | prelaunch |
| [DEL-05](PRODUCTION_CHECKLIST_clone_swap.md#L387) | Factual provenance aids ownership review; fixed version tags and legal conclusions are unnecessary. | prelaunch |
| [DEL-06](PRODUCTION_CHECKLIST_clone_swap.md#L388) | A clean offline verification makes the package reproducible without contacting the reference site. | prelaunch |
| [DEL-07](PRODUCTION_CHECKLIST_clone_swap.md#L389) | Transactional content sync preserves the last good client content after invalid input or failure. | prelaunch |
| [DEL-09](PRODUCTION_CHECKLIST_clone_swap.md#L391) | Accurate linked docs and disclosed defects improve handover; release severity belongs to the gate. | prelaunch |
| [DEL-11](PRODUCTION_CHECKLIST_clone_swap.md#L393) | Service, ownership and renewal records make the delivered site supportable. | prelaunch |
| [DEL-12](PRODUCTION_CHECKLIST_clone_swap.md#L394) | Editing instructions are part of this offer’s handover; page count and tool are arbitrary. | prelaunch |
| [DEL-13](PRODUCTION_CHECKLIST_clone_swap.md#L395) | The client needs accurate runtime and support guidance, tailored to the actual agreement. | recurring |
| [DEL-16](PRODUCTION_CHECKLIST_clone_swap.md#L398) | A scoped brief and acceptance checks reduce invented facts, privacy gaps and unverified claims. | prelaunch |

## Silver

| ID | Purpose and priority reason | When |
|---|---|---|
| [SPD-10](PRODUCTION_CHECKLIST_clone_swap.md#L48) | A poster and deferred video fetch reduce unnecessary bytes, which is a useful optional optimization rather than a release safety gate. | prelaunch |
| [SPD-12](PRODUCTION_CHECKLIST_clone_swap.md#L50) | Speculation Rules are optional and must not trigger side-effect or private requests; ordinary navigation remains the supported fallback. | prelaunch |
| [SPD-15](PRODUCTION_CHECKLIST_clone_swap.md#L53) | Auditor-location TTFB and a fixed RTT formula are diagnostic signals, not stable user outcomes; SPD-20 and SPD-21 retain deployment and field performance evidence. | cutover |
| [SPD-16](PRODUCTION_CHECKLIST_clone_swap.md#L54) | Fourteen KiB is a house transfer cap rather than a standard user threshold; SPD-17 protects the measured critical path. | prelaunch |
| [SPD-21](PRODUCTION_CHECKLIST_clone_swap.md#L59) | Low-traffic sites may never reach an eligible field sample, so unavailable data cannot safely block release; SPD-01/13 retain lab checks and no field-pass claim is allowed. | postlaunch |
| [TYP-01](PRODUCTION_CHECKLIST_clone_swap.md#L65) | Self-hosting and WOFF2 subsetting are implementation optimizations; declared language coverage and visible fallback matter, while no remote/self-host rule is needed for comprehension. | prelaunch |
| [TYP-04](PRODUCTION_CHECKLIST_clone_swap.md#L68) | Synthetic weight or italics can be visually imperfect but do not by themselves block content; TYP-23 readability and TYP-11 contrast protect legibility. | prelaunch |
| [TYP-08](PRODUCTION_CHECKLIST_clone_swap.md#L72) | Tabular numerals prevent animated counters and aligned prices from shifting as digits change, a localized polish improvement. | prelaunch |
| [TYP-09](PRODUCTION_CHECKLIST_clone_swap.md#L73) | Forcing text-size-adjust to 100% can suppress helpful browser text inflation; TYP-06 protects user enlargement, so this remains optional tuning. | prelaunch |
| [TYP-12](PRODUCTION_CHECKLIST_clone_swap.md#L76) | Theme-color and overscroll flash are cosmetic polish; contrast and content access remain protected by TYP-11 and RSP-03. | prelaunch |
| [TYP-13](PRODUCTION_CHECKLIST_clone_swap.md#L77) | A colored placeholder reduces a visual flash, while SPD-04 already prevents image-driven layout shifts that affect task stability. | prelaunch |
| [TYP-14](PRODUCTION_CHECKLIST_clone_swap.md#L78) | Avoiding visible gradient banding and ineffective fixed backgrounds improves visual finish but does not block the main task. | prelaunch |
| [TYP-15](PRODUCTION_CHECKLIST_clone_swap.md#L79) | A vendor prefix and visual fallback are optional implementation details; TYP-11 ensures readability if the blur effect is unavailable. | prelaunch |
| [TYP-16](PRODUCTION_CHECKLIST_clone_swap.md#L80) | On-brand selection, caret and accent colors are a low-cost polish improvement; default UI contrast remains governed by TYP-11. | prelaunch |
| [TYP-19](PRODUCTION_CHECKLIST_clone_swap.md#L83) | CSS media-query gating is implementation detail; RSP-07 keeps hover-only functionality available to touch and keyboard users. | prelaunch |
| [TYP-20](PRODUCTION_CHECKLIST_clone_swap.md#L84) | A print stylesheet is optional convenience for visitors who print the page, not a core web task or accessibility release gate. | prelaunch |
| [TYP-23](PRODUCTION_CHECKLIST_clone_swap.md#L87) | The row mixes useful readability guidance with AAA and house heuristics; only the spacing override is an AA criterion, covered by A11Y-16. | prelaunch |
| [TYP-24](PRODUCTION_CHECKLIST_clone_swap.md#L88) | The 2-family/4-file/100 KB caps are arbitrary and overlap SPD-17; measured critical-path performance is the stronger Gold protection. | prelaunch |
| [A11Y-21](PRODUCTION_CHECKLIST_clone_swap.md#L129) | A contrast-preference enhancement is optional polish; default contrast failures remain Diamond under TYP-11 and cannot be waived by an alternate build. | prelaunch |
| [SEO-05](PRODUCTION_CHECKLIST_clone_swap.md#L140) | Share cards improve previews; image dimensions and payload are optimization details. | prelaunch |
| [SEO-06](PRODUCTION_CHECKLIST_clone_swap.md#L141) | Favicons improve recognition but do not determine whether the site works. | prelaunch |
| [SEO-09](PRODUCTION_CHECKLIST_clone_swap.md#L144) | A security contact file is useful when the client supplies a responsible contact. | prelaunch |
| [SEO-15](PRODUCTION_CHECKLIST_clone_swap.md#L150) | Search research is optional scope, not a universal launch task. | prelaunch |
| [EDGE-13](PRODUCTION_CHECKLIST_clone_swap.md#L170) | Offline support is optional unless promised; stale cached content can mislead. | prelaunch |
| [EDGE-15](PRODUCTION_CHECKLIST_clone_swap.md#L172) | A fixed 14 KB and 1-second target is an unsupported budget for every 404. | prelaunch |
| [EDGE-16](PRODUCTION_CHECKLIST_clone_swap.md#L173) | Path suggestions are optional convenience and must remain safely text-escaped. | prelaunch |
| [MOT-02](PRODUCTION_CHECKLIST_clone_swap.md#L200) | Animation property choices should follow measured cost, not a blanket CSS prescription. | prelaunch |
| [MOT-03](PRODUCTION_CHECKLIST_clone_swap.md#L201) | ScrollTrigger cleanup matters when used; the exact API is an implementation choice. | prelaunch |
| [MOT-08](PRODUCTION_CHECKLIST_clone_swap.md#L206) | Cursor effects are optional; reduced-motion access remains a separate required outcome. | prelaunch |
| [MOT-13](PRODUCTION_CHECKLIST_clone_swap.md#L211) | GPU leak monitoring is optional diagnosis; user-visible context failure is handled by MOT-05. | prelaunch |
| [MOT-14](PRODUCTION_CHECKLIST_clone_swap.md#L212) | Passive listeners are a tuning choice unless they visibly block normal scrolling. | prelaunch |
| [MOT-15](PRODUCTION_CHECKLIST_clone_swap.md#L213) | Long-task observation is useful tuning, but a non-baseline browser API is not a launch gate. | prelaunch |
| [SEC-14](PRODUCTION_CHECKLIST_clone_swap.md#L232) | COOP/COEP can isolate browsing contexts and enable specific APIs, but blanket use can break OAuth popups, downloads and embeds. The row correctly makes adoption conditional on a real need and compatibility test. | prelaunch |
| [BACK-11](PRODUCTION_CHECKLIST_clone_swap.md#L250) | A minimal health endpoint can help a chosen host monitor, but it is optional infrastructure and a universal route can expose unnecessary service detail. Serverless monitoring may use provider-native checks. | prelaunch |
| [BACK-15](PRODUCTION_CHECKLIST_clone_swap.md#L254) | A shared atomic idempotency store across all contact handlers is an architecture tax and can suppress two legitimate identical enquiries. Exactly-once email delivery is unavailable without provider support. Duplicate charge/order side effects remain Diamond in BACK-22/23. | prelaunch |
| [MAIL-03](PRODUCTION_CHECKLIST_clone_swap.md#L270) | Separate identities/streams may reduce operational coupling, but provider reputation isolation is not guaranteed and there is no marketing stream on a transactional-only site. Keeping the monitored Reply-To and N/A predicate avoids overclaiming. | prelaunch |
| [MAIL-04](PRODUCTION_CHECKLIST_clone_swap.md#L271) | MTA-STS is a receiving-domain transport policy, not a requirement for every site’s outgoing form notification. RFC 8461 testing mode reports policy failures while allowing normal delivery; enforcement misconfiguration can delay mail. | cutover |
| [HOST-05](PRODUCTION_CHECKLIST_clone_swap.md#L284) | HTTP/2 or HTTP/3 can improve transport efficiency, but absence does not block a site journey and actual support depends on the selected host/client. This is correctly an optional delivery optimization. | cutover |
| [HOST-06](PRODUCTION_CHECKLIST_clone_swap.md#L285) | A cache hit on hashed static files can reduce latency and origin load, but CDN placement and provider cache headers differ. The row is optional optimization rather than core safety. | cutover |
| [HOST-11](PRODUCTION_CHECKLIST_clone_swap.md#L290) | Monitoring helps detect downtime, but five-minute polling and 30-day alerts have no stated service objective and do not prove that an enquiry reaches a mailbox. HOST-03 and MAIL-06 address the direct expiry and delivery evidence. | recurring |
| [HOST-13](PRODUCTION_CHECKLIST_clone_swap.md#L292) | Spend alerts and CDN routing are useful only when the provider plan, expected media and overage consequences justify them. An alert alone does not cap cost, and “large media” lacks a measurable threshold. | prelaunch |
| [HOST-18](PRODUCTION_CHECKLIST_clone_swap.md#L297) | HTTP/3, Brotli and Early Hints are delivery optimizations; requiring a hint for three named assets across browsers/hosts does not prove a better user journey. The hardcoded support/version matrix will age. | cutover |
| [HOST-20](PRODUCTION_CHECKLIST_clone_swap.md#L299) | An Observatory grade is a dated scanner result, not overall security proof; a public scan also exposes history and may be unavailable. A+ and zero failed tests can reward scanner compatibility rather than actual risk reduction. | cutover |
| [HOST-21](PRODUCTION_CHECKLIST_clone_swap.md#L300) | Internet.nl is a useful optional view of internet standards, but a mandatory 100% target bundles IPv6, DNSSEC, RPKI, security.txt and mail DANE/STARTTLS even where provider control or feature need differs. The score is not a user-journey proof. | cutover |
| [OPS-04](PRODUCTION_CHECKLIST_clone_swap.md#L311) | Real-user vitals collection is optional. Correct aggregation prevents duplicate or stale callback values, but implementing a pinned library, aggregation endpoint and bfcache lifecycle is instrumentation work; privacy controls remain mandatory if it is enabled. | prelaunch |
| [OPS-05](PRODUCTION_CHECKLIST_clone_swap.md#L312) | First-party error/CSP reporting can shorten diagnosis, but requiring a new reporting service on every site adds collection of URLs, IPs and stack data. Reporting observes failures; it does not prevent them, and privacy minimization remains required if enabled. | prelaunch |
| [OPS-08](PRODUCTION_CHECKLIST_clone_swap.md#L315) | Timed support follow-ups are later service obligations; they cannot be observed before launch and do not establish initial quality. | postlaunch |
| [OPS-09](PRODUCTION_CHECKLIST_clone_swap.md#L316) | HTML/CSS validation catches parser and conformance errors but does not prove accessibility or a working journey. Requiring a particular npm command/preset and charset as the literal first head element is narrower than the standard. | prelaunch |
| [LEG-01](PRODUCTION_CHECKLIST_clone_swap.md#L325) | Self-hosting is an implementation option; data-sharing review and font rights remain Diamond. | prelaunch |
| [LEG-03](PRODUCTION_CHECKLIST_clone_swap.md#L327) | Provenance helps review; actual rights and permissions already have dedicated Diamond gates. | prelaunch |
| [LEG-18](PRODUCTION_CHECKLIST_clone_swap.md#L342) | General complaint runbooks are operational improvements; actual legal requirements remain in Diamond rather than duplicating a universal US workflow. | prelaunch |
| [SUS-01](PRODUCTION_CHECKLIST_clone_swap.md#L349) | Weight is an optimization budget; a dated population median is not a universal requirement. | prelaunch |
| [SUS-02](PRODUCTION_CHECKLIST_clone_swap.md#L350) | Reduced-data behavior benefits battery and bandwidth but is an optional enhancement. | prelaunch |
| [CNT-12](PRODUCTION_CHECKLIST_clone_swap.md#L372) | Dynamic widgets should be truthful if used, but need not exist on every site. | prelaunch |

## Bronze

| ID | Purpose and priority reason | When |
|---|---|---|
| [SPD-02](PRODUCTION_CHECKLIST_clone_swap.md#L40) | This is a reference-relative benchmark, so its score is fidelity bookkeeping; SPD-01 and SPD-13 protect actual shipped performance. | cutover |
| [SPD-19](PRODUCTION_CHECKLIST_clone_swap.md#L57) | Requiring precompressed .br/.gz siblings and maximum compression levels is build-system bookkeeping; SPD-07 protects delivered bytes and negotiated compression behavior. | prelaunch |
| [TYP-07](PRODUCTION_CHECKLIST_clone_swap.md#L71) | Balancing and pretty wrapping are reference-dependent visual choices; TYP-23 protects readable body text and RSP-03 protects reflow. | prelaunch |
| [A11Y-02](PRODUCTION_CHECKLIST_clone_swap.md#L110) | Population-frequency percentages do not identify harm on this site, and the six scan categories overlap A11Y-01, A11Y-08, A11Y-11, TYP-05 and TYP-11. | prelaunch |
| [SEO-16](PRODUCTION_CHECKLIST_clone_swap.md#L151) | Distribution needs owner approval and eligibility evidence; it is not build readiness. | prelaunch |
| [SEO-17](PRODUCTION_CHECKLIST_clone_swap.md#L152) | Crawler controls are optional discovery policy and never authenticate private content. | prelaunch |
| [EDGE-01](PRODUCTION_CHECKLIST_clone_swap.md#L158) | A captured baseline helps reproduce the reference’s error-page treatment. | prelaunch |
| [MOT-04](PRODUCTION_CHECKLIST_clone_swap.md#L202) | Lenis wiring is conditional specialist fidelity work, not a general user requirement. | prelaunch |
| [MOT-07](PRODUCTION_CHECKLIST_clone_swap.md#L205) | Transition effects are reference details; focus and navigation outcomes are covered elsewhere. | prelaunch |
| [MOT-09](PRODUCTION_CHECKLIST_clone_swap.md#L207) | Scrubbed-video encoding is a specialized reference-matching technique. | prelaunch |
| [MOT-10](PRODUCTION_CHECKLIST_clone_swap.md#L208) | A ready signal makes capture tests reliable but does not affect visitors. | prelaunch |
| [MOT-11](PRODUCTION_CHECKLIST_clone_swap.md#L209) | Frame-rate review is specialist fidelity evidence, not a reason to copy frame-dependent bugs. | prelaunch |
| [BACK-16](PRODUCTION_CHECKLIST_clone_swap.md#L255) | The row is specialist supply-chain hygiene and is already Bronze; its meaningful lockfile/install-script risks are covered at Diamond by SEC-07/SEC-12. npm audit signatures is explicitly conditional on package-manager support, so it should not be a universal security claim. | prelaunch |
| [HOST-15](PRODUCTION_CHECKLIST_clone_swap.md#L294) | A Green Web Foundation result is environmental reference data, not evidence that a core journey works or that security is adequate. Bronze correctly prevents an external badge from becoming a launch gate. | cutover |
| [LEG-07](PRODUCTION_CHECKLIST_clone_swap.md#L331) | This stable ID is explicitly superseded; preserving its N/A state preserves history. | prelaunch |
| [SUS-03](PRODUCTION_CHECKLIST_clone_swap.md#L351) | A carbon estimate is an optional specialized measurement, not release evidence. | prelaunch |
| [CNT-07](PRODUCTION_CHECKLIST_clone_swap.md#L367) | Contrast is a Diamond accessibility outcome; this row records optional visual treatment. | prelaunch |
| [CNT-16](PRODUCTION_CHECKLIST_clone_swap.md#L376) | Brand mapping is useful fidelity documentation; comparator internals are specialist process. | prelaunch |
