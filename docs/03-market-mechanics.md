# 3. Market Mechanics — How Trading Actually Works

[← Terminology](02-terminology.md) | [Back to README](../README.md) | [Next: Analysis →](04-analysis.md)

---

This section turns vocabulary into mechanics. By the end you'll be able to read a quote, understand exactly what you're buying, calculate what a trade is worth, and know the real cost of every position.

---

## 3.1 Reading a quote (in depth)

A forex quote looks like this:

```
EUR/USD   Bid 1.08495   Ask 1.08505
```

- **EUR** is the **base** — what you're trading.
- **USD** is the **quote** — what the price is measured in.
- **Bid 1.08495** — the price you can **SELL** at.
- **Ask 1.08505** — the price you can **BUY** at.
- **Spread** = Ask − Bid = 1.08505 − 1.08495 = **0.00010 = 1.0 pip**.

> 🔑 **Golden rule of the spread:** You buy at the higher price (ask) and sell at the lower price (bid). So the **instant** you open a trade, you're down by the spread. Price must move *at least* the spread in your favor just to break even.

### Direct vs. indirect quotes
- A pair like **USD/JPY = 150.20** tells you how many yen one dollar buys.
- A pair like **EUR/USD = 1.0850** tells you how many dollars one euro buys.
- The logic is always identical: **price = how much quote currency for one unit of base currency.**

---

## 3.2 Pips, pipettes & price moves — the math

### What is a pip, precisely?
- **Non-JPY pairs:** 1 pip = 0.0001 (4th decimal).
- **JPY pairs:** 1 pip = 0.01 (2nd decimal).
- A **pipette** is 1/10 of a pip (the 5th / 3rd decimal). Modern brokers quote with the extra digit for precision.

### Counting pips
| Pair | From | To | Pips moved |
|------|------|-----|-----------|
| EUR/USD | 1.0850 | 1.0875 | 25 pips |
| GBP/USD | 1.2700 | 1.2660 | 40 pips (down) |
| USD/JPY | 150.20 | 150.95 | 75 pips |

---

## 3.3 Lots & position size — what each pip is worth

Your **position size** (in lots) determines the **dollar value of each pip**, which determines how much you win or lose per pip of movement.

For pairs where **USD is the quote currency** (e.g. EUR/USD, GBP/USD, AUD/USD), pip values are clean:

| Lot size | Units | Value per pip |
|----------|-------|---------------|
| 1 Standard lot | 100,000 | **$10.00** |
| 1 Mini lot | 10,000 | **$1.00** |
| 1 Micro lot | 1,000 | **$0.10** |
| 1 Nano lot | 100 | **$0.01** |

### Worked example
You buy **0.10 lots (1 mini lot)** of EUR/USD at 1.0850. Pip value ≈ **$1/pip**.
- Price rises to 1.0875 → **+25 pips × $1 = +$25 profit.**
- Price falls to 1.0835 → **−15 pips × $1 = −$15 loss.**

> If you'd traded **1 standard lot** instead, every number above is ×10: +$250 or −$150. **Same market, same move — position size is the dial that controls your risk.** This is why beginners trade micro lots.

### Pip value when USD is NOT the quote currency
For pairs like USD/JPY or USD/CHF, pip value depends on the exchange rate and your account currency. Your trading platform calculates this automatically — but the principle is the same. **Always use a position-size calculator** (built into most platforms, or free online) rather than eyeballing it.

---

## 3.4 Leverage & margin — the double-edged sword

### How leverage works
Leverage lets you control a big position with a small deposit (margin).

**Example — 30:1 leverage, want to trade 1 mini lot ($10,000 position) of EUR/USD:**
- Required margin = position ÷ leverage = $10,000 ÷ 30 = **$333**.
- So $333 of your money controls $10,000 of currency.

### Why it's dangerous
Leverage doesn't change the *market* — it changes **how much of your account is exposed.** Consider a $1,000 account:

| Leverage used | Position size | A 1% adverse move (100 pips on EUR/USD) costs | % of account lost |
|---------------|--------------|------------------------------------------------|-------------------|
| Effectively 1:1 ($1,000 position) | 0.01 lots | ~$10 | 1% |
| 10:1 ($10,000 position) | 0.10 lots | ~$100 | 10% |
| 30:1 ($30,000 position) | 0.30 lots | ~$300 | **30%** |
| 100:1 ($100,000 position) | 1.0 lot | ~$1,000 | **100% — account wiped** |

> 🔑 **The leverage your broker offers is a maximum, not a target.** Pros often use *effective* leverage of just 2:1 to 5:1. Beginners blow up because they treat high leverage as free money. **You control your real risk through position size and stop loss — not through the leverage number.** See [Risk Management](05-risk-management.md).

---

## 3.5 The full lifecycle of a trade

```
1. ANALYSIS        → You spot a setup (e.g. EUR/USD bouncing off support in an uptrend).
2. PLAN THE TRADE  → Decide entry, stop loss, take profit BEFORE entering.
3. SIZE THE TRADE  → Calculate lot size so the stop = your fixed % risk (e.g. 1%).
4. EXECUTE         → Place the order (market/limit/stop), with SL and TP attached.
5. MANAGE          → Leave it alone, or trail the stop. Do NOT move your stop further away.
6. EXIT            → TP hits (win), SL hits (controlled loss), or you close manually.
7. JOURNAL         → Record everything. Review. Learn. Repeat.
```

The amateur skips steps 2, 3, and 7. Don't.

---

## 3.6 The real cost of trading

Every trade has costs that your edge must overcome:

1. **Spread** — paid on every trade (built into bid/ask). On EUR/USD it might be ~0.5–1 pip.
2. **Commission** — on ECN/raw accounts, often ~$3.50 per side per standard lot.
3. **Swap/rollover** — if you hold overnight (can be + or −).
4. **Slippage** — occasional, worse in fast markets.

> **Why this matters:** If you scalp for 3-pip gains but pay a 1-pip spread, costs eat a *third* of every winner. Frequent trading multiplies costs. This is a major reason high-frequency styles are hard for beginners — your costs scale with your activity.

---

## 3.7 Choosing what and when to trade

### What to trade (beginner)
- **Stick to 1–3 major pairs.** EUR/USD is the classic starting point: tightest spreads, most liquid, heavily analyzed, well-behaved.
- Avoid exotics (wide spreads, wild moves) and avoid trading 20 pairs at once (you can't follow them all).

### When to trade
- Trade during **high-liquidity sessions** — ideally the **London–New York overlap** (~12:00–16:00 GMT).
- **Check the [economic calendar](04-analysis.md) daily.** Know when high-impact news (NFP, CPI, central-bank decisions) hits — it can cause violent spikes and slippage.
- As a beginner, consider **not** trading in the minutes around major red-flagged news.

---

## 3.8 Putting it together — a full worked trade

**Setup:** Your account is $2,000. EUR/USD is in an uptrend and pulls back to support at 1.0850. You plan a long trade.

1. **Entry:** Buy at 1.0850.
2. **Stop loss:** 1.0820 (30 pips below — beneath the support).
3. **Take profit:** 1.0910 (60 pips above) → **R:R = 1:2**.
4. **Risk budget:** 1% of $2,000 = **$20 max loss**.
5. **Position size:** You're risking 30 pips. To lose only $20, each pip must be worth $20 ÷ 30 = **$0.67/pip**. That's ~**0.067 lots** → round down to **0.06 lots** (6 micro lots) to stay safe.
6. **Outcome A — TP hits:** +60 pips × ~$0.60/pip = **+$36** (≈ +1.8R).
7. **Outcome B — SL hits:** −30 pips × ~$0.60/pip = **−$18** (≈ −1R). A controlled, survivable loss.

Notice: you decided *exactly* how much you could lose **before** entering, and sized the trade to fit that limit. **That is professional trading in a nutshell.**

---

[← Terminology](02-terminology.md) | [Back to README](../README.md) | [Next: Analysis →](04-analysis.md)
