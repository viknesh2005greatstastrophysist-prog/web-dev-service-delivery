# Production priorities: Diamond, Gold, Silver, Bronze

These are agency priorities, not third-party certifications. Use this view to decide what to do next; use the linked full catalogue for the exact criterion and evidence method. All 275 IDs remain. A shorter operating view must not erase a failed check.

| Tier | Meaning | Gate |
|---|---|---|
| Diamond | Essential journeys, accessibility, security, privacy, legal duties, truthful content and safe release | Every applicable item must pass. No waiver. |
| Gold | Smooth, reliable experience, performance and delivery quality | Diamond plus Gold for Gold completion. |
| Silver | Useful enhancements, maintenance improvements and optional scope | Prioritized backlog; adds to Diamond and Gold. |
| Bronze | Specialist polish, reference comparisons and legacy bookkeeping | Retained when useful or contracted; never a weaker safety standard. |

## How to use it

1. Inventory routes, data flows, providers, jurisdictions and contracted features. Unknown applicability is unresolved, not N/A. Privacy review includes hosting logs and processors even on a cookieless site.
2. Clear Diamond before claiming launch completeness. Review core navigation, readable mobile content, keyboard/assistive access, real form delivery, secrets, access controls, TLS, truthful claims, privacy and rights, recovery and exact deployment identity.
3. Prepare final-domain probes and rollback before controlled cutover; final-domain Diamond checks run immediately afterwards. Until then the cutover is provisional. Handover readiness is not launch approval.
4. Work through Gold next. Record optional misses with an owner, reason, next action and date. Contracted features remain delivery obligations even if their generic priority is Silver or Bronze.
5. Keep future field metrics, 7/30-day reviews and recurring checks pending until actually observed. Timing is scheduling metadata, never an exemption from Diamond.

Tier is separate from applicability and evidence status. `G` is always applicable, `C` conditional, `R` an enhancement whose absence needs evidence for N/A. `-L` requires production-domain evidence; `-O` needs named human evidence. No fake PASS, fabricated approval or downgrade to get a green dashboard. An uncovered critical defect or applicable legal duty is Diamond regardless of its row label. Split mixed requirements before any later demotion; their highest-risk clause controls today.

The [release contract](../docs/RELEASE_EVIDENCE.md) explains phases and compatibility. The [row review](../docs/reviews/checklist-tiers-2026-10-05/ROW_REVIEW.md) records mixed requirements and review limits; [sources](../docs/reviews/checklist-tiers-2026-10-05/SOURCES.md) distinguish standards from house choices. Existing website evidence is not retroactively passed by this revision.


## Inventory

| Tier | Rows |
|---|---:|
| Diamond | 150 |
| Gold | 79 |
| Silver | 31 |
| Bronze | 15 |

## Diamond

| ID | Purpose and priority reason | When |
|---|---|---|
| [SPD-06](PRODUCTION_CHECKLIST_clone_swap.md#L34) | Private and mutable responses must not leak through shared caches. | prelaunch |
| [TYP-05](PRODUCTION_CHECKLIST_clone_swap.md#L59) | A valid document language is needed for assistive technology. | prelaunch |
| [TYP-06](PRODUCTION_CHECKLIST_clone_swap.md#L60) | Text must remain usable at 200 percent enlargement. | prelaunch |
| [TYP-11](PRODUCTION_CHECKLIST_clone_swap.md#L65) | WCAG text and interface contrast protects readable content. | prelaunch |
| [TYP-18](PRODUCTION_CHECKLIST_clone_swap.md#L72) | Visible focus indicators preserve keyboard operation. | prelaunch |
| [RSP-01](PRODUCTION_CHECKLIST_clone_swap.md#L84) | Zoom must remain available and layout must target the device width. | prelaunch |
| [RSP-03](PRODUCTION_CHECKLIST_clone_swap.md#L86) | WCAG reflow requires core content without two-dimensional scrolling. | prelaunch |
| [RSP-04](PRODUCTION_CHECKLIST_clone_swap.md#L87) | Orientation changes must not remove access to content or function. | prelaunch |
| [RSP-05](PRODUCTION_CHECKLIST_clone_swap.md#L88) | WCAG AA target sizing prevents inaccessible controls. | prelaunch |
| [RSP-07](PRODUCTION_CHECKLIST_clone_swap.md#L90) | Every action needs a keyboard and touch path. | prelaunch |
| [RSP-09](PRODUCTION_CHECKLIST_clone_swap.md#L92) | A focused form field must remain visible during entry. | prelaunch |
| [A11Y-01](PRODUCTION_CHECKLIST_clone_swap.md#L99) | Automated WCAG A and AA findings must be resolved. | prelaunch |
| [A11Y-03](PRODUCTION_CHECKLIST_clone_swap.md#L101) | Landmarks and skip navigation make the site operable. | prelaunch |
| [A11Y-04](PRODUCTION_CHECKLIST_clone_swap.md#L102) | A coherent heading outline makes content navigable. | prelaunch |
| [A11Y-05](PRODUCTION_CHECKLIST_clone_swap.md#L103) | Keyboard-operable menus and dialogs protect complete journeys. | prelaunch |
| [A11Y-06](PRODUCTION_CHECKLIST_clone_swap.md#L104) | Focused controls must not disappear behind sticky content. | prelaunch |
| [A11Y-07](PRODUCTION_CHECKLIST_clone_swap.md#L105) | Dragging interactions need a single-pointer alternative. | prelaunch |
| [A11Y-08](PRODUCTION_CHECKLIST_clone_swap.md#L106) | Meaningful visual and canvas content needs an accessible equivalent. | prelaunch |
| [A11Y-09](PRODUCTION_CHECKLIST_clone_swap.md#L107) | Reduced-motion settings must not hide content or controls. | prelaunch |
| [A11Y-10](PRODUCTION_CHECKLIST_clone_swap.md#L108) | Required pause controls and flash limits prevent motion harm. | prelaunch |
| [A11Y-11](PRODUCTION_CHECKLIST_clone_swap.md#L109) | Visible labels and recoverable errors are required for usable forms. | prelaunch |
| [A11Y-12](PRODUCTION_CHECKLIST_clone_swap.md#L110) | Route changes must communicate navigation and focus to users. | prelaunch |
| [A11Y-13](PRODUCTION_CHECKLIST_clone_swap.md#L111) | A hidden native cursor needs an accessible visible replacement. | prelaunch |
| [A11Y-14](PRODUCTION_CHECKLIST_clone_swap.md#L112) | Audio must not surprise users before activation. | prelaunch |
| [A11Y-15](PRODUCTION_CHECKLIST_clone_swap.md#L113) | Current location must be identifiable in navigation. | prelaunch |
| [A11Y-16](PRODUCTION_CHECKLIST_clone_swap.md#L114) | WCAG text-spacing overrides must not erase content or labels. | prelaunch |
| [A11Y-17](PRODUCTION_CHECKLIST_clone_swap.md#L115) | Hover content must remain dismissible and reachable. | prelaunch |
| [A11Y-18](PRODUCTION_CHECKLIST_clone_swap.md#L116) | Real desktop and mobile assistive-technology review verifies essential access beyond automated checks. | prelaunch |
| [A11Y-19](PRODUCTION_CHECKLIST_clone_swap.md#L117) | Consistent help and no re-entry support complete form processes. | prelaunch |
| [A11Y-20](PRODUCTION_CHECKLIST_clone_swap.md#L118) | Meaningful media needs applicable captions and alternatives. | prelaunch |
| [A11Y-22](PRODUCTION_CHECKLIST_clone_swap.md#L120) | A complete A/AA review covers manual criteria and processes. | prelaunch |
| [SEO-02](PRODUCTION_CHECKLIST_clone_swap.md#L127) | Unapproved or incomplete content must not be indexed as production. | prelaunch |
| [SEO-03](PRODUCTION_CHECKLIST_clone_swap.md#L128) | A missing route must truthfully return an HTTP 404. | prelaunch |
| [SEO-04](PRODUCTION_CHECKLIST_clone_swap.md#L129) | Primary information must remain available without client-side JavaScript. | prelaunch |
| [SEO-07](PRODUCTION_CHECKLIST_clone_swap.md#L132) | Canonical HTTPS URLs prevent insecure and ambiguous destinations. | cutover |
| [SEO-08](PRODUCTION_CHECKLIST_clone_swap.md#L133) | Real internal links protect navigation and contact routes. | prelaunch |
| [SEO-11](PRODUCTION_CHECKLIST_clone_swap.md#L136) | Structured data must not invent or misstate client facts. | prelaunch |
| [EDGE-02](PRODUCTION_CHECKLIST_clone_swap.md#L149) | A real, understandable 404 gives visitors a safe recovery path. | prelaunch |
| [EDGE-04](PRODUCTION_CHECKLIST_clone_swap.md#L151) | Missing assets and APIs must not masquerade as successful pages. | prelaunch |
| [EDGE-05](PRODUCTION_CHECKLIST_clone_swap.md#L152) | A failed visual asset must not blank essential content. | prelaunch |
| [EDGE-06](PRODUCTION_CHECKLIST_clone_swap.md#L153) | Navigation and copy must remain available without JavaScript. | prelaunch |
| [EDGE-07](PRODUCTION_CHECKLIST_clone_swap.md#L154) | A WebGL failure must preserve readable content and primary actions. | prelaunch |
| [EDGE-09](PRODUCTION_CHECKLIST_clone_swap.md#L156) | Forms must avoid leaking data or claiming false success. | prelaunch |
| [EDGE-12](PRODUCTION_CHECKLIST_clone_swap.md#L159) | Applicable consent must precede non-essential storage. | prelaunch |
| [EDGE-14](PRODUCTION_CHECKLIST_clone_swap.md#L161) | Visible states must retain contrast, overlay function, and dismissal. | prelaunch |
| [EDGE-17](PRODUCTION_CHECKLIST_clone_swap.md#L164) | URL migration must preserve relevant destinations and honest 404s. | prelaunch |
| [EDGE-18](PRODUCTION_CHECKLIST_clone_swap.md#L165) | Server failures need truthful recovery without exposing internals. | prelaunch |
| [UXF-01](PRODUCTION_CHECKLIST_clone_swap.md#L173) | Every apparent control must complete an approved visitor action. | prelaunch |
| [UXF-02](PRODUCTION_CHECKLIST_clone_swap.md#L174) | Form status must be honest and recoverable; exact timings are house targets. | prelaunch |
| [UXF-03](PRODUCTION_CHECKLIST_clone_swap.md#L175) | Primary actions need real destinations and must not be placeholders. | prelaunch |
| [UXF-04](PRODUCTION_CHECKLIST_clone_swap.md#L176) | Displayed phone and email contact paths must actually work. | prelaunch |
| [UXF-05](PRODUCTION_CHECKLIST_clone_swap.md#L177) | Forms must preserve input, explain errors, and report delivery honestly. | prelaunch |
| [UXF-07](PRODUCTION_CHECKLIST_clone_swap.md#L179) | Consent and conversion patterns must not deceive or pressure visitors. | prelaunch |
| [UXF-08](PRODUCTION_CHECKLIST_clone_swap.md#L180) | Essential text must remain real, selectable, accessible content. | prelaunch |
| [MOT-05](PRODUCTION_CHECKLIST_clone_swap.md#L193) | GPU failure must not remove content or primary actions. | prelaunch |
| [MOT-06](PRODUCTION_CHECKLIST_clone_swap.md#L194) | Resizing must not leave stale or broken layouts. | prelaunch |
| [SEC-01](PRODUCTION_CHECKLIST_clone_swap.md#L209) | The audited production build must serve the real security and error configuration. | prelaunch |
| [SEC-02](PRODUCTION_CHECKLIST_clone_swap.md#L210) | Response handling must prevent sniffing, leakage, and unsafe embedding. | prelaunch |
| [SEC-03](PRODUCTION_CHECKLIST_clone_swap.md#L211) | Live HSTS protects transport; subdomain and preload choices need owner review. | cutover |
| [SEC-04](PRODUCTION_CHECKLIST_clone_swap.md#L212) | An enforced, integration-aware CSP reduces script injection risk. | prelaunch |
| [SEC-05](PRODUCTION_CHECKLIST_clone_swap.md#L213) | Unreviewed third-party requests create privacy and supply-chain exposure. | prelaunch |
| [SEC-06](PRODUCTION_CHECKLIST_clone_swap.md#L214) | Secrets in history or outputs require removal and rotation. | prelaunch |
| [SEC-07](PRODUCTION_CHECKLIST_clone_swap.md#L215) | Dependency provenance and exploitable vulnerabilities affect release safety. | prelaunch |
| [SEC-09](PRODUCTION_CHECKLIST_clone_swap.md#L217) | Storage and authentication cookies must protect user data. | prelaunch |
| [SEC-10](PRODUCTION_CHECKLIST_clone_swap.md#L218) | Private inputs and third-party rights must be protected in the handover. | prelaunch |
| [SEC-12](PRODUCTION_CHECKLIST_clone_swap.md#L220) | External scripts need integrity checks when included. | prelaunch |
| [SEC-15](PRODUCTION_CHECKLIST_clone_swap.md#L223) | CI and deployment credentials must not permit unsafe unreviewed releases. | prelaunch |
| [BACK-00](PRODUCTION_CHECKLIST_clone_swap.md#L229) | An accurate endpoint inventory defines the real security boundary. | prelaunch |
| [BACK-01](PRODUCTION_CHECKLIST_clone_swap.md#L230) | A contact submission must reach its configured recipient before launch. | prelaunch |
| [BACK-02](PRODUCTION_CHECKLIST_clone_swap.md#L231) | Request method, media type, and size limits constrain abuse. | prelaunch |
| [BACK-03](PRODUCTION_CHECKLIST_clone_swap.md#L232) | Server-side validation and generic failures prevent injection and leakage. | prelaunch |
| [BACK-04](PRODUCTION_CHECKLIST_clone_swap.md#L233) | Abuse controls must match topology and metered-service exposure. | prelaunch |
| [BACK-05](PRODUCTION_CHECKLIST_clone_swap.md#L234) | Cookie-authenticated mutations need CSRF protection. | prelaunch |
| [BACK-06](PRODUCTION_CHECKLIST_clone_swap.md#L235) | Cross-origin access must be explicitly limited where needed. | prelaunch |
| [BACK-07](PRODUCTION_CHECKLIST_clone_swap.md#L236) | Private and error responses must not be cached or mis-typed. | prelaunch |
| [BACK-08](PRODUCTION_CHECKLIST_clone_swap.md#L237) | Secrets belong in environment configuration and must fail safely. | prelaunch |
| [BACK-09](PRODUCTION_CHECKLIST_clone_swap.md#L238) | Logs must support response while excluding credentials and personal data. | prelaunch |
| [BACK-10](PRODUCTION_CHECKLIST_clone_swap.md#L239) | Bounded idempotent delivery avoids duplicate or ambiguous side effects. | prelaunch |
| [BACK-12](PRODUCTION_CHECKLIST_clone_swap.md#L241) | Spam controls must deter abuse without blocking accessible form use. | prelaunch |
| [BACK-13](PRODUCTION_CHECKLIST_clone_swap.md#L242) | Email header injection could expose data or redirect delivery. | prelaunch |
| [BACK-14](PRODUCTION_CHECKLIST_clone_swap.md#L243) | Data minimization and deletion prevent unnecessary personal-data retention. | prelaunch |
| [BACK-15](PRODUCTION_CHECKLIST_clone_swap.md#L244) | Side-effect retries must not create duplicate submissions or payments. | prelaunch |
| [BACK-17](PRODUCTION_CHECKLIST_clone_swap.md#L246) | Untrusted request bodies must be bounded, encoded, and safely logged. | prelaunch |
| [BACK-18](PRODUCTION_CHECKLIST_clone_swap.md#L247) | Authorization must be enforced for every private data operation. | prelaunch |
| [BACK-20](PRODUCTION_CHECKLIST_clone_swap.md#L249) | Caches must never cross user or tenant privacy boundaries. | prelaunch |
| [BACK-22](PRODUCTION_CHECKLIST_clone_swap.md#L251) | Trusted webhooks require signature, replay, and atomic state protection. | prelaunch |
| [BACK-23](PRODUCTION_CHECKLIST_clone_swap.md#L252) | Live payment verification protects real checkout and entitlement journeys. | prelaunch |
| [MAIL-01](PRODUCTION_CHECKLIST_clone_swap.md#L258) | Authenticated domain mail protects delivery and sender integrity where used. | cutover |
| [MAIL-02](PRODUCTION_CHECKLIST_clone_swap.md#L259) | Marketing messages must meet applicable law and provider opt-out rules. | prelaunch |
| [MAIL-05](PRODUCTION_CHECKLIST_clone_swap.md#L262) | Contact notifications need a safe authenticated sender and usable reply path. | prelaunch |
| [MAIL-06](PRODUCTION_CHECKLIST_clone_swap.md#L263) | Actual recipient receipt proves the enquiry journey works in production. | cutover |
| [MAIL-07](PRODUCTION_CHECKLIST_clone_swap.md#L264) | Promised transactional flows need verified mail and safe links. | cutover |
| [HOST-01](PRODUCTION_CHECKLIST_clone_swap.md#L270) | Every live hostname needs valid TLS and a clear HTTPS destination. | cutover |
| [HOST-02](PRODUCTION_CHECKLIST_clone_swap.md#L271) | Modern supported TLS protects every deployed connection. | cutover |
| [HOST-03](PRODUCTION_CHECKLIST_clone_swap.md#L272) | Automated renewal prevents certificate expiry and outages. | prelaunch |
| [HOST-04](PRODUCTION_CHECKLIST_clone_swap.md#L273) | Correct DNS and no dangling records protect reachability and takeover safety. | cutover |
| [HOST-07](PRODUCTION_CHECKLIST_clone_swap.md#L276) | Unknown deployed routes must return a real 404. | cutover |
| [HOST-08](PRODUCTION_CHECKLIST_clone_swap.md#L277) | Host-specific security headers must reach deployed and function responses. | cutover |
| [HOST-09](PRODUCTION_CHECKLIST_clone_swap.md#L278) | Preview builds need access protection; noindex alone is not security. | prelaunch |
| [HOST-10](PRODUCTION_CHECKLIST_clone_swap.md#L279) | The reviewed deployable artifact and rollback identity must be reproducible. | prelaunch |
| [HOST-12](PRODUCTION_CHECKLIST_clone_swap.md#L281) | Account security and registrar controls reduce takeover risk. | prelaunch |
| [HOST-14](PRODUCTION_CHECKLIST_clone_swap.md#L283) | Recoverable source, content, configuration, and data protect continuity. | prelaunch |
| [HOST-16](PRODUCTION_CHECKLIST_clone_swap.md#L285) | Live confirmation proves required headers are actually enforced. | cutover |
| [HOST-19](PRODUCTION_CHECKLIST_clone_swap.md#L288) | Safe cutover preserves service and a tested rollback path. | cutover |
| [HOST-22](PRODUCTION_CHECKLIST_clone_swap.md#L291) | DNS changes must preserve real business email delivery. | cutover |
| [HOST-23](PRODUCTION_CHECKLIST_clone_swap.md#L292) | Historic routes must map to relevant pages or honest removals. | cutover |
| [OPS-04](PRODUCTION_CHECKLIST_clone_swap.md#L301) | Optional real-user telemetry still needs privacy-safe collection. Verify the initial safety controls before enabling; repeat during operation. | prelaunch |
| [OPS-05](PRODUCTION_CHECKLIST_clone_swap.md#L302) | Error telemetry must scrub personal data before transmission. Verify the initial safety controls before enabling; repeat during operation. | prelaunch |
| [OPS-06](PRODUCTION_CHECKLIST_clone_swap.md#L303) | Exploited vulnerabilities need prompt recurring remediation. Verify the initial safety controls before enabling; repeat during operation. | prelaunch |
| [OPS-10](PRODUCTION_CHECKLIST_clone_swap.md#L307) | Approved analytics must respect privacy choices and avoid sensitive payloads. Verify the initial safety controls before enabling; repeat during operation. | prelaunch |
| [LEG-02](PRODUCTION_CHECKLIST_clone_swap.md#L316) | Trackers must not collect data before valid review and consent. | prelaunch |
| [LEG-03](PRODUCTION_CHECKLIST_clone_swap.md#L317) | Reference assets and unlicensed material create rights and identity risk. | prelaunch |
| [LEG-04](PRODUCTION_CHECKLIST_clone_swap.md#L318) | Child-directed or known child data requires applicable safeguards. | prelaunch |
| [LEG-05](PRODUCTION_CHECKLIST_clone_swap.md#L319) | Marketing messages must include legally required opt-out and sender details. | prelaunch |
| [LEG-06](PRODUCTION_CHECKLIST_clone_swap.md#L320) | Paid checkout terms must be visible before a financial commitment. | prelaunch |
| [LEG-08](PRODUCTION_CHECKLIST_clone_swap.md#L322) | Privacy decisions require the complete actual data flow and jurisdiction. | prelaunch |
| [LEG-09](PRODUCTION_CHECKLIST_clone_swap.md#L323) | Applicable consent must reflect current law and actual storage use. | prelaunch |
| [LEG-10](PRODUCTION_CHECKLIST_clone_swap.md#L324) | Applicable privacy opt-outs must reach downstream processors. | prelaunch |
| [LEG-11](PRODUCTION_CHECKLIST_clone_swap.md#L325) | Privacy notices must describe the real collection and user choices. | prelaunch |
| [LEG-12](PRODUCTION_CHECKLIST_clone_swap.md#L326) | Applicable accessibility disclosures must match the deployed build and evidence. | prelaunch |
| [LEG-13](PRODUCTION_CHECKLIST_clone_swap.md#L327) | Required entity and commerce disclosures protect informed transactions. | prelaunch |
| [LEG-14](PRODUCTION_CHECKLIST_clone_swap.md#L328) | Third-party licences and attribution determine lawful use. | prelaunch |
| [LEG-15](PRODUCTION_CHECKLIST_clone_swap.md#L329) | Safe-harbor measures matter when user content and reliance make them applicable. | prelaunch |
| [LEG-16](PRODUCTION_CHECKLIST_clone_swap.md#L330) | Content rights and approvals must be established before public use. | prelaunch |
| [LEG-17](PRODUCTION_CHECKLIST_clone_swap.md#L331) | Qualified review resolves material legal and rights uncertainty. | prelaunch |
| [I18N-01](PRODUCTION_CHECKLIST_clone_swap.md#L342) | Language routing and locale metadata preserve access to translated journeys. | prelaunch |
| [I18N-03](PRODUCTION_CHECKLIST_clone_swap.md#L344) | Missing glyphs or RTL layout can make language content unusable. | prelaunch |
| [I18N-04](PRODUCTION_CHECKLIST_clone_swap.md#L345) | Locale-aware dates and currencies prevent misleading displayed information. | prelaunch |
| [CNT-02](PRODUCTION_CHECKLIST_clone_swap.md#L352) | Reference text and assets must not enter the client release. | prelaunch |
| [CNT-03](PRODUCTION_CHECKLIST_clone_swap.md#L353) | Media provenance and alternative text protect rights and access. | prelaunch |
| [CNT-04](PRODUCTION_CHECKLIST_clone_swap.md#L354) | Only complete approved content may be indexed as client-ready. | prelaunch |
| [CNT-05](PRODUCTION_CHECKLIST_clone_swap.md#L355) | Invented facts and unsupported claims create deception and legal risk. | prelaunch |
| [CNT-07](PRODUCTION_CHECKLIST_clone_swap.md#L357) | Text contrast over client images must meet WCAG AA. | prelaunch |
| [CNT-08](PRODUCTION_CHECKLIST_clone_swap.md#L358) | Font licensing determines whether the shipped files may be used. | prelaunch |
| [CNT-09](PRODUCTION_CHECKLIST_clone_swap.md#L359) | Removing location metadata protects privacy; format/crop targets are quality. | prelaunch |
| [CNT-10](PRODUCTION_CHECKLIST_clone_swap.md#L360) | Missing translations must not silently fabricate content. | prelaunch |
| [CNT-11](PRODUCTION_CHECKLIST_clone_swap.md#L361) | Live content status and canonical URLs must match release state. | cutover |
| [CNT-14](PRODUCTION_CHECKLIST_clone_swap.md#L364) | Private reference material must never ship or be publicly served. | prelaunch |
| [CNT-15](PRODUCTION_CHECKLIST_clone_swap.md#L365) | Stock rights and client approval must be traceable before publication. | prelaunch |
| [CNT-17](PRODUCTION_CHECKLIST_clone_swap.md#L367) | Descriptive link names are part of accessible navigation. | prelaunch |
| [DEL-01](PRODUCTION_CHECKLIST_clone_swap.md#L373) | Environment and DNS records must be complete without exposing secrets. | prelaunch |
| [DEL-02](PRODUCTION_CHECKLIST_clone_swap.md#L374) | Live probes must distinguish deployment facts from unverified status. | prelaunch |
| [DEL-03](PRODUCTION_CHECKLIST_clone_swap.md#L375) | Legal drafts must match real data and avoid unsupported claims. | prelaunch |
| [DEL-04](PRODUCTION_CHECKLIST_clone_swap.md#L376) | Accessibility deviations must be disclosed and fixed in the shipped build. | prelaunch |
| [DEL-05](PRODUCTION_CHECKLIST_clone_swap.md#L377) | Provenance and reference rights determine whether reproduction can be released. | prelaunch |
| [DEL-08](PRODUCTION_CHECKLIST_clone_swap.md#L380) | Only the separately identified accessible artifact may be deployed. | prelaunch |
| [DEL-09](PRODUCTION_CHECKLIST_clone_swap.md#L381) | Release documentation must state the actual scope and unresolved defects. | prelaunch |
| [DEL-10](PRODUCTION_CHECKLIST_clone_swap.md#L382) | Exact cutover and rollback steps protect service continuity. | prelaunch |
| [DEL-14](PRODUCTION_CHECKLIST_clone_swap.md#L386) | Acceptance must be tied to the actual deployed release and pending checks. | cutover |
| [DEL-15](PRODUCTION_CHECKLIST_clone_swap.md#L387) | Evidence identity and unresolved launch defects must block false readiness. | prelaunch |

## Gold

| ID | Purpose and priority reason | When |
|---|---|---|
| [SPD-01](PRODUCTION_CHECKLIST_clone_swap.md#L29) | Comparable lab speed and layout stability are quality targets. | prelaunch |
| [SPD-02](PRODUCTION_CHECKLIST_clone_swap.md#L30) | Deployed parity informs quality; it is not a safety gate. | cutover |
| [SPD-03](PRODUCTION_CHECKLIST_clone_swap.md#L31) | Early LCP discovery improves loading quality. | prelaunch |
| [SPD-04](PRODUCTION_CHECKLIST_clone_swap.md#L32) | Dimensions and lazy loading reduce layout shifts. | prelaunch |
| [SPD-05](PRODUCTION_CHECKLIST_clone_swap.md#L33) | Responsive image sizing balances visual quality and bytes. | prelaunch |
| [SPD-07](PRODUCTION_CHECKLIST_clone_swap.md#L35) | Compression improves delivery without changing content safety. | prelaunch |
| [SPD-08](PRODUCTION_CHECKLIST_clone_swap.md#L36) | Avoiding excess JavaScript protects loading and interaction quality. | prelaunch |
| [SPD-09](PRODUCTION_CHECKLIST_clone_swap.md#L37) | A stalled intro must not block usable content. | prelaunch |
| [SPD-11](PRODUCTION_CHECKLIST_clone_swap.md#L39) | Back-forward restoration improves repeat-visit continuity. | prelaunch |
| [SPD-13](PRODUCTION_CHECKLIST_clone_swap.md#L41) | These strict lab scores are agency budgets, not certification. | prelaunch |
| [SPD-14](PRODUCTION_CHECKLIST_clone_swap.md#L42) | Origin latency limits are internal performance targets. | prelaunch |
| [SPD-15](PRODUCTION_CHECKLIST_clone_swap.md#L43) | Edge latency depends on the auditor's network and host. | cutover |
| [SPD-17](PRODUCTION_CHECKLIST_clone_swap.md#L45) | Critical-path byte ceilings are strict agency performance budgets. | prelaunch |
| [SPD-18](PRODUCTION_CHECKLIST_clone_swap.md#L46) | Render-blocking limits improve perceived loading quality. | prelaunch |
| [SPD-20](PRODUCTION_CHECKLIST_clone_swap.md#L48) | Live comparison verifies deployed performance quality. | cutover |
| [SPD-21](PRODUCTION_CHECKLIST_clone_swap.md#L49) | Field vitals require real post-launch traffic and sampling. | postlaunch |
| [TYP-01](PRODUCTION_CHECKLIST_clone_swap.md#L55) | Font formats and subsetting improve compatibility and loading. | prelaunch |
| [TYP-02](PRODUCTION_CHECKLIST_clone_swap.md#L56) | Metric fallbacks reduce layout movement during font loading. | prelaunch |
| [TYP-03](PRODUCTION_CHECKLIST_clone_swap.md#L57) | Selective font preloads improve first rendering. | prelaunch |
| [TYP-04](PRODUCTION_CHECKLIST_clone_swap.md#L58) | Real font faces preserve the intended text appearance. | prelaunch |
| [TYP-09](PRODUCTION_CHECKLIST_clone_swap.md#L63) | Preventing unwanted mobile text inflation improves legibility. | prelaunch |
| [TYP-10](PRODUCTION_CHECKLIST_clone_swap.md#L64) | Input sizing avoids mobile zoom in form journeys. | prelaunch |
| [TYP-12](PRODUCTION_CHECKLIST_clone_swap.md#L66) | Matching the canvas color prevents visual flashes. | prelaunch |
| [TYP-13](PRODUCTION_CHECKLIST_clone_swap.md#L67) | Image placeholders reduce loading flashes. | prelaunch |
| [TYP-15](PRODUCTION_CHECKLIST_clone_swap.md#L69) | A fallback keeps used backdrop effects from failing abruptly. | prelaunch |
| [TYP-17](PRODUCTION_CHECKLIST_clone_swap.md#L71) | Stable scrollbars prevent modal layout jumps. | prelaunch |
| [TYP-19](PRODUCTION_CHECKLIST_clone_swap.md#L73) | Pointer-specific hover handling improves touch and keyboard quality. | prelaunch |
| [TYP-21](PRODUCTION_CHECKLIST_clone_swap.md#L75) | Forced-color support improves experience for a system preference. | prelaunch |
| [TYP-24](PRODUCTION_CHECKLIST_clone_swap.md#L78) | Font-count and byte caps are agency performance budgets. | prelaunch |
| [RSP-02](PRODUCTION_CHECKLIST_clone_swap.md#L85) | The broad width matrix checks responsive quality beyond reflow. | prelaunch |
| [RSP-06](PRODUCTION_CHECKLIST_clone_swap.md#L89) | Cross-engine journey checks reduce compatibility defects. | prelaunch |
| [RSP-08](PRODUCTION_CHECKLIST_clone_swap.md#L91) | The large screenshot matrix is expanded device-quality coverage. | prelaunch |
| [RSP-10](PRODUCTION_CHECKLIST_clone_swap.md#L93) | Physical device checks add evidence beyond browser emulation. | prelaunch |
| [SEO-01](PRODUCTION_CHECKLIST_clone_swap.md#L126) | Unique useful metadata improves route identity; exact lengths are house guidance. | prelaunch |
| [SEO-10](PRODUCTION_CHECKLIST_clone_swap.md#L135) | Accurate crawl directives and route maps support discoverability. | prelaunch |
| [SEO-12](PRODUCTION_CHECKLIST_clone_swap.md#L137) | Image semantics and source fallbacks improve discovery and resilience. | prelaunch |
| [SEO-13](PRODUCTION_CHECKLIST_clone_swap.md#L138) | Indexing follow-up can only be measured after deployment. | postlaunch |
| [SEO-14](PRODUCTION_CHECKLIST_clone_swap.md#L139) | Working external destinations preserve visitor paths; link review recurs. | recurring |
| [EDGE-03](PRODUCTION_CHECKLIST_clone_swap.md#L150) | Clear error copy helps visitors recover without blame. | prelaunch |
| [EDGE-08](PRODUCTION_CHECKLIST_clone_swap.md#L155) | Runtime errors and failed resources reveal reliability defects. | prelaunch |
| [EDGE-10](PRODUCTION_CHECKLIST_clone_swap.md#L157) | Browser history should restore a coherent page position. | prelaunch |
| [EDGE-11](PRODUCTION_CHECKLIST_clone_swap.md#L158) | Long content must not break flexible page layouts. | prelaunch |
| [EDGE-15](PRODUCTION_CHECKLIST_clone_swap.md#L162) | The 404 byte and LCP ceilings are house budgets. | prelaunch |
| [UXF-06](PRODUCTION_CHECKLIST_clone_swap.md#L178) | The 44-pixel target is an AAA/policy enhancement over AA sizing. | prelaunch |
| [UXF-09](PRODUCTION_CHECKLIST_clone_swap.md#L181) | The five-second copy test is a useful clarity heuristic. | prelaunch |
| [UXF-10](PRODUCTION_CHECKLIST_clone_swap.md#L182) | Declared color scheme should preserve the intended rendered design. | prelaunch |
| [UXF-11](PRODUCTION_CHECKLIST_clone_swap.md#L183) | Comparing contact-path length with the design reference is conversion polish; real working CTAs remain Diamond under UXF-01 and UXF-03. | prelaunch |
| [MOT-01](PRODUCTION_CHECKLIST_clone_swap.md#L189) | Frame-rate thresholds are agency smoothness budgets, not universal standards. | prelaunch |
| [MOT-02](PRODUCTION_CHECKLIST_clone_swap.md#L190) | Efficient animation properties reduce rendering cost. | prelaunch |
| [MOT-03](PRODUCTION_CHECKLIST_clone_swap.md#L191) | Framework cleanup prevents interaction leaks on route changes. | prelaunch |
| [MOT-12](PRODUCTION_CHECKLIST_clone_swap.md#L200) | Rejected autoplay must leave a usable poster and stable layout. | prelaunch |
| [MOT-13](PRODUCTION_CHECKLIST_clone_swap.md#L201) | GPU context and memory limits prevent resource degradation. | prelaunch |
| [MOT-14](PRODUCTION_CHECKLIST_clone_swap.md#L202) | Appropriate passive listeners improve touch-scroll responsiveness. | prelaunch |
| [MOT-15](PRODUCTION_CHECKLIST_clone_swap.md#L203) | Long-frame limits are internal smoothness targets. | prelaunch |
| [SEC-08](PRODUCTION_CHECKLIST_clone_swap.md#L216) | Public source maps and debug logging are avoidable exposure and quality issues. | prelaunch |
| [SEC-11](PRODUCTION_CHECKLIST_clone_swap.md#L219) | A repeatable verification command improves delivery quality. | prelaunch |
| [SEC-13](PRODUCTION_CHECKLIST_clone_swap.md#L221) | Trusted Types adds defense-in-depth for supported DOM sinks. | prelaunch |
| [BACK-11](PRODUCTION_CHECKLIST_clone_swap.md#L240) | Health probes support hosting operations but are not a visitor journey. | prelaunch |
| [BACK-19](PRODUCTION_CHECKLIST_clone_swap.md#L248) | Database workload budgets and pagination protect query quality at scale. | prelaunch |
| [BACK-21](PRODUCTION_CHECKLIST_clone_swap.md#L250) | Connection-pool limits and recovery are provider-specific performance controls. | prelaunch |
| [HOST-11](PRODUCTION_CHECKLIST_clone_swap.md#L280) | Monitoring intervals are agency operations policy after setup. | recurring |
| [HOST-17](PRODUCTION_CHECKLIST_clone_swap.md#L286) | The five-minute rollback cap is a house target, not the rollback requirement. | prelaunch |
| [HOST-18](PRODUCTION_CHECKLIST_clone_swap.md#L287) | Early Hints and HTTP/3 improve edge delivery when supported. | cutover |
| [OPS-01](PRODUCTION_CHECKLIST_clone_swap.md#L298) | CI quality gates reduce accidental broken releases. | recurring |
| [OPS-02](PRODUCTION_CHECKLIST_clone_swap.md#L299) | Strict Lighthouse and byte thresholds are agency budgets. | recurring |
| [OPS-03](PRODUCTION_CHECKLIST_clone_swap.md#L300) | A complete operations runbook improves recovery quality. | prelaunch |
| [OPS-07](PRODUCTION_CHECKLIST_clone_swap.md#L304) | A supported-browser policy makes compatibility expectations explicit. | recurring |
| [OPS-08](PRODUCTION_CHECKLIST_clone_swap.md#L305) | Seven- and thirty-day reviews are post-launch checks, never prelaunch evidence. | postlaunch |
| [LEG-01](PRODUCTION_CHECKLIST_clone_swap.md#L315) | Self-hosted fonts reduce dependencies; privacy and origin approval remain mandatory under LEG-08 and SEC-05. | prelaunch |
| [I18N-02](PRODUCTION_CHECKLIST_clone_swap.md#L343) | Expansion tests help prevent clipping in supported translations. | prelaunch |
| [CNT-01](PRODUCTION_CHECKLIST_clone_swap.md#L351) | Input reporting keeps preparation resilient without blocking useful work. | prelaunch |
| [CNT-06](PRODUCTION_CHECKLIST_clone_swap.md#L356) | Copy-fit parity protects readable content across real viewports. | prelaunch |
| [CNT-13](PRODUCTION_CHECKLIST_clone_swap.md#L363) | Slot markers must survive motion so supplied content stays intact. | prelaunch |
| [CNT-16](PRODUCTION_CHECKLIST_clone_swap.md#L366) | The default brand shift is a fidelity and approval quality gate. | prelaunch |
| [DEL-06](PRODUCTION_CHECKLIST_clone_swap.md#L378) | A clean offline rebuild adds reproducibility evidence. | prelaunch |
| [DEL-07](PRODUCTION_CHECKLIST_clone_swap.md#L379) | Transactional sync prevents bad content from replacing a good build. | prelaunch |
| [DEL-11](PRODUCTION_CHECKLIST_clone_swap.md#L383) | Complete account, provider, and support handover improves ownership. | prelaunch |
| [DEL-13](PRODUCTION_CHECKLIST_clone_swap.md#L385) | Maintenance tasks need named owners and recurring dates. | recurring |
| [DEL-16](PRODUCTION_CHECKLIST_clone_swap.md#L388) | A scoped brief and flow matrix reduce avoidable delivery defects. | prelaunch |

## Silver

| ID | Purpose and priority reason | When |
|---|---|---|
| [SPD-10](PRODUCTION_CHECKLIST_clone_swap.md#L38) | Video transfer tuning is an optional media enhancement. | prelaunch |
| [SPD-12](PRODUCTION_CHECKLIST_clone_swap.md#L40) | Speculative loading is optional and must avoid side effects. | prelaunch |
| [SPD-16](PRODUCTION_CHECKLIST_clone_swap.md#L44) | The HTML byte cap is a discretionary transfer target. | prelaunch |
| [SPD-19](PRODUCTION_CHECKLIST_clone_swap.md#L47) | Precompressed assets optimize a delivery implementation. | prelaunch |
| [TYP-07](PRODUCTION_CHECKLIST_clone_swap.md#L61) | Text wrapping polish is optional and reference-dependent. | prelaunch |
| [TYP-08](PRODUCTION_CHECKLIST_clone_swap.md#L62) | Tabular numerals are a visual alignment enhancement. | prelaunch |
| [TYP-14](PRODUCTION_CHECKLIST_clone_swap.md#L68) | Gradient grain and fixed-background rules are visual polish. | prelaunch |
| [TYP-16](PRODUCTION_CHECKLIST_clone_swap.md#L70) | Branded selection and control colors are optional polish. | prelaunch |
| [TYP-20](PRODUCTION_CHECKLIST_clone_swap.md#L74) | Print styling is a useful but non-core output enhancement. | prelaunch |
| [TYP-23](PRODUCTION_CHECKLIST_clone_swap.md#L77) | Line-length and font-size targets exceed baseline conformance. | prelaunch |
| [A11Y-21](PRODUCTION_CHECKLIST_clone_swap.md#L119) | Extra contrast-preference rendering is an enhancement beyond the default accessible build. | prelaunch |
| [SEO-05](PRODUCTION_CHECKLIST_clone_swap.md#L130) | Social preview tags and exact image targets are sharing polish. | prelaunch |
| [SEO-06](PRODUCTION_CHECKLIST_clone_swap.md#L131) | A complete multi-size icon set is not a core journey. | prelaunch |
| [SEO-09](PRODUCTION_CHECKLIST_clone_swap.md#L134) | A security contact file is useful when the client provides one. | prelaunch |
| [SEO-15](PRODUCTION_CHECKLIST_clone_swap.md#L140) | Buyer-intent research is commissioned search strategy, not launch safety. | prelaunch |
| [EDGE-13](PRODUCTION_CHECKLIST_clone_swap.md#L160) | Offline shell support is optional and brings service-worker complexity. | prelaunch |
| [EDGE-16](PRODUCTION_CHECKLIST_clone_swap.md#L163) | Path suggestions add convenience; safe text rendering is required if used. | prelaunch |
| [MOT-08](PRODUCTION_CHECKLIST_clone_swap.md#L196) | Cursor effects are optional polish with device and motion limits. | prelaunch |
| [SEC-14](PRODUCTION_CHECKLIST_clone_swap.md#L222) | Cross-origin isolation is an optional capability with compatibility costs. | prelaunch |
| [MAIL-03](PRODUCTION_CHECKLIST_clone_swap.md#L260) | Separate marketing identities can help reputation but are not universal. | prelaunch |
| [MAIL-04](PRODUCTION_CHECKLIST_clone_swap.md#L261) | MTA-STS is a scoped mail-security enhancement requiring administrator coordination. | cutover |
| [HOST-05](PRODUCTION_CHECKLIST_clone_swap.md#L274) | HTTP/2 and HTTP/3 availability is host-dependent performance polish. | cutover |
| [HOST-06](PRODUCTION_CHECKLIST_clone_swap.md#L275) | A CDN cache hit is a performance enhancement, not a safety gate. | cutover |
| [HOST-13](PRODUCTION_CHECKLIST_clone_swap.md#L282) | Cost alerts and edge delivery limit avoidable operating expense. | prelaunch |
| [HOST-20](PRODUCTION_CHECKLIST_clone_swap.md#L289) | An A+ scanner score is one limited optional signal. | cutover |
| [HOST-21](PRODUCTION_CHECKLIST_clone_swap.md#L290) | A 100-percent Internet.nl score is broader than launch safety. | cutover |
| [OPS-09](PRODUCTION_CHECKLIST_clone_swap.md#L306) | Markup and stylesheet validation is useful quality assurance. | prelaunch |
| [SUS-01](PRODUCTION_CHECKLIST_clone_swap.md#L339) | Page-weight comparisons are an optional efficiency benchmark. | prelaunch |
| [SUS-02](PRODUCTION_CHECKLIST_clone_swap.md#L340) | Reduced-data media behavior benefits users but is an enhancement. | prelaunch |
| [CNT-12](PRODUCTION_CHECKLIST_clone_swap.md#L362) | A live clock or ticker is a feature-specific enhancement. | prelaunch |
| [DEL-12](PRODUCTION_CHECKLIST_clone_swap.md#L384) | A concise editing guide makes later content changes easier. | prelaunch |

## Bronze

| ID | Purpose and priority reason | When |
|---|---|---|
| [TYP-22](PRODUCTION_CHECKLIST_clone_swap.md#L76) | Matching reference viewport units is a fidelity experiment. | prelaunch |
| [A11Y-02](PRODUCTION_CHECKLIST_clone_swap.md#L100) | This named subset duplicates the broader axe coverage in A11Y-01. | prelaunch |
| [SEO-16](PRODUCTION_CHECKLIST_clone_swap.md#L141) | Promotion planning is optional and must not trigger unapproved outreach. | prelaunch |
| [SEO-17](PRODUCTION_CHECKLIST_clone_swap.md#L142) | Provider-specific AI crawler policy is niche and never a launch prerequisite. | prelaunch |
| [EDGE-01](PRODUCTION_CHECKLIST_clone_swap.md#L148) | Capturing the reference error page is fidelity evidence, not release safety. | prelaunch |
| [MOT-04](PRODUCTION_CHECKLIST_clone_swap.md#L192) | Lenis wiring is a reference-specific implementation experiment. | prelaunch |
| [MOT-07](PRODUCTION_CHECKLIST_clone_swap.md#L195) | Transition focus checks duplicate A11Y-12 and EDGE-10. | prelaunch |
| [MOT-09](PRODUCTION_CHECKLIST_clone_swap.md#L197) | Scrubbed-video encoding is a niche reference effect. | prelaunch |
| [MOT-10](PRODUCTION_CHECKLIST_clone_swap.md#L198) | A ready flag is test-harness convenience, not visitor safety. | prelaunch |
| [MOT-11](PRODUCTION_CHECKLIST_clone_swap.md#L199) | Matching frame dependence is a reference-motion experiment. | prelaunch |
| [BACK-16](PRODUCTION_CHECKLIST_clone_swap.md#L245) | This install and signature check repeats the broader SEC-07 supply-chain gate. | prelaunch |
| [HOST-15](PRODUCTION_CHECKLIST_clone_swap.md#L284) | A green-host score is an optional sustainability signal. | cutover |
| [LEG-07](PRODUCTION_CHECKLIST_clone_swap.md#L321) | This retired ID is retained as stable legacy bookkeeping. | prelaunch |
| [LEG-18](PRODUCTION_CHECKLIST_clone_swap.md#L332) | Detailed DMCA response planning is niche unless hosting user content or relying on safe harbor. | prelaunch |
| [SUS-03](PRODUCTION_CHECKLIST_clone_swap.md#L341) | A modelled carbon estimate is informational, not a launch control. | prelaunch |
