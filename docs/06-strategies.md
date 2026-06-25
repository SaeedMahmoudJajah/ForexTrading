# 6. Strategies & Trading Styles

[← Risk Management](05-risk-management.md) | [Back to README](../README.md) | [Next: Psychology →](07-psychology.md)

---

A **trading style** is how often and how long you trade. A **strategy** is the specific rule-set for entering and exiting. First pick a style that fits your personality and schedule; then adopt **one** concrete strategy and master it before adding others.

---

## 6.1 The four trading styles

| Style | Hold time | Timeframes | Trades | Screen time | Best for |
|-------|-----------|-----------|--------|-------------|----------|
| **Scalping** | Seconds–minutes | M1–M5 | Many/day | Constant, intense | Fast reflexes, full-time focus, high discipline |
| **Day Trading** | Minutes–hours (flat by day's end) | M5–H1 | A few/day | Several hours/day | People who can dedicate sessions, dislike overnight risk |
| **Swing Trading** | Days–weeks | H4–D1 | A few/week | Check a few times/day | **Most beginners** & people with jobs |
| **Position Trading** | Weeks–months | D1–W1 | A few/month | Occasional | Patient, macro-minded, long-term thinkers |

### Which should a beginner choose?
**Swing trading (or higher-timeframe day trading)** is usually best to start:
- Slower pace = time to *think*, analyze, and decide without panic.
- Fewer trades = **lower costs** (spreads/commissions) and less screen addiction.
- Bigger stops/targets = small position sizes, less sensitivity to spread.
- Works around a job — you don't need to watch screens all day.

**Scalping is the hardest place to start**, despite looking exciting: costs eat tiny profits, it demands elite discipline and speed, and emotions fire constantly. Most beginners who scalp lose fastest.

---

## 6.2 Trend-following vs. mean-reversion (the two great families)

Almost every strategy is one of these (or a blend):

### Trend-following / momentum
*"The trend is your friend."* You enter **in the direction of** an established trend, expecting it to continue.
- **Pros:** Big winners when a trend runs; high R:R; psychologically aligned with "ride your winners."
- **Cons:** Lower win rate (many false starts); painful in choppy, sideways markets.

### Mean-reversion / range trading
You bet price will **return to an average** after stretching too far — buying support and selling resistance within a range.
- **Pros:** Higher win rate; clear levels to trade against.
- **Cons:** Smaller winners; **catastrophic if the range breaks** into a trend and you keep fading it. Disciplined stops are essential.

> A simple rule of thumb: **trend-follow when the market is trending, range-trade when it's ranging.** Telling which regime you're in (e.g. via higher-timeframe structure or a moving average's slope) is half the battle.

---

## 6.3 Concrete beginner strategies (with full rules)

Below are three simple, well-defined strategies. **These are educational examples to learn structure from — not guaranteed money-makers.** Backtest and demo-trade any strategy before risking real money.

### Strategy A — Trend Pullback (swing/day trading) ⭐ recommended starter
The classic "buy the dip in an uptrend." High-probability and beginner-friendly.

```
MARKET:    Trending market (avoid in choppy ranges).
TOOLS:     50 EMA for trend; key support/resistance; candlesticks.

LONG SETUP (mirror for shorts):
1. Higher timeframe (H4/D1) is in a clear UPTREND (higher highs/lows, price above rising 50 EMA).
2. Wait for a PULLBACK down to a support level or the 50 EMA.
3. ENTRY: a bullish confirmation candle at that level (e.g. bullish engulfing or pin bar).
4. STOP: just below the pullback low / support (with a small buffer).
5. TARGET: the prior swing high or next resistance — require R:R ≥ 1:2.
6. SIZE: per your 1% risk rule.
```
Why it works: you join a proven trend at a discount, with a tight, logical stop → strong R:R.

### Strategy B — Support/Resistance Range Bounce (mean-reversion)
For clearly ranging markets between horizontal levels.

```
MARKET:    Sideways/ranging (price bouncing between defined support & resistance).
1. Identify a clean range: a support floor and resistance ceiling tested 2+ times each.
2. BUY near SUPPORT (with a bullish confirmation candle); SELL near RESISTANCE (bearish candle).
3. STOP: just OUTSIDE the range (below support for longs / above resistance for shorts).
4. TARGET: the opposite side of the range.
5. EXIT THE IDEA if price CLOSES decisively outside the range — the range has broken; do not fight it.
```

### Strategy C — Breakout (momentum)
Catches the start of a new move when price escapes a level/consolidation.

```
MARKET:    Consolidation/tight range OR approaching a major level, ideally with rising volatility.
1. Mark a clear level or consolidation boundary.
2. ENTRY: when price CLOSES decisively beyond the level (use a candle close, not just a wick poke,
   to reduce false breakouts). Optional: wait for a retest of the broken level as new support/resistance.
3. STOP: back inside the range/level.
4. TARGET: measured move (e.g. the height of the range projected from the breakout) or next major S/R.
WATCH OUT: "fakeouts" are common — requiring a candle close and/or a retest filters many of them.
```

---

## 6.4 What about automated trading (bots/EAs) and signals?

- **Expert Advisors (EAs) / algos** — software that trades for you. Real algorithmic trading is legitimate but requires programming + deep testing. **The EAs sold online promising automatic riches are almost always scams or curve-fit junk.** Don't outsource your learning to a black box.
- **Signal services / copy trading** — following someone else's calls. You learn nothing, can't verify the track record, and most are mediocre-to-fraudulent. **Skip them** while learning. If you ever use copy trading, treat it as a tiny, high-risk experiment, not a strategy.

---

## 6.5 How to actually adopt a strategy

1. **Pick ONE** strategy that matches your style and schedule. Resist collecting strategies.
2. **Write its exact rules** into your [trading plan](../templates/trading-plan.md) — entry, stop, target, filters, what invalidates it.
3. **Backtest** it: scroll back through historical charts and manually mark where it would have triggered. Record the results.
4. **Demo-trade** it forward for **at least 1–2 months** and 30–50+ trades. [Journal](../templates/trading-journal.md) every one.
5. **Review** the stats: win rate, average R, expectancy, biggest drawdown. Is the edge positive?
6. **Only then** go live — small (micro lots, 0.5% risk) — and keep journaling.
7. **Refine slowly.** Change one variable at a time. Don't abandon a sound strategy after a few losers — variance is normal. Abandon it only if the *data* over many trades says the edge is negative.

> 🔑 **The strategy matters far less than your consistency and risk management.** A mediocre strategy executed with discipline and tight risk beats a "perfect" strategy executed emotionally. **Edge comes from the trader, not just the setup.**

---

[← Risk Management](05-risk-management.md) | [Back to README](../README.md) | [Next: Psychology →](07-psychology.md)
