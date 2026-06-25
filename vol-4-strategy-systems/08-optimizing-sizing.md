# Chapter 8 — Optimizing, Iterating & Position Sizing

[← Metrics & Analytics](07-metrics-analytics.md) | [Volume 4 Home](README.md) | [Next: Templates & Systems Pack →](09-templates.md)

---

You have a defined strategy, a validation process, a journal, and analytics. This chapter closes the development loop: how to **refine** a system using data without breaking it, when to **keep or kill** a strategy, and how **position sizing** turns a proven edge into compounding growth — or into a blow-up if done wrong.

---

## 8.1 The refinement loop — improve without curve-fitting

Optimization done carelessly is just curve-fitting on your own live data (Chapter 4's sin, repeated). Done well, it's disciplined, evidence-based improvement.

```
THE GOLDEN RULES OF ITERATION
1. Change ONE variable at a time. Multiple simultaneous changes make it impossible
   to know what helped or hurt.
2. Base every change on JOURNAL EVIDENCE over a meaningful sample — never on a
   few recent trades or a gut feeling after a loss.
3. RE-VALIDATE each change (ideally on out-of-sample / forward data) before trusting it.
4. Prefer SUBTRACTION: removing a losing bucket (Ch. 7) usually beats adding rules.
5. Stay SIMPLE. If "improving" means adding parameters, be suspicious — you may be
   fitting noise, not strengthening the edge.
```

> 🔑 **The paradox of optimization:** the more you tune a system to its past results, the *worse* it often performs in the future. Your goal is a **robust** edge that survives changing conditions — not a fragile one perfected for history. Resist the urge to over-engineer.

---

## 8.2 What's worth optimizing (in priority order)

Use your segmentation analytics (Ch. 7) to target the highest-leverage changes:

1. **Cut what loses.** If a setup, session, pair, or direction has negative expectancy over a real sample, *stop trading it.* Pure subtraction, biggest impact, lowest risk.
2. **Fix the exits.** MAE/MFE often show winners cut short or stops poorly placed. Improving exits (let winners run, refine targets/trailing) raises avg-win-R — usually the fastest expectancy gain.
3. **Tighten the condition filter.** Add a *logical* regime/time/news filter that removes a cluster of losers (e.g. "don't trade this in ranges / around red news").
4. **Refine entries last.** Entry tweaks have the smallest, noisiest impact and the highest curve-fitting risk. Touch them least.

> 🔑 Notice the order: **exits and filters before entries.** Beginners do the reverse, endlessly fiddling with entry signals while ignoring the exit and risk decisions that actually move the needle.

---

## 8.3 When to keep, fix, or kill a strategy

Distinguish **variance** (normal, expected bad runs) from genuine **edge decay** (the strategy stopped working). Getting this wrong in either direction is costly — abandoning a good system in a normal drawdown, or clinging to a dead one.

```
KEEP & TRADE   → Positive expectancy over a large sample; current drawdown is within
                 historically normal range; you're following the rules.
FIX / REFINE   → Net positive but a clear bucket is leaking (Ch. 7) → cut/adjust that
                 bucket; or a discipline gap (followed-plan analytics) → fix execution.
KILL           → Edge fails out-of-sample/forward; expectancy is negative over a LARGE
                 sample of RULE-FOLLOWED trades; or the market regime it needs is gone
                 and not returning. Don't marry a strategy.
```

**The discipline-vs-strategy test (from Ch. 6):** before killing a strategy, check the **"followed-plan?"** analytics. If your *rule-following* trades are profitable and only your *rule-breaking* trades lose, the strategy is fine — **you** are the problem to fix (Vol 2's psychology), not the system.

---

## 8.4 Position sizing models — converting edge into growth

A positive edge only builds wealth through **position sizing**. The model you choose governs how fast you grow and how deep your drawdowns run.

| Model | How it works | Pros / Cons |
|-------|--------------|-------------|
| **Fixed lot** | Same lot size every trade | Simple; but risk varies with stop distance & ignores account growth. Weak. |
| **Fixed fractional (% risk)** ⭐ | Risk a fixed **%** of equity per trade (e.g. 1%) | **The standard.** Risk scales with the account, auto-compounds, survivable. *Use this.* |
| **Fixed ratio** | Increase size after each fixed profit increment | Smoother scaling for growing accounts; more complex. |
| **Kelly criterion** | Mathematically "optimal" % from your edge & odds | Maximizes *theoretical* growth — but is **far too aggressive** in practice (huge drawdowns, and it assumes you know your true edge exactly). |

### Fixed-fractional is the answer for almost everyone
Risk a constant small % of *current equity* per trade (Vol 1's method). As the account grows, position sizes grow automatically (compounding); as it shrinks, they shrink automatically (capital preservation). It's simple, robust, and mathematically sound.

### On Kelly — useful idea, dangerous in full
The Kelly criterion gives the growth-optimal fraction, but **full Kelly produces gut-wrenching drawdowns and assumes you know your edge precisely (you don't).** Practitioners who use it at all use a small fraction — *"half-Kelly"* or less. **The practical lesson:** there's a mathematically optimal aggressiveness, and you should stay *well below* it. When unsure, **risk less.** A smaller, survivable edge compounded for years beats an "optimal" one that blows up in a bad streak.

> 🔑 **Sizing decides survival.** The same positive-expectancy system can compound beautifully at 1% risk or blow up at 10% risk — *identical edge, opposite outcomes.* Edge earns the money; sizing decides whether you live to keep it.

---

## 8.5 Scaling up — earning the right to trade bigger

When your validated, journaled track record justifies it, scale **gradually**:

```
• Keep risk as a FIXED %; let compounding grow the absolute size automatically.
• Increase the % only in small steps (e.g. 0.5% → 0.75% → 1%), and only after a
  sustained, journaled record of positive expectancy AND rule-following.
• Re-check drawdown tolerance at the larger size — can you stomach it in real money?
• Scale DOWN when out of rhythm or in drawdown (Vol 2's pros do exactly this).
• Never jump risk to chase a hot streak — that's when most blow-ups happen.
```

---

## 8.6 The continuous-improvement mindset

Markets evolve; edges decay; you improve. Trading is never "solved" — it's a permanent loop of **hypothesize → test → execute → measure → refine.**

- Maintain a **strategy pipeline**: as one edge weakens, you should be researching and validating the next, using this volume's process.
- Keep a **research log** of ideas to test (separate from your live journal).
- Review your whole *system* periodically (quarterly), not just individual trades.
- Accept that **iteration never ends** — the traders who last are perpetual students running a disciplined process, not people who found a magic setup.

> 🔑 The edge that matters most isn't any single strategy — it's your **mastery of the development loop itself.** Strategies come and go; a trader who can reliably *find, validate, and refine* edges has the only durable advantage in a changing market.

---

## 8.7 Chapter summary

```
• Iterate carefully: ONE variable at a time, on journal EVIDENCE, RE-VALIDATED,
  favoring SUBTRACTION and SIMPLICITY. Over-tuning fits noise and hurts the future.
• Optimize in order: CUT losers → fix EXITS → tighten FILTERS → entries LAST.
• Keep / Fix / Kill by distinguishing variance from edge decay — and check the
  "followed-plan?" analytics first (discipline problem vs strategy problem).
• Position sizing: use FIXED-FRACTIONAL (% risk). Kelly is theoretically optimal but
  far too aggressive — stay well below it; when unsure, risk LESS.
• Same edge + different sizing = compounding vs blow-up. Sizing decides survival.
• Scale risk % up only on a proven record, in small steps; scale down when struggling.
• The durable edge is mastery of the LOOP itself: hypothesize → test → execute →
  measure → refine, forever.
```

You now have the complete development system. The final section is a **pack of ready-to-use templates** to run all of it.

---

[← Metrics & Analytics](07-metrics-analytics.md) | [Volume 4 Home](README.md) | [Next: Templates & Systems Pack →](09-templates.md)
