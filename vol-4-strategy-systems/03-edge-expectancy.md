# Chapter 3 — Edge, Expectancy & the Math of Profitability

[← Designing a Strategy](02-designing-a-strategy.md) | [Volume 4 Home](README.md) | [Next: Backtesting Properly →](04-backtesting.md)

---

This chapter is the **mathematical heart** of the whole series. Everything — your strategy, your backtest, your journal — exists to answer one question: *does this have a positive **edge**?* Master expectancy and you'll understand profitability more deeply than most retail traders ever do. The math is simple arithmetic; the implications are profound.

---

## 3.1 What "edge" actually means

An **edge** is a *statistical* advantage: a system whose average outcome per trade is positive after costs. It does **not** mean winning often, predicting the future, or being right on the next trade. It means that if you take the trade many times, the math is in your favor.

> 🔑 A casino has an edge of a few percent on roulette. It loses *individual* spins constantly — and is wildly profitable, because it plays the edge over millions of bets. **You are the casino, not the gambler.** Your job is to find a positive edge and execute it enough times for the math to express itself.

---

## 3.2 R-multiples — the universal unit (recap from Vol 1)

Express every result in **R**, where **1R = the amount you risked** on that trade.
- Risk $50, make $150 → **+3R**. Risk $50, lose it → **−1R**.
- R standardizes everything regardless of account size or position size, so you can compare and aggregate trades cleanly. **All the math below uses R.**

---

## 3.3 Expectancy — the single most important number ⭐

**Expectancy** is your average profit (or loss) **per trade**, in R. It is the definition of whether you have an edge.

```
Expectancy (R) = (Win% × Average Win in R) − (Loss% × Average Loss in R)
```

### Worked example
A system wins 40% of the time. Winners average +2.5R; losers average −1R.
```
Expectancy = (0.40 × 2.5R) − (0.60 × 1.0R)
           = 1.00R − 0.60R
           = +0.40R per trade
```
**+0.40R expectancy** means that, on average, every trade earns you 0.4× your risk. Over 100 trades risking 1% each, that's roughly **+40R** of edge expressed (before compounding and variance). A **positive expectancy is the mathematical proof of an edge.** Negative expectancy means no position sizing or psychology can save the system — it must be fixed or abandoned.

---

## 3.4 The win-rate trap: why win% alone is meaningless

Beginners chase high win rates. But win rate is **half** of the equation — and the less important half. Win rate and reward:risk **trade off against each other**:

| Win rate | Avg win | Avg loss | Expectancy (R) | Verdict |
|----------|---------|----------|----------------|---------|
| 90% | +0.5R | −5R | (0.9×0.5) − (0.1×5) = **−0.05R** | **Loses** despite 90% wins |
| 50% | +2R | −1R | (0.5×2) − (0.5×1) = **+0.50R** | Strong edge |
| 35% | +3R | −1R | (0.35×3) − (0.65×1) = **+0.40R** | Strong edge, low win rate |
| 60% | +1R | −1R | (0.6×1) − (0.4×1) = **+0.20R** | Solid edge |

> 🔑 **A 90% win rate can lose money; a 35% win rate can be highly profitable.** Stop asking "how often do I win?" and start asking "what's my expectancy?" This single reframe immunizes you against the most common beginner delusion — and against the snake-oil sellers who advertise win rates.

---

## 3.5 Profit factor — a quick health check

**Profit factor** = total gross profit ÷ total gross loss (in $ or R).

```
Profit Factor = Σ(winning trades) / Σ(losing trades, absolute)
```
- **PF < 1.0** → losing system.
- **PF ≈ 1.0–1.3** → marginal.
- **PF 1.3–1.7** → good, tradeable.
- **PF > 2.0** → excellent (be suspicious if a backtest shows this — possible overfitting, Ch. 4).

Profit factor and expectancy tell related stories; report both. PF is intuitive ("for every $1 I lose, I make $X"); expectancy tells you per-trade edge.

---

## 3.6 Sample size — why 10 trades tell you nothing

A positive result over a few trades is **noise**, not evidence. Variance dominates small samples.

- **Any system can win (or lose) 5–10 in a row by pure luck.** Drawing conclusions from a handful of trades is the road to ruin — you'll trust a lucky losing system or abandon a good one in an unlucky streak.
- **Rules of thumb:**

| Sample size | What it tells you |
|-------------|-------------------|
| < 20 trades | Essentially nothing — pure noise |
| 30 trades | Rough hint, low confidence |
| **100+ trades** | Meaningful estimate of your edge |
| 300+ trades | Solid confidence in the statistics |

> 🔑 **The law of large numbers is your ally and your judge.** An edge only reveals itself over a large sample. This is *why* backtesting (Ch. 4) and patient journaling (Ch. 6) matter — they're how you accumulate a sample big enough to trust. Never judge a system, or yourself, on a small number of trades.

---

## 3.7 Variance, losing streaks & drawdown

Even a great positive-expectancy system has **brutal losing streaks** — this is normal and unavoidable.

- With a 40% win rate, a run of **8+ consecutive losses** is statistically expected over a few hundred trades. If that streak would break you (financially or emotionally), your *risk per trade is too high* (Vol 1).
- **Drawdown** (peak-to-trough equity decline) is the cost of admission for the edge. You must know your system's likely drawdown *in advance* so you can survive it without panicking or abandoning a working system.
- **Expectancy tells you the edge; drawdown tells you whether you can survive long enough to collect it.** Both matter.

```
The two questions every system must answer:
   1. Is expectancy positive?        → Do I have an edge at all?
   2. Can I survive the drawdown?     → Will I still be here when it pays off?
```

---

## 3.8 Putting it together — the profitability identity

```
Long-run profit  ≈  Expectancy (R)  ×  Number of trades  ×  Risk per trade ($)

To grow the account, you can:
   • Raise expectancy   → better strategy / filters / exits (Ch. 8)
   • Take more (quality) trades → more opportunities at the SAME edge
   • Increase risk per trade   → ⚠️ amplifies drawdown too; change LAST and SLOWLY

Survival constraint: risk per trade must be small enough to outlast the
worst expected losing streak. Edge means nothing if you blow up first.
```

> 🔑 The professional path is: **establish a positive expectancy → execute it over a large sample with survivable risk → only then scale.** Most blow-ups come from inverting this — scaling risk before proving the edge. Get the math right and trading becomes what it should be: the patient harvesting of a measured edge.

---

## 3.9 Chapter summary

```
• EDGE = positive average outcome per trade after costs (statistical, not predictive).
• Work in R-MULTIPLES (1R = amount risked).
• EXPECTANCY = (Win% × AvgWinR) − (Loss% × AvgLossR). Positive = an edge. THE key number.
• Win rate alone is meaningless: 90% can lose, 35% can win. It's win% AND reward:risk.
• PROFIT FACTOR = gross profit / gross loss (1.3–1.7 good; >2 suspect overfitting).
• SAMPLE SIZE: need 100+ trades for meaningful stats; <20 is pure noise.
• Positive-expectancy systems still have long losing streaks & drawdowns — size to survive them.
• Profit ≈ expectancy × #trades × risk. Prove the edge first; scale risk last.
```

---

[← Designing a Strategy](02-designing-a-strategy.md) | [Volume 4 Home](README.md) | [Next: Backtesting Properly →](04-backtesting.md)
