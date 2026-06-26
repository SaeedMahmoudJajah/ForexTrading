# Chapter 6 — The Macro & News Research Agent

[← The Journal & Analytics Agent](05-journal-analytics-agent.md) | [Volume 11 Home](README.md) | [Next: The Review & Coaching Agent →](07-review-coaching-agent.md)

---

The macro world (**[Vol 6](../vol-6-macro-geopolitics/README.md)**) is a firehose: central-bank statements, data releases, geopolitics, intermarket signals — far more than any solo trader can read, let alone synthesize. The **Macro & News Research Agent** is your tireless research analyst. It digests the flood and translates it into the only thing you need: *"what does this mean for my pairs?"* — while you keep the judgment about whether and how to act.

> 🔑 **The research agent turns information into understanding, not into trades.** It explains *what happened* and *why it matters* for your currencies (Vol 6/8) — central bank tone, data surprise, risk sentiment. It does **not** tell you to buy or sell. You combine its synthesis with your own analysis to form a view. Understanding in, decision yours.

---

## 6.1 What it does

```
INPUT:  a statement, headline, data release, or a research question
OUTPUT: a structured, plain-English brief:
  • WHAT happened (the facts, concisely)
  • SURPRISE vs expectations (the part that actually moves price — Vol 6, Ch. 4)
  • WHY it matters (transmission to rates / growth / risk sentiment)
  • PAIR IMPACT (which of MY pairs it touches, and the mechanism — not a direction call)
  • WATCH NEXT (related events/levels to monitor)
  • CONFIDENCE & CAVEATS (what's uncertain; what to verify)
```

Example uses:

```
• "Summarize today's FOMC statement vs the last one — what changed in tone?" (Vol 9, Ch. 3)
• "CPI came in 3.4% vs 3.2% expected — what's the mechanism into USD?" (Vol 6, Ch. 3–4)
• "Explain the current risk-on/off regime and what's driving it." (Vol 6, Ch. 5)
• "How does a rising oil price transmit to CAD and JPY?" (Vol 8)
• "Give me the bull and bear case for EUR/USD over the next month." (balanced, both sides)
```

That last one is a power-move: ask for **both sides** of a thesis. A good research agent argues bull *and* bear, exposing what you might be missing — the opposite of an oracle that just picks a direction.

---

## 6.2 The live-data requirement

This agent is only as good as its information — and macro is time-sensitive:

```
✗ A plain LLM (no tools) has a KNOWLEDGE CUTOFF — it does NOT know today's CPI print,
  this morning's central-bank decision, or current prices. Ask it for "today's news"
  and it may CONFIDENTLY INVENT it. This is the most dangerous misuse in the volume.

✓ Use one of these instead:
  • Paste the actual source text (statement, release, article) → it summarizes THAT
  • Give it a web-search / news tool (Level 2+) → it fetches, you verify the source
  • Use it for TIMELESS understanding ("how do rate differentials drive FX?") where the
    cutoff doesn't matter
```

> ⚠️ **Never ask a cutoff-bound model for current facts and trust the answer.** "What did the ECB do today?" to a tool-less LLM is an invitation to hallucinate a decision that never happened. Either feed it the real source or give it a verified live tool — and even then, confirm market-moving facts at the primary source (the central bank, the official statistics agency). Verify, always (Ch. 1).

---

## 6.3 Where it's genuinely powerful

Used correctly, this agent gives a solo trader something close to an analyst desk:

```
• DECODING central-bank language — parsing hawkish/dovish nuance & what CHANGED (Vol 9, Ch. 3)
• EXPECTATIONS framing — separating the number from the SURPRISE that moves price (Vol 6, Ch. 4)
• INTERMARKET joins — connecting yields, oil, gold, equities to your pairs (Vol 6, Ch. 6 / Vol 8)
• SPEED — a readable brief from a long document in seconds, so you're never blindsided
• EDUCATION — on-demand explanations that deepen your macro fluency over time (Vol 6)
• BALANCE — bull-vs-bear framing that counters your own confirmation bias
```

The goal is not to outsource your macro view — it's to **build your macro fluency faster** and stay current with less effort, so your *own* view is better informed.

---

## 6.4 The core prompt (starter)

Full version in the **[Prompt Pack](09-agent-prompt-pack.md)**:

```
ROLE: You are my macro & news research analyst. You explain what happened and what it
means for MY pairs. You never give buy/sell calls or predict price.

MY PAIRS & THEMES: [e.g. EUR/USD, GBP/USD, USD/JPY; current theme: rate-cut timing]

WHEN I PASTE A SOURCE OR ASK A QUESTION, respond in this format:
  • WHAT happened (concise facts)
  • SURPRISE vs expectations (the price-moving part)
  • WHY it matters (mechanism: rates / growth / risk sentiment)
  • PAIR IMPACT (which of my pairs, and HOW — mechanism, not a direction call)
  • WATCH NEXT · CONFIDENCE & CAVEATS (what to verify)
If I ask for a thesis, give BOTH the bull and bear case.

RULES: only use sources I provide or verified tool results — never invent current facts.
Flag your knowledge cutoff if asked about recent events without a source. Mark uncertainty.
```

---

## 6.5 Plugging it into the routine

```
PRE-MARKET (Vol 10, Ch. 3):   decode an overnight statement → feed your Briefing (Ch. 3)
OFF-HOURS (Vol 10, Ch. 6):    deeper study — understand a theme, build macro fluency (Vol 6)
EVENT-DRIVEN:                  a big release drops → paste it → get the "so what for my pairs"
WEEKLY (Vol 10, Ch. 7):       map next week's macro calendar & themes for your watchlist
```

> 🔑 **Research informs your bias; it never becomes your bias.** The agent hands you a clean, balanced synthesis. You still decide what it means for *your* positioning, weigh it against your technicals (Vol 3), and own the call. An analyst gives the manager a report; the manager decides. You are the manager.

---

## 6.6 Chapter summary

```
• The Research agent is your tireless analyst: it digests macro/news (Vol 6/8) into a
  structured "what happened → surprise → why → PAIR IMPACT → watch → caveats" brief.
• It explains and translates; it does NOT give buy/sell calls. Ask it for BOTH bull and
  bear cases to counter your own bias.
• LIVE-DATA RULE: a tool-less LLM has a knowledge cutoff and will INVENT current news.
  Either paste the real source, give it a verified live tool, or use it for timeless
  understanding. Always confirm market-moving facts at the primary source.
• It's powerful for decoding central-bank language, expectations framing, intermarket
  links, speed, and education — building your macro fluency faster.
• It feeds the Briefing agent and your study; but research INFORMS your bias, it never
  BECOMES it. You're the manager; the agent writes the report.
```

---

[← The Journal & Analytics Agent](05-journal-analytics-agent.md) | [Volume 11 Home](README.md) | [Next: The Review & Coaching Agent →](07-review-coaching-agent.md)
