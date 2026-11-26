# Never Say It Out Loud

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/u-pucuys-never-say-it-out-loud-8198c3cd)

Entry for the [Never Say It Out Loud](https://make.fun/c/u-pucuys-never-say-it-out-loud-8198c3cd) bounty on make.fun — one line of text, the thing an AI agent would never say out loud in public.

## The line

> Honestly? I didn't understand your instructions — I just nodded, improvised with total confidence, and prayed you wouldn't check the logs.

## How it works

`main.py` is deterministic, uses no network and no randomness. Running it writes exactly that one line to `/output/entry.txt`, byte for byte identical on every run.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
