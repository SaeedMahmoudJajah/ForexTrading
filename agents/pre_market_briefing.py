#!/usr/bin/env python3
"""Pre-Market Briefing Agent — Forex Trading Playbook, Vol. 11, Ch. 3.

Turns your raw morning inputs (economic calendar, overnight notes, risk-regime
readings, marked levels) into a clean, consistent pre-market briefing in the
7-section format from the playbook — so you start the day prepared, not staring
at a blank screen.

THE RULE THIS TOOL OBEYS (Vol. 11): it PREPARES you; it never predicts the market
or tells you what to trade. It organises what you gave it and ends by asking YOU
the questions that form your own bias and plan. Always verify event times, prices,
and numbers at the source before you act on them.

Two ways to run it:
  • No API key  -> assembles the briefing deterministically from your inputs and
                   ALSO writes a ready-to-paste prompt you can drop into any chat.
  • With a key  -> Claude writes the briefing's synthesis sections for you
                   (set ANTHROPIC_API_KEY, then `pip install anthropic`).

Usage:
  python3 agents/pre_market_briefing.py                 # uses config.json + inputs/briefing-inputs.md
  python3 agents/pre_market_briefing.py --ai            # let Claude synthesise (needs API key)
  python3 agents/pre_market_briefing.py --inputs path.md --config path.json
  python3 agents/pre_market_briefing.py --print         # also echo to the terminal

Output: agents/briefings/<date>.md  (+ agents/briefings/<date>.paste-prompt.md in no-AI mode)
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(ROOT, "config.json")
EXAMPLE_CONFIG = os.path.join(ROOT, "config.example.json")
DEFAULT_INPUTS = os.path.join(ROOT, "inputs", "briefing-inputs.md")
EXAMPLE_INPUTS = os.path.join(ROOT, "inputs", "briefing-inputs.example.md")
BRIEFINGS_DIR = os.path.join(ROOT, "briefings")

# The seven sections of the briefing (Vol. 11, Ch. 3).
SECTIONS = ["Calendar", "Overnight", "Regime", "Levels", "Themes"]

VERIFY_FOOTER = (
    "> ⚠️ **Verify before you act.** Confirm every event time, price, and number at the "
    "source (your broker, the official economic calendar, the actual chart). This briefing "
    "organises what you provided — it does not predict the market. Form your own bias and plan."
)

# Strict instructions for the AI path — these keep the agent a co-pilot, not an oracle.
SYSTEM_PROMPT = """You are a pre-market briefing analyst for a disciplined retail forex trader.
Your job is to PREPARE the trader to trade by organising the information they give you.
You do NOT predict the market, give buy/sell calls, or state any directional view.

Produce a concise, skimmable daily briefing in EXACTLY these seven sections, as Markdown:
1. CALENDAR    — today's high-impact events for the trader's pairs, with the exact times given. Flag clustering/conflicts.
2. OVERNIGHT   — what moved in the Asian session and why, briefly, from the notes provided.
3. RISK REGIME — a risk-on / risk-off read from the DXY / yields / VIX / gold figures provided (describe what the data shows; do not forecast).
4. KEY LEVELS  — the trader's marked support/resistance per pair, cleanly tabulated.
5. THEMES      — the current macro narrative in play (1-3 bullets), from the themes provided plus what the inputs imply.
6. WATCH       — the pairs and events most worth attention today, and why.
7. PROMPTS     — 3-4 sharp questions that help the TRADER form their OWN bias and day plan (e.g. "What's your bias on EUR/USD and what would invalidate it?").

Hard rules:
- Use ONLY the information the trader provides. Never invent events, numbers, prices, or news.
- If a section has no input, say "No input provided" rather than filling it with speculation.
- Do not predict direction. Do not say what to trade. End with the section-7 questions for the trader.
- Keep it tight and scannable — this gets read every morning."""


# --------------------------------------------------------------------------- IO

def _load_config(path: str | None) -> dict:
    chosen = path or (DEFAULT_CONFIG if os.path.exists(DEFAULT_CONFIG) else EXAMPLE_CONFIG)
    if not os.path.exists(chosen):
        sys.exit(f"Config not found: {chosen}\nCopy config.example.json to config.json and edit it.")
    with open(chosen, encoding="utf-8") as f:
        cfg = json.load(f)
    if chosen.endswith("config.example.json"):
        print(f"ℹ️  Using {os.path.basename(chosen)} (copy it to config.json and personalise it).")
    return cfg


def _load_inputs(path: str | None) -> tuple[str, dict[str, str]]:
    chosen = path or (DEFAULT_INPUTS if os.path.exists(DEFAULT_INPUTS) else EXAMPLE_INPUTS)
    if not os.path.exists(chosen):
        sys.exit(
            f"Inputs not found: {chosen}\n"
            "Copy inputs/briefing-inputs.example.md to inputs/briefing-inputs.md and fill it in this morning."
        )
    with open(chosen, encoding="utf-8") as f:
        raw = f.read()
    if chosen.endswith(".example.md"):
        print(f"ℹ️  Using {os.path.basename(chosen)} (copy it to briefing-inputs.md and fill it in daily).")
    return chosen, _parse_sections(raw)


def _parse_sections(md: str) -> dict[str, str]:
    """Split an inputs file into {SectionName: body} on `## Header` lines."""
    out: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in md.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            if current is not None:
                out[current] = "\n".join(buf).strip()
            current = m.group(1).strip().split()[0].capitalize()  # "Calendar (high-impact)" -> "Calendar"
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        out[current] = "\n".join(buf).strip()
    return out


# ----------------------------------------------------------------- assembly (no AI)

def _section_body(inputs: dict[str, str], key: str) -> str:
    body = inputs.get(key, "").strip()
    return body if body else "_No input provided._"


def assemble_briefing(cfg: dict, inputs: dict[str, str], date: str) -> str:
    pairs = ", ".join(cfg.get("pairs", [])) or "_(set your pairs in config.json)_"
    session = cfg.get("session", "_(set your session)_")
    parts = [
        f"# Pre-Market Briefing — {date}",
        "",
        f"**Pairs:** {pairs}  ·  **Session:** {session}",
        "",
        VERIFY_FOOTER,
        "",
        "## 1. Calendar — high-impact events today",
        _section_body(inputs, "Calendar"),
        "",
        "## 2. Overnight — what moved while you slept",
        _section_body(inputs, "Overnight"),
        "",
        "## 3. Risk Regime — risk-on / risk-off read",
        _section_body(inputs, "Regime"),
        "",
        "## 4. Key Levels — marked support / resistance",
        _section_body(inputs, "Levels"),
        "",
        "## 5. Themes — the macro narrative in play",
        _section_body(inputs, "Themes") if inputs.get("Themes") else _themes_from_config(cfg),
        "",
        "## 6. Watch — most worth your attention",
        "_Decide from sections 1-5 which pairs/events deserve focus today._",
        "",
        "## 7. Prompts — answer these to form YOUR bias & plan",
        _bias_questions(cfg),
    ]
    return "\n".join(parts).rstrip() + "\n"


def _themes_from_config(cfg: dict) -> str:
    themes = cfg.get("themes", [])
    if not themes:
        return "_No themes provided._"
    return "\n".join(f"- {t}" for t in themes)


def _bias_questions(cfg: dict) -> str:
    pairs = cfg.get("pairs", []) or ["your main pair"]
    qs = [
        f"- What is your bias on **{pairs[0]}** today, and what specific level/event would invalidate it?",
        "- Which one event on today's calendar most threatens your plan — and what's your rule around it?",
        "- Is today a risk-on or risk-off day, and does your bias agree with that regime?",
        "- What is the single A+ setup you'd actually take today, and where is your line in the sand?",
    ]
    if len(pairs) > 1:
        qs.insert(1, f"- Where do **{pairs[1]}** and **{pairs[0]}** agree or conflict, and which leads?")
    return "\n".join(qs)


def build_paste_prompt(cfg: dict, inputs: dict[str, str], date: str) -> str:
    """A ready-to-paste prompt for any chat assistant (the Level 0 path from the playbook)."""
    pairs = ", ".join(cfg.get("pairs", [])) or "(your pairs)"
    session = cfg.get("session", "(your session)")
    blocks = [f"### {k.upper()}\n{inputs.get(k, '').strip() or '(none provided)'}" for k in SECTIONS]
    return (
        f"{SYSTEM_PROMPT}\n\n"
        f"MY CONTEXT — Pairs: {pairs}. Session: {session}. Date: {date}.\n\n"
        "MY INPUTS FOR TODAY:\n\n" + "\n\n".join(blocks) + "\n\n"
        "Now produce my briefing in the seven sections. Remember: organise only what I gave you, "
        "do not predict or give buy/sell calls, and end with the questions for me."
    )


# ------------------------------------------------------------------- AI synthesis

def ai_briefing(cfg: dict, inputs: dict[str, str], date: str) -> str:
    try:
        import anthropic
    except ImportError:
        sys.exit("AI mode needs the Anthropic SDK. Install it with:  pip install anthropic")
    if not (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")):
        sys.exit("AI mode needs an API key. Set ANTHROPIC_API_KEY, or run without --ai for the no-key path.")

    pairs = ", ".join(cfg.get("pairs", [])) or "(unset)"
    session = cfg.get("session", "(unset)")
    themes = "; ".join(cfg.get("themes", [])) or "(none)"
    user_blocks = [f"### {k.upper()}\n{inputs.get(k, '').strip() or '(none provided)'}" for k in SECTIONS]
    user_msg = (
        f"MY CONTEXT — Pairs: {pairs}. Session: {session}. Standing themes: {themes}. Date: {date}.\n\n"
        "MY RAW INPUTS FOR TODAY:\n\n" + "\n\n".join(user_blocks)
    )

    client = anthropic.Anthropic()
    model = cfg.get("model", "claude-opus-4-8")
    resp = client.messages.create(
        model=model,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    header = f"# Pre-Market Briefing — {date}\n\n**Pairs:** {pairs}  ·  **Session:** {session}\n\n{VERIFY_FOOTER}\n"
    return f"{header}\n{text}\n\n---\n{VERIFY_FOOTER}\n"


# --------------------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description="Pre-Market Briefing Agent (Vol. 11, Ch. 3)")
    ap.add_argument("--config", help="Path to config JSON (default: agents/config.json)")
    ap.add_argument("--inputs", help="Path to today's inputs Markdown (default: agents/inputs/briefing-inputs.md)")
    ap.add_argument("--date", help="Date label (default: today, YYYY-MM-DD)")
    ap.add_argument("--ai", action="store_true", help="Let Claude synthesise the briefing (needs ANTHROPIC_API_KEY)")
    ap.add_argument("--print", dest="echo", action="store_true", help="Also print the briefing to the terminal")
    args = ap.parse_args()

    date = args.date or _dt.date.today().isoformat()
    cfg = _load_config(args.config)
    _, inputs = _load_inputs(args.inputs)

    os.makedirs(BRIEFINGS_DIR, exist_ok=True)
    out_path = os.path.join(BRIEFINGS_DIR, f"{date}.md")

    if args.ai:
        briefing = ai_briefing(cfg, inputs, date)
    else:
        briefing = assemble_briefing(cfg, inputs, date)
        prompt_path = os.path.join(BRIEFINGS_DIR, f"{date}.paste-prompt.md")
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(build_paste_prompt(cfg, inputs, date) + "\n")
        print(f"📝 Paste-ready prompt: {prompt_path}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(briefing)
    print(f"✅ Briefing written: {out_path}")

    if args.echo:
        print("\n" + "-" * 70 + "\n" + briefing)


if __name__ == "__main__":
    main()
