# Video lessons, fourth batch: local search at go-live

Source: Vaughn Major (Major Design), Instagram reel by majordesignagency, https://www.instagram.com/reel/DfKo9f9z1tu/, posted 2026-10-31, reviewed 2026-11-01. The reel is 59.7 s at 1080x1920. Reviewed from the caption, a transcript made on the reviewer's own computer (Whisper base.en, nothing uploaded) and frames at 1 per second, with the on-screen cards read at the full 1080 px source. No frames are stored here: this repository is public and the reel is someone else's work, so the link above is the reference. Times below are reel times.

Read this with the [first add-on](VIDEO_LESSONS_ADDON.md), the [second batch](VIDEO_LESSONS_BATCH2.md) and the [third batch](VIDEO_LESSONS_BATCH3.md). It adds no rows and changes no tier. It sets how the existing SEO rows apply to a local-business client and what must be done when the site goes live. The design reference is unchanged: in a clone run these lessons change copy, routes in scope and launch steps, never the reference's layout, type or motion. Two launch steps are added to `docs/LAUNCH_CHECKLIST.md` (§4 and §5 below) and a local-search block to `CLIENT_INPUT/brief.md`. Lines marked "the author's claim" are his account, not measured results.

**The author's result (0 to 8 s).** A card labelled "THE RESULT" shows a Google local result for "junk removal in evansville, wi". His client, Evansville Junk Removal (5.0, 3 reviews), is listed first, above A Guy With A Truck (5.0, 140 reviews) and Evansville Trash Disposal (5.0, 43 reviews). The author's claim is that reviews matter but are not the whole game. The card also reads "You manage this Business Profile", so the screenshot was taken while signed in as the profile's manager. Local results change with the searcher's location and account, so one screenshot does not measure a ranking. Never promise a ranking or a position to a client (SEO-13, SEO-16).

## 1. The H1 says what the business does and where (8 to 18 s)

**Observed.** A card labelled "ON-PAGE" shows the home hero. Its headline reads "Junk Removal Made Easy in Evansville, WI". Beside it are a "What We Haul" list, a call button with the phone number and a "Get a Free Quote" button. The author says the biggest headline on the site should come from real market research and say exactly where the business is and what it does.

**Rule for our builds.** For a local-business client, the home route's one H1 is the visible hero headline. It names the main service and the place served, in the words buyers actually search. Those words come from the dated buyer-intent sample (SEO-15): queries of the form "service in town", with the date and region recorded. Each service page's H1 names that service and the place. Keep it a plain sentence: no keyword stuffing, and no list of towns in a heading. In a clone run the H1 sits in the reference's own headline slot at its measured type scale. If the reference's display line is a single word or a brand mark, the H1 is the nearest visible headline that can carry the sentence, never a hidden heading. In template mode the H1 holds template copy, listed as a content gap, until the client's facts arrive.

**Rows.** SEO-15 (dated query sample), SEO-01 (the title and description carry the same service and place), A11Y-04 (one H1 per route by convention), SEO-04 (real, readable text), CNT-04 and CNT-11 (no placeholder in a live H1).

**Evidence to record.** The H1 of every route, taken from the built HTML, beside its title and description, and the dated query sample each H1 came from.

## 2. One page for every service (18 to 23 s)

**Observed.** A service page card titled "Couches, mattresses & more" ("gone in one trip"). It shows a real photo of the client's truck, a list of the items taken and a quote button. The author says to give every service its own page so Google knows the business offers it and ranks it for it.

**Rule for our builds.** Make one route for each service the client actually sells, taken from the approved service list in the brief. Each page gets its own copy: what the service covers, where, how it is quoted, and a real job photo when the client has one. Link each page from the Services page and list it in the sitemap. Never make a page for a service the client does not sell, and never make near-duplicate pages per town (SEO-15). In a clone run, the service pages use a layout measured from the reference: one of its deeper routes or its detail template, under the scope rule in prompt §1 (the client's copy has pages the landing route cannot carry). One reference layout carries every service page with different copy, and no layout is invented. Because every service page is the same template filled with different copy, the extra cost is copy and checks, not design. How many service pages the package includes is the owner's decision, and the written offer states it.

**Rows.** SEO-15, SEO-01, SEO-08 (links reach each page), SEO-10 (every service page is in the sitemap), A11Y-04, CNT-04, CNT-11.

**Evidence to record.** The route list checked one to one against the brief's service list. For each page: its H1, title and description, the internal links that reach it, and its sitemap entry.

## 3. Questions and answers on every service page (23 to 35 s)

**Observed.** A card titled "Junk Removal Questions, Answered" shows three questions: whether estimates are free, which areas are served (with the nearby towns named), and which items are taken. The author says to fill these with the most common objections customers raise about that service. The author's claim is that Google shows these answers in search results, and that customers get their questions answered before the phone call.

**Rule for our builds.** Each service page ends with 3 to 6 questions and answers drawn from what this client's customers actually ask. Sources:
- the client's own list
- their call notes and reviews
- the related questions in the dated search sample

Answer each with approved facts only. The questions and answers are real text on the page, in a native disclosure element or the reference's own disclosure pattern, and readable without JavaScript. Structured data is optional and is never sold as a search feature. In August 2023 Google limited FAQ rich results to well-known government and health sites (Search Central blog, "Changes to HowTo and FAQ rich results"), and later reports say they are gone entirely (SEO-11). The value is the answer on the page and the objection settled before the call. In a clone run, the FAQ uses a disclosure or list pattern measured from the reference. If the reference has none, it uses the reference's own text and list styles, and the addition is recorded as a fidelity exception.

**Rows.** SEO-11, CNT-04 (approved facts), UXF-08 (real text), SEO-04, A11Y-05 (keyboard operation).

**Evidence to record.** Each page's questions with their source (the client, a review, or the dated search sample), the client's approval, a keyboard capture and a no-script capture of the block, and the JSON-LD parse if markup is used.

## 4. Sitemap submitted, then every page checked as indexed (35 to 49 s)

**Observed.** A card labelled "TECHNICAL" shows the Search Console "Submitted sitemaps" table. The row reads `https://evansvillejunkremoval.net/sitemap.xml`, type Sitemap, submitted Sep 23, 2026, last read Sep 23, 2026, status Success. The next card shows "Indexed pages" with the note "These pages can be served on Google". The author says most web builders skip this step, and that a page Google has not indexed does not exist in search.

**Rule at go-live.** After the controlled cutover and the live checks, the owner works with the client's verified Search Console property:
1. Submit the sitemap. Record its status and its "last read" date.
2. The same day, run URL Inspection on every sitemap URL on the live domain. Request indexing for each route not yet indexed.
3. At the 7-day review (OPS-08) and again at two weeks (SEO-13), read the Pages report. Record each route as indexed, or give the reason it is not (for example discovered or crawled but not indexed, a duplicate canonical, or excluded by noindex), and fix every technical cause.

A check that is not yet due is listed as pending, never as passed. Indexing is never guaranteed and never promised to the client.

**Rows.** SEO-10, SEO-13, SEO-02 (production is indexable only when CLIENT-COMPLETE), SEO-07 (one canonical host), OPS-08.

**Evidence to record.** Dated captures or exports of the Sitemaps report, the URL Inspection result for every route on launch day, and the Pages report per route on day 7 and day 14, with each unindexed route's reason and fix.

## 5. Google Business Profile completed at go-live (49 to 59.7 s)

**Observed.** A card labelled "GOOGLE BUSINESS PROFILE" shows the Services list: the primary category "Junk removal service", then Yard Waste Removal, Junk Removal, Appliance Removal, Small Electronics Recycling, Construction Debris Removal and Property Cleanouts. Each service has its own short description; the Junk Removal one starts "Same-day and next-day junk removal for homes and businesses in Evansville and Rock Cou...". A later card shows the photos: a cover, the logo and several real job photos. The author says every service needs a real description written for search, that the business should post every week, and that it should add real job photos. The reel ends mid-sentence.

**Rule at go-live.** For a local-business client that has a Business Profile, or is eligible for one, SEO-16 is in scope by default. The handover prepares a profile pack for the client or the owner to apply in the client-owned profile:
- the website link set to the canonical URL
- the primary category, and a service list that matches the site's service pages one to one
- for each service, a plain description naming the service and the area, within the profile editor's own character counter
- the photo list: the client's own job photos, a cover and the logo
- the first four weekly posts, drafted, each tied to a real job or a service page

Generated pictures are never uploaded as job photos. No review is invented, bought or filtered. After the first month, weekly posting belongs to the client and is written into `docs/MAINTENANCE.md` (DEL-13); otherwise it is quoted as a separate service. Preparing the pack does not authorize posting: the client or the owner publishes.

**Rows.** SEO-16, SEO-07 (the profile links to the canonical URL), SEO-14 (any link from the site to the profile answers), CNT-04, DEL-13.

**Evidence to record.** The profile pack in the handover (services, descriptions, photo list, four posts), the owner's dated record of what was applied and when, and a dated view of the live profile showing the website link and the services.

## Summary

| Lesson | When | Rows | Evidence |
| --- | --- | --- | --- |
| H1 names the service and the place (§1) | Build, filled with client facts before CLIENT-COMPLETE | SEO-15, SEO-01, A11Y-04, SEO-04, CNT-04, CNT-11 | H1, title and description per route; dated query sample |
| One page per service (§2) | Build | SEO-15, SEO-01, SEO-08, SEO-10, A11Y-04, CNT-04, CNT-11 | Routes matched to the service list; links and sitemap entries |
| Questions and answers per service page (§3) | Build | SEO-11, CNT-04, UXF-08, SEO-04, A11Y-05 | Questions with sources and approval; keyboard and no-script captures |
| Sitemap submitted and every page indexed (§4) | Go-live, day 7, day 14 | SEO-10, SEO-13, SEO-02, SEO-07, OPS-08 | Sitemaps report; URL Inspection per route; Pages report per route |
| Business Profile pack (§5) | Go-live, then weekly by the client | SEO-16, SEO-07, SEO-14, CNT-04, DEL-13 | Profile pack; dated record of what was applied; live profile view |

## Gaps

- The reel does not show how the headline research was done: no tool, query list or search volume. Our rule uses the dated sample of SEO-15 instead and invents no search volume.
- The ranking result is one screenshot taken by the profile's manager. It is the author's claim, not a measurement.
- No row sets the number of service pages or of questions per page. The numbers above are our build rules, recorded per site.
- Third-party guides give a 300-character limit for a profile service description, but no Google source was found, so the profile editor's own counter decides.
- Weekly posting is ongoing work with no row. It lives in the maintenance guide or a quoted service, never in the launch approval.
