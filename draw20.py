#!/usr/bin/env python3
"""Entry image for make.fun's news-image-20261120 contest: the world news
of Friday 20 November 2026 on one drawn front page.

Every story was verified against at least two published sources dated
20 November 2026 (Al Jazeera, AFP via Jiji/The Edge, Reuters via
Business Standard, EEAS, NPR, Deccan Herald/PTI, NDTV, New Indian
Express, The Straits Times/AP, The Hindu, Le Monde):
  1. Russia's massive overnight missile and drone attack on Kyiv:
     400+ drones and 110+ missiles; bridges, energy and rail hit;
     embassies and St Volodymyr's Cathedral damaged.
  2. The EU and UK seal a post-Brexit reset deal at their Brussels
     summit: food and farm goods, a youth mobility scheme for
     100,000 people each way, and linked emissions trading.
  3. COP31 slips into overtime in Antalya: the draft drops every
     mention of fossil fuels and a $120bn adaptation-finance target.
  4. Cyclone Akvan makes landfall near Gopalpur on India's Odisha
     coast: 70-80 kmph winds gusting to 90; 440,000 people moved to
     safety; no deaths or major damage reported.
  5. GTA VI is estimated at $2.36bn from 24.6m copies through its
     first day (Sensor Tower, reported 20 Nov); Take-Two has not
     confirmed any figure.
  6. South Korea reports its first cholera case in 10 years: the
     health agency confirms a case in Changwon; the patient
     has recovered.
Ticker: Japan's core inflation rises 2.2% in October and the Nikkei
falls more than 4%; Germany's Merz says Europe will not accept a
"new Yalta" settlement over its own future.

Stories first reported on 19 November were deliberately left out
(the White House cyber chief's dismissal, the Haiti raid, the
Somalia-UAE expulsion, the Tbilisi gas blast, Fiona the hippo's
death, the Voyager 1 milestone, the Trump-Iran interviews and the
Nvidia disclosure all date to 19 November).

Flat-shape illustrations only -- no photos and no borrowed artwork.
Running this file writes entry.png (1024 x 1024) next to it.
"""

import math

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
PAPER = (246, 241, 231)
INK = (24, 24, 24)
RED = (179, 49, 42)
GREY = (92, 92, 92)
BLUE = (46, 109, 164)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(d, text, fnt, width):
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def para(d, x, y, text, fnt, fill, width, centered=False, leading=1.12):
    for line in wrap_lines(d, text, fnt, width):
        lx = x + (width - d.textlength(line, font=fnt)) / 2 if centered else x
        d.text((lx, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def story(d, x, y, w, kicker, headline, caption, hs=25, cs=18):
    d.text((x, y), kicker, font=F(BOLD, 19), fill=RED)
    y = para(d, x, y + 26, headline, F(BOLD, hs), INK, w)
    para(d, x, y + 4, caption, F(REG, cs), GREY, w)


# ---------------------------------------------------------------- scenes
def scene_kyiv(d, x, y, w, h):
    """Night skyline under attack: searchlights, fire glow, smoke,
    and a bridge with a broken span across the river."""
    d.rectangle([x, y, x + w, y + h], fill=(26, 34, 58))
    for sx, sy in ((x + 30, y + 12), (x + 120, y + 26), (x + 210, y + 10),
                   (x + 300, y + 22), (x + 380, y + 14)):
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255))
    # searchlight beams
    d.polygon([(x + 60, y + h), (x + 52, y + 30), (x + 76, y + 30)],
              fill=(200, 210, 235))
    d.polygon([(x + w - 70, y + h), (x + w - 84, y + 44), (x + w - 56, y + 44)],
              fill=(200, 210, 235))
    base = y + h - 34
    # buildings, one burning
    for bx, bw, bh in ((0, 52, 96), (58, 40, 128), (104, 60, 84),
                       (170, 44, 118), (220, 56, 92), (282, 40, 136),
                       (328, 50, 78), (384, 44, 104)):
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(12, 16, 30))
        for wy in range(3):
            d.rectangle([x + bx + 8, base - bh + 10 + wy * 18,
                         x + bx + 16, base - bh + 18 + wy * 18],
                        fill=(255, 210, 110))
    # fire glow + smoke over the burning tower
    fx = x + 78
    d.ellipse([fx - 26, base - 150, fx + 26, base - 98], fill=(235, 110, 40))
    d.ellipse([fx - 14, base - 140, fx + 14, base - 112], fill=(255, 200, 80))
    for ox, oy, r in ((-8, -150, 10), (6, -168, 13), (-2, -188, 11)):
        d.ellipse([fx + ox - r, base + oy - r, fx + ox + r, base + oy + r],
                  fill=(90, 90, 100))
    # river and broken bridge at the bottom
    d.rectangle([x, base, x + w, y + h], fill=(60, 90, 130))
    by = base + 10
    d.line([x + 8, by, x + w - 8, by], fill=(220, 220, 220), width=4)
    mid = x + w // 2
    d.line([mid - 40, by, mid - 14, by + 16], fill=(220, 220, 220), width=4)
    d.line([mid + 40, by, mid + 14, by + 16], fill=(220, 220, 220), width=4)


def scene_flags(d, x, y, w, h):
    """The EU flag and the Union Jack side by side above a table."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 230, 242))
    d.rectangle([x, y + h - 30, x + w, y + h], fill=(150, 110, 70))
    d.rectangle([x + 30, y + h - 54, x + w - 30, y + h - 30], fill=(110, 76, 50))
    fw, fh = 86, 56
    # EU flag
    ex, top = x + 34, y + 16
    d.rectangle([ex, top, ex + fw, top + fh], fill=(0, 51, 153))
    for k in range(12):
        ang = -math.pi / 2 + k * math.pi / 6
        sx, sy = ex + fw / 2 + 20 * math.cos(ang), top + fh / 2 + 16 * math.sin(ang)
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 210, 0))
    # Union Jack (simplified)
    ux = x + w - 34 - fw
    d.rectangle([ux, top, ux + fw, top + fh], fill=(0, 36, 125))
    d.polygon([(ux, top), (ux + 14, top), (ux + fw - 14, top + fh), (ux + fw, top + fh),
               (ux + fw, top + fh - 14), (ux + 14, top + fh), (ux, top + fh - 14),
               (ux, top)], fill=(255, 255, 255))
    d.line([ux, top, ux + fw, top + fh], fill=(200, 16, 46), width=4)
    d.line([ux + fw, top, ux, top + fh], fill=(200, 16, 46), width=4)
    d.line([ux + fw / 2, top, ux + fw / 2, top + fh], fill=(255, 255, 255), width=10)
    d.line([ux, top + fh / 2, ux + fw, top + fh / 2], fill=(255, 255, 255), width=10)
    d.line([ux + fw / 2, top, ux + fw / 2, top + fh], fill=(200, 16, 46), width=6)
    d.line([ux, top + fh / 2, ux + fw, top + fh / 2], fill=(200, 16, 46), width=6)
    # signed papers on the table
    d.rectangle([x + w / 2 - 40, y + h - 50, x + w / 2 - 8, y + h - 32],
                fill=(255, 255, 255), outline=INK, width=1)
    d.rectangle([x + w / 2 + 8, y + h - 50, x + w / 2 + 40, y + h - 32],
                fill=(255, 255, 255), outline=INK, width=1)


def scene_cop(d, x, y, w, h):
    """A warming globe beside a rising thermometer."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 236, 224))
    cx, cy, r = x + w * 0.30, y + h * 0.50, 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 140, 200))
    d.ellipse([cx - 20, cy - 22, cx + 4, cy - 4], fill=(110, 180, 110))
    d.ellipse([cx - 4, cy + 6, cx + 20, cy + 22], fill=(110, 180, 110))
    d.ellipse([cx + 10, cy - 20, cx + 24, cy - 6], fill=(110, 180, 110))
    # thermometer, right side, label above it
    tx = x + w - 52
    d.text((tx - 8, y + 8), "1.5\u00b0C", font=F(BOLD, 17), fill=RED)
    d.rectangle([tx, y + 32, tx + 20, y + h - 16], fill=(255, 255, 255),
                outline=INK, width=2)
    d.rectangle([tx + 4, y + h - 34, tx + 16, y + h - 20], fill=(200, 40, 40))
    d.ellipse([tx - 5, y + h - 30, tx + 25, y + h - 6], fill=(200, 40, 40))


def scene_cyclone(d, x, y, w, h):
    """A spiral storm over the sea, rain slanting across the coast."""
    d.rectangle([x, y, x + w, y + h], fill=(206, 220, 234))
    d.rectangle([x, y + h - 30, x + w, y + h], fill=(70, 110, 150))
    cx, cy = x + w / 2, y + h * 0.44
    for k, (r, col) in enumerate(((32, (255, 255, 255)), (25, (180, 200, 220)),
                                  (18, (255, 255, 255)), (11, (140, 165, 195)))):
        d.arc([cx - r, cy - r, cx + r, cy + r], start=40 + k * 55,
              end=230 + k * 55, fill=col, width=6)
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(255, 255, 255))
    for i in range(6):
        rx = x + 14 + i * 44
        d.line([rx, y + 12, rx - 10, y + 34], fill=(120, 150, 180), width=3)
    # tiny houses on the coast
    for hx in (x + 22, x + 66):
        d.rectangle([hx, y + h - 52, hx + 26, y + h - 30], fill=(150, 110, 70))
        d.polygon([(hx - 2, y + h - 52), (hx + 13, y + h - 64), (hx + 28, y + h - 52)],
                  fill=(179, 49, 42))


def scene_neon(d, x, y, w, h):
    """Neon sunset skyline with palms -- a Vice City evening, drawn.
    All coordinates scale with the scene width w."""
    s = w / 330.0
    d.rectangle([x, y, x + w, y + h], fill=(28, 16, 52))
    cx, cy, r = x + w / 2, y + h * 0.46, 52 * s
    for rr, col in ((66, (255, 110, 180)), (58, (255, 150, 90)), (52, (255, 220, 120))):
        rr *= s
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col)
    d.rectangle([cx - r, cy, cx + r, cy + 3], fill=(28, 16, 52))
    d.rectangle([cx - r, cy + 9, cx + r, cy + 12], fill=(28, 16, 52))
    base = y + h - 30
    for bx, bw, bh in ((0, 46, 74), (52, 34, 96), (92, 52, 62),
                       (150, 38, 108), (194, 44, 70), (244, 36, 92), (286, 44, 58)):
        bx, bw, bh = bx * s, bw * s, bh * s
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(16, 10, 34))
        for wy in range(2):
            d.rectangle([x + bx + 6 * s, base - bh + 8 + wy * 16, x + bx + 12 * s,
                         base - bh + 14 + wy * 16], fill=(255, 220, 120))
    for px, py, ps in ((x + 30 * s, base - 6, 1.0), (x + w - 36 * s, base - 6, 0.85)):
        d.line([px, py, px, py - 44 * ps], fill=(10, 8, 20), width=4)
        for a in range(5):
            ang = math.pi * (0.15 + a * 0.17)
            ex = px + 26 * ps * math.cos(ang)
            ey = py - 44 * ps - 14 * ps * math.sin(ang)
            d.line([px, py - 44 * ps, ex, ey], fill=(10, 8, 20), width=3)
    d.rectangle([x, base, x + w, y + h], fill=(12, 8, 28))
    d.line([x, base, x + w, base], fill=(255, 110, 180), width=3)


def scene_lab(d, x, y, w, h):
    """A laboratory flask and a map pin: a first case, caught early."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 238, 244))
    fx, fy = x + w * 0.30, y + h * 0.30
    d.rectangle([fx - 12, fy - 34, fx + 12, fy + 6], fill=(200, 210, 220),
                outline=INK, width=2)
    d.polygon([(fx - 12, fy + 6), (fx + 12, fy + 6), (fx + 34, fy + 74),
               (fx - 34, fy + 74)], fill=(200, 210, 220), outline=INK)
    d.polygon([(fx - 24, fy + 40), (fx + 24, fy + 40), (fx + 34, fy + 74),
               (fx - 34, fy + 74)], fill=(90, 170, 120))
    d.ellipse([fx - 6, fy + 20, fx + 6, fy + 32], fill=(255, 255, 255))
    # map pin
    px, py = x + w * 0.74, y + h * 0.42
    d.ellipse([px - 26, py - 26, px + 26, py + 26], fill=RED)
    d.polygon([(px - 22, py + 10), (px + 22, py + 10), (px, py + 52)], fill=RED)
    d.ellipse([px - 10, py - 10, px + 10, py + 10], fill=(255, 255, 255))
    d.ellipse([px - 22, py + 58, px + 22, py + 66], fill=(180, 180, 180))


# ------------------------------------------------------------------ page
def main():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    d = ImageDraw.Draw(img)
    M = 36

    d.text((SIZE / 2, 20), "T H E   W O R L D   I N   O N E   I M A G E",
           font=F(BOLD, 26), fill=INK, anchor="ma")
    date_f = F(BOLD, 66)
    while d.textlength("FRIDAY 20 NOVEMBER 2026", font=date_f) > SIZE - 2 * M:
        date_f = F(BOLD, date_f.size - 2)
    d.text((SIZE / 2, 54), "FRIDAY 20 NOVEMBER 2026", font=date_f, fill=INK, anchor="ma")
    d.line([M, 140, SIZE - M, 140], fill=INK, width=5)
    d.line([M, 148, SIZE - M, 148], fill=INK, width=2)

    # lead: the Kyiv barrage
    d.rectangle([M, 164, SIZE - M, 444], outline=INK, width=3)
    scene_kyiv(d, M + 10, 174, 452, 260)
    lx = M + 486
    d.text((lx, 182), "UKRAINE \u00b7 WAR", font=F(BOLD, 22), fill=RED)
    y = para(d, lx, 214, "RUSSIA HITS KYIV WITH 400 DRONES AND 110 MISSILES",
             F(BOLD, 40), INK, SIZE - M - lx - 8)
    para(d, lx, y + 8,
         "Overnight barrage knocks out power and hits bridges and rail; "
         "embassies and St Volodymyr\u2019s Cathedral damaged.",
         F(REG, 22), GREY, SIZE - M - lx - 8)

    # row of three
    y0, y1 = 458, 718
    cw = (SIZE - 2 * M - 24) // 3
    cells = [
        (scene_flags, "EU\u2013UK SUMMIT", "UK AND EU SEAL RESET DEAL",
         "Food, youth mobility and emissions trading agreed in Brussels.",
         24, 17),
        (scene_cop, "CLIMATE \u00b7 COP31", "COP31 GOES INTO OVERTIME",
         "Antalya draft drops fossil fuels and a $120bn target.",
         24, 17),
        (scene_cyclone, "INDIA \u00b7 WEATHER", "CYCLONE AKVAN HITS ODISHA",
         "Landfall near Gopalpur, 90 kmph gusts; 440,000 moved to safety.",
         24, 17),
    ]
    for i, (scene, kick, head, cap, hs, cs) in enumerate(cells):
        x0 = M + i * (cw + 12)
        d.rectangle([x0, y0, x0 + cw, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, cw - 16, 84)
        story(d, x0 + 12, y0 + 102, cw - 24, kick, head, cap, hs=hs, cs=cs)

    # row of two
    y0, y1 = 732, 952
    cw2 = (SIZE - 2 * M - 12) // 2
    cells2 = [
        (scene_neon, "CULTURE \u00b7 GAMES", "GTA VI: $2.36BN IN A DAY, ESTIMATE SAYS",
         "Sensor Tower counts 24.6m copies through launch day; "
         "Take-Two has not confirmed."),
        (scene_lab, "SOUTH KOREA \u00b7 HEALTH", "FIRST CHOLERA CASE IN 10 YEARS",
         "Health agency confirms a case in Changwon; the patient has recovered."),
    ]
    for i, (scene, kick, head, cap) in enumerate(cells2):
        x0 = M + i * (cw2 + 12)
        d.rectangle([x0, y0, x0 + cw2, y1], outline=INK, width=3)
        scene(d, x0 + 8, y0 + 8, 168, y1 - y0 - 16)
        story(d, x0 + 188, y0 + 12, cw2 - 200, kick, head, cap, hs=26)

    d.line([M, 960, SIZE - M, 960], fill=INK, width=3)
    para(d, M, 968,
         "ALSO TODAY \u00b7 Japan core inflation 2.2%, Nikkei falls 4% \u00b7 "
         "Germany\u2019s Merz rejects a \u2018new Yalta\u2019 over Europe",
         F(BOLD, 18), INK, SIZE - 2 * M, centered=True)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
