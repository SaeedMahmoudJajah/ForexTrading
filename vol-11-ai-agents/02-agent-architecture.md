# Chapter 2 — The Agent Architecture

[← The AI-Augmented Trader](01-ai-augmented-trader.md) | [Volume 11 Home](README.md) | [Next: The Pre-Market Briefing Agent →](03-pre-market-briefing-agent.md)

---

You don't want *one* do-everything AI; you want a **small team of specialized agents**, each with a narrow job, mapped onto the moments of your trading day. This chapter gives you the architecture — what an "agent" actually is, which agents to build, in what order, and how they connect into the routine of **[Vol 10](../vol-10-daily-routine/README.md)**.

> 🔑 **Specialized beats general.** A single agent told to "help me trade" gives vague, mediocre output. Five agents each with one sharp job — brief me, vet this trade, log this, research this, review my week — each give excellent output, because each has a clear role, a fixed format, and a focused context. Build narrow specialists, not one generalist.

---

## 2.1 What "an agent" actually means here

Strip away the hype and an AI "agent," for your purposes, is just three things:

```
AN AGENT =  ROLE + INSTRUCTIONS + (optionally) TOOLS & MEMORY

  ROLE          a clear identity and single job ("You are my pre-market briefing analyst")
  INSTRUCTIONS  exactly what to do, what format to output, and what NOT to do (its rules)
  TOOLS         optional access to live data (web, calendar, your files, a price API)
  MEMORY        optional persistence — your rules, your plan, your trade history
```

In practice an agent can be as simple as **a saved prompt you paste into a chat**, or as advanced as **a script that calls an LLM API, pulls live data, and writes to your journal file**. Start simple. A well-written prompt you actually use beats a sophisticated system you never finish building (Ch. 8).

```
MATURITY LADDER (start at the top; climb only as needed):
  LEVEL 0  A saved prompt you paste into a chat app each day            ← start here
  LEVEL 1  A "custom" reusable assistant with a fixed system prompt
  LEVEL 2  + tools: it can search the web / read your files / a calendar
  LEVEL 3  + memory & data: it reads your journal, knows your plan
  LEVEL 4  + orchestration: a script chains agents and writes outputs    ← advanced
```

---

## 2.2 The support-layer model

The core architectural idea: AI sits as a **support layer wrapped around you**, the decision-maker. It never sits *between* you and the market.

```
        ❌ WRONG (oracle)                    ✅ RIGHT (co-pilot)

     MARKET → AI → YOU → order         MARKET → YOU → order
                                                  ▲
       AI decides, you click            AI support layer feeds YOU:
                                          briefing · checks · logs ·
                                          research · review
```

Every agent's output flows *to you* to improve your decision. No agent's output flows *to the market* without you in the loop. This single rule keeps the whole system safe (Ch. 1).

---

## 2.3 The five core agents (and how they map to your day)

Map the agents directly onto the **[Vol 10](../vol-10-daily-routine/README.md)** routine — that's what makes them stick, because they attach to cues you already have:

| Agent | When (routine cue) | Its one job | Chapter | Feeds from |
|-------|--------------------|-------------|---------|------------|
| **Pre-Market Briefing** | Morning prep | Assemble a structured daily briefing | [Ch. 3](03-pre-market-briefing-agent.md) | Vol 3, 6 |
| **Trade-Plan Gatekeeper** | Before each entry | Vet the trade against your rules | [Ch. 4](04-trade-plan-gatekeeper-agent.md) | Vol 4, 7 |
| **Journal & Analytics** | Post-market close | Log trades & compute KPIs | [Ch. 5](05-journal-analytics-agent.md) | Vol 4 |
| **Macro & News Research** | Off-hours / as needed | Digest news → pair impact | [Ch. 6](06-macro-research-agent.md) | Vol 6, 8 |
| **Review & Coaching** | Weekly / monthly | Find patterns, teach, plan | [Ch. 7](07-review-coaching-agent.md) | Vol 4, 7, 10 |

> 🔑 **Anchor each agent to an existing routine cue and it becomes automatic.** "Coffee → run the Briefing agent." "Before I click buy → run the Gatekeeper." "Session close → feed the Journal agent." "Sunday → run the Review agent." The agents don't add a new routine; they plug into the one you already have from Vol 10.

---

## 2.4 The build order — Tier by tier

Don't build all five at once (that's the Vol 10 over-reach mistake). Build in tiers, mastering each before adding the next:

```
TIER 1 — build first (highest leverage, lowest risk):
  1. JOURNAL & ANALYTICS  — the single highest-ROI agent; start logging immediately
  2. PRE-MARKET BRIEFING  — removes the biggest daily friction (prep)
  3. TRADE-PLAN GATEKEEPER — your discipline enforcer at the point of decision

TIER 2 — add as you mature:
  4. MACRO & NEWS RESEARCH — depth on fundamentals (pairs well with Vol 6)
  5. REVIEW & COACHING     — runs on your now-rich journal data

TIER 3 — optional / advanced (Ch. 8):
  • Backtest & strategy-analysis helper · Accountability/habit checker
  • Orchestration that chains the above
```

> ⚠️ **Resist the urge to automate the decision as you climb tiers.** The more capable your system gets, the more tempting it is to let it "just take the obvious trades." Don't. Capability is not permission. The prime directive (Ch. 1) holds at every tier: agents support, you decide.

---

## 2.5 Three things every agent needs from you

Whatever the agent, it can only be as good as what you give it. Every agent in this volume depends on three inputs you must supply:

1. **Your rules & plan (context).** The Gatekeeper can't check a trade against rules it doesn't have. Feed each agent the relevant parts of your **[Vol 7](../vol-7-complete-trading-plan/README.md)** trading plan — your strategy, risk limits, and checklist. *Garbage-in still equals garbage-out.*
2. **A fixed output format.** Tell the agent *exactly* how to respond (a template, a table, a checklist). Consistent format = output you can actually use day after day and compare over time.
3. **Verification by you.** Every factual claim (a data time, a price level, a rate) is a *draft* until you confirm it at the source (Ch. 1). The agent drafts; you ratify.

---

## 2.6 A note on tools, data, and privacy

We cover the build details in **[Ch. 8](08-building-orchestrating-safeguarding.md)**, but architecturally, know the trade-offs now:

- **A plain chat LLM** (Level 0–1) has no live data — great for structuring, checking, explaining, and reviewing *information you paste in*. It does **not** know today's price or news.
- **An agent with tools** (Level 2+) can fetch live news, an economic calendar, or prices — far more powerful, but you must verify sources and watch costs.
- **Privacy:** your journal and plan are sensitive. Prefer providers/settings that don't train on your data; never paste broker credentials, account numbers, or anything you wouldn't want stored (Ch. 8).

---

## 2.7 Chapter summary

```
• An AGENT = ROLE + INSTRUCTIONS + (optional) TOOLS & MEMORY. It can be as simple as a
  saved prompt or as rich as a script with live data. Start simple (Level 0).
• SUPPORT-LAYER model: AI wraps around YOU and feeds your decisions; it never sits
  between you and the market. Output flows to you, never to the order, without you.
• FIVE core agents map to your Vol 10 routine: Briefing (prep), Gatekeeper (entry),
  Journal (close), Research (off-hours), Review (weekly/monthly).
• Anchor each agent to an existing routine CUE so it becomes automatic.
• BUILD ORDER: Tier 1 = Journal, Briefing, Gatekeeper. Tier 2 = Research, Review.
  Tier 3 = advanced/orchestration. Master each tier before the next.
• Every agent needs three things from you: your RULES/PLAN as context, a FIXED output
  FORMAT, and your VERIFICATION of its facts. Capability is never permission to decide.
```

---

[← The AI-Augmented Trader](01-ai-augmented-trader.md) | [Volume 11 Home](README.md) | [Next: The Pre-Market Briefing Agent →](03-pre-market-briefing-agent.md)
