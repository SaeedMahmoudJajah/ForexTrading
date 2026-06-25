# Appendix — Templates & Systems Pack

[← Optimizing & Sizing](08-optimizing-sizing.md) | [Volume 4 Home](README.md)

---

Copy these and fill them in. Together they run the entire development loop: **specify → backtest → journal → measure → review → refine.** They complement the trading-plan and trading-journal templates in [Volume 1](../templates/trading-plan.md).

---

## A. Strategy Specification Sheet

> One per strategy. If a stranger couldn't trade identically from this sheet, it isn't finished.

```
STRATEGY NAME: ________________________________   Version: ____  Date: ______

1. HYPOTHESIS / EDGE (one sentence):
   _____________________________________________________________________
   Logical reason this edge should exist: ______________________________

2. MARKET(S):        ______________________  (why these: __________________)
3. TIMEFRAMES:       Bias ____  | Setup ____  | Entry ____
4. CONDITION FILTER (when VALID / when to STAND ASIDE):
   • Valid when:   __________________________________________________
   • Invalid when: __________________________________________________

5. ENTRY RULES (exact, repeatable — all must be TRUE):
   1) ______________________________________________________________
   2) ______________________________________________________________
   3) ______________________________________________________________
   Entry execution: ☐ on close  ☐ on retest  ☐ limit at level

6. STOP-LOSS RULE (the invalidation point): ______________________________
7. TAKE-PROFIT RULE (targets / trailing / scaling): ______________________
8. MINIMUM RISK:REWARD: 1 : ____

9. RISK PER TRADE: ____ %    Position-size formula: (Acct × Risk%) ÷ (Stop pips × pip value)
10. TRADE MANAGEMENT: break-even at ____ R | partial at ____ | max hold: ____
11. WHAT INVALIDATES THE STRATEGY (stop trading it when): ________________

ACCEPTANCE CRITERIA (set BEFORE testing — Ch. 2 & 4):
   □ Expectancy > ____ R   □ Profit factor ≥ ____   □ Max drawdown ≤ ____ %
   □ Min sample ≥ ____ trades   □ Holds OUT-OF-SAMPLE
```

---

## B. Backtest Log

> One row per simulated trade. Costs included. Log winners, losers, and ugly ones.

```
| # | Date | Pair | Dir | Entry | Stop | Target | Exit | Stop(pips) | R | W/L | Cost | Notes |
|---|------|------|-----|-------|------|--------|------|-----------|---|-----|------|-------|
| 1 |      |      |     |       |      |        |      |           |   |     |      |       |
| 2 |      |      |     |       |      |        |      |           |   |     |      |       |

SUMMARY (auto-computed):
  Sample size: ____   In-sample: ____  Out-of-sample: ____
  Win rate: ____%   Avg win: ____R   Avg loss: ____R
  EXPECTANCY: ____R   Profit factor: ____   Max drawdown: ____%
  Verdict vs acceptance criteria:  ☐ PASS → forward-test   ☐ FAIL → revise/kill
```

---

## C. Trade Journal Schema (spreadsheet — one row per LIVE/demo trade)

```
IDENTITY:  Trade# | Date | Time | Pair | Session | Setup | Dir
PLAN:      Entry | Stop | Target | Size | Risk% | StopPips | Planned-R:R | Confluence/Reasons
RESULT:    Exit | Outcome(W/L/BE) | Pips | $P/L | R-multiple | Costs
PROCESS:   Followed-Plan?(Y/N) | What-I-broke | Emotion | Mistake | Did-Well | Lesson | Screenshot
CONTEXT:   Regime(trend/range) | DayOfWeek | MAE(R) | MFE(R)

AUTO-CALCULATED DASHBOARD (formulas over all rows):
  Win rate · Avg win R · Avg loss R · EXPECTANCY (R) · Profit factor ·
  Cumulative R (→ equity curve chart) · Max drawdown · % plan-followed
```

---

## D. KPI Dashboard (review at a glance — Ch. 7)

```
┌─ EDGE ──────────────────────────────────────────────────────────┐
│ Sample size: ____    Win rate: ____%    Expectancy: ____R         │
│ Avg win: ____R   Avg loss: ____R   Profit factor: ____            │
├─ SURVIVAL ──────────────────────────────────────────────────────┤
│ Max drawdown: ____%   Longest losing streak: ____                 │
│ Return/Drawdown: ____   Current drawdown: ____% (normal? Y/N)      │
├─ EQUITY CURVE ──────────────────────────────────────────────────┤
│ Shape: ☐ steady-rise  ☐ outlier-dependent  ☐ choppy/declining     │
├─ SEGMENTATION (expectancy by bucket — find leaks) ──────────────┤
│ Best setup: ______ (__R)     Worst setup: ______ (__R)            │
│ Best session: ____ (__R)     Worst session: ____ (__R)            │
│ Longs: __R  Shorts: __R   Trend: __R  Range: __R                  │
├─ DISCIPLINE ────────────────────────────────────────────────────┤
│ % plan-followed: ____%   Expectancy when followed: ____R          │
│                          Expectancy when broken:   ____R          │
└─ ACTION: cut ______ | fix exit/filter ______ | keep ______ ──────┘
```

---

## E. Weekly Review

```
WEEK OF: __________   Trades: ____
Win%: ____  Total R: ____  Expectancy: ____R  Profit factor: ____
% plan-followed: ____%
Best decision: _______________________  Worst mistake: ____________________
Respected loss limits? ☐Y ☐N    Revenge/overtrade/oversize? ☐Y ☐N
Patterns noticed: ______________________________________________________
ONE adjustment for next week (one variable): __________________________
Mindset note: _________________________________________________________
```

---

## F. Monthly System Review

```
MONTH: __________
PER-STRATEGY (one block each):
  Strategy: __________  Trades: ____  Expectancy: ____R  PF: ____  MaxDD: ____%
  Verdict: ☐ KEEP   ☐ FIX (what: ________)   ☐ KILL (why: ________)

OVERALL:
  Equity curve trend: ____________   Edge holding / decaying? ____________
  Biggest leak found (segmentation): ____________________________________
  One refinement to test next month (re-validate before trusting): ______
  Sizing: current risk ____%  → change? ☐ no  ☐ yes to ____% (justified by: ____)
  Discipline grade (process, not P/L): ____ / 10
```

---

## G. Research / Idea Pipeline

> Keep new edge ideas here — separate from live trading — to test via the loop.

```
| Idea (one-sentence hypothesis) | Logical reason | Status (idea/backtest/forward) | Notes |
|--------------------------------|----------------|--------------------------------|-------|
|                                |                |                                |       |
```

---

## H. The development loop (keep this in view)

```
HYPOTHESIZE → SPECIFY → BACKTEST → FORWARD-TEST → TRADE LIVE (small) →
ANALYZE (KPIs) → REFINE (one variable, re-validate) → ↺ repeat forever

Prove the edge first. Journal everything. Grade yourself on process.
Size to survive. Scale only on proof. The loop IS the edge.
```

---

[← Optimizing & Sizing](08-optimizing-sizing.md) | [Volume 4 Home](README.md)
