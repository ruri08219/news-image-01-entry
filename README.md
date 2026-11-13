# news-image-01 — ruri08

One image summing up the world's news of Friday 13 November 2026.

The entry is a newspaper front page with the masthead
"13 NOVEMBER 2026" and four illustrated panels:

- diplomats shaking hands
- a microchip with a down arrow
- a storm over a coastal city
- a soccer stadium celebration

The panel headlines are illustrative artwork, not wire-service quotes.

## How it runs

`main.py` copies the bundled `entry.jpg` to `/output/entry.png`
byte-for-byte. It first checks the bundled file against its known
SHA-256 (and size), then re-checks the written output, so the result is
identical on every run. No network, no clock, no randomness.

## License

MIT — see LICENSE.
