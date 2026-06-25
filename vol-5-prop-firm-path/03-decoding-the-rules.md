# Chapter 3 — Decoding the Rules

[← Choosing a Legitimate Firm](02-choosing-a-firm.md) | [Volume 5 Home](README.md) | [Next: Building Your Prop System →](04-prop-trading-system.md)

---

In funded trading, **the rules are the game.** Most failures aren't from bad trades — they're from misunderstanding a rule and breaching it. This chapter dissects every common rule, how it's calculated, and exactly how each one trips people up. Read it twice; then read your specific firm's rules with this lens.

> 🔑 **The single highest-value habit in prop trading:** before you place one trade, know your *exact* numbers — your hard floor, your daily floor, how they're calculated, and what voids your account. Write them down (Chapter 9's rule tracker). Ambiguity here is how accounts die.

---

## 3.1 The profit target

The amount you must gain to pass a phase (e.g. **+8%** phase 1, **+5%** phase 2). On a funded account there's usually **no** profit target — just keep within the rules and withdraw.

- It's almost always **smaller than the drawdown allowance is large** — by design, you have more room to lose than you need to gain. **The challenge is not making the target; it's not breaching drawdown while you do.**
- ⚠️ **Don't rush it.** A target with no tight time limit (most modern firms) means you can hit it slowly and safely. Trying to smash an 8% target in two days is how people breach drawdown. *Slow is the strategy* (Chapter 5).

---

## 3.2 Maximum drawdown (the hard floor) ⭐

The total amount you can lose before the account is **terminated**. Usually **~10%** of the starting balance. This is your single most important number — breach it and it's over, instantly, no matter how well you were doing.

There are two fundamentally different ways it's calculated, and confusing them is catastrophic:

### Static / absolute drawdown
A **fixed floor** set from your starting balance. E.g. on a $100k account with 10% max DD, the floor is **$90,000 — and it stays there.** As you profit, your cushion grows; the floor doesn't move.

### Trailing / scaling drawdown ⚠️ (the dangerous one)
The floor **trails your account's highest point.** As your balance (or equity) makes new highs, the drawdown limit rises with it.

```
$100k account, 10% TRAILING drawdown:
   Start:            floor = $90,000
   Balance → $105k:  floor trails up to $95,000
   Balance → $108k:  floor trails up to $98,000   ← you can now lose only to $98k
   ...even though you're still in profit overall!
```

- Some firms trail on **closing balance** (locks the floor once you bank profits); others trail on **intraday equity** (the floor follows your unrealized highs — much harsher, and it can catch you on a wick).
- Many firms **stop trailing once the floor reaches your starting balance** (i.e. once you're "in profit," the floor locks at break-even). Know your firm's exact mechanic.

> 🔑 **Trailing drawdown is the #1 silent account-killer.** Traders profit, relax, give back a normal amount — and breach a floor that quietly rose beneath them. If your firm uses trailing DD, you must track your *real-time distance to the floor* constantly (Chapter 4), not your distance from the starting balance.

---

## 3.3 Daily drawdown (the daily floor) ⭐

The most you can lose **in a single day** (e.g. **~5%**) before the account is terminated. It resets each day (at a defined server time — **know that reset time**).

- Calculated from either the **day's starting balance** or **starting equity** — check which, as it changes your room.
- ⚠️ Some firms count **open (unrealized) losses** toward the daily limit in real time, so a deep drawdown on an open trade can breach you even if it later recovers. Others count only **closed** losses. This matters enormously for how you manage open positions.
- The daily floor is whatever is **higher** (closer to you) of the daily limit and the max-drawdown floor — you're bound by both simultaneously.

> 🔑 The daily drawdown is your circuit-breaker. The disciplined prop trader sets a **personal daily stop well inside** the firm's limit (e.g. stop trading at −2% when the firm allows −5%) so a bad day can *never* approach a breach. More on this in Chapters 4–5.

---

## 3.4 Consistency rules (the quiet payout-blockers)

Designed to ensure you're a *consistent* trader, not a one-lucky-trade gambler. They vary widely and **often apply to payouts, not just evaluations** — so they can block your withdrawal even after you've "made" the money.

Common forms:
- **Single-day / single-trade profit caps:** no one day (or trade) may exceed e.g. **X%** of your total profit. If one trade makes most of your gains, the payout can be delayed or denied until you "balance" it with more consistent results.
- **Minimum trading days:** you must trade on at least e.g. **3–5 distinct days** — no passing in a single session.
- **Lot-size / risk consistency:** suspiciously large or erratic position sizes can flag the account.

> ⚠️ **You can pass the profit target and still fail on consistency.** Read these rules *before* you trade and size your trades so no single day/trade dominates your P/L. Consistency rules reward exactly the steady, risk-controlled approach this whole series teaches.

---

## 3.5 Trading restrictions — make sure your strategy is even allowed

Your strategy must be *legal* under the firm's rules. Check each:

- **News trading:** many firms **restrict or ban** trading around high-impact news (e.g. no entries X minutes before/after). If your edge is news-driven, this firm may not fit.
- **Expert Advisors / bots / copy trading:** allowed? restricted? fully banned? Some ban certain automation or "prohibited strategies" (latency arbitrage, tick-scalping, grid/martingale, reverse-arbitrage, group/copy trading across accounts).
- **Holding over weekends / overnight:** some firms forbid holding positions over the weekend or impose swap rules.
- **Maximum lot size / max positions:** caps on size or simultaneous trades.
- **Hedging across accounts / "all-in" trades:** often prohibited and a payout-voiding offense.

> 🔑 **A breach of a trading restriction can void the account AND forfeit profits — even profits you'd otherwise have withdrawn.** Match the firm's allowed strategies to *your* tested system (Vol 4) *before* you buy.

---

## 3.6 Profit split, payouts & scaling

The reward side — also rule-bound:

- **Profit split:** your share (commonly **80–90%**; some scale the split up the longer you stay/perform).
- **Payout frequency & first payout:** when you can first withdraw (e.g. after 14–30 days or a min number of trading days) and how often thereafter. Faster/more frequent is better, all else equal.
- **Payout minimums & methods:** minimum withdrawal amounts and how you're paid.
- **Scaling plan:** how your account *size* grows as you stay profitable (e.g. +25% account size every time you hit a profit milestone over several months). This is your **long-term ceiling** — a good scaling plan is how a $50k start becomes meaningful size (Chapter 8).

---

## 3.7 Putting the rules together — your "rule map"

Before trading any account, fill in your exact numbers (template in Chapter 9):

```
FIRM: __________  ACCOUNT SIZE: $__________  PHASE: __________
Profit target:        +____%   = $__________
MAX drawdown:         ____%    → hard floor at $__________   Type: ☐ static ☐ trailing
   (if trailing: trails on ☐ balance ☐ equity; stops trailing at: __________)
Daily drawdown:       ____%    → daily floor at $__________   Reset time: __________
   Counts open losses? ☐ yes ☐ no
Consistency rule:     __________ (e.g. no day > ____% of total profit)
Min trading days:     ____
News rule:            __________   EA/bots: __________   Weekend holds: __________
Max lot / positions:  __________
Profit split:         ____%   First payout: ____   Frequency: ____   Scaling: __________

MY PERSONAL LIMITS (set INSIDE the firm's):
  Personal daily stop: −____% (well inside the daily floor)
  Per-trade risk:      ____% (≤ ~0.5–1%)
  "Done for the day" trigger: __________
```

> 🔑 This rule map is your pre-flight checklist. A funded trader who can recite their hard floor, daily floor, drawdown *type*, and reset time at any moment is far less likely to breach than one who's vaguely "aware of the rules." **Precision here is survival.**

---

## 3.8 Chapter summary

```
• In prop trading, the RULES are the game. Most failures are rule breaches, not bad trades.
• Profit target is the easy part; NOT breaching drawdown while reaching it is the challenge.
• MAX DRAWDOWN = hard floor (~10%). Know if it's STATIC (fixed) or TRAILING (follows your
  highs) — trailing is the #1 silent killer; track real-time distance to the floor.
• DAILY DRAWDOWN (~5%) resets daily; know the reset time and whether OPEN losses count.
• CONSISTENCY RULES (single-day caps, min days) can block PAYOUTS — size so no day dominates.
• TRADING RESTRICTIONS (news, EAs, weekends, max lots) can VOID the account — match them to
  your tested strategy before buying.
• Build a RULE MAP with your exact numbers + personal limits set INSIDE the firm's limits.
```

---

[← Choosing a Legitimate Firm](02-choosing-a-firm.md) | [Volume 5 Home](README.md) | [Next: Building Your Prop System →](04-prop-trading-system.md)
