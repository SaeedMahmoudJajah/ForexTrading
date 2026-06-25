# Chapter 6 — The Journaling System

[← Forward Testing](05-forward-testing.md) | [Volume 4 Home](README.md) | [Next: Metrics & Analytics →](07-metrics-analytics.md)

---

The journal is the **engine of improvement** for the entire series. Volume 1 gave you a starter template; Volume 2 showed that every great trader keeps detailed records; this chapter turns journaling into a **system** — a structured database of your trading that powers the analytics (Chapter 7) and the refinement loop (Chapter 8). Without it, you are flying blind, and no amount of strategy knowledge can save a trader who doesn't measure.

> 🔑 **You cannot improve what you do not measure.** The journal converts scattered experience into structured data, and structured data into insight. It is the difference between *ten years of experience* and *one year of experience repeated ten times.*

---

## 6.1 Why most traders don't journal (and why that's their downfall)

Journaling is tedious, it's confronting (it forces you to face losses and mistakes honestly), and its payoff is delayed. So most traders skip it — and then wonder why they never improve. They remember their wins, forget their losses, misjudge their own win rate, and "fix" the wrong things.

A journaling *system* defeats this by making logging **routine, structured, and non-optional** — part of every trade, like the stop-loss.

---

## 6.2 What to log — the anatomy of a journal entry

A useful journal captures three layers: **the plan, the result, and the process.** The process layer is what most people omit and what matters most.

```
── IDENTITY ──────────────────────────────────────────────
  Trade #, Date/Time, Pair, Session, Strategy/Setup name, Long/Short

── THE PLAN (recorded at entry) ──────────────────────────
  Entry price, Stop, Target(s), Position size, Risk %, Stop distance (pips),
  Planned R:R, The CONFLUENCE / reasons for the trade

── THE RESULT ────────────────────────────────────────────
  Exit price, Outcome (win/loss/BE), Pips, $ P/L, R-multiple,
  Costs (spread/commission/swap)

── THE PROCESS (the highest-value part) ──────────────────
  □ Did I follow my plan EXACTLY?  (Yes / No — and what I broke)
  □ Entry & exit execution quality
  □ Emotional state (calm / FOMO / fearful / greedy / revenge / bored)
  □ Mistakes made
  □ What I did WELL
  □ Lesson / one thing to do differently
  □ Screenshot (chart at entry & exit)

── CONTEXT (optional but powerful for analytics) ─────────
  Market regime (trend/range), day of week, time of day, MAE & MFE (Ch. 7)
```

> 🔑 The **"Did I follow my plan?"** field is the most important in the whole journal. It lets you separate *strategy* problems (followed the plan, still lost over a large sample → fix the strategy) from *discipline* problems (broke the plan → fix yourself). These require opposite responses, and only the journal can tell them apart.

---

## 6.3 The tools — pick one and start

There's no single right tool; the best one is the one you'll actually use consistently.

| Tool | Best for | Notes |
|------|----------|-------|
| **Spreadsheet** (Excel / Google Sheets) | Most traders | Flexible, free, auto-calculates KPIs with formulas. **Recommended starting point.** |
| **Markdown / Notion / docs** | Narrative + screenshots | Great for qualitative review; weaker at analytics. (Vol 1's template is this style.) |
| **Dedicated journal apps** | Automation & deep analytics | Auto-import trades, rich stats/charts. Convenient; costs money; less customizable. |
| **Trading platform reports** | Raw trade history | A data *source* to feed your journal — not a substitute for the process layer. |

**Recommendation:** start with a **spreadsheet** — one row per trade, columns matching the fields above. It costs nothing, computes your metrics automatically (Chapter 7), and teaches you exactly what drives your results. (Schema provided in [Chapter 9](09-templates.md).)

---

## 6.4 A spreadsheet schema that auto-computes your edge

One row per trade; let formulas do the analytics:

```
Core columns:
  Date | Pair | Setup | Dir | Entry | Stop | Target | Exit | Size | Risk$ |
  R-multiple | Win/Loss | Followed-Plan? | Emotion | Mistake | Note | Screenshot-link

Derived (formulas across the rows):
  • Win rate        = COUNT(wins) / COUNT(trades)
  • Average win (R) / Average loss (R)
  • EXPECTANCY (R)  = (Win% × AvgWinR) − (Loss% × AvgLossR)
  • Profit factor   = SUM(win R) / ABS(SUM(loss R))
  • Cumulative R    → plot as your EQUITY CURVE
  • % plan-followed = COUNT(Followed=Yes) / COUNT(trades)
```

Now your journal isn't just a diary — it's a **live dashboard of your edge** that updates with every trade. This is the bridge to Chapter 7.

---

## 6.5 The review cadence — journaling is nothing without review

Logging is only half the system; **review** is where the value is extracted. Build a fixed rhythm:

```
PER TRADE (immediately after closing):
  • Fill the full entry while it's fresh — especially emotion & mistakes.

DAILY (end of session, ~10 min):
  • Did I follow my rules today? Any tilt? Quick note of lessons.

WEEKLY (~30–45 min):
  • Compute the week's stats (win%, R, expectancy, profit factor).
  • % of trades I followed the plan.
  • Best decision & worst mistake of the week.
  • One adjustment for next week.

MONTHLY (deep review):
  • Full KPI review (Ch. 7): equity curve, drawdown, performance BY setup,
    BY session, BY day, BY emotion.
  • Is each strategy's edge holding? Refine ONE variable (Ch. 8).

PERIODIC (quarterly):
  • Big-picture: which setups to keep, cut, or scale? Are my rules still valid?
```

> 🔑 **Grade yourself on PROCESS, not P/L** (Vol 2, Ch. 6). The most important review question isn't "did I make money?" — it's *"did I follow my system?"* Over a large sample, a faithfully executed positive-expectancy system *must* make money; your job in review is to ensure faithful execution and to feed the refinement loop.

---

## 6.6 Turning journal insights into action

The journal exists to drive *change*. Common, high-value patterns it reveals:

- *"My expectancy is positive overall but deeply negative on counter-trend trades."* → stop taking counter-trend setups.
- *"I lose most when I trade during the Asian session / around news."* → add a condition filter (Ch. 2).
- *"My 'broke the plan' trades have a far worse R than my disciplined ones."* → it's a discipline problem; tighten execution, not the strategy.
- *"Win rate is fine but I cut winners early (low avg win R)."* → fix the *exit* (let winners run; Vol 3).
- *"All my profit comes from 2 outlier trades."* → fragile edge; investigate before scaling.

Each insight becomes a **specific, testable change** — fed back into the development loop (Ch. 8), validated, and re-measured. That loop, powered by the journal, is how trading skill actually compounds.

---

## 6.7 Chapter summary

```
• The journal is the ENGINE of improvement — you can't improve what you don't measure.
• Log three layers: the PLAN, the RESULT (in R), and the PROCESS (emotion, mistakes,
  and especially "Did I follow my plan?").
• The "followed-plan?" field separates STRATEGY problems from DISCIPLINE problems —
  which need opposite fixes.
• Start with a SPREADSHEET (one row/trade) that auto-computes your KPIs & equity curve.
• Journaling without REVIEW is useless: build a per-trade / daily / weekly / monthly cadence.
• Grade yourself on PROCESS, not P/L. Turn each insight into one specific, testable change.
```

Your journal is now generating data. Chapter 7 turns that data into the specific **metrics** that tell you whether — and *why* — your trading works.

---

[← Forward Testing](05-forward-testing.md) | [Volume 4 Home](README.md) | [Next: Metrics & Analytics →](07-metrics-analytics.md)
