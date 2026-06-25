# Chapter 4 — Backtesting Properly

[← Edge & Expectancy](03-edge-expectancy.md) | [Volume 4 Home](README.md) | [Next: Forward Testing →](05-forward-testing.md)

---

**Backtesting** is applying your strategy's rules to *historical* data to estimate its edge before risking money. Done well, it's the cheapest way to learn whether a strategy is worth trading. Done badly — which is how *most* people do it — it produces beautiful, completely worthless results that lead straight to live losses. This chapter teaches the discipline that makes backtesting honest.

> ⚠️ **The central warning of this volume:** it is trivially easy to produce a backtest that looks amazing and predicts nothing. The market's history is full of patterns that existed by chance and never repeat. Your enemy in backtesting is **not the market — it's your own ability to fool yourself.** Everything below is about defeating that.

---

## 4.1 What backtesting can and can't do

**It CAN:**
- Estimate expectancy, win rate, profit factor, and drawdown over a large sample.
- Quickly reject bad strategies (saving real money).
- Build your familiarity with how a strategy behaves.

**It CAN'T:**
- Guarantee future results — *past performance does not predict the future.*
- Capture your real-world psychology, slippage, or execution mistakes.
- Save a strategy with no logical edge from eventually failing.

> 🔑 Treat a backtest as **evidence, not proof.** A good backtest earns a strategy the right to be *forward-tested* (Ch. 5) — never the right to be trusted with size immediately.

---

## 4.2 Two ways to backtest

### Manual backtesting (start here)
Scroll back through historical charts (bar-by-bar replay, e.g. TradingView's replay or MT4's strategy tester in visual mode), find every instance of your setup, and **log each hypothetical trade** (entry, stop, target, result in R).
- ✅ Builds deep intuition and chart-reading skill; works for discretionary strategies; no coding.
- ❌ Slow; vulnerable to **hindsight bias** (it's tempting to "see" trades you'd have missed live).

### Automated backtesting
Code the rules and run them over historical data (MT4/MT5 Expert Advisors, Python with libraries, TradingView Pine Script strategies, dedicated platforms).
- ✅ Fast, tests thousands of trades, perfectly consistent, only works for fully mechanical rules.
- ❌ Requires coding; **far easier to curve-fit**; only as good as your data and assumptions.

**Most retail traders should start manual** to build judgment, then automate the mechanical parts once the logic is proven.

---

## 4.3 The seven deadly biases (how backtests lie to you)

These are the ways a backtest produces fake results. Know each one by name so you can hunt it down.

### 1. Curve-fitting / Overfitting ⭐ (the big one)
Tuning rules and parameters until they fit the historical data *perfectly* — capturing **noise**, not edge. A curve-fit system looks flawless on the past and falls apart live.
- **Tells:** many parameters, oddly specific values (e.g. "RSI 27.5", "exit after 13 bars"), incredible equity curve, performance collapses if you nudge any setting.
- **Defense:** few parameters, logical rules, and **out-of-sample testing** (4.4).

### 2. Look-ahead bias
Using information that wouldn't have been available at decision time (e.g. using a candle's close to enter *at* that close, or referencing future bars). Inflates results impossibly.
- **Defense:** only act on data that was knowable *before* the decision point.

### 3. Hindsight bias (manual testing's curse)
Unconsciously taking the trades you *know* worked and skipping the ambiguous ones. Your rules feel clearer in hindsight than they were live.
- **Defense:** mechanical, pre-written rules; use bar-replay so you can't see the future; log *every* qualifying setup, including the losers and the ugly ones.

### 4. Survivorship bias
Testing only on instruments/periods that "survived" or trended nicely, ignoring the ones that died or chopped. Common when cherry-picking a pair that happened to trend.
- **Defense:** test across multiple pairs and varied market regimes.

### 5. Optimization / data-snooping bias
Trying hundreds of variations and picking the best — by chance, *something* will look great on past data. You've selected for luck.
- **Defense:** out-of-sample/walk-forward validation; limit how much you optimize.

### 6. Ignoring costs
Backtesting without spread, commission, and slippage. A strategy with small average wins can be profitable on paper and a loser after real costs (Vol 1).
- **Defense:** subtract realistic spread/commission/slippage from every simulated trade.

### 7. Unrealistic execution
Assuming perfect fills at exact prices, no requotes, trading illiquid hours, or sizes the market couldn't absorb.
- **Defense:** model conservative, realistic fills; assume you get the *worse* side of ambiguity.

---

## 4.4 In-sample vs out-of-sample — the honesty test ⭐

The most important technique for trustworthy backtesting: **split your data.**

```
┌──────────────────────────────┬───────────────────────────┐
│   IN-SAMPLE (e.g. 70%)       │   OUT-OF-SAMPLE (e.g. 30%) │
│   Build & refine the strategy│   NEVER touched during dev │
│   here. Optimize here.       │   Used ONCE to validate.   │
└──────────────────────────────┴───────────────────────────┘
```

- Develop and tune the strategy **only** on the in-sample data.
- Then run it **once** on the untouched out-of-sample data. If performance **holds up**, the edge is likely real. If it **collapses**, you curve-fit — back to the drawing board.
- **Walk-forward analysis** extends this: repeatedly optimize on a window, test on the next unseen window, and roll forward — simulating how the strategy would have adapted over time. It's the gold standard for mechanical systems.

> 🔑 **If a strategy only works on the data you built it on, it doesn't work.** Out-of-sample validation is the difference between discovering an edge and memorizing the past. Protect your out-of-sample data like gold — you only get to use it honestly once.

---

## 4.5 A disciplined backtesting procedure

```
1. SPECIFY    Write the exact rules first (Ch. 2). Do NOT change them mid-test.
2. SPLIT      Reserve out-of-sample data you won't look at during development.
3. SAMPLE     Test enough trades (100+) across varied conditions & multiple pairs.
4. LOG        Record EVERY qualifying trade in R — winners, losers, and ugly ones.
              (Use the backtest log template, Ch. 9.)
5. COST       Subtract realistic spread/commission/slippage from each trade.
6. MEASURE    Compute expectancy, win%, profit factor, max drawdown (Ch. 7).
7. VALIDATE   Run ONCE on out-of-sample data. Does the edge survive?
8. DECIDE     Meets your pre-set criteria (Ch. 2)? → forward-test. If not → revise or kill.
```

---

## 4.6 Interpreting results with healthy skepticism

- **Too good to be true usually is.** A 90% win rate or PF > 3 in backtest screams overfitting or a bug (often look-ahead bias). Real edges are modest.
- **Look at the equity curve, not just the bottom line.** A smooth, steady rise is more trustworthy than a jagged line that made all its money in one freak period. Check the **drawdowns** — could you stomach the worst one *live*?
- **Check trade distribution.** Is the profit spread across many trades, or dependent on a few outliers? Outlier-dependent results are fragile.
- **Stress-test:** does it still work if you shift parameters slightly, test a different period, or another pair? Robust edges degrade *gracefully*; fitted ones break.

> 🔑 The right attitude is **active distrust of your own backtest.** Assume it's flawed and try to break it. The strategies that survive your honest attempts to disprove them are the ones worth real money.

---

## 4.7 Chapter summary

```
• Backtesting = applying rules to history to estimate edge. Evidence, not proof.
• Manual builds intuition (start here); automated is fast but easy to curve-fit.
• Beware the 7 biases: OVERFITTING, look-ahead, hindsight, survivorship,
  optimization/data-snooping, ignored costs, unrealistic execution.
• OUT-OF-SAMPLE validation is the honesty test: develop on in-sample, validate ONCE
  on untouched data. Walk-forward is the gold standard. If it only works where you
  built it, it doesn't work.
• Always include realistic costs. Demand 100+ trades across varied conditions.
• Distrust beautiful results; inspect the equity curve, drawdowns, and trade distribution.
```

A backtest that survives this discipline has earned the right to be tested *forward* — on data the strategy has never seen, in conditions closer to real trading. That's Chapter 5.

---

[← Edge & Expectancy](03-edge-expectancy.md) | [Volume 4 Home](README.md) | [Next: Forward Testing →](05-forward-testing.md)
