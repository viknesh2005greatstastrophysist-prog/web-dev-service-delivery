# Primary source register

Checked 2026-10-02. These sources support the corrections listed below, not a claim that every historical statistic, version or provider feature in the kit has been freshly verified. House targets remain policy. Recheck changing provider/tool behaviour for the actual release.

| Source | Correction or boundary supported |
|---|---|
| [web.dev: Web Vitals](https://web.dev/articles/vitals) | Field p75 thresholds and distinction between field and lab evidence; SPD-01, SPD-21. |
| [web.dev: Optimize LCP](https://web.dev/articles/optimize-lcp) | TTFB is part of full LCP; resource discovery and phase diagnostics do not justify subtracting server time for a cross-environment pass. |
| [W3C: Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) | A11Y-10 requires the relevant mechanism; reduced-motion preference alone is not a blanket substitute. |
| [W3C: Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) | A11Y-07 needs a non-dragging single-pointer alternative; keyboard support is separate. |
| [W3C: Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | RSP-05 permits the criterion's spacing and other exceptions; one full hit-box sampling test cannot represent all conforming cases. |
| [OWASP: HTTP Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html) | Security headers must be interpreted in their feature/context; scanner grades and headers are partial controls. |
| [Google: Search technical requirements](https://developers.google.com/search/docs/essentials/technical) | SEO-13 records indexing status; technical eligibility does not guarantee indexing. |
| [MDN: Observatory FAQ](https://developer.mozilla.org/en-US/observatory/docs/faq) | HOST-20 stores actual report version/count and treats A+ as a limited header-scan result, not security certification. Its scan history is public. |
| [MDN: crossOriginIsolated](https://developer.mozilla.org/en-US/docs/Web/API/Window/crossOriginIsolated) | SEC-14 describes risk mitigation and compatibility limits, not complete side-channel immunity. |
| [Cloudflare: TCP sockets](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) | Port 25 restrictions and runtime-specific networking reinforce BACK-01: test the chosen runtime and provider transport, not a Node-only substitute. |
| [Google: Email sender guidelines](https://support.google.com/a/answer/81126?hl=en) | MAIL-01/02 distinguish general, bulk and marketing/subscription requirements. SPF/DKIM/DMARC together remain this kit's stated policy. |
| [RFC 8461: MTA-STS, section 5](https://datatracker.ietf.org/doc/html/rfc8461#section-5) | MAIL-04 testing mode permits delivery on policy failure; enforce is a separate administrator decision. |
| [FTC: CAN-SPAM business guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) | MAIL-02 tests advertising disclosure, opt-out, identity, postal details, suppression timing and continued mechanism availability. Removed penalty trivia from the active gate. |
| [California DOJ: CCPA](https://oag.ca.gov/privacy/ccpa) | LEG-10 applies opt-out rules to covered data use; a first-party browser request does not prove that a business has no sale/sharing. |
| [US Copyright Office: section 512](https://www.copyright.gov/512/) | LEG-15 depends on applicable safe-harbor conditions; having an upload field or registering an agent alone does not establish eligibility. |

Implementation judgments include immutable artifact identity, integrity checks, fail-closed statuses, no automatic fidelity waiver, always-accessible deployment, cross-worker idempotency tests, recovery evidence and redacted owner confirmation. These are delivery controls, not external certification claims.

The audit did not deploy a client site, buy a screen-reader licence, change DNS/mail policy, send mail to a recipient or conduct a legal opinion. Existing historical source notes are retained and explicitly labeled historical.
