# Example CLIENT_INPUT

A starter set of the files the prompt looks for (see "Inputs" in `prompt/PROMPT_awwwards_clone_swap_v6.md`).
Copy this folder next to the project you are building, rename it `CLIENT_INPUT`, and replace the
example text with the client's real details.

Every file is optional. The prompt never stops because something is missing: gaps are filled from the
content ladder (client, drafted from the brief, CC0 stock, marked placeholder). The more of these the
client fills, the less placeholder content ships and the sooner the site can be marked `CLIENT-COMPLETE`.

| File | What the client gives you | What happens if it is missing |
|---|---|---|
| `brief.md` | What the business does and how, audience, tone, niche, languages, domain, competitors to avoid | The agent picks a target on its own; copy slots use placeholder text |
| `copy.md` or `copy.json` | Any copy the client already wrote (headings, about-us, services, testimonials) | Copy is drafted from the brief, or left as a marked placeholder |
| `images/` + `images.csv` | Photos and video, with alt text, focal point, credit and licence | CC0 stock where it fits, else marked placeholder images |
| `logo/` | The client's own logo (SVG, PNG or WebP) | A text wordmark of the brand name |
| `brand.md` | Brand colours, typefaces, and `design_shift` | A palette and typefaces are derived (the default) |
| `fonts/` | Licensed font files, if the client owns any | Open-licensed fonts are used |
| `rights.md` | The client's statement that they own or license everything supplied | Content status stays `CONTENT-PENDING` |
| `legal.md` | Jurisdiction, legal entity, forms, email provider, analytics, retention | The minimum is assumed (no accounts, payments, analytics or cookies) |

Rules the prompt enforces, so tell the client up front:
- Testimonials, client names, statistics and awards are only ever the client's own. They are never drafted or stocked.
- The client's own copy is never edited, shortened or "improved". If it does not fit a box, it is kept and the problem is reported.
- Do not commit the real `CLIENT_INPUT` to a public repository (photos can carry GPS data).
