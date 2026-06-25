# 5. Risk Management — The Section That Keeps You Alive

[← Analysis](04-analysis.md) | [Back to README](../README.md) | [Next: Strategies →](06-strategies.md)

---

> **If you only truly master one section of this playbook, make it this one.** Analysis helps you find trades. Risk management decides whether you survive long enough for your edge to pay off. **Most traders don't fail because they can't predict the market — they fail because one or two oversized trades destroy their account.**

The professional's mindset flips the beginner's: a beginner asks *"How much can I make?"* A pro asks *"How much can I lose, and how do I make sure it's small?"*

---

## 5.1 Rule #1: Risk a small, fixed percentage per trade

Never risk more than a **small fixed % of your account on any single trade.**

- **Beginners: risk 0.5%–1% per trade. Never more.**
- This means even a brutal losing streak can't wipe you out.

### Why this works — the math of survival
Look at how many *consecutive* losses it takes to lose half your account at different risk levels:

| Risk per trade | Losses to drop 50% of account |
|----------------|-------------------------------|
| 1% | ~69 trades |
| 2% | ~34 trades |
| 5% | ~14 trades |
| 10% | ~7 trades |
| 20% | ~3 trades |

At 1% risk, a 10-trade losing streak costs you ~10%. **Recoverable.** At 20% risk, a 3-trade streak halves your account. **The same losing streak is trivial or fatal depending entirely on your risk per trade.**

### The brutal math of drawdowns
Losses hurt more than equivalent gains help, because you're working with a smaller base to recover from:

| Account drawdown | Gain needed to recover |
|------------------|------------------------|
| −10% | +11% |
| −25% | +33% |
| −50% | **+100%** |
| −75% | **+300%** |
| −90% | **+900%** |

This is *why* you protect capital obsessively. A 50% loss isn't "half as bad" as a 100% loss — it already requires doubling your money to get back. **Avoiding big losses matters more than capturing big wins.**

---

## 5.2 Rule #2: Every trade has a stop loss — always

A **stop loss** is a non-negotiable, pre-set exit that caps your loss. Place it **before** you enter, at a price that means *"my trade idea was wrong"* — not at an arbitrary dollar amount.

- Place stops **beyond market structure** (below support for longs, above resistance for shorts), ideally with a small buffer, so normal noise / stop hunts don't clip you.
- A volatility-based method: stop = entry ± (1.5 × **ATR**), so the stop fits current conditions.
- **Never, ever move your stop further away to avoid taking a loss.** This single habit destroys more accounts than anything else. You may move a stop *toward* profit (to break-even or to trail), never away.
- Accept that **some trades will hit your stop. That's normal and fine.** A stop-out is the system working, not a failure.

---

## 5.3 Rule #3: Position sizing — the formula that ties it together

Position sizing converts your fixed % risk + your stop distance into the correct **lot size**. This is the single most important calculation in trading.

```
Position size (lots) =  (Account × Risk%)  ÷  (Stop distance in pips × Pip value per lot)
```

### Step-by-step
1. **Risk amount** = Account balance × Risk%.
2. **Stop distance** = how many pips from entry to your stop loss.
3. **Lot size** = Risk amount ÷ (Stop pips × value-per-pip-per-lot).

### Worked example
- Account: **$5,000**. Risk: **1%** → **$50 max loss**.
- You want to short GBP/USD; your stop is **40 pips** away.
- Pip value for a standard lot ≈ **$10/pip** (USD-quote pair).
- Risk per standard lot at this stop = 40 pips × $10 = $400.
- **Lot size = $50 ÷ $400 = 0.125 lots.** Round down → **0.12 lots**.

Now no matter what happens, if the stop hits you lose ~$50 (1%). The wider your stop, the *smaller* your position must be — and vice versa. **Your stop and your size move together to keep risk constant.**

> 💡 Use the **position-size calculator** built into your platform or a free online one. Never guess.

---

## 5.4 Rule #4: Risk/reward & the truth about win rate

Aim for trades where the potential **reward is larger than the risk** — at least **1:1.5**, ideally **1:2 or more**.

Why R:R lets you be wrong often and still win — at **1:2 R:R**, risking 1R to make 2R:

| Win rate | Outcome over 10 trades (risking 1R, winning 2R) | Net |
|----------|--------------------------------------------------|-----|
| 50% | +5×2R − 5×1R | **+5R (very profitable)** |
| 40% | +4×2R − 6×1R | **+2R (profitable)** |
| 34% | +3.4×2R − 6.6×1R | **≈ +0R (break-even)** |

**You can be wrong 60% of the time and still make money** with good R:R. This is liberating: you don't need to be a market psychic. Conversely, a **90% win rate** with 1:5 *negative* R:R (small wins, huge losses) is a guaranteed account-killer. **Never chase win rate at the expense of R:R.**

### Expectancy — your edge in one number
```
Expectancy = (Win% × Average Win) − (Loss% × Average Loss)
```
If it's **positive**, you have an edge and should keep executing. If it's negative, no amount of position sizing saves you — you must fix the strategy. You can only know your expectancy by **journaling** (see [Journal template](../templates/trading-journal.md)).

---

## 5.5 Rule #5: Control total & correlated exposure

Risk per trade isn't the whole story — watch your **aggregate** risk:

- **Cap total open risk.** A common rule: no more than **3–5% of your account at risk across all open trades at once**.
- **Beware correlation.** Many pairs move together. Being long EUR/USD, GBP/USD, *and* AUD/USD is essentially **one big bet against the dollar** — three "1% risks" can act like a single 3% risk. Likewise, EUR/USD and USD/CHF are strongly *inversely* correlated.
- **Limit simultaneous positions** as a beginner (e.g. 1–2 at a time) so you can actually manage them.

---

## 5.6 Rule #6: Daily / weekly loss limits (circuit breakers)

Emotion compounds losses. Set hard stops on *yourself*:

- **Daily loss limit** — e.g. "If I'm down 3% on the day, I stop trading until tomorrow." This prevents **revenge trading** (angrily trying to win it back, which usually digs the hole deeper).
- **Weekly loss limit** — e.g. "Down 6% on the week → I'm done until next week and I review my journal."
- **Max trades per day** — prevents overtrading out of boredom.

Write these into your trading plan and obey them like laws.

---

## 5.7 Advanced tools (use once you have the basics down)

- **Break-even stop** — once a trade moves in your favor by ~1R, move the stop to your entry. Now it's a "free" trade — you can't lose.
- **Trailing stop** — let the stop follow price to lock in profit on trending trades while giving room to run.
- **Scaling out** — close part of the position at the first target, let the rest run with a trailed stop. Banks profit while keeping upside.
- **Scaling in** — add to a winning position only (pyramiding), never to a loser ("averaging down" into a loss is how accounts die).

---

## 5.8 The risk-management commandments (print these)

```
1.  Risk ≤1% of the account per trade. Period.
2.  Every single trade has a stop loss, set BEFORE entry.
3.  Never move a stop further from entry to avoid a loss.
4.  Size the position to the stop, so risk is constant.
5.  Only take trades with R:R of at least 1:1.5.
6.  Cap total open risk (~3–5%) and watch correlation.
7.  Hit your daily loss limit → stop trading for the day.
8.  Never add to a losing position.
9.  Never trade money you can't afford to lose.
10. When in doubt, stay out. No trade is a position.
```

> **Capital preservation is the job.** Profits are a byproduct of surviving long enough, with discipline, for a positive-expectancy edge to compound. Protect your account above all else, and you give yourself the one thing 80% of traders lose first: **the ability to still be in the game next month.**

---

[← Analysis](04-analysis.md) | [Back to README](../README.md) | [Next: Strategies →](06-strategies.md)
