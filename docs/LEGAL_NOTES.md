# Legal notes (United States)

This is research for the operator, not legal advice, and the author is not a lawyer. It was done on 2026-10-01
for a client base in the United States. Nothing in the kit makes a layout-faithful clone safe from a claim.
Anyone can file a suit; the question is exposure. Use this to prepare questions for a US IP attorney.

## Scope of these notes

Replacing content does not establish permission to reproduce a reference design. This historical research identifies issues for project-specific counsel review; it does not quantify claim strength, litigation likelihood or takedown probability. Active checklist rules and its 2026-10-02 audit supersede conflicting delivery instructions below.

## What the swap removes

The US Copyright Office (Circular 66) lists what is protectable on a website: text, photographs, illustrations and
other two-dimensional artwork, music, and audiovisual works. The kit replaces all of these, and the leak gates
(finish gates 6 and 13, CNT-02, CNT-14) check that nothing of the original's text, images, video, fonts, logo, code
or domain ships.

## What remains, and how strong each claim is

1. **Layout, format and "look and feel".** Weaker than most people assume.
   - Circular 66 lists "the layout, format, or 'look and feel' of a web page" as uncopyrightable, says a
     registration does not cover the general layout or format of a web page, and says the Office generally refuses
     claims made only of style sheet languages such as CSS.
   - A website can still be registered as a compilation if there is creative selection, coordination or
     arrangement of its content, or creative overall hierarchy.
   - That protection is thin (Feist v. Rural Telephone limits compilation protection to the original selection and
     arrangement). In Apple v. Microsoft (9th Cir. 1994) the court held that infringement of a thinly protected
     interface needs works that are "virtually identical", and Apple lost most claims because windows, icons and
     menus were generic ideas. An award-winning composition is more original than generic interface concepts, and
     near-identical copying is the kit's design goal. No US decision on a layout-only clone of such a site was found,
     either way.
2. **Trade dress (Lanham Act section 43(a)).** The party claiming unregistered trade dress must prove it is not
   functional (15 U.S.C. 1125(a)(3)). Product design needs secondary meaning to be protected (Wal-Mart v. Samara).
   Likelihood of confusion is required. It is strongest for a famous brand in the same market, which is why the
   prompt excludes the client's own industry and market from target choice.
3. **Design patents.** The USPTO allows design patents for icons and graphical user interfaces shown on a display
   (MPEP 1504). Protection does not depend on proof of copying. Most studios hold none, and checking a given
   studio is not cheap.
4. **Embedded art and animation.** Illustrations, video, audio and audiovisual works stay protected. The prompt
   draws its own icons and re-authors effects from measured values, but closely recreating a distinctive visual
   effect is the most exposed part for motion-heavy references.
5. **Code.** Written fresh from measured values. Measured values are facts. Low exposure.
6. **Reading and saving the original.** The agent saves the original's text and images privately for measurement.
   That is reproduction, even if private. It stays in `WS`, is never published, and can be deleted after client
   acceptance.
7. **Awwwards' terms.** Featured sites "remain the intellectual property of their creators". An award is not a
   licence.

## The practical route: a DMCA takedown

Under 17 U.S.C. 512 an owner can send a notice to your client's host. The host must act expeditiously to remove
or disable the material to keep its safe harbour, so the site can go down without any lawsuit. A counter-notice is
made under penalty of perjury and consents to a federal district court's jurisdiction. The host restores the
material not less than 10 nor more than 14 business days after receiving it, unless the claimant first notifies the
host that it has filed suit. A registrar acts under its own terms, not section 512. The kit's LEG-18 requires a
written response plan before launch.

## Other US exposure for client sites

- **ADA.** The Department of Justice says the ADA applies to business websites and points to WCAG and the
  Section 508 Standards as helpful guidance, with no single mandated technical standard for private businesses.
  The kit requires accessibility fixes in every deployed build as delivery policy, without ranking
  accessibility claims against design-rights claims or treating WCAG checks as a legal guarantee. How often such claims are filed was not
  checked.
- **FTC testimonials rule (effective 2024-10-21).** Fake or false consumer reviews and testimonials, including
  AI-generated ones, are prohibited, and it reaches agencies. The kit never drafts, stocks or paraphrases a testimonial.
- **AI-written code.** The Copyright Office's January 2025 report (Part 2) concludes that copyright does not extend
  to purely AI-generated material, that prompts alone do not give sufficient control, and that human selection,
  coordination, arrangement and creative modification can be protected. This does not raise infringement exposure,
  but a claim that the client owns the copyright in the delivered code is shaky. SEC-10 and DEL-05 are worded for it.
- **Already covered by checklist rows:** CAN-SPAM, Global Privacy Control and California rules, COPPA, DMCA agent
  safe-harbor applicability and agent registration where relevant, cookie consent, third-party font and licence compliance.

## Verified and not verified

| Source | How it was read |
|---|---|
| US Copyright Office Circulars 33 and 66, AI copyrightability report Part 2 | Primary PDFs, text extracted and read |
| 15 U.S.C. 1125(a)(3) | Primary (Cornell LII) |
| Wal-Mart v. Samara | Cornell LII Supreme Court page |
| 17 U.S.C. 512 | copyright.gov page and the statute text (reviewer) |
| USPTO MPEP 1504 on design patents for GUIs | Primary |
| FTC consumer reviews and testimonials rule | FTC business guidance page |
| DOJ ADA web guidance | Primary (ada.gov) |
| Awwwards terms | Primary (awwwards.com) |
| Feist; Apple v. Microsoft | Secondary summaries only (the primary pages blocked the fetch) |
| Trade dress for websites | Law-firm summaries only |
| EU design reform (animation and GUIs in the definition of design) | Search summaries only; not relevant to a US client base |
| Frequency of ADA web claims | Not checked |
| Any court decision on a layout-only clone of an award-winning site | None found; absence is not proof |

## Risk-reducing measures built into the kit

- Reference chosen outside the client's own industry and market, and preferably one whose studio allows reuse.
- Nothing of the original's text, images, video, fonts, logo, code or domain ships (leak gates, git-history checks).
- The brand shift (derived or the client's palette and typefaces) makes the result a little less like the reference.
- Own code, own icons, effects re-authored from measured values.
- Provenance file records what was measured, what was not copied, and who directed the AI-written code.
- Launch steps for the rights question, counsel review of the draft legal pages (LEG-17) and a takedown response
  plan (LEG-18).

## What would reduce the risk further

1. Written permission from the reference's creators. Confirm that permission covers the intended use, the relevant rights and the granting party's authority. Or choose
   references from studios that allow reuse, or from properly licensed templates.
2. Avoid highly distinctive or famous references, and those built around custom illustrations or shader art.
3. Book an hour with a US IP attorney on this exact workflow: client contract language, warranties and indemnity
   limits, who bears the cost of a takedown, and whether media or IP insurance fits.
4. Keep `docs/PROVENANCE.md` evidence for every project; it supports independent creation of the code.

## Questions for counsel

- Is a near-identical arrangement of an award-winning page's layout, hierarchy and motion, with all content replaced,
  an infringing derivative work, and how much does a palette and typeface change help?
- Could the reference's overall look be trade dress in our market, and does the client's industry choice matter?
- What should the client contract say about reference-based design, content warranties and indemnities?
- How should we answer a section 512 notice, and when is a counter-notice worth the jurisdiction consent?
- Who owns copyright in AI-written code delivered to a client, and how should the LICENSE be worded?
