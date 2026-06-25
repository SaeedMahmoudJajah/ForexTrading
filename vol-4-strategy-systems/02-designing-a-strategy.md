# Chapter 2 — Designing a Strategy

[← From Knowledge to a System](01-trading-system.md) | [Volume 4 Home](README.md) | [Next: Edge & Expectancy →](03-edge-expectancy.md)

---

A strategy starts as an **idea** and must become a **specification** precise enough to test, journal, and execute identically every time. This chapter is the workshop where that transformation happens.

---

## 2.1 Start with a hypothesis (an edge you can state in one sentence)

Every strategy is really a **hypothesis about market behavior** — a claim that *"when condition X occurs, price tends to do Y often enough to be profitable after costs."* Examples:

- *"In a strong daily uptrend, pullbacks to a fresh demand zone tend to resume the trend."*
- *"After London-session consolidation, a break of the range tends to run during the New York session."*
- *"Following a bullish RSI divergence at a major support level, price tends to reverse upward."*

> 🔑 If you can't state your edge in a single clear sentence, you don't understand it well enough to test it. **Vagueness is the enemy of validation.** "I buy when it looks good" is not a hypothesis.

Good hypotheses come from: the technical concepts in Vol 3, observed market behavior, the principles of the masters in Vol 2, or a logical cause (e.g. session liquidity, central-bank themes from Vol 1). Avoid hypotheses with **no logical reason** behind them — random correlations don't survive forward into the future.

---

## 2.2 The strategy specification — turn the idea into rules

Take your hypothesis and define **every** component until it's unambiguous. This is your **strategy spec sheet** (full template in [Chapter 9](09-templates.md)):

```
STRATEGY NAME:   ____________________________________

1. HYPOTHESIS / EDGE (one sentence):
   _________________________________________________

2. MARKET(S):        Which pairs, and why they suit this edge
3. TIMEFRAMES:       Bias TF + setup TF + entry TF
4. CONDITION FILTER: When is this strategy VALID / INVALID?
                     (e.g. ADX>25 trend only; specific session; not around red news)

5. ENTRY RULES (exact & repeatable):
   • Trigger 1: ____________________________________
   • Trigger 2: ____________________________________
   • Everything that must be TRUE to enter

6. STOP-LOSS RULE:   Where & why (structure / ATR-based); the invalidation point
7. TAKE-PROFIT RULE: Target(s), trailing, scaling-out logic
8. MIN RISK:REWARD:  e.g. ≥ 1:2

9. RISK PER TRADE:   ____ % (≤1%); position-size formula
10. TRADE MANAGEMENT: break-even rule, partials, max hold time
11. WHAT INVALIDATES THE WHOLE STRATEGY: when do you STOP trading it?
```

The test of a good spec (from Ch. 1): a disciplined stranger could read it and take the same trades you would.

---

## 2.3 The building blocks, in detail

### Market & instrument selection
- Match the pair to the edge. A breakout strategy wants volatile, trending pairs; a range strategy wants ones that respect levels. Spreads/costs matter (Vol 1) — a scalp edge dies on wide-spread exotics.
- **Start narrow:** 1–3 pairs. You can't meaningfully test or monitor twenty.

### Timeframe selection
- Pick a **bias TF**, a **setup TF**, and an **entry TF** (~4–6× apart — Vol 3, Ch. 8). The combination must fit your available screen time and personality (swing vs day vs scalp — Vol 1).

### Condition filters — *when NOT to trade*
This is where amateurs leave money on the table. A strategy that's brilliant in trends is a disaster in ranges. Define the **regime** it needs:
- Trend vs range (e.g. ADX, structure, MA slope).
- Session/time-of-day (liquidity).
- News blackout windows (avoid high-impact releases).

> 🔑 A huge portion of edge comes from **not** trading the strategy when conditions are wrong. The filter is as important as the entry.

### Entry rules — the trigger
Define the *exact* event that puts you in: e.g. *"a bullish engulfing candle closing inside the demand zone, with the entry-TF making a CHoCH up."* Specify whether you enter on the close, on a retest, or via a limit order at a level.

### Exit rules — stop & target (the part that actually pays)
- **Stop:** at the **invalidation point** — the price that proves the hypothesis wrong (beyond structure / a multiple of ATR), with a buffer (Vol 3).
- **Target:** logical level / measured move / Fib extension, or a multiple of R. Define trailing and scaling rules explicitly.

### Risk & sizing
Fixed % risk (≤1%) and the position-size formula (Vol 1; sizing models deepened in Ch. 8). This is constant across the system, independent of the setup.

---

## 2.4 Keep it simple — complexity is fragility

A frequent beginner mistake is piling on conditions ("RSI < 30 AND MACD cross AND 3 MAs aligned AND a doji AND Fibonacci AND...") believing more rules = more accuracy.

The opposite is usually true:
- **More parameters = more curve-fitting** (Chapter 4). A rule with ten conditions can be tuned to fit the past perfectly and fail completely in the future.
- **Simple, logical strategies are more robust** — they capture a *real* behavior rather than memorizing historical noise.
- Each added rule needs *more* data to validate and reduces the number of trades, weakening your statistics.

> 🔑 **Aim for the fewest rules that capture a genuine edge.** Robustness beats complexity. If a strategy needs five exotic filters to look good in backtest, it's probably fitting noise, not finding an edge.

---

## 2.5 Define how you'll measure success *before* testing

Decide your acceptance criteria *now*, so you can't move the goalposts later (a classic self-deception):

```
Before testing, write down the MINIMUMS you'll require to trade it live:
  • Positive EXPECTANCY over the sample (Ch. 3)
  • Profit factor ≥ ____ (e.g. 1.3+)
  • Max drawdown ≤ ____ % (tolerable for you)
  • Minimum sample size ≥ ____ trades (e.g. 100)
  • Acceptable on OUT-OF-SAMPLE data, not just in-sample (Ch. 4)
```

Pre-committing to these numbers is what keeps backtesting *honest* (Chapter 4 is all about the ways we fool ourselves).

---

## 2.6 Chapter summary

```
• Every strategy = a one-sentence HYPOTHESIS about market behavior, with a logical reason.
• Forge it into a precise SPEC SHEET covering market, timeframes, condition filter,
  entry, stop, target, R:R, risk/sizing, management, and invalidation.
• A big edge lies in the CONDITION FILTER — knowing when NOT to trade it.
• Obsess over exits & sizing as much as entries.
• Keep it SIMPLE: fewer, logical rules are more robust; complexity = curve-fitting.
• Pre-commit to your success criteria (expectancy, profit factor, drawdown, sample)
  BEFORE you test, so you can't fool yourself later.
```

You have a defined strategy. Before testing it, you need to understand the **math that decides whether any strategy is actually profitable** — that's Chapter 3.

---

[← From Knowledge to a System](01-trading-system.md) | [Volume 4 Home](README.md) | [Next: Edge & Expectancy →](03-edge-expectancy.md)
