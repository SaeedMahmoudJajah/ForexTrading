# Chapter 3 — The Pre-Market Briefing Agent

[← The Agent Architecture](02-agent-architecture.md) | [Volume 11 Home](README.md) | [Next: The Trade-Plan Gatekeeper Agent →](04-trade-plan-gatekeeper-agent.md)

---

The pre-market routine (**[Vol 10, Ch. 3](../vol-10-daily-routine/03-pre-market-routine.md)**) is where your edge is *built* — before any trade. But it's also friction-heavy: calendar, overnight news, risk regime, levels, bias. On a tired morning it's tempting to skip. The **Pre-Market Briefing Agent** removes that friction by assembling a structured briefing so you start every day prepared, not staring at a blank screen.

> 🔑 **The briefing agent's job is preparation, not prediction.** It does *not* tell you what will happen or what to trade. It *gathers and organizes* what you need to form your own bias and plan — turning 45 minutes of scattered prep into a 10-minute review of a clean, consistent briefing. You still form the bias. You still write the plan.

---

## 3.1 What the briefing agent produces

A single, consistent **daily briefing** in a fixed format you review each morning:

```
┌─ DAILY BRIEFING — [date] ──────────────────────────────────────────────┐
│ 1. CALENDAR    Today's high-impact events for my pairs + exact times    │
│ 2. OVERNIGHT   What moved while I slept (Asian session) + why, briefly   │
│ 3. RISK REGIME Risk-on / risk-off read: DXY, yields, equities, VIX, gold │
│ 4. KEY LEVELS  Pre-marked support/resistance on my watchlist pairs       │
│ 5. THEMES      The current macro narrative in play (1–3 bullets, Vol 6)  │
│ 6. WATCH       Pairs/events most worth attention today                   │
│ 7. PROMPTS     Questions for ME to answer to form my own bias & plan     │
└─────────────────────────────────────────────────────────────────────────┘
```

Note section 7: a *good* briefing agent ends by handing the decision back to you — "Based on the above, what's your bias on EUR/USD and what would invalidate it?" It prepares you to think; it doesn't think for you.

---

## 3.2 Two ways to build it

```
LEVEL 0–1 (no live data) — you paste, it structures:
  You gather the raw inputs (calendar screenshot, overnight notes, level list)
  and paste them in. The agent organizes them into the briefing format above,
  flags conflicts, and asks you the bias-forming questions.
  → Simple, private, reliable. The agent never invents data — YOU supplied it.

LEVEL 2+ (with tools) — it fetches, you verify:
  The agent has web/calendar/price tools and assembles the briefing itself.
  → Far less effort, but you MUST verify every event time and number at the
    source. Treat it as a draft analyst report, not gospel.
```

> ⚠️ **The data-accuracy line.** A high-impact event at the wrong time can wreck your day (you trade into an NFP you thought was an hour away). If the agent fetches the calendar, **cross-check every high-impact event against the official source** before you rely on it. The fastest place for hallucination to hurt you is a wrong event time.

---

## 3.3 The core prompt (starter)

A Level 0–1 version you can use today — full versions are in the **[Prompt Pack](09-agent-prompt-pack.md)**:

```
ROLE: You are my pre-market briefing analyst. You prepare me to trade; you never
predict the market or tell me what to trade.

MY CONTEXT:
  • Pairs I trade: [e.g. EUR/USD, GBP/USD, USD/JPY]
  • My session: [e.g. London–NY overlap]
  • My style/bias inputs: [scorecard / trend method from Vol 3 & 6]

INPUTS I'll paste: today's economic calendar, overnight price action notes,
current DXY/yields/VIX read, and my marked key levels.

DO:
  1. Organize everything into my fixed BRIEFING format (7 sections).
  2. Flag any conflicts or notable risk events explicitly.
  3. Keep it concise and factual — only what I gave you; do not invent data.
  4. End with 3–4 sharp questions that help ME form my own bias and day plan.

DON'T: predict direction, give buy/sell calls, or state facts I didn't provide.
```

---

## 3.4 How it plugs into your routine

```
ROUTINE CUE: "coffee → run the briefing agent"  (Vol 10, Ch. 3 & 8)

  07:00  Wake, hydrate, move (Vol 10, Ch. 2)
  08:30  Gather raw inputs → run Briefing agent → review the briefing (10 min)
  08:45  Using section 7's questions, write MY OWN bias + day plan (Vol 10, Ch. 3)
  09:30  At the screen, prepared — hand the plan to the Gatekeeper (Ch. 4)
```

The agent compresses the *gathering*; you keep the *thinking*. You still produce a written bias and an if-then plan in your own words — that act of writing is the prep that builds the edge (Vol 10).

---

## 3.5 Pitfalls to avoid

```
✗ Letting the briefing REPLACE your analysis — it's an input to your thinking, not a substitute
✗ Trusting fetched event times/numbers without verifying at the source
✗ Asking it "so what should I trade?" — that's the oracle trap (Ch. 1); it prepares, you decide
✗ A bloated 3-page briefing you won't read — keep the format tight and skimmable
✗ Skipping the section-7 questions — that's where YOU do the actual prep work
```

---

## 3.6 A working build of this agent

This volume ships a runnable version of the Briefing agent in [`agents/pre-market-briefing.py`](../agents/pre_market_briefing.py) (see [`agents/README.md`](../agents/README.md)). You fill in a short daily inputs file (calendar, overnight, regime, levels), run one command, and get this exact 7-section briefing — either assembled locally (no API key, plus a ready-to-paste prompt) or synthesised by Claude (`--ai`). It enforces every rule above: it organises only what you provide, never predicts, and ends with the bias-forming questions.

---

## 3.7 Chapter summary

```
• The Briefing agent automates the GATHERING of pre-market prep (Vol 10, Ch. 3) into a
  fixed, skimmable daily briefing — calendar, overnight, regime, levels, themes, watch.
• It PREPARES you; it never predicts or gives buy/sell calls. It ends by asking YOU the
  questions that form your own bias and plan.
• Build it Level 0–1 (you paste inputs, it structures) for privacy & reliability, or
  Level 2+ (it fetches) for less effort — but then VERIFY every event time/number.
• Anchor it to a routine cue ("coffee → briefing"). It compresses gathering; you keep
  the thinking and still write your own bias + if-then plan.
• Avoid letting it replace your analysis, trusting unverified data, or asking it what to
  trade. Keep the briefing tight enough that you'll actually read it daily.
```

---

[← The Agent Architecture](02-agent-architecture.md) | [Volume 11 Home](README.md) | [Next: The Trade-Plan Gatekeeper Agent →](04-trade-plan-gatekeeper-agent.md)
