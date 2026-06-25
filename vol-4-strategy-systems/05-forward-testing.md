# Chapter 5 — Forward Testing: Demo to Live

[← Backtesting Properly](04-backtesting.md) | [Volume 4 Home](README.md) | [Next: The Journaling System →](06-journaling-system.md)

---

A backtest tells you how a strategy *would have* done on the past. **Forward testing** tells you how it does on data it has never seen — in real time, with real execution friction, and (eventually) real emotion. It's the bridge between a promising backtest and risking actual capital, and skipping it is one of the most expensive shortcuts a trader can take.

---

## 5.1 Why forward testing is non-negotiable

Backtesting has an unavoidable blind spot: **the strategy was developed with knowledge of the period it's tested on.** Even with out-of-sample discipline, you chose the rules in a world where that history already happened. Forward testing removes that contamination entirely — the future genuinely hasn't happened yet.

It also surfaces things a backtest *can't*:
- **Real execution:** actual spreads, slippage, fills, requotes, platform quirks.
- **Real timing:** can you actually be at the screen when setups occur?
- **Real psychology** (once live): hesitation, fear, the urge to override rules.
- **Regime change:** does the edge still exist in *today's* market, not just history's?

> 🔑 Backtest answers *"did this edge exist?"* Forward test answers *"does this edge exist NOW, and can I actually execute it?"* You need both yeses before sizing up.

---

## 5.2 The validation ladder — climb it in order

Move to the next rung only after the current one passes. Each rung adds realism and risk gradually.

```
RUNG 1 — BACKTEST           Historical edge established (Ch. 4). Pre-set criteria met.
            ↓
RUNG 2 — PAPER / DEMO        Trade the LIVE market in real time with virtual money.
            ↓                Validates execution & timing without financial risk.
RUNG 3 — LIVE, MICRO          Real money, smallest size, 0.25–0.5% risk. Adds real
            ↓                 emotion — the only thing demo can't replicate.
RUNG 4 — LIVE, NORMAL          Scale toward your normal (still ≤1%) risk, slowly,
                              ONLY after a proven, journaled live track record.
```

Most blow-ups come from jumping rungs — going from a pretty backtest straight to meaningful live size, skipping the two rungs that catch execution and psychology problems.

---

## 5.3 Demo / paper trading — do it right

Demo is free and risk-free, which is its strength *and* its weakness — it's easy to treat it carelessly and learn nothing.

**Make demo meaningful:**
- **Trade it exactly like real money.** Use realistic position sizes and your real risk %. Don't trade 50 lots "because it's fake" — you'll build worthless habits.
- **Follow the strategy spec mechanically.** The point is to validate *the system*, not to freestyle.
- **Journal every trade** (Chapter 6) exactly as you will live.
- **Run a meaningful sample** — weeks of trading and ideally 30–50+ trades before judging.

**What demo proves:** that you can execute the strategy in real time, that your rules are actually clear enough to follow live, and that the edge appears to persist in current conditions.

**Demo's honest limitation:** it **cannot replicate the emotion** of real money. People are disciplined on demo and fall apart live. That's exactly why Rung 3 (live micro) exists — and why you start it *tiny*.

---

## 5.4 The leap to live — managing the psychology gap

The single biggest surprise traders report: **the same strategy feels completely different with real money.** Fear makes you exit winners early and hesitate on valid setups; the sting of real losses tempts you to override your stop.

**How to cross the gap:**
- **Start so small the money barely matters** (micro lots, 0.25–0.5% risk). The goal of Rung 3 is **not profit — it's executing your proven system under real emotion.**
- **Treat the rules as sacred.** The whole point is to prove you can run the *tested* system, not a panicked variation of it.
- **Compare live results to your backtest/demo.** A reasonable match suggests the edge is real and you're executing well. A big negative gap usually means an *execution/psychology* problem (you're not trading your system), not a strategy problem — the journal will reveal which.

> 🔑 If your live results diverge sharply from a well-validated backtest, suspect **yourself before the strategy.** The most common cause is deviation from the rules under emotional pressure — which is a journaling and discipline fix (Ch. 6, and Vol 2), not a reason to scrap the system.

---

## 5.5 How long, and how many trades?

There's no magic number, but useful guidance:
- **Demo:** at least a few weeks and ~30+ trades, enough to confirm you can execute and the edge shows up.
- **Live micro:** long enough to experience real winning *and* losing streaks and prove you hold discipline through both — often 1–3 months and 30–50+ trades.
- **The deciding factor isn't time — it's a journaled track record** showing positive expectancy *and* consistent rule-following across a real sample (Ch. 7).

Be patient. The cost of a few extra months of testing is trivial; the cost of going live too early with too much size is how accounts die.

---

## 5.6 When to advance, hold, or go back

```
ADVANCE a rung when:  expectancy is positive over a real sample AND you followed
                      your rules consistently AND you can stomach the drawdowns.

HOLD / repeat when:   results are inconclusive, the sample is too small, or your
                      rule-following is shaky. More data, same rung.

GO BACK when:         the edge clearly fails out-of-sample/live, OR you keep
                      breaking rules (fix discipline before risking more).
```

> ⚠️ **Never "promote" a strategy out of impatience or because you're bored.** Promotion is earned by *data*. The market will still be there next month; an account blown by rushing may not be.

---

## 5.7 Chapter summary

```
• Forward testing validates a strategy on data it has NEVER seen — removing the
  contamination backtests can't avoid, and exposing execution/timing/psychology.
• Climb the VALIDATION LADDER in order: Backtest → Demo → Live-Micro → Live-Normal.
  Don't skip rungs.
• Demo only works if you trade it like real money, by the spec, fully journaled.
• Demo CAN'T replicate real-money emotion — that's why live-micro (tiny size) exists.
• If live diverges from a solid backtest, suspect YOUR execution first, not the edge.
• Advance rungs on DATA (positive expectancy + rule-following over a real sample),
  never on impatience.
```

Every rung of that ladder depends on one thing: a disciplined record of what you actually did. That record — the journal — is the engine of the entire development loop, and it's the subject of Chapter 6.

---

[← Backtesting Properly](04-backtesting.md) | [Volume 4 Home](README.md) | [Next: The Journaling System →](06-journaling-system.md)
