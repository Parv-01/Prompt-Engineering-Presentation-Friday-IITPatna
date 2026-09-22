# Prompt Engineering, from Zero to Everything

An interactive, 40-slide research talk for Research Friday. It covers the history of prompting, the mathematics of tokens, attention and decoding, in-context learning theory, reasoning techniques, tools and agents, automatic prompt optimisation, reliability, prompt hacking, image prompting, reasoning models and context engineering. Every slide carries a full voiceover.

Inspired by the open-source [Learn Prompting](https://learnprompting.org/docs/introduction) guide by Sander Schulhoff and contributors.

Presenter: Parv Agarwal, JRA (Tech) 

Supervisor: Dr. Asif Ekbal, 

IIT Patna Lab: AI-NLP-ML Research Group

## Run it

It is a static site with no build step.

```bash
# any static server works
python -m http.server 8000
# open http://localhost:8000
```

Opening `index.html` directly from disk also works.

## Deploy on GitHub Pages

1. Create a repository, for example `prompting-talk`, and push this folder to the `main` branch.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**. The included workflow in `.github/workflows/pages.yml` publishes the site on every push.
   (Or choose **Deploy from a branch**, select `main` and `/ (root)`. The empty `.nojekyll` file keeps GitHub from processing the files.)
4. The talk will be live at `https://<your-username>.github.io/prompting-talk/`.

Link to a slide directly with a hash: `…/prompting-talk/#20` opens self-consistency.

## Presenting

| Key | Action |
|---|---|
| → Space PgDn | Next slide |
| ← PgUp | Previous slide |
| Home / End | First / last slide |
| N | Show the voiceover for this slide under the stage |
| G | Jump to a slide |
| T | Switch light and dark theme |
| F | Full screen |
| ? | Keyboard help |

Touch screens: swipe left or right. The faint controls in the top-right corner do the same things with a mouse.

**Offline:** fonts and KaTeX load from Google Fonts and cdnjs. If the venue has no internet, open the deck once beforehand so the browser caches them, or download KaTeX and the three font families into `assets/` and update the `<link>` tags.

## Interactive slides

All demos run in the browser. There are no API keys and no network calls, so nothing can fail live.

| Slide | Widget | What it shows |
|---|---|---|
| 5 | Timeline | Ten years of prompting history, 2013 to 2025 |
| 9 | Tokenizer | An illustrative sub-word splitter with token counts |
| 12 | Decoding | Temperature and top-p acting on next-token probabilities, with sampling |
| 13 | Prompt builder | Eight prompt components assembled into a live prompt |
| 19 | Technique playground | Standard, zero-shot CoT, few-shot CoT and self-consistency on one question |
| 20 | Voting calculator | Exact binomial accuracy plus a Monte Carlo simulation of scattered errors |
| 32 | Injection demo | Four defences against a classic prompt injection |
| 37 | Quiz | Three scenarios with reveal-on-click answers |

Model outputs in the playground and injection demo are scripted to illustrate typical behaviour. The slides say so.

## Files

```
index.html                 all 40 slides; voiceover lives in <aside class="notes">
assets/css/deck.css        design tokens and components
assets/js/deck.js          navigation, scaling, tokenized headings, voiceover drawer
assets/js/widgets.js       the eight interactive widgets
VOICEOVER.md               full script, generated from the slides
tools/extract_voiceover.py regenerates VOICEOVER.md after you edit notes
```

Edit a slide's notes in `index.html`, then run `python tools/extract_voiceover.py` so the script and the deck never drift apart.

---

## Design system: "The Context Window"

The talk treats itself as one long prompt. Two devices carry that idea, and everything else stays quiet.

1. **Tokenized headings.** Every heading is split into rough sub-word tokens with alternating violet and amber underlines, the way a model sees text. On entering a slide, one attention sweep passes across the tokens. This is the only automatic motion in the deck, and it is disabled when the system asks for reduced motion.
2. **The context bar.** One cell per slide at the bottom. Filled cells are tokens already in context; the amber cell is the current slide.

### Tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `--paper` | `#EDF1F5` | `#0E1624` | Slide background |
| `--paper-2` | `#E1E7EE` | `#16213A` | Recessed panels, consoles |
| `--ink` | `#0F1B2D` | `#E6ECF3` | Primary text |
| `--muted` | `#5B6B7F` | `#8C9CB0` | Captions, citations |
| `--rule` | `#C4CFDA` | `#2B3A55` | Hairlines, slider tracks |
| `--attn` | `#4B2BD6` | `#A493FF` | Attention: interactive elements, emphasis |
| `--heat` | `#FFB020` | `#FFC24A` | Heat: token boundaries and highlights only |

Type: **Bricolage Grotesque** for headings and UI, **Source Serif 4** for body text, **JetBrains Mono** only for text a model reads or writes. Scale at the 1600 × 900 canvas: 96 / 58 / 30 / 27 / 21 / 17 px. Spacing follows an 8 px scale. Radii: 3 px for tokens, 6 px for panels and controls.

### Components

| Component | Class | Use when | Notes |
|---|---|---|---|
| Console | `.console` | Showing a prompt or model output | Violet rule for input, amber (`.out`) for output. `.hl` highlights the words that matter. |
| Fact | `.fact` | Reporting a result from a paper | Always paired with a `.cite`. Only for real numbers. |
| Panel | `.panel` | Holding an interactive widget | Starts with an `h3` and a `.hint` saying what to do. |
| Equation | `.eq` | Display maths via KaTeX | Follow with `.eq-caption` to define symbols. |
| Segmented control | `.seg` | Picking one of a few modes | Uses `aria-pressed`. |
| Button | `.btn`, `.btn.quiet` | One clear action | Label starts with a verb: "Sample a token", "Show answer". |

### Copy rules

Buttons say exactly what happens ("Sample a token", "Show answer", then "Hide answer"). Hints say what to do, not what the widget is. Every simulated output is labelled "illustrative". Every number carries its source on the same slide. Sentence case throughout, no all-caps labels.

### Accessibility

Visible amber focus ring on every control, full keyboard navigation, `aria-live` regions on widget outputs, `aria-label` on tokenized headings so screen readers hear whole words, reduced-motion support, and contrast at or above WCAG AA for body text in both themes.

## Credits

Content draws on the Learn Prompting guide and bibliography, The Prompt Report (Schulhoff et al., 2024), and the primary papers listed on slide 39. Talk and design by Parv Agarwal.
