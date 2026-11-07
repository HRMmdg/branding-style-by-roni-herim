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
