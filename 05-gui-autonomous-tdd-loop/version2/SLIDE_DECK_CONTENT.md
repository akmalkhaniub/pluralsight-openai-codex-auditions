# Slide Deck Content — v2

File: `Audition Slides - Akmal Khan - TDD v2.pptx` (8 slides; the Pluralsight template is kept). Each slide's speaker notes contain its narration.
Every content slide builds on click, so something on screen changes every 10–20 seconds. Callouts are yellow for "watch this" and pink or blue for key facts.

| # | Time | Layout | Visual | Click builds |
|---|------|--------|--------|--------------|
| 1 | 0:00–0:25 | Course Module title | Title; circular headshot beside Akmal Khan, Senior Full Stack AI Architect | none |
| 2 | 0:25–1:00 | Overview (gradient panel) | **Checkout receipt** showing Total $100.00 in red, with the total circled in red and a pink **callout "Should be $90.00"** pointing at it; a 3-step chevron flow (Specify → Delegate → Verify) | 1 receipt · 2 callout + hook line · 3–5 chevrons one at a time + takeaway |
| 3 | 1:00–1:30 | Comparison | **Boundary table**: $99.99, $100.00, $100.01, $100.05, each with a tag (below / at / above / half-cent). The $100 row is highlighted | 1 row · 2 highlight + inline tag "← >= includes $100" · 3 row · 4 row + inline note "← 90.045 rounds half up" |
| 4 | 1:30–2:00 | Title left / content right | **TDD cycle diagram**: Red, Green and Refactor circles with arrows and a "run tests" hub | 1 RED · 2 arrow + GREEN · 3 arrow + REFACTOR · 4 arrow + hub · 5 banner "Never saw it fail?…" |
| 5 | 2:00–2:30 | Title left / content right | **The actual prompt** as a dark code block (scope lines in yellow, command in green) with coloured bars beside the RULE / SCOPE / PROOF lines and matching labels | 1 code · 2 RULE · 3 SCOPE · 4 PROOF + "A request, not a lock" |
| 6 | 2:30–3:00 | Demo (blue panel) | **Numbered roadmap**: Red → Prompt → Review → Green → Refactor? (improve only if useful), with colour-coded circles | one step per click |
| 7 | 6:30–6:55 | Summary | Four short "why it matters" bullets | one bullet per click |
| 8 | 6:55–7:15 | Title left / content right | Large question "An order of -$5.00 arrives. What should calculate_total return?" + chevron flow Decide → RED → GREEN | 1 question · 2–4 chevrons |

## Before recording
- Open the deck in PowerPoint and check the animations in Slide Show mode (they were built in code and tested in LibreOffice, not PowerPoint).
- Check fonts. The prompt and prices use Consolas; if it is missing, Courier New is a fine substitute.
- Headshot: Akmal pic 3 (its warm background suits the pink template), cropped to a circle with a pink ring.
- Demo callouts (8 errors, >=, ROUND_HALF_UP, 8 OK, Round once, Covered / Not yet) are added in video editing, as listed in the script.

## Annotation styles (varied on purpose)
- Slide 2: red ring around the wrong total + speech-bubble callout
- Slide 3: row highlight + inline arrow tags
- Slide 4: banner
- Slide 5: coloured margin bars + side labels
- Demo: short on-screen callouts added in video editing
