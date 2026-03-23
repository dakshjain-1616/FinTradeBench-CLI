"""
Embedded dataset of 50+ financial reasoning questions across 5 categories.
Each question has: id, category, question, reference_answer, keywords
"""

QUESTIONS = [
    # ─── MARKET ANALYSIS (10 questions) ───────────────────────────────────────
    {
        "id": "MA001",
        "category": "market_analysis",
        "question": (
            "A stock has a P/E ratio of 35 while its industry peers average 18. "
            "What does this suggest about investor expectations for the company?"
        ),
        "reference_answer": (
            "A P/E ratio of 35 versus an industry average of 18 indicates the stock is trading "
            "at a premium. Investors expect higher future earnings growth for this company "
            "compared to its peers. This premium valuation reflects optimism about the company's "
            "growth prospects, but also implies higher risk if growth expectations are not met."
        ),
        "keywords": ["premium", "growth", "expectations", "valuation", "earnings"],
    },
    {
        "id": "MA002",
        "category": "market_analysis",
        "question": (
            "Describe the significance of a 'golden cross' pattern in technical analysis "
            "and what trading signal it typically generates."
        ),
        "reference_answer": (
            "A golden cross occurs when a short-term moving average (typically the 50-day) "
            "crosses above a long-term moving average (typically the 200-day). It is considered "
            "a bullish signal indicating upward momentum and potential trend reversal from "
            "bearish to bullish. Traders often interpret this as a buy signal."
        ),
        "keywords": ["moving average", "bullish", "crossover", "momentum", "buy signal"],
    },
    {
        "id": "MA003",
        "category": "market_analysis",
        "question": (
            "A stock's price has declined 15% over three months while its volume has "
            "steadily decreased. What does this price-volume relationship suggest?"
        ),
        "reference_answer": (
            "Declining price accompanied by decreasing volume suggests weakening selling "
            "pressure. This pattern may indicate the downtrend is losing momentum and could "
            "signal a potential reversal or stabilization. Low volume during a decline means "
            "fewer sellers are participating, which is less bearish than high-volume declines."
        ),
        "keywords": ["volume", "selling pressure", "momentum", "downtrend", "reversal"],
    },
    {
        "id": "MA004",
        "category": "market_analysis",
        "question": (
            "What does a price-to-book (P/B) ratio below 1.0 indicate about a stock, "
            "and in which sectors is this most commonly observed?"
        ),
        "reference_answer": (
            "A P/B ratio below 1.0 indicates the stock is trading below its book value, "
            "meaning the market values the company at less than its net assets. This can signal "
            "undervaluation or financial distress. It is most commonly observed in banking, "
            "insurance, and other financial sectors, as well as in cyclical industries during "
            "downturns."
        ),
        "keywords": ["book value", "undervaluation", "financial", "banking", "assets"],
    },
    {
        "id": "MA005",
        "category": "market_analysis",
        "question": (
            "Explain how the VIX index (CBOE Volatility Index) relates to market sentiment "
            "and how investors typically use it."
        ),
        "reference_answer": (
            "The VIX measures expected market volatility derived from S&P 500 options prices. "
            "A high VIX (above 30) indicates fear and uncertainty, while a low VIX (below 20) "
            "suggests complacency or confidence. Investors use it as a contrarian indicator: "
            "extreme fear (high VIX) may signal a buying opportunity, while extreme low VIX "
            "may warn of complacency. It is often called the 'fear gauge'."
        ),
        "keywords": ["volatility", "fear", "options", "contrarian", "sentiment"],
    },
    {
        "id": "MA006",
        "category": "market_analysis",
        "question": (
            "A company's stock forms a 'head and shoulders' pattern. What is the expected "
            "price movement and how should a trader respond?"
        ),
        "reference_answer": (
            "A head and shoulders pattern is a bearish reversal pattern consisting of three "
            "peaks: a higher middle peak (head) flanked by two lower peaks (shoulders). Once "
            "the neckline support is broken, the expected price movement is downward by "
            "approximately the distance from the head to the neckline. A trader should "
            "consider selling or shorting the stock after the neckline break."
        ),
        "keywords": ["bearish", "reversal", "neckline", "sell", "short"],
    },
    {
        "id": "MA007",
        "category": "market_analysis",
        "question": (
            "What is the significance of RSI (Relative Strength Index) values above 70 "
            "and below 30?"
        ),
        "reference_answer": (
            "An RSI above 70 indicates overbought conditions, suggesting the asset may be "
            "due for a price correction or pullback. An RSI below 30 indicates oversold "
            "conditions, suggesting potential upward price reversal. Traders use these levels "
            "as signals to sell when overbought and buy when oversold, though these signals "
            "are most reliable in sideways markets."
        ),
        "keywords": ["overbought", "oversold", "correction", "reversal", "RSI"],
    },
    {
        "id": "MA008",
        "category": "market_analysis",
        "question": (
            "How does the dividend discount model (DDM) determine a stock's intrinsic value, "
            "and what are its main limitations?"
        ),
        "reference_answer": (
            "The DDM values a stock as the present value of all expected future dividends, "
            "calculated as D1 / (r - g), where D1 is next year's dividend, r is the required "
            "rate of return, and g is the constant growth rate. Its main limitations include: "
            "it only works for dividend-paying stocks, it is sensitive to small changes in "
            "growth assumptions, and it assumes constant growth, which is unrealistic."
        ),
        "keywords": ["dividend", "present value", "growth rate", "intrinsic value", "discount"],
    },
    {
        "id": "MA009",
        "category": "market_analysis",
        "question": (
            "Describe the concept of 'support and resistance' in technical analysis and "
            "explain what happens when a support level is broken."
        ),
        "reference_answer": (
            "Support is a price level where buying interest is strong enough to prevent "
            "further decline, while resistance is a level where selling pressure stops upward "
            "movement. When a support level is broken, it often becomes a new resistance level "
            "(role reversal). A break of support typically signals continued downward movement "
            "and can trigger stop-loss orders, accelerating the decline."
        ),
        "keywords": ["support", "resistance", "breakout", "role reversal", "stop-loss"],
    },
    {
        "id": "MA010",
        "category": "market_analysis",
        "question": (
            "A stock's forward P/E is significantly lower than its trailing P/E. "
            "What does this indicate about earnings expectations?"
        ),
        "reference_answer": (
            "A forward P/E significantly lower than the trailing P/E indicates that analysts "
            "expect earnings to grow substantially in the coming year. This means the stock "
            "appears cheaper on a forward basis, suggesting positive earnings momentum. "
            "It can signal that the market has already priced in recent poor performance "
            "and expects improvement."
        ),
        "keywords": ["earnings growth", "forward", "trailing", "expectations", "momentum"],
    },

    # ─── RISK ASSESSMENT (11 questions) ──────────────────────────────────────
    {
        "id": "RA001",
        "category": "risk_assessment",
        "question": (
            "A portfolio is 80% invested in technology stocks. What are the primary risks "
            "of this concentration and how would you mitigate them?"
        ),
        "reference_answer": (
            "The primary risk is concentration risk: high exposure to a single sector means "
            "sector-specific downturns will severely impact the portfolio. Technology stocks "
            "are also sensitive to interest rate rises (growth stocks lose value), regulatory "
            "changes, and market sentiment shifts. Mitigation includes diversification across "
            "sectors, adding defensive stocks, bonds, and alternative assets to reduce "
            "correlation."
        ),
        "keywords": ["concentration risk", "diversification", "sector", "correlation", "mitigation"],
    },
    {
        "id": "RA002",
        "category": "risk_assessment",
        "question": (
            "What is Value at Risk (VaR) and how would you interpret a 1-day 95% VaR "
            "of $1 million for a portfolio?"
        ),
        "reference_answer": (
            "Value at Risk (VaR) is a statistical measure of the maximum potential loss "
            "over a specific time period at a given confidence level. A 1-day 95% VaR of "
            "$1 million means there is a 5% probability that the portfolio will lose more "
            "than $1 million in a single day. Conversely, 95% of the time, daily losses "
            "will be less than $1 million."
        ),
        "keywords": ["VaR", "confidence level", "probability", "loss", "statistical"],
    },
    {
        "id": "RA003",
        "category": "risk_assessment",
        "question": (
            "Explain the difference between systematic risk and unsystematic risk, "
            "and which type can be eliminated through diversification."
        ),
        "reference_answer": (
            "Systematic risk (market risk) affects the entire market and cannot be eliminated "
            "through diversification. Examples include recessions, interest rate changes, and "
            "geopolitical events. Unsystematic risk (specific risk) is company or industry-"
            "specific and can be substantially reduced through diversification by holding "
            "uncorrelated assets. Only unsystematic risk can be diversified away."
        ),
        "keywords": ["systematic", "unsystematic", "diversification", "market risk", "specific risk"],
    },
    {
        "id": "RA004",
        "category": "risk_assessment",
        "question": (
            "A bond has a duration of 8 years. If interest rates rise by 1%, "
            "approximately how much will the bond's price change?"
        ),
        "reference_answer": (
            "Using duration as an approximation, a bond with duration of 8 years will "
            "decrease in price by approximately 8% for a 1% rise in interest rates. "
            "This inverse relationship between bond prices and interest rates is fundamental "
            "to fixed income investing. The modified duration formula gives: "
            "Price change ≈ -Duration × Change in yield."
        ),
        "keywords": ["duration", "interest rates", "price change", "inverse", "8%"],
    },
    {
        "id": "RA005",
        "category": "risk_assessment",
        "question": (
            "What is the Sharpe ratio and how is it used to evaluate risk-adjusted returns? "
            "What does a Sharpe ratio below 1.0 indicate?"
        ),
        "reference_answer": (
            "The Sharpe ratio measures excess return per unit of risk, calculated as "
            "(Portfolio Return - Risk-Free Rate) / Standard Deviation. It allows comparison "
            "of returns across portfolios with different risk levels. A Sharpe ratio below 1.0 "
            "indicates the portfolio generates less than 1 unit of excess return per unit of "
            "risk, which is generally considered suboptimal. A ratio above 2.0 is considered "
            "excellent."
        ),
        "keywords": ["Sharpe ratio", "risk-adjusted", "standard deviation", "excess return", "risk-free"],
    },
    {
        "id": "RA006",
        "category": "risk_assessment",
        "question": (
            "Describe liquidity risk in financial markets and explain how it can amplify "
            "losses during a market crisis."
        ),
        "reference_answer": (
            "Liquidity risk is the risk that an asset cannot be sold quickly enough at a "
            "fair price when needed. During a market crisis, liquidity risk amplifies losses "
            "because bid-ask spreads widen dramatically, buyers disappear, and forced sellers "
            "must accept large discounts. This can trigger a cascade of margin calls and "
            "forced selling, further depressing prices in a liquidity spiral."
        ),
        "keywords": ["liquidity", "bid-ask spread", "forced selling", "margin calls", "crisis"],
    },
    {
        "id": "RA007",
        "category": "risk_assessment",
        "question": (
            "What is beta in the context of stock investing, and what does a beta of 1.5 "
            "mean for a stock relative to the market?"
        ),
        "reference_answer": (
            "Beta measures a stock's volatility relative to the overall market. A beta of 1.0 "
            "means the stock moves in line with the market. A beta of 1.5 means the stock is "
            "50% more volatile than the market: if the market rises 10%, the stock is expected "
            "to rise 15%; if the market falls 10%, the stock is expected to fall 15%. "
            "High-beta stocks amplify market movements."
        ),
        "keywords": ["beta", "volatility", "market", "1.5", "amplify"],
    },
    {
        "id": "RA008",
        "category": "risk_assessment",
        "question": (
            "Explain counterparty risk in derivatives trading and how collateral "
            "requirements help manage it."
        ),
        "reference_answer": (
            "Counterparty risk is the risk that the other party in a financial contract will "
            "default on their obligations. In derivatives trading, if one counterparty becomes "
            "insolvent, the other party may lose money on contracts that have positive value. "
            "Collateral requirements (margin) manage this by requiring parties to post assets "
            "proportional to their exposure, reducing potential losses if default occurs."
        ),
        "keywords": ["counterparty", "default", "derivatives", "collateral", "margin"],
    },
    {
        "id": "RA009",
        "category": "risk_assessment",
        "question": (
            "What is drawdown in portfolio management and why is maximum drawdown "
            "an important risk metric?"
        ),
        "reference_answer": (
            "Drawdown measures the peak-to-trough decline in portfolio value over a specific "
            "period. Maximum drawdown represents the largest such decline, showing the worst "
            "case loss an investor would have experienced. It is important because it captures "
            "the psychological and financial impact of losses, recovery time required, and "
            "helps investors assess whether they can tolerate a strategy's worst periods."
        ),
        "keywords": ["drawdown", "peak", "trough", "maximum drawdown", "recovery"],
    },
    {
        "id": "RA010",
        "category": "risk_assessment",
        "question": (
            "How does currency risk affect an international portfolio, and what hedging "
            "instruments can be used to reduce it?"
        ),
        "reference_answer": (
            "Currency risk arises when a portfolio holds assets denominated in foreign "
            "currencies; exchange rate fluctuations can erode returns even if the underlying "
            "assets perform well. For example, a strong home currency reduces returns from "
            "foreign investments when converted back. Hedging instruments include currency "
            "forwards, futures, options, and currency swaps to lock in exchange rates."
        ),
        "keywords": ["currency risk", "exchange rate", "hedging", "forwards", "foreign"],
    },
    {
        "id": "RA011",
        "category": "risk_assessment",
        "question": (
            "A company has a debt-to-equity ratio of 3.5. What does this imply about "
            "its financial risk profile?"
        ),
        "reference_answer": (
            "A debt-to-equity ratio of 3.5 indicates the company uses $3.50 of debt for "
            "every $1 of equity, meaning it is highly leveraged. This high leverage amplifies "
            "returns when times are good but significantly increases financial risk: the company "
            "faces higher interest expenses, reduced financial flexibility, and greater "
            "insolvency risk if earnings decline. Lenders may require higher interest rates."
        ),
        "keywords": ["leverage", "debt", "equity", "financial risk", "insolvency"],
    },

    # ─── EARNINGS INTERPRETATION (11 questions) ───────────────────────────────
    {
        "id": "EI001",
        "category": "earnings_interpretation",
        "question": (
            "A company reports revenue of $500M and net income of $50M. "
            "Calculate the net profit margin and explain what it means."
        ),
        "reference_answer": (
            "Net profit margin = Net Income / Revenue = $50M / $500M = 10%. "
            "This means the company keeps $0.10 of profit for every $1 of revenue after "
            "all expenses, taxes, and interest. A 10% net margin is considered average for "
            "most industries. Higher margins indicate more efficient cost management and "
            "stronger pricing power."
        ),
        "keywords": ["10%", "net profit margin", "revenue", "net income", "efficiency"],
    },
    {
        "id": "EI002",
        "category": "earnings_interpretation",
        "question": (
            "What does EBITDA represent and why do analysts prefer it over net income "
            "when comparing companies across different capital structures?"
        ),
        "reference_answer": (
            "EBITDA stands for Earnings Before Interest, Taxes, Depreciation, and "
            "Amortization. Analysts prefer it over net income for cross-company comparisons "
            "because it removes the effects of financing decisions (interest), accounting "
            "choices (depreciation/amortization), and tax environments, providing a cleaner "
            "view of operational profitability. It approximates operating cash flow."
        ),
        "keywords": ["EBITDA", "depreciation", "amortization", "interest", "operational"],
    },
    {
        "id": "EI003",
        "category": "earnings_interpretation",
        "question": (
            "A company's gross margin has declined from 45% to 38% over two years "
            "while revenue grew 20%. What are the most likely causes and implications?"
        ),
        "reference_answer": (
            "Gross margin compression despite revenue growth suggests rising cost of goods "
            "sold (COGS) relative to revenue. Likely causes include: increased raw material "
            "costs, supply chain disruptions, pricing pressure from competitors, shift to "
            "lower-margin products, or inability to pass cost increases to customers. "
            "Implications include reduced profitability and potential competitive weakness."
        ),
        "keywords": ["gross margin", "COGS", "cost", "compression", "profitability"],
    },
    {
        "id": "EI004",
        "category": "earnings_interpretation",
        "question": (
            "Explain the difference between operating cash flow and net income. "
            "When can a company be profitable but have negative cash flow?"
        ),
        "reference_answer": (
            "Operating cash flow measures actual cash generated from operations, while net "
            "income includes non-cash items like depreciation and accruals. A company can be "
            "profitable but have negative cash flow when: accounts receivable grow rapidly "
            "(revenue recognized but not yet collected), inventory builds up, or capital "
            "expenditure requirements are high. High-growth companies often face this issue."
        ),
        "keywords": ["operating cash flow", "net income", "receivables", "accruals", "non-cash"],
    },
    {
        "id": "EI005",
        "category": "earnings_interpretation",
        "question": (
            "What is earnings per share (EPS) dilution and when does it occur? "
            "How should investors interpret diluted versus basic EPS?"
        ),
        "reference_answer": (
            "EPS dilution occurs when the number of shares outstanding increases, reducing "
            "earnings per share. It occurs with stock option exercises, convertible bond "
            "conversions, secondary stock offerings, or stock-based compensation. Diluted EPS "
            "assumes all dilutive securities are exercised, showing the worst-case per-share "
            "earnings. Investors should use diluted EPS for a more conservative and accurate "
            "assessment."
        ),
        "keywords": ["dilution", "EPS", "shares outstanding", "stock options", "convertible"],
    },
    {
        "id": "EI006",
        "category": "earnings_interpretation",
        "question": (
            "A company reports a one-time gain of $200M from asset sales in its quarterly "
            "earnings. How should analysts adjust their earnings assessment?"
        ),
        "reference_answer": (
            "Analysts should exclude the one-time $200M gain to assess normalized or core "
            "earnings from ongoing operations. One-time or non-recurring items distort the "
            "true profitability trend. Adjusted or 'normalized' earnings remove these items "
            "to provide a cleaner picture of sustainable earnings power. Analysts focus on "
            "recurring operating income as a better predictor of future performance."
        ),
        "keywords": ["non-recurring", "normalized", "adjusted", "one-time", "core earnings"],
    },
    {
        "id": "EI007",
        "category": "earnings_interpretation",
        "question": (
            "What does the interest coverage ratio measure and what level signals "
            "financial stress?"
        ),
        "reference_answer": (
            "The interest coverage ratio measures how many times a company can cover its "
            "interest expense with operating earnings: EBIT / Interest Expense. A ratio below "
            "1.5 generally signals financial stress, as the company barely generates enough "
            "earnings to cover interest payments. Below 1.0 means the company cannot cover "
            "interest from operating earnings, risking default. Healthy companies maintain "
            "ratios above 3.0."
        ),
        "keywords": ["interest coverage", "EBIT", "financial stress", "default", "3.0"],
    },
    {
        "id": "EI008",
        "category": "earnings_interpretation",
        "question": (
            "Compare the significance of revenue growth versus margin expansion "
            "for a mature company versus a high-growth startup."
        ),
        "reference_answer": (
            "For a mature company, margin expansion is more significant as revenue growth "
            "typically slows. Improving profitability through efficiency, pricing power, or "
            "cost control drives value. For a high-growth startup, revenue growth is more "
            "critical as it demonstrates market penetration and scalability potential. "
            "Investors accept low or negative margins in startups if revenue is growing rapidly, "
            "expecting margins to improve at scale."
        ),
        "keywords": ["margin expansion", "revenue growth", "mature", "startup", "scalability"],
    },
    {
        "id": "EI009",
        "category": "earnings_interpretation",
        "question": (
            "What is return on equity (ROE) and how does the DuPont analysis break it "
            "down into component drivers?"
        ),
        "reference_answer": (
            "ROE measures profitability relative to shareholders' equity: Net Income / "
            "Shareholders' Equity. DuPont analysis decomposes ROE into three components: "
            "net profit margin (profitability), asset turnover (efficiency), and equity "
            "multiplier (leverage). Formula: ROE = Net Margin × Asset Turnover × Equity "
            "Multiplier. This helps identify whether ROE is driven by genuine profitability "
            "or financial leverage."
        ),
        "keywords": ["ROE", "DuPont", "net margin", "asset turnover", "leverage"],
    },
    {
        "id": "EI010",
        "category": "earnings_interpretation",
        "question": (
            "A company's revenue grew 30% but accounts receivable grew 60%. "
            "What concern does this raise about earnings quality?"
        ),
        "reference_answer": (
            "When accounts receivable grow significantly faster than revenue, it raises "
            "concerns about earnings quality. It may indicate the company is recognizing "
            "revenue aggressively before cash is collected, offering extended credit terms "
            "to boost sales, or that some receivables may be uncollectible. This suggests "
            "reported earnings may not convert to actual cash, questioning sustainability."
        ),
        "keywords": ["accounts receivable", "earnings quality", "revenue recognition", "cash", "aggressive"],
    },
    {
        "id": "EI011",
        "category": "earnings_interpretation",
        "question": (
            "Explain how depreciation choices affect reported earnings and cash flow, "
            "and why cash flow from operations can be a more reliable measure."
        ),
        "reference_answer": (
            "Depreciation reduces reported net income but is a non-cash charge, so it "
            "does not reduce cash flow. Companies can choose different depreciation methods "
            "(straight-line vs. accelerated) affecting reported earnings. Accelerated "
            "depreciation lowers near-term earnings but increases cash flow statements' "
            "add-backs. Operating cash flow is more reliable as it adjusts for non-cash "
            "items and reflects actual cash generation."
        ),
        "keywords": ["depreciation", "non-cash", "straight-line", "cash flow", "reliable"],
    },

    # ─── TRADING STRATEGY (10 questions) ──────────────────────────────────────
    {
        "id": "TS001",
        "category": "trading_strategy",
        "question": (
            "Explain the logic behind a mean reversion trading strategy and what "
            "market conditions make it most effective."
        ),
        "reference_answer": (
            "Mean reversion assumes that prices deviate temporarily from their historical "
            "average and will eventually return to it. Traders buy when prices fall "
            "significantly below the mean and sell when they rise above it. This strategy "
            "is most effective in range-bound, sideways markets with low volatility and "
            "when assets have strong fundamental anchors. It underperforms in strong trending "
            "markets."
        ),
        "keywords": ["mean reversion", "average", "range-bound", "buy low", "revert"],
    },
    {
        "id": "TS002",
        "category": "trading_strategy",
        "question": (
            "What is the risk-reward ratio in trading and why is a minimum 1:2 ratio "
            "often recommended for retail traders?"
        ),
        "reference_answer": (
            "The risk-reward ratio compares potential loss (risk) to potential gain (reward) "
            "for a trade. A 1:2 ratio means risking $1 to potentially gain $2. A minimum 1:2 "
            "is recommended because it allows traders to be profitable even with a 40-45% "
            "win rate. If you win 50% of trades at 1:2, gains outpace losses significantly. "
            "It provides a mathematical edge over time."
        ),
        "keywords": ["risk-reward", "1:2", "win rate", "profitable", "edge"],
    },
    {
        "id": "TS003",
        "category": "trading_strategy",
        "question": (
            "Compare momentum trading and contrarian trading strategies. "
            "What market conditions favor each approach?"
        ),
        "reference_answer": (
            "Momentum trading buys assets that have been rising (winners) and shorts those "
            "falling (losers), betting trends continue. It works best in trending markets "
            "with sustained directional moves. Contrarian trading takes the opposite side "
            "of prevailing sentiment, buying oversold assets and selling overbought ones. "
            "Contrarian strategies work best during market extremes, bubbles, or panic sell-offs "
            "when assets deviate far from fundamentals."
        ),
        "keywords": ["momentum", "contrarian", "trending", "oversold", "overbought"],
    },
    {
        "id": "TS004",
        "category": "trading_strategy",
        "question": (
            "What is pairs trading and how does it attempt to profit from relative "
            "price movements between two correlated securities?"
        ),
        "reference_answer": (
            "Pairs trading is a market-neutral strategy that identifies two historically "
            "correlated securities and takes a long position in the underperforming one "
            "while shorting the outperforming one. Profit comes when the spread reverts to "
            "its historical mean. It reduces market exposure since gains from one leg offset "
            "losses in the other during broad market moves. It relies on mean-reversion of "
            "the price spread."
        ),
        "keywords": ["pairs trading", "market-neutral", "long", "short", "spread"],
    },
    {
        "id": "TS005",
        "category": "trading_strategy",
        "question": (
            "Explain the concept of dollar-cost averaging (DCA) and when it is "
            "advantageous compared to lump-sum investing."
        ),
        "reference_answer": (
            "Dollar-cost averaging involves investing fixed amounts at regular intervals "
            "regardless of price, automatically buying more shares when prices are low and "
            "fewer when prices are high. DCA reduces the risk of investing a large sum at a "
            "market peak. It is most advantageous in volatile, sideways, or declining markets. "
            "Lump-sum investing statistically outperforms DCA in consistently rising markets "
            "since all capital benefits from gains immediately."
        ),
        "keywords": ["dollar-cost averaging", "DCA", "fixed amount", "volatile", "lump-sum"],
    },
    {
        "id": "TS006",
        "category": "trading_strategy",
        "question": (
            "What is algorithmic trading and what are its key advantages over "
            "discretionary trading?"
        ),
        "reference_answer": (
            "Algorithmic trading uses computer programs to execute trades based on "
            "predefined rules without human intervention. Key advantages include: speed "
            "(executes at milliseconds), elimination of emotional biases, ability to "
            "monitor multiple markets simultaneously, consistent rule-based execution, "
            "backtesting capabilities to validate strategies on historical data, and "
            "reduced transaction costs through optimal execution timing."
        ),
        "keywords": ["algorithmic", "automated", "emotion", "backtesting", "speed"],
    },
    {
        "id": "TS007",
        "category": "trading_strategy",
        "question": (
            "Describe the carry trade strategy in forex markets and the risks involved."
        ),
        "reference_answer": (
            "The carry trade involves borrowing in a low-interest-rate currency and investing "
            "in a high-interest-rate currency to profit from the interest rate differential. "
            "For example, borrowing Japanese yen at near-zero rates and investing in "
            "Australian dollars at higher rates. Risks include: exchange rate risk (the "
            "high-yield currency may depreciate), sudden unwinding during risk-off periods, "
            "and leverage amplifying losses."
        ),
        "keywords": ["carry trade", "interest rate differential", "forex", "unwinding", "depreciate"],
    },
    {
        "id": "TS008",
        "category": "trading_strategy",
        "question": (
            "What is a covered call options strategy and under what market conditions "
            "does it generate optimal returns?"
        ),
        "reference_answer": (
            "A covered call involves holding a long stock position and selling call options "
            "on that stock to collect premium income. The strategy generates optimal returns "
            "in flat to mildly bullish markets where the stock price stays near or slightly "
            "below the strike price at expiration. The premium collected enhances returns "
            "but caps upside if the stock rises above the strike price. It reduces downside "
            "risk by the premium amount."
        ),
        "keywords": ["covered call", "premium", "options", "flat market", "strike price"],
    },
    {
        "id": "TS009",
        "category": "trading_strategy",
        "question": (
            "Explain the concept of position sizing in trading and why it is critical "
            "for long-term trading survival."
        ),
        "reference_answer": (
            "Position sizing determines how much capital to allocate to each trade. "
            "It is critical because even a winning strategy will fail if position sizes "
            "are too large (risking ruin from a losing streak) or too small (insufficient "
            "returns). The Kelly Criterion and fixed fractional methods (e.g., risking 1-2% "
            "per trade) help optimize position sizes to maximize growth while controlling "
            "the risk of catastrophic loss."
        ),
        "keywords": ["position sizing", "Kelly Criterion", "risk of ruin", "capital", "allocation"],
    },
    {
        "id": "TS010",
        "category": "trading_strategy",
        "question": (
            "What is the efficient market hypothesis (EMH) and what are its implications "
            "for active trading strategies?"
        ),
        "reference_answer": (
            "The EMH states that asset prices fully reflect all available information, "
            "making it impossible to consistently achieve above-market returns through "
            "active trading. It exists in three forms: weak (prices reflect historical "
            "data), semi-strong (prices reflect all public information), and strong (prices "
            "reflect all information including private). If EMH holds, active strategies "
            "cannot consistently outperform passive indexing after fees."
        ),
        "keywords": ["EMH", "efficient market", "information", "passive", "outperform"],
    },

    # ─── MACRO ECONOMICS (11 questions) ───────────────────────────────────────
    {
        "id": "ME001",
        "category": "macro_economics",
        "question": (
            "How does an unexpected rise in inflation typically affect stock markets, "
            "bond markets, and the currency in the short term?"
        ),
        "reference_answer": (
            "Unexpected inflation typically: depresses bond prices (yields rise to compensate), "
            "causes mixed stock market reaction (value stocks may hold up better than growth "
            "stocks which lose value as discount rates rise), and strengthens the currency if "
            "markets expect the central bank to raise interest rates in response. Real assets "
            "and commodities often benefit from inflation surprises."
        ),
        "keywords": ["inflation", "bond prices", "interest rates", "discount rates", "currency"],
    },
    {
        "id": "ME002",
        "category": "macro_economics",
        "question": (
            "Explain the relationship between central bank interest rate decisions "
            "and mortgage rates, and how this affects the housing market."
        ),
        "reference_answer": (
            "When central banks raise benchmark rates, mortgage rates typically rise "
            "because lenders increase rates to maintain profit margins and fund mortgages "
            "at higher costs. Higher mortgage rates reduce housing affordability, decrease "
            "demand for home purchases, slow price appreciation or cause price declines, "
            "and reduce housing construction activity. The reverse occurs when rates are cut."
        ),
        "keywords": ["mortgage rates", "central bank", "housing", "affordability", "demand"],
    },
    {
        "id": "ME003",
        "category": "macro_economics",
        "question": (
            "What is the yield curve and what economic signal does an inverted yield "
            "curve historically send?"
        ),
        "reference_answer": (
            "The yield curve plots interest rates of bonds with equal credit quality "
            "but different maturities. Normally it slopes upward (longer maturities yield "
            "more). An inverted yield curve (short-term rates exceed long-term rates) has "
            "historically been one of the most reliable recession predictors, as it suggests "
            "markets expect economic slowdown and future rate cuts. It has preceded every "
            "US recession in the past 50 years."
        ),
        "keywords": ["yield curve", "inverted", "recession", "maturities", "interest rates"],
    },
    {
        "id": "ME004",
        "category": "macro_economics",
        "question": (
            "Describe quantitative easing (QE) and explain how it is intended to "
            "stimulate economic activity."
        ),
        "reference_answer": (
            "Quantitative easing is a monetary policy where a central bank purchases "
            "financial assets (typically government bonds) to inject money into the economy "
            "when conventional rate cuts are insufficient. It lowers long-term interest rates, "
            "increases money supply, encourages lending and investment, boosts asset prices "
            "(wealth effect), and weakens the currency to support exports. It was used "
            "extensively after the 2008 financial crisis and during COVID-19."
        ),
        "keywords": ["quantitative easing", "QE", "central bank", "asset purchases", "money supply"],
    },
    {
        "id": "ME005",
        "category": "macro_economics",
        "question": (
            "How does the Federal Reserve's dual mandate influence its monetary policy "
            "decisions when unemployment is low but inflation is high?"
        ),
        "reference_answer": (
            "The Federal Reserve's dual mandate is to achieve maximum employment and "
            "price stability (targeting ~2% inflation). When unemployment is low but inflation "
            "is high, the two objectives conflict: raising rates controls inflation but risks "
            "increasing unemployment. The Fed typically prioritizes inflation control in this "
            "scenario, accepting slower growth and potential job losses to restore price "
            "stability, as entrenched inflation is harder to combat."
        ),
        "keywords": ["dual mandate", "employment", "price stability", "Federal Reserve", "interest rates"],
    },
    {
        "id": "ME006",
        "category": "macro_economics",
        "question": (
            "Explain the concept of fiscal multiplier and when government stimulus "
            "spending is most effective."
        ),
        "reference_answer": (
            "The fiscal multiplier measures the change in GDP resulting from a change in "
            "government spending. A multiplier above 1 means $1 of government spending "
            "generates more than $1 of GDP growth. Stimulus is most effective during "
            "recessions with high unemployment (idle resources), low interest rates (no "
            "crowding out of private investment), and when spending targets consumption "
            "rather than savings. It is less effective in full-employment economies."
        ),
        "keywords": ["fiscal multiplier", "GDP", "government spending", "recession", "crowding out"],
    },
    {
        "id": "ME007",
        "category": "macro_economics",
        "question": (
            "What is stagflation and why does it create a particularly difficult "
            "challenge for central banks?"
        ),
        "reference_answer": (
            "Stagflation is the rare combination of high inflation, high unemployment, and "
            "slow economic growth simultaneously. It creates a dilemma for central banks: "
            "raising rates to combat inflation would further slow growth and increase "
            "unemployment, while cutting rates to stimulate growth would worsen inflation. "
            "Traditional monetary tools are ineffective as they cannot address both problems "
            "simultaneously. The 1970s oil shocks produced the most notable stagflation period."
        ),
        "keywords": ["stagflation", "inflation", "unemployment", "dilemma", "1970s"],
    },
    {
        "id": "ME008",
        "category": "macro_economics",
        "question": (
            "How do trade deficits affect a country's currency and what are the "
            "long-term economic implications of persistent trade deficits?"
        ),
        "reference_answer": (
            "Trade deficits mean a country imports more than it exports, creating net demand "
            "for foreign currency and downward pressure on the domestic currency. A weaker "
            "currency makes exports cheaper (partially self-correcting) but increases import "
            "costs. Long-term persistent deficits can lead to: growing foreign debt, "
            "dependency on foreign capital inflows, reduced domestic manufacturing capacity, "
            "and potential currency crises if foreign investors lose confidence."
        ),
        "keywords": ["trade deficit", "currency", "imports", "exports", "foreign debt"],
    },
    {
        "id": "ME009",
        "category": "macro_economics",
        "question": (
            "Explain the impact of rising oil prices on both importing and "
            "exporting economies."
        ),
        "reference_answer": (
            "For oil-importing economies, rising oil prices increase production costs "
            "across all sectors (transportation, manufacturing), boost inflation, reduce "
            "consumer spending power, and widen trade deficits. For oil-exporting economies, "
            "rising prices increase government revenues, strengthen the currency (petrocurrency "
            "effect), stimulate domestic investment, but can create 'Dutch disease' where "
            "other export sectors become uncompetitive."
        ),
        "keywords": ["oil prices", "inflation", "importing", "exporting", "Dutch disease"],
    },
    {
        "id": "ME010",
        "category": "macro_economics",
        "question": (
            "What is the money multiplier effect in banking and how does it relate "
            "to fractional reserve banking?"
        ),
        "reference_answer": (
            "The money multiplier describes how initial deposits create a larger increase "
            "in the total money supply through fractional reserve banking. Banks are required "
            "to hold only a fraction of deposits as reserves and can lend the rest. Each loan "
            "creates a new deposit elsewhere, which is again partially lent out. The theoretical "
            "multiplier = 1 / reserve ratio; a 10% reserve ratio creates a maximum 10x "
            "multiplication of the initial deposit."
        ),
        "keywords": ["money multiplier", "fractional reserve", "deposits", "reserve ratio", "lending"],
    },
    {
        "id": "ME011",
        "category": "macro_economics",
        "question": (
            "How does purchasing power parity (PPP) theory explain long-run exchange "
            "rate movements between countries?"
        ),
        "reference_answer": (
            "Purchasing power parity states that exchange rates should adjust so that "
            "identical goods cost the same in different countries when measured in the same "
            "currency. In the long run, currencies of high-inflation countries should "
            "depreciate relative to low-inflation currencies. PPP is most useful for "
            "long-run exchange rate forecasting and cross-country GDP comparisons, but "
            "short-run deviations can persist for years due to capital flows and other factors."
        ),
        "keywords": ["PPP", "purchasing power parity", "exchange rate", "inflation", "depreciate"],
    },

    # ─── NEW MARKET ANALYSIS (3 additional) ───────────────────────────────────
    {
        "id": "MA011",
        "category": "market_analysis",
        "question": (
            "A stock's RSI reading is 78 after a 3-week rally. What does this "
            "indicate and how should a trader interpret it?"
        ),
        "reference_answer": (
            "An RSI of 78 is in overbought territory (above 70), suggesting the stock "
            "has risen too far too fast and may be due for a pullback or consolidation. "
            "Traders may consider taking profits, tightening stop-losses, or avoiding "
            "new long entries. However, in strong trending markets RSI can remain "
            "overbought for extended periods, so confirmation from other signals is prudent."
        ),
        "keywords": ["RSI", "overbought", "pullback", "momentum", "70"],
    },
    {
        "id": "MA012",
        "category": "market_analysis",
        "question": (
            "What is the difference between a support level and a resistance level "
            "in technical analysis, and what happens when price breaks through one?"
        ),
        "reference_answer": (
            "Support is a price level where buying interest historically exceeds selling "
            "pressure, causing price to bounce upward. Resistance is the opposite: a level "
            "where selling exceeds buying, capping price advances. When price breaks through "
            "support, that level often becomes new resistance (role reversal). When price "
            "breaks through resistance, it often becomes new support. Breakouts on high "
            "volume are considered more significant."
        ),
        "keywords": ["support", "resistance", "breakout", "role reversal", "volume"],
    },
    {
        "id": "MA013",
        "category": "market_analysis",
        "question": (
            "A company's stock has a forward P/E of 22 and a PEG ratio of 1.1. "
            "How do these metrics together inform a valuation assessment?"
        ),
        "reference_answer": (
            "A forward P/E of 22 indicates the stock trades at 22 times next year's "
            "expected earnings, which is above-average but not extreme. The PEG ratio "
            "of 1.1 (P/E divided by earnings growth rate) close to 1.0 suggests the "
            "valuation is roughly in line with growth expectations — a PEG near 1 is "
            "often considered fairly valued. Together they indicate a moderately valued "
            "growth stock rather than an expensive or cheap one."
        ),
        "keywords": ["PEG ratio", "forward P/E", "valuation", "growth", "fairly valued"],
    },

    # ─── NEW RISK ASSESSMENT (3 additional) ───────────────────────────────────
    {
        "id": "RA012",
        "category": "risk_assessment",
        "question": (
            "What is liquidity risk and how does it differ from market risk? "
            "Give an example of when liquidity risk becomes critical."
        ),
        "reference_answer": (
            "Liquidity risk is the risk of being unable to buy or sell an asset quickly "
            "at a fair price without significantly moving the market. Market risk is the "
            "risk of price movements against your position. Liquidity risk becomes critical "
            "during market crises when bid-ask spreads widen dramatically, volumes dry up, "
            "and even large institutions cannot exit positions without incurring substantial "
            "losses — for example, during the 2008 financial crisis when mortgage-backed "
            "securities became nearly impossible to sell."
        ),
        "keywords": ["liquidity risk", "market risk", "bid-ask spread", "crisis", "exit"],
    },
    {
        "id": "RA013",
        "category": "risk_assessment",
        "question": (
            "A portfolio has a Sharpe ratio of 0.4 and another has 1.2. "
            "What does this tell you about each portfolio's risk-adjusted performance?"
        ),
        "reference_answer": (
            "The Sharpe ratio measures excess return per unit of risk (standard deviation). "
            "A Sharpe ratio of 0.4 indicates poor risk-adjusted performance — the portfolio "
            "earns little reward for the volatility it carries. A Sharpe ratio of 1.2 is "
            "considered good, meaning the portfolio generates solid returns relative to its "
            "risk. Generally, Sharpe above 1.0 is acceptable, above 2.0 is very good. "
            "Investors prefer higher Sharpe ratios as they indicate more efficient portfolios."
        ),
        "keywords": ["Sharpe ratio", "risk-adjusted", "standard deviation", "volatility", "efficient"],
    },
    {
        "id": "RA014",
        "category": "risk_assessment",
        "question": (
            "Explain counterparty risk in derivatives trading and how central clearing "
            "houses reduce this risk."
        ),
        "reference_answer": (
            "Counterparty risk is the risk that the other party in a derivatives contract "
            "will default on their obligations before the contract is settled. In bilateral "
            "OTC derivatives, each party bears the other's credit risk directly. Central "
            "clearing houses (CCPs) mitigate this by stepping in as buyer to every seller "
            "and seller to every buyer, requiring margin deposits, conducting daily mark-to-"
            "market, and maintaining default funds — so the failure of one participant "
            "does not cascade through the system."
        ),
        "keywords": ["counterparty risk", "default", "clearing house", "margin", "OTC"],
    },

    # ─── NEW EARNINGS INTERPRETATION (3 additional) ───────────────────────────
    {
        "id": "EI012",
        "category": "earnings_interpretation",
        "question": (
            "A company's EPS grew from $2.10 to $2.73 year-over-year. "
            "What is the growth rate and what does it signal about the business?"
        ),
        "reference_answer": (
            "EPS growth rate = ($2.73 - $2.10) / $2.10 = $0.63 / $2.10 = 30%. "
            "A 30% year-over-year EPS growth rate is strong and signals improving "
            "profitability, effective cost management, revenue growth, or share buybacks "
            "reducing share count. Sustained double-digit EPS growth typically commands "
            "premium valuations and attracts growth-oriented investors. Analysts will watch "
            "whether this growth is sustainable or driven by one-time items."
        ),
        "keywords": ["EPS", "30%", "growth rate", "profitability", "earnings per share"],
    },
    {
        "id": "EI013",
        "category": "earnings_interpretation",
        "question": (
            "What is the difference between GAAP and non-GAAP earnings, and why do "
            "companies often report both?"
        ),
        "reference_answer": (
            "GAAP (Generally Accepted Accounting Principles) earnings follow standardized "
            "accounting rules and include all expenses, including stock-based compensation, "
            "restructuring charges, and amortization of acquired intangibles. Non-GAAP "
            "earnings exclude these items to show 'adjusted' or 'core' profitability. "
            "Companies report both because non-GAAP figures can better reflect ongoing "
            "operational performance, but critics argue they can be used to obscure poor "
            "performance by excluding recurring costs."
        ),
        "keywords": ["GAAP", "non-GAAP", "adjusted", "stock-based compensation", "restructuring"],
    },
    {
        "id": "EI014",
        "category": "earnings_interpretation",
        "question": (
            "A retailer reports same-store sales growth of -3% despite opening 15 new "
            "stores. What does this signal about the underlying business health?"
        ),
        "reference_answer": (
            "Same-store sales (comps) measure revenue growth at existing locations, "
            "excluding the impact of new store openings. A -3% comp decline despite "
            "aggressive expansion signals underlying weakness: existing stores are losing "
            "customers or selling less per visit. This is a red flag indicating the growth "
            "from new stores is masking deteriorating performance at mature locations. "
            "It may suggest market saturation, competitive pressure, or weakening consumer "
            "demand for the brand."
        ),
        "keywords": ["same-store sales", "comps", "decline", "expansion", "underlying"],
    },

    # ─── NEW TRADING STRATEGY (3 additional) ──────────────────────────────────
    {
        "id": "TS011",
        "category": "trading_strategy",
        "question": (
            "What is a stop-loss order and how should a trader determine "
            "an appropriate stop-loss level for a position?"
        ),
        "reference_answer": (
            "A stop-loss order automatically exits a position when price reaches a "
            "predetermined level, limiting the trader's loss. Appropriate stop-loss levels "
            "can be determined by: technical analysis (below key support for longs, above "
            "resistance for shorts), volatility-based stops (e.g., 2x ATR from entry), "
            "percentage-based stops (e.g., 2% of portfolio value), or chart pattern invalidation "
            "points. The stop should be placed where the original trade thesis is proven wrong, "
            "not so tight it triggers on normal price noise."
        ),
        "keywords": ["stop-loss", "support", "ATR", "risk", "position"],
    },
    {
        "id": "TS012",
        "category": "trading_strategy",
        "question": (
            "Explain the concept of position sizing in trading and why it is "
            "considered more important than entry timing by many professional traders."
        ),
        "reference_answer": (
            "Position sizing determines how much capital to allocate to each trade, "
            "controlling risk exposure. Professional traders consider it paramount because "
            "even a high win-rate strategy can blow up an account with poor position sizing, "
            "while a modest win-rate strategy can be profitable with disciplined sizing. "
            "Common methods include fixed fractional (risk 1-2% of account per trade), "
            "Kelly Criterion, and volatility-adjusted sizing. Proper sizing ensures no single "
            "loss is catastrophic and allows surviving a losing streak."
        ),
        "keywords": ["position sizing", "risk", "Kelly Criterion", "capital", "losing streak"],
    },
    {
        "id": "TS013",
        "category": "trading_strategy",
        "question": (
            "What is the difference between a limit order and a market order, "
            "and when should a trader prefer each?"
        ),
        "reference_answer": (
            "A market order executes immediately at the best available price but offers "
            "no price guarantee — execution may differ from the last quoted price, especially "
            "in fast or illiquid markets. A limit order only executes at the specified price "
            "or better, giving price control but risking non-execution if price never reaches "
            "the limit. Market orders suit urgent entries/exits in liquid markets. Limit orders "
            "are preferred for precise entries, illiquid securities, or when the trader can "
            "wait for a specific price level."
        ),
        "keywords": ["limit order", "market order", "execution", "price", "liquidity"],
    },

    # ─── NEW MACRO ECONOMICS (3 additional) ───────────────────────────────────
    {
        "id": "ME012",
        "category": "macro_economics",
        "question": (
            "How does a country's current account deficit relate to its capital "
            "account, and what are the financing implications?"
        ),
        "reference_answer": (
            "The current account and capital account are two sides of the balance of payments "
            "that must balance. A current account deficit (spending more abroad than earning) "
            "must be financed by a capital account surplus — meaning the country must attract "
            "foreign investment, borrow from abroad, or run down foreign reserves. Persistent "
            "current account deficits make a country dependent on foreign capital inflows and "
            "vulnerable to sudden stops if foreign investors lose confidence, potentially "
            "triggering currency crises."
        ),
        "keywords": ["current account", "capital account", "balance of payments", "deficit", "foreign investment"],
    },
    {
        "id": "ME013",
        "category": "macro_economics",
        "question": (
            "What is the Taylor Rule and how do central banks use it to guide "
            "interest rate decisions?"
        ),
        "reference_answer": (
            "The Taylor Rule is a monetary policy guideline that prescribes how central banks "
            "should set nominal interest rates based on: the neutral real interest rate, the "
            "deviation of inflation from target, and the deviation of GDP from potential "
            "(output gap). Specifically: rate = neutral rate + 1.5×(inflation - target) + "
            "0.5×(output gap). Central banks use it as a benchmark to assess whether policy "
            "is too tight or too loose, though they do not follow it mechanically."
        ),
        "keywords": ["Taylor Rule", "interest rate", "inflation target", "output gap", "monetary policy"],
    },
    {
        "id": "ME014",
        "category": "macro_economics",
        "question": (
            "Explain how tariffs affect domestic consumers, domestic producers, "
            "and the overall economy in a large importing country."
        ),
        "reference_answer": (
            "Tariffs (taxes on imports) raise the price of imported goods. Domestic "
            "consumers pay higher prices, reducing consumer surplus. Domestic producers "
            "benefit from reduced foreign competition, allowing them to charge higher prices "
            "and expand output — producer surplus increases. Government gains tariff revenue. "
            "However, overall economic welfare typically declines because the losses to "
            "consumers exceed the gains to producers and government. Tariffs can also invite "
            "retaliation, harming export sectors."
        ),
        "keywords": ["tariffs", "consumer surplus", "producer surplus", "imports", "retaliation"],
    },
]


def get_categories() -> list[str]:
    """Return list of unique categories in the dataset."""
    return list({q["category"] for q in QUESTIONS})


def get_questions_by_category(category: str) -> list[dict]:
    """Return all questions for a given category."""
    return [q for q in QUESTIONS if q["category"] == category]


CATEGORY_DISPLAY_NAMES = {
    "market_analysis": "Market Analysis",
    "risk_assessment": "Risk Assessment",
    "earnings_interpretation": "Earnings Interpretation",
    "trading_strategy": "Trading Strategy",
    "macro_economics": "Macro Economics",
}

CATEGORIES = list(CATEGORY_DISPLAY_NAMES.keys())
