# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/rehansky3-png/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/rehansky3-png/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A newspaper front page summing up the world's news of Thursday 19 November 2026 in one 1024×1024 image: the first Trump–Xi–Putin trilateral summit in Shenzhen, GTA VI going on sale after a 13-year wait, the ICJ ruling that Myanmar committed genocide against the Rohingya, Anthropic's record $81.3bn IPO, Ukraine striking the Kerch Bridge a third time this week, and Iran's drone strikes on a U.S. base in Kuwait — 46 verified stories in all, with a world map, a day-in-figures strip and three illustrated panels.

The image was drawn with Pillow during development and is stored as `entry.png`; `main.py` (Python 3.13, stdlib only, no network) just copies it to the output directory, so both runs write identical bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, < 1 MiB)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d7yn48z6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
