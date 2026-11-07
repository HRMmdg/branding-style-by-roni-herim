---
name: branding-style-by-roni-herim
description: Branding Style by Roni Herim. Builds brand color systems with the 2+1 Mood & Character rule (two quiet tones plus one loud accent) and applies them to Instagram carousels, logos, UI/UX, websites, posters, brochures and any branded visual, with verified WCAG contrast and an anti-AI-slop check. Use whenever the user asks for brand colors, a palette, a brand look or style, colors for any design, wants a style pulled from screenshots, links or a brand book, or wants a design to stop looking generic or AI-made.
---

# Branding Style by Roni Herim

## Overview

This skill turns a brief, an existing set of colors, or reference material (screenshots, links, uploaded brand books) into a brand color system built on the **2+1 rule**. It then applies that system to whatever is being designed: carousels, logos, UI/UX, websites, posters, brochures and other branded material. Every output is checked for accessibility with real contrast numbers and screened for the tells of generic AI-made design.

The rule in one line: **two quiet colors set the mood; one loud, unexpected color does the work.** Restraint is what makes a brand recognisable, and the accent only works because it is scarce, so the whole system protects that scarcity.

| Role | Share of a layout | Job |
|---|---|---|
| **Tone 1 (Primary)** | ~60% | Dominant atmosphere: large surfaces |
| **Tone 2 (Secondary)** | ~30% | Second layer in the same mood; headings, panels, imagery tint |
| **Character (Accent)** | ~10% or less | Personality and focus: CTAs, one highlighted word, logo detail, key UI states |

60-30-10 is a starting ratio, not a law. In product UI (dashboards, apps), neutrals usually take far more space; real products run closer to 90/8/2. Keep the order of dominance, but let the accent shrink rather than grow.

## Operating Rules

**"Quiet" means the two tones belong together, not that they are light.** A tone pair follows one of two patterns, in light or dark versions alike:
- **Neutral + one hue:** white + sky blue, near-black + orange, black + indigo.
- **Two shades of one hue family:** dark sapphire + bright ocean blue, deep forest + jungle green.

Two unrelated hues as the tones (for example purple + blue) are not quiet and compete with the accent.

**"Loud" means the character color breaks the mood.** Choose it from the opposite side of the color wheel: a hue gap of about **90–180°** from the main tone, usually the opposite temperature (warm against cool). Loudness comes mostly from that hue jump plus a strong, clean color. Raw saturation numbers matter less: a fully saturated electric blue cannot be out-saturated. The one accepted exception is a neon or acid version of a nearby hue (acid lime on tangerine), which works because it is so much more electric than the tone.

**What counts toward the three colors.** A tone may itself be a neutral (white or near-black), and then it counts as one of the three. Outside the count are:
- *Functional neutrals*: the text and surface greys needed to make a UI work, ideally tinted slightly toward Tone 1's hue so they feel related.
- *Shades and tints* of the core colors (hover states, borders, subtle backgrounds), as long as the hue stays the same.
- *Semantic status colors* (error red, success green, warning amber): app UI only, listed separately, never decorative. Shift their hue to fit, but keep their saturation and brightness close to the brand color so they don't feel pasted on.

A fourth decorative hue is never allowed. If the user wants one, explain that it dilutes the accent and offer a tint or shade of an existing color instead.

**Every hex value must be real and exact.** Give HEX and RGB for each color.

**Numbers come from the scripts, not estimation.** Run `contrast_check.py` for every contrast you report and `palette_check.py` for every palette you propose (see Helper Scripts). Eyeballed contrast is regularly wrong by enough to fail WCAG, and users ship these colors into real products.

**Colors taken from images come from the extractor whenever the file is on disk.** Hex codes printed on screenshots or in reels can be wrong. In testing, two of nine printed codes did not match the color shown, so measure the swatch rather than trusting the label. If you can only see an image (no file path), label any hex values "approximate, from visual inspection".

**Locked colors stay exact.** If the user says a color must stay, build around it. If it fails contrast, keep it and restrict where it can be used (for example "large text and icons only") rather than changing it silently.

**Frame color psychology as association, not fact,** and tie it to the specific audience and culture.

**When the brief is thin, ask before building, at most 3 questions in one message:** the audience, the feeling the brand should create, and where the colors will mainly appear. Also ask about any colors that must stay. If the user says to go ahead, make sensible assumptions and state them in section 1.

**When the user's reference material conflicts with the 2+1 rule,** the rule wins. Say in one line which colors were kept, which became tints or neutrals, and which were dropped.

## Workflow

### Step 1: Gather and analyse inputs

- **Written brief:** pull out the audience, product, desired emotion, competitors, and where the colors will appear.
- **Uploaded documents (PDF, mini-book, brand guide):** extract the color rules, audience descriptions and dos and don'ts. List the 3–6 rules you will apply before building, so the user can correct any misreading.
- **Screenshots or images:** run `extract_colors.py`. Separate brand colors from content colors (skin, sky, photos). Ignore fringe colors under ~1%; they are anti-aliasing blends.
- **Links:**
  - A plain page fetch of YouTube returns only text, never video frames. Instagram usually needs a login.
  - If a signed-in browser is available, use it.
  - Otherwise ask for 2–4 screenshots. Never invent colors for a page you could not see.
- **An existing palette:** assign every color a fate: Tone 1, Tone 2, Character, functional neutral, tint, or drop.

### Step 2: Profile the audience and the competition

Define:
- Demographics and psychographics
- Viewing context: phone feed, desktop, print. Small phone screens punish low contrast.
- Cultural notes for the main markets
- An emotional goal in 2–3 words

Build a quick mood board in words: the product, the competitors, the vibe. Then look at what the competitors use, and either refine that color family or deliberately go opposite to stand apart. The Color Association Reference below is a starting point.

### Step 3: Build the 2+1 palette

1. **Tone 1:** start from one good mid-strength color that carries the core emotion. If the brand already has a color, start there.
2. **Tone 2:** choose a neutral partner or a lighter/darker shade from the same hue family. It must differ in lightness enough to read as a separate layer.
3. **Character:** take Tone 1's hue and move 90–180° around the wheel. Use the true complement for maximum punch, or a split-complementary neighbour (one step to either side of the complement) for high contrast with a little less tension. Then pick a clean, strong version of that hue.
4. **Size the accent by its brightness.** Light, bright hues (yellow, lime, mint, cyan) dominate the eye and need *less* area; dark hues (blue, violet) can take more. Itten calls this the contrast of extension.
5. **Run `palette_check.py`.** Resolve every FLAG or explain why the exception is intentional.
6. **Pick the functional neutrals:** a near-white and a near-black rather than pure #FFFFFF / #000000, tinted toward Tone 1. Warm palettes get warm off-whites and brown-blacks; cool palettes get cool greys.
7. **Judge the accent in place, never as an isolated swatch.** The same color looks different depending on what surrounds it (Albers). Picture or render it on Tone 1 and on Tone 2 before deciding.

### Step 4: Verify contrast

Run `contrast_check.py` on at least these pairs:
- Body text on Tone 1, and on Tone 2
- The button label on the Character color
- The Character color on Tone 1, and on Tone 2 (UI target 3:1)

On a failure, re-run with `--fix`, keep the hue, adjust only lightness, and report "original → adjusted". Then re-check every pair that uses the adjusted color.

**Watch for vibration.** Two strongly contrasting hues of similar lightness (for example red text on blue) shimmer at the edge and tire the eye, even when the contrast ratio looks acceptable. Keep text and its background clearly apart in lightness.

**Grayscale test:** if the palette collapses into one grey when desaturated, it relies on hue alone and will fail color-blind users. The 3:1 accent target guards against this.

### Step 5: Apply to the medium

Use the rules in **Applying the Style by Medium** for whatever is being designed. If the user hasn't named a medium, give the UI/UX mapping plus one line on social and print use.

### Step 6: Run the anti-slop check

Go through the **Anti-AI-Slop Checklist** for the palette and any design you produce or review. Fix every hit, or state why it is intentional.

### Step 7: Present

Use the output format below. If inline visuals are available, show a swatch strip of the core colors and neutrals after section 2, and ideally a mini mock-up in the target medium (a hero section, a carousel cover, a poster thumbnail) so the user judges the accent in context.

## Output Format

### 1. Audience & Psychological Profile
- **Target Audience:** [persona: demographics + psychographics + viewing context]
- **Core Emotional Goal:** [2–3 words + one sentence on the atmosphere]
- **Competitive Angle:** [what competitors use and how this palette stands apart]
- **Assumptions:** [only if you had to assume anything]

### 2. The 2+1 Palette Definition
- **Tone Color 1 (Primary):** `#HEX` · `rgb(r, g, b)` — *role and psychological purpose*
- **Tone Color 2 (Secondary):** `#HEX` · `rgb(r, g, b)` — *role and how it partners Tone 1*
- **Character Color (Accent/CTA):** `#HEX` · `rgb(r, g, b)` — *the personality it injects*
- **Pattern check:** tone pattern (neutral + hue / one hue family) · hue gap to accent (X°) · result of `palette_check.py`
- **Functional Neutrals:** `#HEX` (light) · `#HEX` (dark) — *not counted in 2+1*

### 3. Application Mapping
Cover the medium the user asked for (carousel, poster, brochure and so on) using the Applying the Style by Medium rules. For digital products and websites, include:
- **Logo Usage:** mark vs. wordmark colors; a one-color version; behaviour on Tone 1 vs. on white. A logo should still work in one color and in black and white.
- **UI Hierarchy (60-30-10):** element-by-element assignment, covering:
  - background, surfaces/cards, borders
  - headings, body text, subtext
  - primary button, secondary button, links, highlights
  - hover/pressed states (as shades)
- **Dark Mode (only if relevant):** see the Dark Mode rules.
- **Accessibility Check:**

| Pair | Ratio | AA text (4.5) | AA large/UI (3.0) |
|---|---|---|---|
| Body text on Tone 1 | x.xx:1 | ✅/❌ | ✅/❌ |

Follow the table with one line on usage restrictions, for example "accent text only at 24px+".

- **Anti-Slop Check:** "passed", or the hits found and how they were fixed.

### 4. Design Tokens

```css
:root {
  --color-tone-1: #......;
  --color-tone-2: #......;
  --color-character: #......;
  --color-neutral-light: #......;
  --color-neutral-dark: #......;
}
```

For print work, add a line noting that CMYK/Pantone equivalents must be specified and proofed, because screen colors (especially neons) shift or dull in print.

## Applying the Style by Medium

The 2+1 system stays the same everywhere; only the proportions and placement change. On every medium, the accent marks the single thing you want noticed first.

### Instagram carousels
- **Cover slide:** Tone 1 background. The headline goes in the light or dark tone with the strongest contrast. Put the Character color on one word or one graphic element that earns the swipe, never on the whole headline.
- **Value slides:** keep the same background tone throughout. Alternating Tone 1 / Tone 2 per slide is fine, but don't introduce new colors. Allow at most one accent element per slide, such as a key number, an arrow or an underline.
- **Final slide:** the CTA ("save", "follow", "book now") goes in the Character color. It is the one place the accent may grow to a button-sized block.
- Feeds are viewed on phones, often in sunlight. Keep body text at 4.5:1 or higher, and avoid thin type on saturated backgrounds.
- Check the grid view: neighbouring posts should read as one brand, so the same Tone 1 / Tone 2 rhythm should repeat across posts.

### Logos
- The logo must work in **one color**, in **black and white**, and **reversed** (light on Tone 1). Design those versions first and add color last.
- Use the Character color as a detail (a dot, one letter, a cut or a symbol), not as the whole mark. The detail is what people remember.
- Check it small, at favicon and profile-picture size. Thin accent details vanish below about 32px, so they need a simplified version.
- Test it on Tone 1, Tone 2, white and a photo. A logo that only works on one background is not finished.

### UI/UX and websites
- Follow the 60-30-10 hierarchy and the Tones, Neutrals and Dark Mode rules. Marketing pages can use a bold Tone 1 hero; app screens sit on neutrals.
- Keep the accent for the primary action on each screen. If two buttons are both in the accent, one of them is wrong.

### Posters and flyers
- A poster is read from a distance, in seconds. Aim for one focal point in the Character color, one dominant headline, and everything else quiet.
- Use large type and high contrast: target 7:1 for key text, because posters meet bad light and fast passers-by.
- Size the accent by its brightness (contrast of extension): a lime or yellow accent can be tiny and still dominate.

### Brochures and print
- **Screen colors shift in print.** Neons and electric blues can't be reproduced in standard CMYK and will dull. Specify CMYK and Pantone (spot) values, request a printed proof, and warn the user if the accent is out of the print gamut.
- **Paper changes color.** Uncoated stock absorbs ink and makes everything darker and softer; coated stock keeps colors cleaner. Ask which stock is planned when it matters.
- Body text goes in a near-black on the paper color, never in the accent. Use the accent for headings, callouts, pull quotes and the contact/CTA panel.
- Keep the same tone rhythm across spreads, so the brochure feels like one brand from cover to back.

### Any other branded material
Merch, packaging, slides and signage follow the same logic. Tone 1 owns the large areas, Tone 2 supports, and the Character color marks the one thing to notice. Packaging ranges can swap the accent per product while keeping the two tones fixed, so the range still reads as one brand.

## Anti-AI-Slop Checklist

AI tools tend to fall back on the same defaults, so their designs all look alike. Viewers now spot these defaults instantly and read them as cheap or generic. Run this check on every palette and every design you produce or review. A hit isn't automatically wrong, but it must be a deliberate choice, never a default.

### Color tells
- **Purple-to-blue or indigo gradients:** the number-one tell. They trace back to framework defaults (Tailwind's indigo) that AI tools copied everywhere.
- **Purple or indigo added for no brand reason**, on buttons, blobs and glows.
- **Glowing blur blobs** or mesh-gradient backgrounds behind the hero.
- **Rainbow UI**, where every card or section gets its own color.
- **Gradient text** on headlines and gradient borders on cards.

### Layout tells
- **The default SaaS page:** a centered hero, then a row of 3 feature cards, then logos, then testimonials, then pricing.
- **A colored bar on the left edge of every card.**
- **Rounded cards with soft drop shadows everywhere**, all with the same radius and the same shadow.
- **Too much crammed in:** every section full and no breathing room. Strong designs leave space.
- **Everything centered.** Real hierarchy uses alignment, scale and asymmetry.

### Type and icon tells
- **Inter (or a system font) for everything**, or the usual "creative" swap to Space Grotesk. Pick a typeface that fits the brand's voice.
- **The default icon set** (generic line icons) at large sizes, next to every item.
- **Emojis in headings, bullets and buttons:** one of the fastest ways to make a design look cheap.
- **Sparkle ✨ icons** used to signal "AI" or "magic".

### Content and imagery tells
- **Generic taglines** like "Empowering your tomorrow", "Unlock your potential" or "Elevate your experience".
- **Fake testimonials** and invented statistics.
- **Stock-perfect AI imagery** with plastic skin, symmetric smiles, impossible lighting or mangled hands and text.

### How to escape the defaults
1. **Start from references, not a blank prompt.** Use real designs the user admires (screenshots, sites, the brand book) and extract their colors with `extract_colors.py`.
2. **Lock the system first:** the 2+1 colors, typefaces, spacing scale, corner radius, shadow style and icon set. Do this before designing any screen or slide.
3. **Make one unexpected but justified choice:** the Character color, a distinctive typeface, an asymmetric layout or real photography.
4. **Edit down:** remove decoration that carries no meaning, such as emojis, extra gradients or a third card added just to fill a row.
5. **Re-run this checklist** on the result before presenting.

## Design Rules Library

These rules apply while building and reviewing. Sources are listed at the end.

### Accent behaviour
- The accent is for things you want people to act on or notice: CTAs, a highlighted word, a price, one small card, a logo detail.
- Pick one dominant color first. The other colors are found from it through color-wheel harmonies, and used only as accents or small details.
- Use few colors. If something isn't important, it doesn't get a color; a simple border or a neutral shade often beats a colored fill.
- The more important a button, the stronger its color; secondary buttons stay neutral.

### Tones, neutrals and shades
- Think of each color as a ramp of shades, not a single swatch. Keep each ramp to about 10 shades at most, and tweak existing shades before adding new ones.
- For ramp endpoints, a dark shade near HSB S90–100 / B20–30 suits text, and a light shade near S5–10 / B95–100 suits tinted backgrounds (for example an alert box).
- Neutral text in light mode:
  - Important text around 10–12% lightness, not pure black.
  - Body text around 15–20%.
  - Subtext around 30–40%.
- On dark backgrounds, headings should not be pure 100% white either; a slightly muted light grey is easier on the eye.
- Borders should define an edge without shouting. A light grey at roughly 85% lightness usually beats a black or saturated outline.
- Saturated or bright colors almost never work as the background of *product UI*. On marketing pages and hero sections a bold Tone 1 background can work, but app screens should sit on neutrals.

### Dark mode
- Don't invert the light palette. Build dark mode on purpose.
- Dark surfaces look more alike, so double the lightness steps between layers: about 4–6% instead of the 2–3% that works in light mode.
- Elevated surfaces get lighter: light comes from above, so the base background is the darkest and raised cards are lighter.
- Use light greys for text rather than pure white, and desaturate brand colors and the logo slightly so they don't glow.

### Perception (*Interaction of Color*, Josef Albers)
- Color is relative. The same color changes appearance with its neighbours, so an accent must be judged against the actual tones it will sit on.
- One color can be made to look like two different colors, and two different colors can be made to look alike, depending on their surroundings. Never approve a palette from loose swatches alone.
- Quantity changes the effect: a color used over a large area behaves differently from the same color in a small spot. Test the accent at its real size.
- Strongly contrasting hues of equal lightness vibrate where they meet. Use this deliberately for energy, never for reading text.

### Contrasts (*The Elements of Color*, Johannes Itten)
The 2+1 model mostly uses three of Itten's seven contrasts:
- **Warm–cool:** the tones sit on one temperature and the accent on the other.
- **Saturation:** calm tones against a clean, strong accent.
- **Extension (proportion):** bright colors need less area to balance dark ones.

The others are useful vocabulary when explaining choices: hue, light–dark, complementary and simultaneous contrast.

### Brand system (*Designing Brand Identity*, Alina Wheeler)
- People take in a brand's shape first, then its color, then its words. Color is one of the fastest brand signals, so choose it strategically, not decoratively.
- Audit the category before choosing. Aim to "own" a color that competitors don't, and check meanings in every market the brand sells into.
- A color system needs a clear dominant brand color, a limited supporting palette, and rules for how they are used together.
- Specify every color for every medium (HEX/RGB for screens; CMYK/Pantone for print) and test across media, because colors drift between them.
- Consistency over time builds recognition. Once the palette is set, document its usage rules so every channel applies it the same way.

### Color anti-patterns (in addition to the Anti-AI-Slop Checklist)
- Pure #000 on pure #FFF for large text areas; it is harsh. Use a near-black on an off-white.
- Using brand red (or any brand color) for errors when it isn't the error color, or making the brand color the same as a status color.
- Two loud colors fighting. If both tones are vivid and unrelated, one of them must become quiet.

## Color Association Reference

Starting points, not rules. Check them against the specific audience.

| Emotional goal | Color families | Watch out for |
|---|---|---|
| Trust, stability, finance | Navy, deep blue, slate | Very common in finance; differentiate through the accent |
| Growth, wealth, nature | Greens, emerald, sage | Red + green accents confuse red-green color-blind users |
| Energy, urgency, action | Red, orange, coral | Tiring over large areas; usually best as the Character color |
| Optimism, warmth, youth | Yellow, warm orange | Fails contrast with white text; pair with dark text |
| Luxury, premium | Black, charcoal, deep plum, muted gold | Gold looks muddy on screen if over-saturated |
| Calm, wellness, escape, travel | Soft teal, sand, sage, sky blue | Can feel generic; needs a confident accent |
| Earthy, adventurous, authentic | Terracotta, ochre, forest green, clay | Can look dull on phones; keep one color clean and vivid |
| Precision, tech | Cool greys, graphite, electric accent | Feels cold without one warm element |
| Playful, Gen Z | Saturated, unexpected pairings | Accessibility suffers fast; check every pair |

**Cultural notes:**
- White is linked to mourning in parts of East Asia.
- Red signals luck in China, but losses in Western finance.
- Green carries religious significance in much of the Middle East.
- Older audiences need higher contrast and larger text.

## Proven Examples (measured)

Real 2+1 palettes from niki.aroca's design reels, measured from the source screenshots. Use them to calibrate what "quiet + loud" looks like.

| Tone 1 | Tone 2 | Character | Pattern | Hue gap |
|---|---|---|---|---|
| `#0099FF` sky blue | `#FDFDFE` white | `#FA2507` red | neutral + hue | 163° |
| `#0593C6` sky blue | `#FCFFFF` white | `#D83995` hot pink | neutral + hue | 129° |
| `#02070A` black | `#0297DE` electric blue | `#FC734D` cantaloupe | neutral + hue | 174° |
| `#0C0C0A` black | `#F15419` blaze orange | `#77E7FE` glacier blue | neutral + hue | 174° |
| `#01010D` black | `#6331FB` indigo | `#88F9C0` mint | neutral + hue (deliberate indigo, see slop flag) | 105° |
| `#012B1D` forest | `#01B36C` jungle green | `#FC6E00` orange | one hue family | 130° |
| `#0042AC` sapphire | `#00D3FB` ocean blue | `#83FD80` neon jade | one hue family | 98° |
| `#7BDFF2` lagoon | `#FCFFFF` white | `#F2B5D4` bubblegum | neutral + hue (pastel) | 140° |
| `#EE5001` tangerine | `#FCFFFF` white | `#C8FD03` acid lime | neutral + hue (neon exception) | 53° |

## Helper Scripts

Save these scripts to a scratch folder (for example `./palette-tools/`) the first time you need them, then run them with `python3`. They need only Python 3, plus Pillow for the extractor (`pip install pillow --break-system-packages` if it is missing).

### extract_colors.py: dominant colors from an image

```python
#!/usr/bin/env python3
"""List the dominant colors in an image, largest share first.

Usage: python3 extract_colors.py IMAGE [--k 8]
"""
import argparse

from PIL import Image


def main():
    p = argparse.ArgumentParser()
    p.add_argument("image")
    p.add_argument("--k", type=int, default=8, help="number of colors to find")
    a = p.parse_args()

    img = Image.open(a.image).convert("RGB")
    img.thumbnail((300, 300))
    # Max-coverage + k-means refinement + no dithering keeps small accent
    # areas as their own color and returns their exact hex values.
    q = img.quantize(colors=a.k, method=Image.Quantize.MAXCOVERAGE,
                     kmeans=3, dither=Image.Dither.NONE)
    pal = q.getpalette()
    counts = sorted(q.getcolors(), reverse=True)
    total = sum(c for c, _ in counts)

    for count, idx in counts:
        r, g, b = pal[idx * 3: idx * 3 + 3]
        tag = ""
        if min(r, g, b) > 220:
            tag = "near-white"
        elif max(r, g, b) < 35:
            tag = "near-black"
        elif max(r, g, b) - min(r, g, b) < 20:
            tag = "grey"
        print(f"#{r:02X}{g:02X}{b:02X}  rgb({r},{g},{b})  {100 * count / total:5.1f}%  {tag}")


if __name__ == "__main__":
    main()
```

Use `--k 12` for busy images such as an Instagram grid.

### palette_check.py: does the palette follow Mood & Character?

```python
#!/usr/bin/env python3
"""Check a 2+1 palette against the Mood & Character rules.

Usage: python3 palette_check.py TONE1 TONE2 CHARACTER
Prints HSL for each color, the hue gap between the main hued tone and the
character color, the saturation gap, and flags anything outside the rules.
"""
import argparse
import colorsys


def hsl(h):
    h = h.strip().lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hh, l, s = colorsys.rgb_to_hls(r, g, b)
    return round(hh * 360), round(s * 100), round(l * 100)


def is_neutral(c):
    _, s, l = c
    return s < 12 or l < 6 or l > 95


def main():
    p = argparse.ArgumentParser()
    p.add_argument("tone1")
    p.add_argument("tone2")
    p.add_argument("character")
    a = p.parse_args()
    t1, t2, ch = hsl(a.tone1), hsl(a.tone2), hsl(a.character)
    for name, hx, c in (("Tone 1", a.tone1, t1), ("Tone 2", a.tone2, t2), ("Character", a.character, ch)):
        tag = " (neutral)" if is_neutral(c) else ""
        print(f"{name:10} #{hx.lstrip('#').upper()}  H{c[0]:>3} S{c[1]:>3} L{c[2]:>3}{tag}")

    hued = [c for c in (t1, t2) if not is_neutral(c)]
    flags = []
    if not hued:
        print("Both tones are neutral: any hue works for the character; judge by audience.")
    else:
        main_tone = max(hued, key=lambda c: c[1])  # most saturated tone carries the mood hue
        gap = abs(main_tone[0] - ch[0])
        gap = min(gap, 360 - gap)
        print(f"Hue gap main tone -> character: {gap} deg (target 90-180)")
        if gap < 90:
            flags.append("character hue is close to the tone hue; it may not read as 'unexpected'. "
                         "Fine only if it is a neon/acid version that still clearly breaks the mood")
        if len(hued) == 2:
            tg = abs(hued[0][0] - hued[1][0])
            tg = min(tg, 360 - tg)
            if tg > 45:
                flags.append(f"the two tones are {tg} deg apart; quiet tone pairs are usually one hue "
                             "family (or a neutral + one hue)")
        sat_gap = ch[1] - max(c[1] for c in hued)
        # Info only: loudness comes mainly from the hue jump; a fully saturated
        # tone (e.g. electric blue) can't be out-saturated.
        print(f"Saturation vs most saturated tone: {sat_gap:+d} (info)")
    # Anti-AI-slop: purple/indigo is the most common default of AI design tools.
    purples = [n for n, c in (("Tone 1", t1), ("Tone 2", t2), ("Character", ch))
               if 225 <= c[0] <= 290 and c[1] >= 45 and not is_neutral(c)]
    if purples:
        flags.append(f"AI-SLOP RISK: {', '.join(purples)} in the purple/indigo range, the most common "
                     "AI-design default. Keep only with a clear brand reason, and never as a purple-to-blue gradient")
    if ch[1] < 60:
        flags.append("character saturation is under 60; it may look soft rather than loud")
    if is_neutral(ch):
        flags.append("character color is a neutral; the accent must carry hue")
    for f in flags:
        print("FLAG:", f)
    if not flags:
        print("OK: palette follows the Mood & Character pattern")


if __name__ == "__main__":
    main()
```

### contrast_check.py: WCAG 2.x contrast, with automatic fixes

```python
#!/usr/bin/env python3
"""WCAG 2.x contrast checker.

Usage:
  python3 contrast_check.py FG BG [FG BG ...]
  python3 contrast_check.py FG BG --fix [--target 4.5]
      --fix suggests the nearest passing shade of the foreground AND of the
      background (same hue, only lightness changed).
"""
import argparse
import colorsys


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def norm(h):
    return "#" + h.strip().lstrip("#").upper()


def luminance(rgb):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(hex_to_rgb(a)), luminance(hex_to_rgb(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r):
    def ok(x):
        return "PASS" if r >= x else "FAIL"
    return f"AA text {ok(4.5)} | AA large text & UI {ok(3)} | AAA text {ok(7)}"


def nearest_passing(fg, bg, target):
    r, g, b = (c / 255 for c in hex_to_rgb(fg))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    for step in range(1, 101):
        for sign in (-1, 1):
            nl = l + sign * step / 100
            if not 0 <= nl <= 1:
                continue
            rr, gg, bb = colorsys.hls_to_rgb(h, nl, s)
            cand = "#{:02X}{:02X}{:02X}".format(round(rr * 255), round(gg * 255), round(bb * 255))
            if ratio(cand, bg) >= target:
                return cand
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("colors", nargs="+", help="hex colors in FG BG pairs")
    p.add_argument("--fix", action="store_true")
    p.add_argument("--target", type=float, default=4.5)
    a = p.parse_args()
    if len(a.colors) % 2:
        p.error("give colors in FG BG pairs")

    for fg, bg in zip(a.colors[0::2], a.colors[1::2]):
        r = ratio(fg, bg)
        print(f"{norm(fg)} on {norm(bg)}: {r:.2f}:1  ->  {verdict(r)}")
        if a.fix and r < a.target:
            # Offer both options: adjust the foreground, or adjust the background.
            for moving, fixed, label in ((fg, bg, "foreground"), (bg, fg, "background")):
                c = nearest_passing(moving, fixed, a.target)
                if c:
                    print(f"   fix {label}: {norm(moving)} -> {c} ({ratio(c, fixed):.2f}:1)")
                else:
                    print(f"   fix {label}: no shade of {norm(moving)} reaches {a.target}:1")


if __name__ == "__main__":
    main()
```

Check several pairs at once: `python3 contrast_check.py 1F2A2E F4EFE6 FFFFFF E8743B`. Use `--target 3` for pairs that only need the UI or large-text level.

## Sources

- niki.aroca, Instagram design reels (10 latest as of Nov 2026): 2 quiet + 1 loud method, measured examples, "vibecoded" anti-patterns
- The Futur Academy, *How To Balance Your Color Palette – The 60-30-10 Rule*: https://www.youtube.com/watch?v=V-SD_zV9S2c
- Kole Jain, *Why the 60-30-10 Rule is RUINING Your UI Designs*: https://www.youtube.com/watch?v=66oOi9OLMCw
- Kole Jain, *The 7 Color Mistakes that RUIN your UI Designs*: https://www.youtube.com/watch?v=EOcY3hPMQkk
- Sajid, *The Easy Way to Pick UI Colors*: https://www.youtube.com/watch?v=vvPklRN0Tco
- UX Tools, *How I make UI color palettes*: https://www.youtube.com/watch?v=yYwEnLYT55c
- Sarah Renae Clark, *Color Theory Basics: Color Wheel & Color Harmonies*: https://www.youtube.com/watch?v=YeI6Wqn4I78
- Will Paterson, *How To Choose The RIGHT Logo Color*: https://www.youtube.com/watch?v=F-Zw7CbM-ps
- Kenny Gunderman, *Why Every Website Looks Like This*: https://www.youtube.com/watch?v=nDI43WVDxHo
- Flux Academy, *Why All AI Generated Designs Look The Same*: https://www.youtube.com/watch?v=DLzzhG1ORm8
- DesignCode, *How to Avoid AI Slop in Vibe-Coded Landing Pages*: https://www.youtube.com/watch?v=M4DNgmI7MIM
- Oliur Online, *Stop AI slop and making stuff look vibe coded*: https://www.youtube.com/watch?v=soZgjJi7xNw
- Josef Albers, *Interaction of Color*
- Alina Wheeler, *Designing Brand Identity*
- Johannes Itten, *The Elements of Color*
