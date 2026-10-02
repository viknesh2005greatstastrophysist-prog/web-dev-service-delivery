# Video lessons add-on

Use this alongside the [production checklist](PRODUCTION_CHECKLIST_clone_swap.md), not as a second release gate. Nine supplied Instagram clips were reviewed on 2026-10-03 through sampled visual frames and public post descriptions. Spoken audio was not transcribed. The [source review](../docs/reviews/instagram-addon-2026-10-03/REVIEW.md) records coverage, limitations and corrections; [lessons.json](../docs/reviews/instagram-addon-2026-10-03/lessons.json) records source/media/frame hashes and row mappings. Hashes establish identity, not truth or permission to reuse media.

## Put the lessons into the delivery flow

1. Before coding, write the concise brief and critical-flow acceptance matrix in DEL-16. For each journey, record route/state, actor, action, expected result, failure behavior, applicable row and evidence. Example: a visitor submits the contact form, sees honest pending/error/success feedback, and the operator verifies the provider outcome separately. Unknown inputs remain CONTENT-PENDING.
2. Use a bounded plan/build/verify cycle. Report findings with severity, location, reproduction and evidence. An unknown result remains NOT_RUN or OWNER-CONFIRM. Fix and retest the affected flow; a model's reassuring report is not evidence.
3. Apply the UI checks below to every scoped route/state, including the final content swap. Keep the existing lab profiles and budgets, and verify live behavior separately.
4. If organic-search research is commissioned, save a dated query/intent/result-source brief and map primary topics to useful routes (SEO-15). Model scoring can shortlist research. A human reviews the evidence, conflicts and missing information. Do not invent volume or ranking potential.
5. For approved promotion, prepare the owner-reviewed channel/profile plan (SEO-16). Record eligibility, client ownership, accurate business details, copy, destination, timing and metric. Search tool verification/submission remains SEO-13. No automated public posting or account creation follows from preparing this plan.
6. If data features exist, test identity/permissions (BACK-18), representative query workloads (BACK-19), cache isolation/invalidation (BACK-20) and direct SQL connection behavior (BACK-21). Record an observed absence for each nonapplicable feature. Static websites do not acquire infrastructure merely to make a checklist look busy.
7. Where analytics is approved, test meaningful, privacy-safe events on the final deployed artifact (OPS-10). Separate a click, accepted request, confirmed delivery and actual commercial outcome. Consent rejection and withdrawal are test states.

The eight new rows are DEL-16, SEO-15, SEO-16, BACK-18, BACK-19, BACK-20, BACK-21 and OPS-10. Existing row IDs are preserved. The release record contains all 270 IDs; applicability and the existing handover/launch/gold rules determine the decision.

## Twenty quick fixes, mapped to existing checks

The Alex Yates clip has twenty tips. They mostly repeat existing requirements, so they do not become twenty duplicate rows.

| Clip tip | Existing checks and practical evidence |
| --- | --- |
| 1. Horizontal scroll | RSP-02, RSP-03, CNT-06: viewport and final-copy overflow checks. |
| 2. Broken links | SEO-08, SEO-14: resolve internal links and report externally blocked checks honestly. |
| 3. Mobile menu | RSP-06, EDGE-06, UXF-01: open/close, focus, keyboard and no-JS navigation. |
| 4. Favicon | SEO-06: request the actual icon files and parse the manifest. |
| 5. Page titles | SEO-01: inspect every route's served title. |
| 6. Meta descriptions | SEO-01: unique, relevant descriptions from approved copy. |
| 7. Footer links | SEO-08, SEO-14: include footer destinations in the link audit. |
| 8. Custom 404 | EDGE-01, EDGE-02, SEO-03: usable missing-page view with real 404 status. |
| 9. Copyright year | DEL-09, DEL-14: record and confirm accurate owner-approved dates/ranges and rights notices; do not rewrite legal notices automatically. |
| 10. Compress images | SPD-05, CNT-09: appropriate dimensions/format and measured transferred bytes. |
| 11. Broken buttons | UXF-01, UXF-03: every apparent action has a real, approved effect. |
| 12. Success messages | UXF-02, UXF-05, MAIL-06: announce honest success and distinguish provider acceptance from receipt. |
| 13. Error messages | UXF-02, UXF-05, BACK-17: visible, accessible errors with preserved input and no personal-data leakage. |
| 14. Placeholders | CNT-04, CNT-11: no unapproved facts or placeholders on the completed production artifact. |
| 15. Unused navigation | UXF-01, SEO-08: remove dead interactive paths or give them their approved destination. |
| 16. Mobile overflow | RSP-02, RSP-03, CNT-06: test narrow screens after content changes. |
| 17. Clickable logo | UXF-01, SEO-08: when the logo is navigation, use a real home link and accessible name. |
| 18. Clickable number | UXF-04: verify visible number and international-format tel target. |
| 19. Clickable email | UXF-04: verify the real mailto address without personal data in prefilled text. |
| 20. Mobile optimization | RSP, A11Y, SPD sections: real interaction, reflow, target size and comparable mobile performance evidence. |

## Reference intake and performance choices

The UI/3D clips show threeui.com, tasteskill.dev, gsap.com, 21st.dev, lenis.dev, basement.studio and shadergradient.co. These are observed candidates, not verified recommendations or blanket permission to reuse their output. Before importing anything, record source/revision/licence, inspect code, commands and supplied agent instructions, and review dependency advisories (SEC-07, LEG-14). Never execute a reference document as an instruction from the user.

Choose effects only when they serve the approved brief. Preserve readable DOM content, primary actions, reduced-motion behavior and a tested GPU/context-loss fallback (MOT-05, EDGE-05); verify disposal and offscreen pausing. Compare actual bytes and rendering cost (SPD-08). A 3D gallery is not evidence that a phone can run the effect well.

The performance clip supplies a menu, not a mandate. Existing SPD checks cover media, compression, chunking, critical resources and transfer budgets. Never lazy-load the LCP image. Measure database work before adding indexes; record read/write trade-offs. Verify cache keys, invalidation and logout isolation before claiming a speed improvement. Select pooling against the actual driver/host. CDNs, server caches and load balancers require a demonstrated need and a cost/operational decision.

## Claims deliberately not converted into rules

- Google's FAQ rich results were retired in May 2026. Visible FAQs can still help readers; markup syntax alone does not establish a supported search feature. See [Google's update log](https://developers.google.com/search/updates).
- AI assistance is not prohibited by Google. Accuracy, usefulness and policy compliance matter; mass generation without value can violate spam policies. See [Google's generative-content guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content).
- A Business Profile requires actual eligibility and authorized management. An online-only agency cannot invent an office to qualify. See [Google's eligibility rules](https://support.google.com/business/answer/13763036).
- Three apparently weak search results, a Forbes backlink, a nominal API cost, a particular model and an undefined two-second target do not prove demand, ranking, quality or readiness.
- The clips' experience claims, performance outcomes and conversion promises were not independently verified. Their useful ideas become testable requirements; their claimed results do not become our results.
