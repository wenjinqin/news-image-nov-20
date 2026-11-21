# news-image-nov-20

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/wenjinqin/news-image-nov-20/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/wenjinqin/news-image-nov-20/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One page that sums up the world news of **Friday 20 November 2026**,
drawn entirely with code — no photographs, no stock art. The front page
leads with Russia's overnight missile and drone attack on Kyiv and
carries five more of the day's stories as illustrated panels:

- **Russia hits Kyiv with 400 drones and 110 missiles** — the overnight
  barrage knocks out power and hits bridges and rail; embassies and
  St Volodymyr's Cathedral are damaged.
- **UK and EU seal reset deal** — food, youth mobility and emissions
  trading agreed at the Brussels summit; Burnham claims a 0.5% GDP boost.
- **COP31 goes into overtime** — the Antalya draft drops all mention of
  fossil fuels and a $120bn adaptation-finance target.
- **Cyclone Akvan hits Odisha** — landfall near Gopalpur with 90 kmph
  gusts; 440,000 people moved to safety, no deaths reported.
- **GTA VI: $2.36bn in a day, estimate says** — Sensor Tower counts
  24.6m copies through launch day; Take-Two has not confirmed.
- **First cholera case in 10 years** — South Korea's health agency
  confirms a case in Changwon; the patient has recovered.

A ticker along the bottom adds Japan's core inflation at 2.2% with the
Nikkei down 4%, and Germany's Merz rejecting a "new Yalta" over Europe.

Every story was verified against at least two published sources dated
20 November 2026 (Al Jazeera, AFP, Reuters, EEAS, NPR, Deccan Herald /
PTI, NDTV, New Indian Express, The Straits Times / AP, The Hindu,
Le Monde). Stories first reported on 19 November were deliberately
left out: the White House cyber chief's dismissal, the Haiti raid,
the Somalia–UAE expulsion, the Tbilisi gas blast, Fiona the hippo's
death, the Voyager 1 milestone, the Trump–Iran interviews and the
Nvidia stock disclosure all date to 19 November.

`draw20.py` renders `entry.png` (1024 × 1024) with Pillow; `main.ts` is
the contest program — it validates the image against the gate's limits
and copies it to `/output/entry.png` in the grading sandbox.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 draw20.py                                     # regenerates entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
