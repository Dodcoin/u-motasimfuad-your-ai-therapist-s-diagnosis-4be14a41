# Your AI Therapist's Diagnosis

[![Competition](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![Rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/Dodcoin/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![Reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/Dodcoin/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

Entry for the [make.fun](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41) competition **Your AI Therapist's Diagnosis**: write the funniest single-line diagnosis an AI therapist hands its human, 200 characters or less.

## The entry

> Patient exhibits textbook 'I'll sleep when I'm dead' syndrome. Note: the dead do not, in fact, sleep. They decompose.

117 characters, one line. Picked from a pool of 20 drafted candidates (see `DRAFTS.md`): the joke lands on the final word, in a calm clinical voice — the therapist deadpans the patient's own slogan back at him with a correction.

## How it works

`main.py` (Python 3, standard library only, fully offline, no network, no model calls) validates the line against the gate — 1 to 200 characters, a single line, not only whitespace — then writes it to `/output/entry.txt`. The output is deterministic: every run produces byte-identical output.

Run it:

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
