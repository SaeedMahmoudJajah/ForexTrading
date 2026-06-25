# Chapter 4 — Building Your Prop Trading System

[← Decoding the Rules](03-decoding-the-rules.md) | [Volume 5 Home](README.md) | [Next: The Evaluation Playbook →](05-evaluation-playbook.md)

---

You already know how to build a tested, positive-expectancy system (Volume 4). The prop environment doesn't change your *edge* — it adds **hard constraints** you must engineer around: drawdown limits that end the account, daily limits, and consistency rules. This chapter adapts your system to **survive and pass** within those constraints. The headline: in prop trading, **risk management isn't part of the system — it *is* the system.**

---

## 4.1 The mindset shift: defense wins funded accounts

In your own account, a drawdown is painful but recoverable. In a funded account, **hitting the drawdown floor is account death** — permanent, instant, total. That changes the optimization target:

```
Personal account goal:   maximize long-run growth (survive + compound).
Prop account goal:       reach a modest target WITHOUT EVER touching the floor.
```

This is a **survival-first** game. The trader who passes isn't the one who makes the most — it's the one who **never breaches.** Everything below serves that.

> 🔑 Reframe the whole challenge: you are not trying to *make 10%*. You are trying to *not lose 10%* while a small edge drifts you upward. Get that backwards and the rules will end you.

---

## 4.2 Risk-per-trade: the math of not breaching

Your per-trade risk must be small enough that a **realistic losing streak** can't approach the drawdown floor. Use the streak math from Volume 4.

```
Example — $100k account, 10% max DD ($10,000), 5% daily DD ($5,000):

  Risk 1% ($1,000) per trade:
     • 5 losses in a row = −$5,000 = breaches the DAILY limit. Too much for one day.
  Risk 0.5% ($500) per trade:
     • A 10-loss streak = −$5,000 → still within max DD, but a brutal stretch.
     • To stay safe, cap LOSSES PER DAY (see 4.4), not just risk per trade.

  Practical prop default: risk ~0.25%–0.5% per trade during evaluations.
```

- **Lower risk per trade than you might use personally.** 0.25–0.5% is typical for evaluations; it makes the drawdown floor almost unreachable through normal losing streaks.
- Remember the asymmetry from Chapter 3: targets are small, the floor is large — **you don't need big risk to hit the target slowly.** Small risk + patience reaches +8% safely; big risk reaches the floor fast.

---

## 4.3 Managing the trailing-drawdown trap

If your firm uses **trailing** drawdown (Chapter 3), your floor moves up beneath you. Engineer for it:

- **Track distance-to-floor in real time**, not distance from the starting balance. Your only relevant number is *"how far is price/equity from the trailing floor right now?"*
- **Bank profits deliberately** if the floor trails on *closing balance* — realizing gains can lock the floor higher and is safer than sitting on big unrealized profit that, if given back, drops you toward a risen floor.
- **Be extra conservative right after a winning run.** That's when the floor has trailed up the most and complacency is highest — the classic trailing-DD blow-up. Tighten risk, don't loosen it, after a hot streak.

> 🔑 With trailing drawdown, **a string of wins is when you're most fragile, not least.** Respect the risen floor.

---

## 4.4 The layered risk model — limits inside limits

Professionals build **personal limits well inside the firm's limits**, so the firm's hard floor is never even threatened. This is the core defensive structure of prop trading:

```
┌─ FIRM HARD LIMITS (account death) ────────────────────────────┐
│   Max DD 10%   |   Daily DD 5%                                  │
│                                                                │
│   ┌─ YOUR PERSONAL LIMITS (you stop voluntarily) ───────────┐  │
│   │   Personal daily stop: −2%  (stop trading the day)       │  │
│   │   Personal max DD: −5%      (pause, review, reduce size) │  │
│   │   Max LOSSES per day: 2–3 trades → done for the day      │  │
│   │   Max risk per trade: 0.25–0.5%                          │  │
│   │   Max open risk at once: ~1% (correlation-aware, Vol 1)  │  │
│   └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

- **Personal daily stop (e.g. −2%):** if you're down this much on the day, you're **done** — close the platform. This guarantees you never approach the firm's daily floor, and it stops revenge trading and tilt cold (Chapter 7).
- **Loss-count limit (e.g. 2–3 losers → stop):** protects against a death-by-a-thousand-cuts day even if each loss is small.
- **Personal max-DD pause (e.g. −5% from peak):** if the *account* is struggling, you pause, review the journal, and reduce size — you don't push.

> 🔑 The firm's limits should be a fence you can barely see from where you trade. If you regularly get *near* the firm's daily limit, your personal limits are too loose — tighten them. **You breach your own soft limit and stop; you should never reach the firm's hard one.**

---

## 4.5 Which strategy works best for prop?

Your *tested* system (Vol 4) is the foundation — but some characteristics fit prop constraints better:

- **High reward:risk, lower frequency setups** are ideal: they reach the target with fewer trades and less exposure to the daily/streak risk. A 1:3+ R:R means a few winners hit the target while small losers stay far from the floor.
- **Trend/structure-based swing or intraday setups** (Vol 3) tend to fit better than high-frequency scalping, where costs and frequent exposure raise breach risk and may bump consistency/lot rules.
- **Avoid martingale, grid, and "averaging into losers"** entirely — they're often *banned*, and they're the fastest path to a drawdown breach.
- **Confirm your strategy is allowed** (news/EA/weekend rules, Chapter 3). A great edge you're not permitted to use is useless here.

> 🔑 You don't need a *new* strategy for prop — you need your *proven* strategy, executed at **lower risk, with tighter personal limits, and full rule-compliance.** The edge is the same; the risk envelope is smaller.

---

## 4.6 Position sizing under prop rules

Tie it together with the sizing discipline from Volume 4:

```
1. Risk a FIXED small % per trade (0.25–0.5% during evaluations).
2. Size each position so the STOP = that fixed % (Vol 1 formula). Never skip the stop.
3. Respect MAX OPEN RISK across correlated trades (don't let 3 trades = one 1.5% bet).
4. Bank toward the target in small increments; don't swing for it.
5. After reaching the target, STOP or drastically reduce size — protect the pass (Ch. 5).
```

---

## 4.7 Backtest your system *against the rules*

Before risking a fee, run your system through Volume 4's process **with the prop constraints applied**:

- In your backtest/journal, **mark the maximum drawdown** your system produced over a large sample. Is it comfortably **inside** the firm's max-DD limit at your chosen risk %? If your system's historical drawdown is 12% and the firm's limit is 10%, your risk % is too high *or* this firm doesn't fit.
- Check your **worst single day** historically against the daily limit.
- Check whether your **trade distribution** would trip consistency rules (does one trade often dominate your profit?).
- Simulate "pass the evaluation": at your risk %, how many trades/days does it typically take to reach +8% **without** hitting the floor? This is your realistic plan.

> 🔑 **Know your system's drawdown profile before you pay.** The whole point of Volume 4 was to *measure* your edge. Now you use those measurements to choose a risk % and firm where your historical drawdown sits safely inside the rules. This single step prevents most evaluation failures.

---

## 4.8 Chapter summary

```
• Prop changes the GOAL: not "make the most" but "reach a modest target WITHOUT ever
  touching the drawdown floor." Survival-first.
• Risk SMALL per trade (~0.25–0.5% in evaluations) so realistic losing streaks can't breach.
• For TRAILING drawdown, track real-time distance to the (rising) floor; be MOST careful
  right after winning streaks.
• Build LAYERED limits: personal daily stop (~−2%), loss-count cap (2–3/day), personal
  max-DD pause — all well INSIDE the firm's hard limits.
• Favor high-R:R, lower-frequency, rule-compliant setups; avoid martingale/grid (often banned).
• Backtest your system AGAINST the rules: is its historical max drawdown safely inside the
  firm's limit at your risk %? Choose risk % and firm accordingly.
```

You have a rule-fit, survival-first system. Next: the precise playbook for actually passing the evaluation.

---

[← Decoding the Rules](03-decoding-the-rules.md) | [Volume 5 Home](README.md) | [Next: The Evaluation Playbook →](05-evaluation-playbook.md)
