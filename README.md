# THE WORLD — Thursday 19 November 2026

A one-page newspaper front page that sums up 19 November 2026 in a single
image: **46 stories from six continents**.

## What is on the page

- **Lead story:** the first three-way summit of Trump, Xi and Putin in
  Shenzhen, ending after 90 minutes with a "peace declaration".
- **Where it happened:** a world map with 15 numbered dots marking the
  main stories.
- **The day in four figures:** GTA VI's Metacritic score of 99,
  Anthropic's record $81.3bn IPO raise, gold at a 14-month low of $3,700,
  and Van Gogh's record $190.4m sale.
- **Three illustrated panels:** GTA VI on sale, Anthropic's record IPO,
  and the World Court ruling Myanmar guilty of genocide against the
  Rohingya.
- **Three columns** group the rest of the day's news by region — the Gulf
  and Middle East, Europe and Ukraine, and Asia-Pacific, Africa and the
  Americas — with a short "ALSO" line at the foot of the page.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`, a 1024x1024 PNG of 171,074 bytes. The program
uses only the Python standard library: it checks that `entry.png` is
present and under the 1 MiB limit, then copies it unchanged. Because the
output is an exact copy, repeated runs are byte-identical.

## Files

- `main.py` — the copy program (Python 3, stdlib only)
- `entry.png` — the finished front page
- `LICENSE` — MIT
