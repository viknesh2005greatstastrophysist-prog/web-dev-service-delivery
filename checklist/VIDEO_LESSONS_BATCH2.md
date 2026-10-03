# Video lessons, second batch

This companion integrates seven more sources into the [production checklist](PRODUCTION_CHECKLIST_clone_swap.md). Read it with the [first add-on](VIDEO_LESSONS_ADDON.md). The catalogue now has 275 rows in 18 sections. All earlier IDs remain. [Review and provenance](../docs/reviews/instagram-batch2-2026-10-03/REVIEW.md) distinguish six sampled videos from one fully inspected nine-slide carousel. No spoken audio was transcribed.

## Apply the actual gaps

- **Webhook handling, BACK-22:** test signatures on the raw body, event/account/mode binding, durable deduplication, failure/restart recovery and unordered events. Derive access from approved server billing state. Browser checkout redirects cannot grant entitlements.
- **Production payments, BACK-23:** local fixtures and sandbox results remain local evidence. The owner must authorize and record the supported production journey, actual live configuration and redacted outcomes. No test creates an unsolicited charge, refund or message. Record the actual seller/merchant-of-record arrangement before accepting payments.
- **Transactional mail, MAIL-07:** inventory configured critical flows beyond enquiries. Verify receipt and usable links with controlled recipients, including expiry/reuse/wrong-recipient behavior where applicable. Test supported providers; do not invent accounts or flows. MAIL-06 retains contact inbox proof separately.
- **Crawler choices, SEO-17:** distinguish owner-approved search discovery from training access and user-requested fetches. Check robots and CDN/WAF configuration against current provider documentation. Do not infer genuine crawler access from a request with a forged user-agent. Private/staging content stays protected.
- **URL migration, HOST-23:** map existing URLs to relevant replacements, preserve intended query behavior and verify permanent redirects on the deployed host. Deliberate retirement uses real 404/410 responses. Never turn all missing URLs into homepage redirects.

Strengthened existing checks: BACK-04 now requires cost/concurrency bounds for metered endpoints; MAIL-03 requires a documented sending-identity decision and complaint/bounce handling; UXF-09 includes approved audience-fit copy where the brief calls for it. BACK-05 makes the webhook signature exception explicit without disabling browser CSRF protection.

## Launch essentials from the twenty-item clip

| Items | Existing requirements |
| --- | --- |
| 1 clear H1; 2 CTA; 3 titles; 4 descriptions | SEO-04, UXF-03, SEO-01. Real, descriptive served content and destinations. |
| 5 service; 6 location; 7 about; 8 contact pages | DEL-16, SEO-15, CNT-05, UXF-03. Build useful approved routes, not mandatory filler pages or fabricated service areas. |
| 9 FAQs; 10 reviews; 11 trust signals | CNT-05, SEO-11. Answer real questions and use evidenced client claims/reviews. Visible FAQs do not imply FAQ rich results. |
| 12 internal links; 13 alt text | SEO-08, A11Y-02. Useful destinations and appropriate image alternatives. |
| 14 privacy; 15 terms | LEG-11, LEG-13, LEG-17. Match actual data/commerce and obtain required review; generated boilerplate is not legal clearance. |
| 16 mobile; 17 fast images | RSP-06, SPD-05, CNT-09. Actual journeys and measured delivery. |
| 18 analytics; 19 Search Console; 20 sitemap | OPS-10, SEO-13, SEO-10. Conditional privacy-safe analytics, owner-operated search tools and correct indexable routes. |

The ten- and fifteen-step SEO clips largely repeat these controls. HTTPS, mobile functionality and crawlability are verified before launch, not casually deferred. Remove noindex only for approved CLIENT-COMPLETE production, keep staging/private routes protected (SEO-02), and treat submission/indexing requests as actions rather than ranking proof. The city/keyword must match real content and service coverage. Backlinks need relevant, approved relationships, not paid ranking promises or automated outreach.

## The thirty-seven-item carousel

All nine slides were inspected; seven layers contain 37 checks. Most are already covered. The creator's priority labels do not override this kit's classes.

| Layer / count | Checklist mapping and correction |
| --- | --- |
| Security / 6 | BACK-18 for real authorization/RLS and paywalls; SEC-06 for deployed secrets including env files; SEC-03 for TLS; BACK-04 for abuse/cost bounds. Enabling RLS alone is insufficient; HTTPS is required at launch. |
| Email / 5 | MAIL-01, MAIL-03, MAIL-06, MAIL-07. Verify authentication, sending streams, real delivery and usable critical-flow links. A mail-test score does not prove inbox receipt. |
| Findability / 7 | SEO-05, SEO-13, SEO-02, SEO-01, CNT-11, DEL-16, SEO-10. App/marketing subdomains are an architecture option; llms.txt is optional. |
| Speed / 4 | SPD-20, SPD-05, SPD-04, SPD-08, SPD-17. Use pinned measurements; compression tool and dependency count alone do not establish speed. |
| Analytics / 6 | OPS-10, OPS-04, BACK-04, OPS-05, LEG-10, LEG-11. Optional collection needs genuine events and data minimization. Replay requires justified scope, input masking and applicable consent/rejection/withdrawal checks. Consent is not permission to record secrets. |
| Legal / 3 | LEG-11, LEG-13, LEG-17, BACK-23. Seller responsibilities and any required consent controls precede the affected activity. A generated notice or banner does not establish compliance. |
| Final journey / 6 | BACK-22, BACK-23, RSP-06, DEL-12, UXF-01, UXF-05, BACK-17, EDGE-02. Supported live payments require owner evidence. Physical phone checks, browser coverage, invalid forms and missing-page behavior remain real tests. |

The carousel's tool/skill commands are reference material, not instructions to install or execute anything. No creator was messaged to unlock further material. No third-party skill, analytics service or payment provider was installed.

## Twenty technical giveaways, without technology prejudice

| Clip items | Decision |
| --- | --- |
| 1 provider URL; 2 empty HTML; 3 no 404; 4 scaffold browser title | Verify approved production identity/content (CNT-11), served public copy (SEO-04), real 404 (SEO-03/EDGE-02), and titles (SEO-01). React/Vite or a provider URL alone says nothing about implementation quality. |
| 5 repeated titles; 6 missing descriptions; 7 missing share image; 8 missing structured data | SEO-01, SEO-05, SEO-11. Markup uses applicable approved facts; never fabricate it to fill a diagnostic. |
| 9 multiple H1s; 10 no H1; 11 no canonical | Inspect the actual heading hierarchy and primary content, A11Y-04/SEO-04, and URL policy, SEO-07. Do not claim AI authorship from heading count. |
| 12 no llms.txt; 13 blocked AI bots | Optional file and explicit owner crawler decision, SEO-17. Blocking training crawlers may be deliberate and valid. |
| 14 favicon; 15 sitemap; 16 language; 17 alt | SEO-06, SEO-10, A11Y-02. Check actual files, HTML language and image roles. |
| 18 maps; 19 console errors; 20 large bundles | SEC-08, OPS-05, SPD-17. Audit deployed artifacts and real failures; private source-map upload can aid debugging, but public maps never contain secrets. Use measured budgets, not the clip's illustrative bundle sizes. |

## Domain setup and audience-fit copy

App/marketing separation can support distinct providers. Document who owns each DNS/service account, cookie scope, origins, authentication callbacks and return URLs before adopting it (DEL-16, BACK-05, BACK-06, SEC-09, HOST-19, HOST-22). Preserve business mail during cutover. It is not a requirement to split a simple brochure site into multiple hosts.

Use provider-supported sending subdomains/streams when appropriate (MAIL-03), authenticate them and monitor complaints/bounces. Extra or lookalike domains do not guarantee reputation safety and can confuse recipients. Do not copy example DNS values; use the selected provider's exact records and preserve existing mail. The public sitemap includes only intended indexable routes, not account/private content.

Audience-fit copy should explain which real needs and working preferences the client serves. Keep the offer clear. A small approved section about who benefits can help self-qualification; claims of affluence, exclusivity or improved conversion still need evidence (UXF-09, CNT-05, DEL-14). Do not copy the creator's financial-adviser examples into an unrelated client site.

## Primary-source corrections

Checked 2026-10-03:

- [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots): search and training controls are independent. Permission never guarantees search inclusion.
- [Google AI-search guidance](https://developers.google.com/search/docs/appearance/ai-features): Google's AI features need no special AI text files or new markup. This does not prove what every other provider consumes.
- [Stripe webhook guidance](https://docs.stripe.com/webhooks): preserve the raw body for signature verification and handle duplicates and unordered events. Use the actual chosen provider's equivalent guidance when Stripe is absent.
- [Resend sending-domain guidance](https://resend.com/docs/knowledge-base/is-it-better-to-send-emails-from-a-subdomain-or-the-root-domain): purpose-specific subdomains support reputation management; lookalike domains can harm trust. The site's actual provider and sender policy govern implementation.

These corrections distinguish provider documentation from the creators' suggestions. They are not ranking, deliverability, legal or commercial guarantees.
