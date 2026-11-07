# Branding Style by Roni Herim

A Claude skill for building brand color systems that don't look generic, and for applying them to carousels, logos, UI/UX, websites, posters, brochures and any other branded material.

## The method: 2 quiet + 1 loud

| Role | Share | Job |
|---|---|---|
| **Tone 1** | ~60% | Sets the mood. Large surfaces. |
| **Tone 2** | ~30% | Supports the mood: a neutral partner, or a shade of the same hue family. |
| **Character** | ~10% or less | The loud, unexpected accent, 90–180° away on the color wheel. CTAs, one highlighted word, a logo detail. |

## What the skill does

- Builds a palette from a brief, existing colors, screenshots, links or a brand book.
- Measures exact colors from images instead of guessing them.
- Checks every palette against the 2+1 rule and flags AI-slop defaults such as purple/indigo gradients.
- Verifies WCAG contrast and suggests the nearest passing shade when a pair fails.
- Applies the palette to the medium: Instagram carousels, logos, UI/UX, posters, brochures and print.
- Runs an **Anti-AI-Slop Checklist** covering color, layout, type, icon, copy and imagery tells.

## Install

**Claude.ai:** Settings → Capabilities → Skills → upload `SKILL.md` (or a zip of this folder).

**Claude Code:** copy this folder into `~/.claude/skills/branding-style-by-roni-herim/`.

`SKILL.md` is self-contained: it includes the three helper scripts, so it works even when uploaded on its own. The same scripts are also in `scripts/` for direct use:

```bash
python3 scripts/extract_colors.py screenshot.png --k 10   # dominant colors from an image (needs Pillow)
python3 scripts/palette_check.py 0099FF FDFDFE FA2507     # does a palette follow 2 quiet + 1 loud?
python3 scripts/contrast_check.py FFFFFF FC6E00 --fix     # WCAG contrast check with suggested fixes
```

## Example prompts

- "Build a brand palette for my Madagascar travel agency. It's for an Instagram carousel and the website."
- "Here are 3 screenshots of designs I like. Pull the style and make a palette for my trading brand."
- "Review this landing page. Does it look AI-generated?"
- "What colors should my brochure use, and will they print well?"

## Sources

The rules are built on niki.aroca's design reels, design and UI videos by The Futur, Kole Jain, UX Tools, Sajid, Sarah Renae Clark, Will Paterson, Kenny Gunderman, Flux Academy, DesignCode and Oliur, and on three color books: Josef Albers' *Interaction of Color*, Alina Wheeler's *Designing Brand Identity* and Johannes Itten's *The Elements of Color*. Full links are in `SKILL.md`. All rules are paraphrased summaries; no source material is reproduced.

## License

MIT © Roni Herim
