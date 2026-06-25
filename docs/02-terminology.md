# 2. Terminology & Complete Glossary

[← Foundations](01-foundations.md) | [Back to README](../README.md) | [Next: Market Mechanics →](03-market-mechanics.md)

---

This is your dictionary. Don't try to memorize it all at once — read it through once to get the vocabulary, then refer back whenever you hit a term you don't know. The **core terms** (marked ⭐) are the ones you must understand cold before trading.

---

## 2.1 The absolute essentials (learn these first)

### ⭐ Currency Pair
Two currencies quoted together, e.g. **EUR/USD**. The first is the **base currency**, the second is the **quote (or counter) currency**.

### ⭐ Base Currency
The **first** currency in a pair — the one you are buying or selling. In EUR/USD, the base is **EUR**. The price tells you how much of the quote currency it takes to buy **one unit** of the base.

### ⭐ Quote / Counter Currency
The **second** currency — the one the price is expressed in. In EUR/USD, the quote is **USD**.

### ⭐ Exchange Rate
The price of the pair. **EUR/USD = 1.0850** means 1 EUR = 1.0850 USD.

### ⭐ Going Long (Buy)
Opening a trade expecting the price to **rise**. You buy the base currency. Profit if EUR/USD goes up.

### ⭐ Going Short (Sell)
Opening a trade expecting the price to **fall**. You sell the base currency (forex lets you sell *first* and buy back later). Profit if EUR/USD goes down. **In forex, shorting is as natural and easy as buying** — there's always another currency on the other side.

### ⭐ Pip (Percentage in Point)
The **standard unit of price movement**. For most pairs, a pip is the **4th decimal place** (0.0001).
- EUR/USD moves from 1.0850 → 1.0851 = **1 pip**.
- For **JPY pairs**, a pip is the **2nd decimal place** (0.01). USD/JPY 150.25 → 150.26 = 1 pip.

### ⭐ Pipette (Fractional Pip)
One-tenth of a pip — the **5th decimal place** (or 3rd for JPY pairs). Brokers quote these for precision: EUR/USD shown as **1.08505** — that last digit is a pipette.

### ⭐ Spread
The difference between the **bid** (sell) price and the **ask** (buy) price. This is the broker's primary fee and **your first cost on every trade**.
- Bid 1.08495 / Ask 1.08505 → spread = **1 pip**.
- You always **buy at the ask** and **sell at the bid**. The moment you open a trade you're down by the spread.

### ⭐ Bid Price
The price at which you can **sell** the base currency (the price the market will *bid* to buy it from you). The **lower** of the two quoted prices.

### ⭐ Ask (Offer) Price
The price at which you can **buy** the base currency. The **higher** of the two quoted prices.

### ⭐ Lot (Position Size)
The standardized quantity of currency you trade. Sizes:

| Lot type | Units of base currency | Approx. value per pip (USD-quote pairs) |
|----------|------------------------|------------------------------------------|
| **Standard lot** | 100,000 | ~$10 per pip |
| **Mini lot** | 10,000 | ~$1 per pip |
| **Micro lot** | 1,000 | ~$0.10 per pip |
| **Nano lot** | 100 | ~$0.01 per pip |

**Beginners should trade micro (or nano) lots.** Position size controls how much each pip is worth — and therefore how much you win or lose.

### ⭐ Leverage
Borrowed buying power from your broker, letting you control a large position with a small deposit. Expressed as a ratio:
- **30:1** leverage means $1,000 of your money controls $30,000 of currency.
- Leverage **magnifies both profits AND losses by the same factor.** It is the #1 reason beginners blow up their accounts. High leverage is a *tool*, not a goal — use far less than your broker offers. See [Risk Management](05-risk-management.md).

### ⭐ Margin
The amount of **your own money** the broker sets aside (locks up) to open a leveraged position. It's a deposit/collateral, not a fee.
- With 30:1 leverage, **margin requirement = 1/30 ≈ 3.33%** of the position size.
- A $30,000 position requires ~$1,000 margin.

### ⭐ Stop Loss (SL)
A pre-set order that **automatically closes your trade at a loss** if price moves against you to a defined level. **The single most important risk tool.** Every trade should have one. It caps your downside so a bad trade can't wreck you.

### ⭐ Take Profit (TP)
A pre-set order that **automatically closes your trade in profit** at a target level. Locks in gains without you watching the screen.

---

## 2.2 Margin, leverage & account terms

### Account Balance
The total cash in your account when you have **no open trades**.

### Equity
Your balance **plus or minus** the floating profit/loss of any open trades. `Equity = Balance + Unrealized P/L`. This is your account's *real-time* value.

### Used Margin (Required Margin)
The total margin currently locked up across all your open positions.

### Free Margin (Usable Margin)
`Equity − Used Margin`. The money still available to open new trades or absorb losses.

### Margin Level
`(Equity / Used Margin) × 100%`. A health gauge — the higher, the safer. Brokers act when it drops too low.

### ⭐ Margin Call
A warning from your broker that your equity has fallen too close to your used margin (e.g. margin level hits 100%). You must add funds or close positions. **A margin call means you're in serious trouble — you should never get close to one with proper risk management.**

### ⭐ Stop Out
If losses continue past the margin call, the broker **automatically closes your positions** (at a defined margin level, e.g. 50%) to stop you going negative. This is forced liquidation at the worst possible time.

### Negative Balance Protection
A broker feature (mandatory in EU/UK) ensuring you **can't lose more than your deposit** — your account can't go below zero. Prefer brokers that offer it.

---

## 2.3 Cost & execution terms

### ⭐ Swap (Rollover)
The interest paid or earned for holding a position **overnight**, based on the interest-rate difference between the two currencies. Can be positive (you earn) or negative (you pay). Charged once per day; typically **triple on Wednesdays** (to account for the weekend). Irrelevant for day traders who close out daily; significant for swing/position traders.

### Commission
A flat fee some brokers charge **per trade** (common on raw/ECN accounts), instead of or alongside a wider spread.

### Slippage
The difference between the price you **expected** and the price you **actually got**. Happens in fast markets or thin liquidity. Can be negative (worse) or positive (better). Worst around major news.

### Requote
When a broker can't fill your order at the requested price and offers a new one. A sign of a low-quality (often dealing-desk) broker. Good brokers fill instantly.

### Liquidity
How easily an asset can be bought/sold without moving its price. Majors like EUR/USD are extremely liquid (tight spreads); exotics are not (wide spreads, more slippage).

### Volatility
How much and how fast price moves. High volatility = bigger opportunity **and** bigger risk. Measured by indicators like **ATR** (see [Analysis](04-analysis.md)).

---

## 2.4 Order types (how you enter & exit)

### ⭐ Market Order
Buy or sell **immediately at the current price**. Fast, but you accept whatever price is available (possible slippage).

### ⭐ Limit Order
An order to buy/sell at a **specific price or better**, only filled if price reaches it.
- **Buy Limit** — buy *below* current price (waiting for a dip).
- **Sell Limit** — sell *above* current price (waiting for a rally to fade).

### ⭐ Stop Order (Stop Entry)
An order that triggers once price passes a level, used to enter on momentum/breakouts.
- **Buy Stop** — buy *above* current price (catch an upside breakout).
- **Sell Stop** — sell *below* current price (catch a downside breakdown).

### Trailing Stop
A stop loss that **automatically follows price** as it moves in your favor, locking in profit while giving the trade room to run. E.g. a 20-pip trailing stop stays 20 pips behind the best price reached.

### GTC (Good 'Til Cancelled)
An order that stays active until you cancel it or it fills.

### OCO (One-Cancels-the-Other)
A pair of orders where filling one automatically cancels the other (e.g. a TP and SL bracketing a trade).

---

## 2.5 Currency pair categories

### ⭐ Major Pairs
The most traded pairs, **all containing the USD**, with the tightest spreads and most liquidity:
`EUR/USD`, `USD/JPY`, `GBP/USD`, `USD/CHF`, `USD/CAD`, `AUD/USD`, `NZD/USD`.
**Start here as a beginner** — EUR/USD especially.

### Minor Pairs (Crosses)
Pairs that **don't include the USD** but combine other major currencies, e.g. `EUR/GBP`, `EUR/JPY`, `GBP/JPY`, `AUD/JPY`. Slightly wider spreads.

### Exotic Pairs
A major currency paired with an **emerging-market** currency, e.g. `USD/TRY` (Turkish lira), `USD/ZAR` (South African rand), `USD/MXN` (Mexican peso). **Wide spreads, high volatility, prone to violent moves.** Avoid as a beginner.

### Safe-Haven Currencies
Currencies investors flock to in times of fear: **USD, JPY, CHF** (and gold). They tend to strengthen during crises.

### Commodity Currencies
Currencies of resource-exporting nations, sensitive to commodity prices: **AUD** (metals), **CAD** (oil), **NZD** (dairy/agri).

---

## 2.6 Price action & chart terms

### Candlestick
The standard chart format. Each "candle" shows the **open, high, low, and close** for a time period. A green/white candle closed up; a red/black candle closed down. (Detailed in [Analysis](04-analysis.md).)

### Timeframe
The duration each candle represents: M1 (1 min), M5, M15, M30, H1 (1 hour), H4, D1 (daily), W1 (weekly), MN (monthly). Your strategy dictates which you use.

### ⭐ Support
A price level where falling prices have **historically bounced up** — buyers tend to step in. Acts like a "floor."

### ⭐ Resistance
A price level where rising prices have **historically stalled and reversed** — sellers step in. Acts like a "ceiling." When broken, support and resistance often **swap roles**.

### Trend
The general direction of price.
- **Uptrend** — higher highs and higher lows.
- **Downtrend** — lower highs and lower lows.
- **Range / Sideways** — no clear direction; price oscillates between support and resistance.
- *"The trend is your friend"* — trading with the trend is generally higher-probability for beginners.

### Breakout
When price moves decisively **through** a support or resistance level, often signaling the start of a new move.

### Pullback (Retracement)
A temporary move **against** the prevailing trend before it resumes. Traders often look to enter on pullbacks ("buy the dip" in an uptrend).

### Consolidation
A period where price moves sideways in a tight range, "catching its breath" before the next move.

### Liquidity Grab / Stop Hunt
A sharp move that pushes price just beyond an obvious support/resistance to trigger clustered stop-loss orders, then reverses. Why you avoid placing stops at the *most obvious* levels.

---

## 2.7 Strategy & performance terms

### ⭐ Risk/Reward Ratio (R:R)
The ratio of how much you risk to how much you aim to gain. Risking 20 pips to make 60 = **1:3 R:R**. Higher is better; aim for at least **1:1.5 or 1:2**. Good R:R means you can be wrong more than half the time and still profit.

### ⭐ R-Multiple ("R")
A way to express results in units of risk. If you risk $100 (= 1R) and make $300, that's a **+3R** trade. Thinking in R standardizes everything regardless of position size and is the pro's language for performance.

### ⭐ Win Rate
The percentage of your trades that are profitable. **A high win rate means nothing on its own** — a 90% win rate with tiny wins and huge losses still loses money. Win rate must be judged alongside R:R.

### Expectancy
The average amount you can expect to win (or lose) **per trade** over many trades:
`Expectancy = (Win% × Avg Win) − (Loss% × Avg Loss)`.
A **positive expectancy** is the mathematical definition of having an "edge."

### Edge
A repeatable reason your trades have positive expectancy over time. Without an edge, you're gambling.

### Drawdown
The peak-to-trough decline in your account. A 20% drawdown means your account fell 20% from its high. Recovering from drawdowns is mathematically hard: a **50% loss requires a 100% gain** just to break even.

### Position Sizing
Calculating *how big* a trade should be so that your loss (if the stop is hit) equals a fixed, small % of your account. **The core skill of risk management.** (Full method in [Risk Management](05-risk-management.md).)

### Scaling In / Out
**Scaling in** = adding to a position in pieces rather than all at once. **Scaling out** = closing a position in pieces to lock in partial profit.

### Hedging
Holding offsetting positions to reduce risk (e.g. long and short related pairs). Advanced and often restricted; not for beginners.

---

## 2.8 Trading styles (defined in detail in [Strategies](06-strategies.md))

| Style | Holding time | Trades/day | Timeframes |
|-------|-------------|-----------|------------|
| **Scalping** | Seconds–minutes | Many (10s–100s) | M1–M5 |
| **Day Trading** | Minutes–hours (closed same day) | A few | M5–H1 |
| **Swing Trading** | Days–weeks | A few/week | H4–D1 |
| **Position Trading** | Weeks–months | A few/month | D1–W1 |

---

## 2.9 Fundamental / economic terms

### Interest Rate
Set by **central banks** — the single biggest long-term driver of currencies. Higher rates generally attract capital and strengthen a currency.

### Central Bank
The institution managing a nation's money & rates: **Fed** (USA), **ECB** (Eurozone), **BoE** (UK), **BoJ** (Japan), **RBA** (Australia), **BoC** (Canada), **SNB** (Switzerland), **RBNZ** (New Zealand).

### Hawkish vs. Dovish
- **Hawkish** = leaning toward *raising* rates / tightening (generally currency-positive).
- **Dovish** = leaning toward *cutting* rates / easing (generally currency-negative).

### Inflation (CPI)
Rising prices. High inflation often pushes central banks to raise rates. **CPI** (Consumer Price Index) is the headline inflation report markets watch closely.

### NFP (Non-Farm Payrolls)
A major **US jobs report** released the first Friday of each month. One of the most market-moving events in forex — expect big, fast volatility. Beginners often **stay out** around NFP.

### GDP (Gross Domestic Product)
The total economic output of a country; a broad health gauge.

### Economic Calendar
A schedule of upcoming data releases and their expected impact (low/medium/high). **Check it every day before trading** to avoid being blindsided by news.

### Quantitative Easing (QE) / Tightening (QT)
Central-bank programs that expand (QE) or shrink (QT) the money supply, heavily influencing currency value.

---

## 2.10 Platform & broker terms

### MT4 / MT5 (MetaTrader)
The two most common retail trading **platforms** (software). MT4 is the long-time forex standard; MT5 is newer with more markets. Many brokers also offer **cTrader** or their own platforms.

### Spread Betting vs. CFD vs. Spot Forex
Different *legal wrappers* for the same trading. **CFDs** (Contracts for Difference) are most common globally; **spread betting** is a tax-advantaged UK form; **spot forex** is the underlying market. They behave nearly identically for a retail trader. (Availability depends on your country.)

### ECN / STP vs. Market Maker (Dealing Desk)
- **ECN/STP brokers** route your orders to the real market — tighter spreads, usually a commission, no conflict of interest. **Preferred.**
- **Market makers (dealing desks)** take the other side of your trade themselves — possible conflict of interest, but fine if well-regulated.

### Regulation
Oversight by a financial authority that protects you. Trade **only** with brokers regulated by a top-tier body: **FCA** (UK), **ASIC** (Australia), **CySEC** (Cyprus/EU), **NFA/CFTC** (USA), **BaFin** (Germany), **FINMA** (Switzerland), **FSCA** (South Africa). (See [Getting Started](08-getting-started.md).)

### Demo Account
A **free practice account** with virtual money that trades live market prices. Where you learn, risk-free. **Use it for months.**

### Live Account
A real-money account. Same mechanics as demo, but now your emotions are real — which changes everything.

### Slippage / Execution Speed / Latency
How fast and how accurately your broker fills orders. Matters most for scalpers and during news.

---

[← Foundations](01-foundations.md) | [Back to README](../README.md) | [Next: Market Mechanics →](03-market-mechanics.md)
