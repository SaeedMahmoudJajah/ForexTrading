#!/usr/bin/env python3
"""Build the Forex Trading Playbook into a styled, print-ready PDF (book format).

Combines the markdown sources into one HTML document with a cover page,
table of contents, and professional typography, then renders to PDF using
headless Google Chrome (no extra binaries required).

Usage:  python3 build/build_pdf.py
Output: dist/Forex-Trading-Playbook-Vol-1.pdf
"""
import os
import re
import subprocess
import sys

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

TITLE = "The Forex Trading Playbook"
AUTHOR = "Saeed Mahmoud Jajah"
YEAR = "2026"

# Each volume: metadata + its chapter list as (file path, label, TOC title).
VOLUMES = [
    {
        "volume": "Volume 1 — Foundations",
        "subtitle": "A Complete Beginner-From-Scratch Guide",
        "output": "Forex-Trading-Playbook-Vol-1.pdf",
        "intro": "README.md",
        "chapters": [
            ("docs/01-foundations.md",       "Chapter 1", "Foundations — What Forex Actually Is"),
            ("docs/02-terminology.md",       "Chapter 2", "Terminology & Complete Glossary"),
            ("docs/03-market-mechanics.md",  "Chapter 3", "Market Mechanics — How Trading Works"),
            ("docs/04-analysis.md",          "Chapter 4", "Analysis — Deciding What to Trade"),
            ("docs/05-risk-management.md",   "Chapter 5", "Risk Management — Staying Alive"),
            ("docs/06-strategies.md",        "Chapter 6", "Strategies & Trading Styles"),
            ("docs/07-psychology.md",        "Chapter 7", "Trading Psychology — The Mental Game"),
            ("docs/08-getting-started.md",   "Chapter 8", "Getting Started — Step by Step"),
            ("templates/trading-plan.md",    "Appendix A", "Trading Plan Template"),
            ("templates/trading-journal.md", "Appendix B", "Trading Journal Template"),
        ],
    },
    {
        "volume": "Volume 2 — Secrets of the Masters",
        "subtitle": "Secrets & Tactics of the World's Top Traders",
        "output": "Forex-Trading-Playbook-Vol-2.pdf",
        "intro": "vol-2-top-traders/README.md",
        "chapters": [
            ("vol-2-top-traders/01-the-legends.md",        "Chapter 1", "The Legends"),
            ("vol-2-top-traders/02-common-threads.md",     "Chapter 2", "The Common Threads"),
            ("vol-2-top-traders/03-risk-secrets.md",       "Chapter 3", "Risk Secrets of the Elite"),
            ("vol-2-top-traders/04-macro-edge.md",         "Chapter 4", "The Macro Edge"),
            ("vol-2-top-traders/05-trade-construction.md", "Chapter 5", "Trade Construction & Tactics"),
            ("vol-2-top-traders/06-mental-edge.md",        "Chapter 6", "The Mental Edge"),
            ("vol-2-top-traders/07-process-business.md",   "Chapter 7", "Process & The Business of Trading"),
            ("vol-2-top-traders/08-applying-it.md",        "Chapter 8", "Applying It as a Retail Trader"),
            ("vol-2-top-traders/09-quotes-and-reading.md", "Appendix", "Quotes & Reading List"),
        ],
    },
]

MD_EXT = ["tables", "fenced_code", "sane_lists", "nl2br", "attr_list"]


def strip_nav(md: str) -> str:
    """Remove the in-page nav lines (← / → links) and the first H1 (we add our own)."""
    lines = md.splitlines()
    out = []
    h1_removed = False
    for ln in lines:
        s = ln.strip()
        # nav lines look like:  [← X](..) | [Back to README](..) | [Next: Y →](..)
        if ("](" in s) and (("←" in s) or ("→" in s) or ("Back to README" in s)):
            continue
        if s == "---" and not out:  # leading rule after stripped nav
            continue
        if not h1_removed and s.startswith("# "):
            h1_removed = True
            continue
        out.append(ln)
    return "\n".join(out)


# Headings whose entire section is dropped from the intro (handled elsewhere in the PDF).
_SKIP_SECTIONS = ("contents", "how to use this playbook", "license & disclaimer")
# Lines dropped from the intro because they are repo/build meta, not book content.
_SKIP_LINE_MARKERS = (
    "download the book", "➡️", "regenerate", "build/build_pdf",
    "📂 volume 2", "forex-trading-playbook-vol", "educational disclaimer.",
)


def clean_intro(md: str) -> str:
    """Turn a volume README into self-contained book front matter.

    Drops the leading H1, nav lines, the duplicate Contents/TOC section, license
    boilerplate, and repo-only meta (download links, build commands) so the
    introduction reads as part of the book rather than a GitHub landing page.
    """
    md = strip_nav(md)
    lines = md.splitlines()
    out = []
    skipping = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("#"):
            heading = s.lstrip("#").strip().lower()
            skipping = any(heading.startswith(h) for h in _SKIP_SECTIONS)
            if skipping:
                continue
        if skipping:
            continue
        if any(m in s.lower() for m in _SKIP_LINE_MARKERS):
            continue
        out.append(ln)
    # Collapse any runs of blank lines left by removals.
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    return text


def convert(md: str) -> str:
    # Drop internal relative links to other docs/READMEs but keep the link text.
    md = re.sub(r"\[([^\]]+)\]\((?:\.\./)*[\w./#-]*\.md[^)]*\)", r"\1", md)
    html = markdown.markdown(md, extensions=MD_EXT)
    return html


CSS = """
@page {
  size: A4;
  margin: 22mm 18mm 20mm 18mm;
  @bottom-center { content: counter(page); }
}
* { box-sizing: border-box; }
body {
  font-family: "Georgia", "Times New Roman", serif;
  font-size: 10.6pt;
  line-height: 1.55;
  color: #1a1a1a;
  margin: 0;
}
h1, h2, h3, h4 { font-family: "Helvetica Neue", Arial, sans-serif; line-height: 1.25; color: #0b2545; }
h2 { font-size: 17pt; margin: 0 0 6pt; padding-bottom: 6pt; border-bottom: 3px solid #134074; }
h3 { font-size: 13pt; margin: 18pt 0 4pt; color: #134074; }
h4 { font-size: 11pt; margin: 14pt 0 3pt; color: #3a5a8c; }
p { margin: 6pt 0; }
a { color: #134074; text-decoration: none; }
strong { color: #0b2545; }
ul, ol { margin: 6pt 0 6pt 0; padding-left: 20pt; }
li { margin: 2.5pt 0; }
code {
  font-family: "SF Mono", "Menlo", "Consolas", monospace;
  font-size: 8.9pt; background: #eef2f7; padding: 1px 4px; border-radius: 3px; color: #0b2545;
}
pre {
  background: #0b2545; color: #e8eef7; padding: 11pt 13pt; border-radius: 7px;
  overflow: hidden; font-size: 8.4pt; line-height: 1.4; white-space: pre-wrap; word-wrap: break-word;
}
pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
blockquote {
  margin: 9pt 0; padding: 7pt 13pt; background: #fff8e6;
  border-left: 4px solid #e0a800; border-radius: 0 5px 5px 0; font-size: 10pt;
}
blockquote p { margin: 3pt 0; }
table { border-collapse: collapse; width: 100%; margin: 9pt 0; font-size: 9pt; }
th, td { border: 1px solid #c9d4e2; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #134074; color: #fff; font-family: "Helvetica Neue", Arial, sans-serif; }
tr:nth-child(even) td { background: #f4f7fb; }
hr { border: none; border-top: 1px solid #d6dde6; margin: 14pt 0; }

/* Cover */
.cover {
  page-break-after: always; height: 247mm; display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
  background: linear-gradient(160deg, #0b2545 0%, #134074 55%, #1d6fa5 100%);
  color: #fff; margin: -22mm -18mm 0 -18mm; padding: 0 24mm; border-radius: 0;
}
.cover .badge {
  font-family: "Helvetica Neue", Arial, sans-serif; letter-spacing: 3px; font-size: 11pt;
  text-transform: uppercase; opacity: .85; border: 1px solid rgba(255,255,255,.5);
  padding: 5pt 14pt; border-radius: 30px; margin-bottom: 26pt;
}
.cover h1 {
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 38pt; color: #fff;
  margin: 0; line-height: 1.1; font-weight: 800;
}
.cover .chart { font-size: 46pt; margin-bottom: 14pt; }
.cover .sub { font-size: 15pt; opacity: .92; margin-top: 14pt; font-style: italic; }
.cover .vol {
  margin-top: 40pt; font-family: "Helvetica Neue", Arial, sans-serif; font-size: 13pt;
  letter-spacing: 1px; background: rgba(255,255,255,.12); padding: 8pt 20pt; border-radius: 6px;
}
.cover .author { margin-top: 46pt; font-size: 12pt; opacity: .9; }
.cover .year { font-size: 10pt; opacity: .7; margin-top: 4pt; }

/* TOC */
.toc { page-break-after: always; }
.toc h2 { border-bottom: 3px solid #134074; }
.toc ol { list-style: none; padding: 0; counter-reset: none; }
.toc li {
  display: flex; justify-content: space-between; align-items: baseline;
  padding: 7pt 0; border-bottom: 1px dotted #c9d4e2; font-family: "Helvetica Neue", Arial, sans-serif;
}
.toc .ch { font-size: 8.5pt; letter-spacing: 1px; color: #1d6fa5; text-transform: uppercase; display: block; }
.toc .tt { font-size: 11.5pt; color: #0b2545; }

.chapter { page-break-before: always; }
.chapter-head { margin-bottom: 4pt; }
.chapter-head .kicker {
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 9pt; letter-spacing: 2px;
  text-transform: uppercase; color: #1d6fa5; margin-bottom: 2pt;
}
.disclaimer {
  page-break-before: always; font-size: 9pt; color: #555; border-top: 1px solid #ccc;
  padding-top: 10pt; margin-top: 12pt;
}
"""


def build_html(vol: dict) -> str:
    volume, subtitle, chapters = vol["volume"], vol["subtitle"], vol["chapters"]
    cover = f"""
    <div class="cover">
      <div class="chart">📈</div>
      <div class="badge">Forex Trading</div>
      <h1>{TITLE}</h1>
      <div class="sub">{subtitle}</div>
      <div class="vol">{volume}</div>
      <div class="author">{AUTHOR}</div>
      <div class="year">Edition {YEAR}</div>
    </div>
    """

    toc_items = []
    if vol.get("intro"):
        toc_items.append(
            '<li><span><span class="ch">Front Matter</span>'
            '<span class="tt">Introduction</span></span></li>'
        )
    for _, ch, title in chapters:
        toc_items.append(
            f'<li><span><span class="ch">{ch}</span><span class="tt">{title}</span></span></li>'
        )
    toc = (
        '<div class="toc"><h2>Contents</h2><ol>'
        + "".join(toc_items)
        + "</ol>"
        '<p style="margin-top:18pt;font-style:italic;color:#555;font-size:9.5pt">'
        "Read in order on your first pass — each chapter builds on the last — then keep this as a reference."
        "</p></div>"
    )

    body_parts = []
    if vol.get("intro"):
        with open(os.path.join(ROOT, vol["intro"]), encoding="utf-8") as f:
            intro_md = f.read()
        intro_html = convert(clean_intro(intro_md))
        body_parts.append(
            '<section class="chapter"><div class="chapter-head">'
            '<div class="kicker">Front Matter</div></div>'
            f"<h2>Introduction</h2>{intro_html}</section>"
        )
    for path, ch, title in chapters:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            md = f.read()
        md = strip_nav(md)
        inner = convert(md)
        body_parts.append(
            f'<section class="chapter"><div class="chapter-head">'
            f'<div class="kicker">{ch}</div></div>'
            f"<h2>{title}</h2>{inner}</section>"
        )

    disclaimer = (
        '<div class="disclaimer"><strong>Educational disclaimer.</strong> '
        "This material is for educational and informational purposes only and is NOT financial, "
        "investment, or trading advice. Forex/CFD trading carries a high risk of loss; most retail "
        "traders lose money. Past performance does not guarantee future results. You are solely "
        "responsible for your own decisions. Consult a licensed financial professional regarding "
        f"your circumstances. © {YEAR} {AUTHOR}. Released under the MIT License.</div>"
    )

    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{TITLE} — {volume}</title><style>{CSS}</style></head>
<body>{cover}{toc}{''.join(body_parts)}{disclaimer}</body></html>"""


def find_chrome() -> str:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    sys.exit("No Chrome/Chromium/Edge found for PDF rendering.")


def build_volume(vol: dict, chrome: str):
    out_pdf = os.path.join(DIST, vol["output"])
    out_html = os.path.join(DIST, vol["output"].replace(".pdf", ".html"))
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(build_html(vol))
    subprocess.run(
        [
            chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={out_pdf}", "--no-margins",
            "file://" + out_html,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    size = os.path.getsize(out_pdf) / 1024
    print(f"✅ Built {out_pdf} ({size:.0f} KB)")


def main():
    os.makedirs(DIST, exist_ok=True)
    chrome = find_chrome()
    # Optional arg: a substring to build only matching volume(s), e.g. "Vol-2".
    want = sys.argv[1] if len(sys.argv) > 1 else None
    for vol in VOLUMES:
        if want and want.lower() not in vol["output"].lower():
            continue
        build_volume(vol, chrome)


if __name__ == "__main__":
    main()
