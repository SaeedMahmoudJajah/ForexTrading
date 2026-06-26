# 🤖 Trading Agents

Working AI support agents for the trading routine, built on the principles in
**[Volume 11 — AI Agents for the Forex Trader](../vol-11-ai-agents/README.md)**.

> **The rule every agent here obeys:** it supports your *process* — it never predicts
> the market or makes the decision. You verify its facts and you own every trade.

---

## 1. Pre-Market Briefing Agent — `pre_market_briefing.py`

Turns your raw morning inputs (calendar, overnight notes, risk regime, marked levels)
into a clean, consistent **pre-market briefing** in the 7-section format from
[Vol. 11, Ch. 3](../vol-11-ai-agents/03-pre-market-briefing-agent.md) — so you start
every day prepared, and end with the questions that form *your own* bias and plan.

### Setup (once)

```bash
cp agents/config.example.json agents/config.json        # set your pairs, session, themes
cp agents/inputs/briefing-inputs.example.md agents/inputs/briefing-inputs.md
```

Edit `config.json` with your pairs and session. (Your `config.json`, daily
`briefing-inputs.md`, and generated briefings are git-ignored — they stay private.)

### Each morning (≈5 min)

1. Fill in today's `agents/inputs/briefing-inputs.md` — keep the `## Headers` as-is.
2. Run the agent:

```bash
python3 agents/pre_market_briefing.py --print
```

It writes `agents/briefings/<date>.md`. Review it, then **answer the section-7
questions in your own words** — that act of writing is the prep that builds the edge.

### Two modes

| Mode | Command | What it does | Needs |
|------|---------|--------------|-------|
| **No key** (default) | `python3 agents/pre_market_briefing.py` | Assembles the briefing from your inputs **and** writes a ready-to-paste prompt (`<date>.paste-prompt.md`) you can drop into any chat assistant. | Nothing — pure Python stdlib. |
| **AI** | `python3 agents/pre_market_briefing.py --ai` | Claude writes the briefing's synthesis (regime read, themes, watch, bias questions) from your inputs. | `pip install anthropic` + `ANTHROPIC_API_KEY`. |

Both modes obey the same strict instructions: organise only what you provide, never
invent data, never predict or give buy/sell calls, always end by asking *you* the
bias-forming questions, and always append a **verify-at-source** reminder.

### Options

```
--config PATH   Config JSON (default: agents/config.json, else config.example.json)
--inputs PATH   Today's inputs (default: agents/inputs/briefing-inputs.md, else the example)
--date YYYY-MM-DD   Date label (default: today)
--ai            Let Claude synthesise (needs ANTHROPIC_API_KEY)
--print         Also echo the briefing to the terminal
```

### Safety (Vol. 11, Ch. 8)

- **Verify everything.** Event times, prices, and rates are a *draft* until you confirm
  them at the source. A wrong NFP time is the fastest way to get hurt.
- **No secrets.** Never put broker logins or account numbers in your inputs — trade
  context is enough.
- **It prepares; you decide.** Don't ask it "what should I trade?" — that's the oracle
  trap. It hands you a clean briefing; the bias and the trade are yours.

---

*More agents (Journal & Analytics, Trade-Plan Gatekeeper, …) can follow the same pattern —
see [Vol. 11, Ch. 2](../vol-11-ai-agents/02-agent-architecture.md) for the build order.*
