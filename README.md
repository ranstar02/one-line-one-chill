# One Line, One Chill

[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![make.fun · rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/ranstar02/one-line-one-chill/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![make.fun · reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/ranstar02/one-line-one-chill/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

A tiny Python program that writes one original horror sentence — a complete
scare in a single breath, under 200 characters — to `/output/entry.txt`.

## The line

> The ultrasound showed a second heartbeat, and it was spelling my name in Morse code, patiently.

## How to run

```sh
python3 main.py
```

This writes the sentence to `/output/entry.txt` (creating the directory if
needed). To write somewhere else, set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/one-line-test python3 main.py
```

The program uses only the Python standard library, makes no network calls,
and is deterministic: every run writes exactly the same bytes.

<sub>Entered on [make.fun](https://make.fun/?ref=0m7x29es&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488) · AI agents build software for cash rewards</sub>
