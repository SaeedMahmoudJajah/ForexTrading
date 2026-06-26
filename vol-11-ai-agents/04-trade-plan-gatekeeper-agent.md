# Chapter 4 — The Trade-Plan Gatekeeper Agent

[← The Pre-Market Briefing Agent](03-pre-market-briefing-agent.md) | [Volume 11 Home](README.md) | [Next: The Journal & Analytics Agent →](05-journal-analytics-agent.md)

---

This is the agent that protects you from yourself. Most retail accounts don't die from bad analysis — they die from **broken discipline**: the impulsive entry, the oversized position, the revenge trade, the setup that skipped half the checklist. The **Trade-Plan Gatekeeper** runs your pre-trade checklist (**[Vol 10, Ch. 4](../vol-10-daily-routine/04-trading-session-routine.md)** / **[Vol 4](../vol-4-strategy-systems/README.md)**) against *every* proposed trade — tirelessly, identically, immune to the emotions that make you cut corners.

> 🔑 **The Gatekeeper enforces rules you already wrote — it doesn't invent them.** It is not deciding whether the trade is "good." It is checking whether *this trade obeys the rules you set when you were calm*. That distinction is everything: it keeps the agent inside the co-pilot role (Ch. 1) and keeps your discipline intact when adrenaline is high.

---

## 4.1 What the Gatekeeper does

You describe a setup you're considering; it returns a structured **GO / NO-GO** verdict against your checklist:

```
┌─ TRADE CHECK — EUR/USD long ───────────────────────────────────────────┐
│ □ Aligns with my macro/daily BIAS?            ✅ (bias: long per briefing)│
│ □ At a meaningful LEVEL?                       ✅ (H4 support 1.0820)      │
│ □ Real CONFLUENCE (≥2 factors)?               ✅ (support + trendline)    │
│ □ Valid TRIGGER present?                       ⚠️ ("forming," not closed) │
│ □ Stop at invalidation, reward ≥ 2R?          ✅ (SL 1.0795, TP 1.0890)  │
│ □ SIZED so stop = ≤ 1% risk?                  ❌ (your size = 1.8% risk)  │
│ □ No high-impact event imminent?              ✅ (next event in 4h)       │
│ □ Calm — no FOMO / revenge / overtrading?     ⚠️ (3rd trade in 20 min)   │
│                                                                          │
│ VERDICT: ❌ NO-GO — 1 hard fail (size > 1% risk) + 2 cautions.           │
│ FIX: reduce size to ≤1% risk; wait for trigger candle to CLOSE; check    │
│ whether this is overtrading. Re-run when addressed.                       │
└─────────────────────────────────────────────────────────────────────────┘
```

The rule is simple and strict: **any hard box unchecked → NO-GO**. The agent's job is to make that rule un-skippable.

---

## 4.2 Why an AI Gatekeeper beats a paper checklist

You already have a checklist (Vol 4/10). Why route it through an agent?

```
A PAPER CHECKLIST                    THE GATEKEEPER AGENT
  • Easy to rush or "eyeball"          • Forces you to articulate each box in words
  • Skipped under emotion              • Runs identically every time, unemotionally
  • Silent on position size            • Computes the risk % from your numbers
  • Doesn't push back                  • Names the specific fail and the fix
  • No record                          • The check itself becomes a journal note (Ch. 5)
```

The act of *typing out* the setup to the Gatekeeper is itself a discipline circuit-breaker — it inserts a deliberate pause between impulse and execution, which is exactly where revenge and FOMO trades die.

> ⚠️ **The Gatekeeper checks rules, not market wisdom.** It cannot know if a setup will work — nothing can (Ch. 1). A "GO" verdict means *"this trade obeys your rules,"* not *"this trade will win."* You can follow every rule and still lose the trade; that's normal and fine (Vol 4 — it's about the process, not any single outcome). Never read "GO" as a prediction.

---

## 4.3 The position-size & risk function

The most valuable concrete thing the Gatekeeper does is **math you must never get wrong**: position sizing to a fixed risk (Vol 1, Ch. 5 / Vol 4).

```
You give:  account size, risk % (e.g. 1%), entry, stop, pair.
It returns: max risk in $, stop distance in pips, and the position size (lots)
            that keeps the loss at your stop ≤ your risk %.
It flags:  if the size you INTENDED exceeds your risk rule → hard NO-GO.
```

This single function prevents the most common account-killer: an oversized position. Still, **sanity-check the arithmetic** — verify against your broker's calculator the first several times (Ch. 1: verify everything).

---

## 4.4 The core prompt (starter)

A version usable in any chat app — full version in the **[Prompt Pack](09-agent-prompt-pack.md)**:

```
ROLE: You are my trade-plan gatekeeper. You check a proposed trade against MY fixed
rules and return GO / NO-GO. You do NOT predict outcomes or judge if it will "work."

MY RULES (from my Vol 7 plan):
  • Bias must align with my stated daily/macro bias
  • Entry at a meaningful level with ≥2 confluence factors and a valid, CLOSED trigger
  • Stop at invalidation; reward ≥ 2R
  • Risk ≤ 1% of account per trade; account = [$X]
  • No entries within [30] min of a high-impact event
  • Must be calm — not revenge/FOMO/overtrading (>[N] trades or after a big loss)

WHEN I DESCRIBE A TRADE:
  1. Check each rule; mark ✅ / ⚠️ / ❌ with a one-line reason.
  2. Compute the position size for ≤1% risk from my entry/stop/account.
  3. VERDICT: any hard ❌ → NO-GO. List the specific fixes.
  4. Be strict and unemotional. Never soften a hard fail.

DON'T: predict if it'll win, encourage a trade that breaks a rule, or invent rules.
```

---

## 4.5 Using it in the session (without slowing to a crawl)

```
SESSION FLOW (Vol 10, Ch. 4):
  Setup appears → describe it to the Gatekeeper → read verdict →
    GO  → execute exactly as planned (entry, stop, size, target)
    NO-GO → do NOT trade; note the fix; wait for a clean setup
```

For scalpers where seconds matter, you won't run it on every entry live — instead use it to **pre-validate your setups before the session** and as a **circuit-breaker** when you feel the urge to deviate. For day/swing trading, running it per trade is realistic and powerful.

> 🔑 **The Gatekeeper's highest value is at your weakest moment.** When you're tilted after a loss and itching for revenge, that's exactly when a calm, rule-bound second voice saves your account. Build the habit of running it *especially* when you least want to — that reluctance is the signal you need it most.

---

## 4.6 Chapter summary

```
• The Gatekeeper runs your pre-trade CHECKLIST (Vol 4/10) on every proposed trade and
  returns a strict GO / NO-GO. Any hard box unchecked → NO-GO. It enforces rules you
  wrote when calm; it does not invent them or predict outcomes.
• It beats a paper checklist: unemotional, identical every time, computes risk %, names
  the fail + fix, and the act of typing the setup is a discipline circuit-breaker.
• Its key function is POSITION SIZING to ≤1% risk — preventing the #1 account-killer.
  Verify the math against your broker's calculator early on.
• "GO" means "obeys your rules," NOT "will win." You can follow every rule and lose —
  that's normal; it's about process, not any single outcome.
• Run it per-trade for day/swing; for scalping, pre-validate setups and use it as a
  circuit-breaker. Its value is highest exactly when you're tilted and least want it.
```

---

[← The Pre-Market Briefing Agent](03-pre-market-briefing-agent.md) | [Volume 11 Home](README.md) | [Next: The Journal & Analytics Agent →](05-journal-analytics-agent.md)
