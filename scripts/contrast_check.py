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
