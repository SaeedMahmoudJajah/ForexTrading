# Chapter 7 — Performance Metrics & Analytics

[← The Journaling System](06-journaling-system.md) | [Volume 4 Home](README.md) | [Next: Optimizing & Sizing →](08-optimizing-sizing.md)

---

Your journal (Chapter 6) is now a database of trades. This chapter is the **analytics layer** — the specific metrics (KPIs) that turn that data into a precise diagnosis of your trading: not just *whether* you're profitable, but *why*, and *where the leaks are*. These are the numbers professionals live by.

---

## 7.1 The core profitability KPIs

These five answer "do I have an edge, and how strong?" (foundations from Chapter 3):

| KPI | Formula | What it tells you | Healthy range |
|-----|---------|-------------------|---------------|
| **Win rate** | wins ÷ total | How often you win (context only!) | Any — judge with R |
| **Avg win / Avg loss (R)** | mean win R, mean loss R | The *size* side of the edge | Avg win > avg loss ideal |
| **Expectancy (R)** ⭐ | (Win%×AvgWinR) − (Loss%×AvgLossR) | **Average profit per trade — the edge** | > 0; higher better |
| **Profit factor** | gross profit ÷ gross loss | $ made per $ lost | 1.3–1.7 good; >2 suspect |
| **R-expectancy × #trades** | total R captured | Total edge expressed | Trending up |

> 🔑 Report **expectancy and profit factor together**, always alongside **sample size**. A great expectancy over 12 trades means nothing (Ch. 3). The number of trades is the confidence level on every other metric.

---

## 7.2 Risk & survival KPIs

Profitability tells you the upside; these tell you whether you'll *survive* to collect it.

### Maximum drawdown ⭐
The largest peak-to-trough fall in your equity, in % (or R). **The single most important risk metric** — it's the worst pain the system put you through, and a preview of what you must be able to endure live.
- Know it *before* going live so a normal drawdown doesn't make you abandon a working system.
- Recovery math is brutal (Vol 1): −50% needs +100% to recover. Keeping max drawdown modest is survival.

### Longest losing streak
The most consecutive losers. Tells you the emotional and financial endurance the system demands. If the streak would break you at your risk %, **lower the risk %.**

### Risk of ruin
The probability of losing enough to be unable to continue, given your edge, win rate, and risk per trade. The practical takeaway: **small risk per trade (≤1%) + positive expectancy = risk of ruin near zero.** Large risk per trade can produce meaningful ruin probability *even with a positive edge.*

### Return / drawdown ratio
Net return ÷ max drawdown — "how much pain per unit of gain." Higher is better; it captures *risk-adjusted* performance better than raw return alone.

---

## 7.3 The equity curve — your trading at a glance ⭐

Plot **cumulative R** (or account balance) trade by trade. The *shape* tells you more than any single number:

```
 Healthy edge:                    Fragile / problematic:
   R                                R
   │            ╱                   │         ╱╲    ╱
   │        ╱╲ ╱                    │        ╱  ╲  ╱
   │      ╱╲╱  ╲╱                   │   ╱╲  ╱    ╲╱
   │   ╱╲╱                          │  ╱  ╲╱   (one spike, then chop/decline)
   │ ╱                              │ ╱
   └────────────── trades           └────────────── trades
  Steady rise, shallow dips        Lumpy, outlier-dependent, deep drawdowns
```

- **Smooth, steadily rising** → a robust, consistent edge.
- **One big jump then flat/declining** → profit depends on outliers; fragile.
- **Deep, prolonged drawdowns** → high risk; check sizing and the strategy's regime fit.
- A rising equity curve with a **flat or rising "% plan-followed"** line is the signature of a maturing trader.

---

## 7.4 Segmentation analytics — where the edge really lives

This is where the journal earns its keep. **Slice your results by category** to find your real strengths and the hidden leaks. A net-profitable trader is often *very* profitable in some buckets and bleeding in others.

```
Break your trades down BY:
  • SETUP / strategy   → which edges actually work? (cut the losers)
  • SESSION / time     → are you profitable in London but losing in Asia?
  • DAY OF WEEK        → any consistently bad day?
  • PAIR               → is one instrument dragging you down?
  • DIRECTION          → are your shorts much worse than your longs?
  • MARKET REGIME      → trend vs range — does your edge need one?
  • EMOTIONAL STATE    → how much worse are "FOMO"/"revenge" trades?
  • FOLLOWED-PLAN y/n  → the expectancy gap between disciplined & undisciplined trades
```

> 🔑 **The most common discovery:** "I'm net positive, but one or two buckets are killing me." Cutting your worst-performing setup, session, or pair often does more for your bottom line than finding a brand-new strategy. **Subtraction is an underrated edge.**

---

## 7.5 Trade-quality analytics: MAE & MFE

Two advanced metrics that diagnose your **entries and exits** specifically:

- **MAE (Maximum Adverse Excursion):** the furthest a trade went *against* you before you closed it. Aggregated, it reveals whether your **stops** are well-placed — e.g. if winners rarely go more than 0.5R against you, a 1R stop may be wider than necessary.
- **MFE (Maximum Favorable Excursion):** the furthest a trade went *in your favor* before you closed it. Reveals whether you're **leaving profit on the table** — e.g. if trades routinely reach +3R but you exit at +1R, your targets/trailing need work (you're cutting winners short).

Together, MAE/MFE turn vague feelings ("I think I exit too early") into evidence you can act on.

---

## 7.6 System Quality — combining edge and consistency

For a single summary of system quality, some traders use metrics that blend **expectancy with consistency** (how reliable the per-trade results are, via their variability) and **sample size**. The intuition you need, without the formula worship:

- A system with a **steady** +0.3R per trade is often *better to trade* than one averaging +0.5R with wild swings — because the steadier one has shallower drawdowns and is far easier to execute with discipline.
- **Consistency has real value.** When comparing strategies, don't just rank by average return; weigh the **smoothness of the equity curve and the depth of drawdowns** too.

> 🔑 The best system isn't the one with the highest expectancy on paper — it's the one with a positive edge you can **actually execute and survive**, given its drawdowns and your psychology.

---

## 7.7 Reading the numbers honestly

- **Always anchor to sample size.** Every KPI is an estimate; small samples give noisy, untrustworthy estimates.
- **Look for stability over time**, not a single great month. Recent performance vs overall — is the edge persisting or decaying?
- **Beware over-reaction.** A normal losing streak is not a broken system (Ch. 3). Distinguish variance from genuine edge decay (a sustained, large divergence over a meaningful sample).
- **Let the data, not emotion, drive decisions** — but interpret it with the context of how trading actually works.

---

## 7.8 Chapter summary

```
• Core KPIs: win rate (context only), avg win/loss R, EXPECTANCY, profit factor — always
  with SAMPLE SIZE as the confidence level.
• Survival KPIs: MAX DRAWDOWN (the key risk metric), longest losing streak, risk of ruin,
  return/drawdown ratio. Know your drawdown BEFORE going live.
• The EQUITY CURVE's shape reveals robustness vs fragility at a glance.
• SEGMENT results by setup/session/day/pair/direction/regime/emotion/followed-plan —
  cutting your worst bucket often beats finding a new strategy.
• MAE/MFE diagnose stop placement and whether you're cutting winners short.
• Prefer a steady, survivable edge over a high-but-wild one. Judge risk-adjusted, not raw.
```

You can now diagnose your trading precisely. Chapter 8 uses that diagnosis to **optimize and iterate** — and to size positions so the edge compounds without blowing up.

---

[← The Journaling System](06-journaling-system.md) | [Volume 4 Home](README.md) | [Next: Optimizing & Sizing →](08-optimizing-sizing.md)
