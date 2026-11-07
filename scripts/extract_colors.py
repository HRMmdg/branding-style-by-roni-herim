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
