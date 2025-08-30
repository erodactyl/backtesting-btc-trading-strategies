# Bitcoin Trading Strategy Backtesting

A comprehensive analysis and backtesting framework for evaluating Bitcoin investment strategies using historical price data. This project compares three distinct approaches to Bitcoin accumulation over a 5-year period (July 2020 - August 2025) to determine optimal investment methodologies.

## Project Overview

This research project analyzes the effectiveness of different Bitcoin investment strategies by simulating a consistent $1 daily investment budget across multiple approaches. The study aims to identify which strategy provides the best risk-adjusted returns while maintaining capital efficiency.

### Dataset

- **Data Source**: CoinMarketCap historical Bitcoin price data
- **Time Period**: July 30, 2020 - August 29, 2025 (1,856 days)
- **Investment Budget**: $1 per day ($1,856 total over the period)
- **Data Points**: OHLC prices, volume, and market capitalization

## Investment Strategies Analyzed

### 1. Dollar Cost Averaging (DCA)
**Strategy**: Invest $1 every day regardless of market conditions.

- **Implementation**: Purchases Bitcoin with the full daily budget on every trading day
- **Philosophy**: Eliminates market timing risk through consistent, disciplined investing
- **Capital Efficiency**: 100% - all available capital is immediately deployed

### 2. Moving Average Strategy
**Strategy**: Accumulate $1 daily and invest only when Bitcoin price falls below the moving average.

- **Implementation**: 
  - Accumulates $1 per day in cash reserves
  - Purchases Bitcoin with all accumulated cash when price < moving average
  - Never sells - pure buy-and-hold after purchase
- **Philosophy**: Buy during temporary price weakness below the trend
- **Variants Tested**: 10-day, 20-day, and 50-day moving averages

### 3. All-Time High (ATH) Dip Strategy
**Strategy**: Accumulate $1 daily and invest when Bitcoin drops a specified percentage below its all-time high.

- **Implementation**:
  - Accumulates $1 per day in cash reserves
  - Tracks rolling all-time high prices
  - Invests all accumulated cash when price drops X% below ATH
  - Pure buy-and-hold strategy
- **Philosophy**: Capitalize on significant market corrections
- **Variants Tested**: 10%, 15%, 20%, 25%, 30%, 40%, and 50% dip thresholds

## Key Findings

### Performance Results (5-Year Period)

| Strategy | Total Return | Return % | Bitcoin Accumulated | Purchases Made |
|----------|--------------|----------|-------------------|----------------|
| **Dollar Cost Averaging** | **$4,167.90** | **224.56%** | **0.05557 BTC** | **1,856** |
| **Moving Average (MA-20)** | $4,066.55 | 219.10% | 0.05463 BTC | 851 |
| **ATH Dip (20% threshold)** | $3,536.64 | 205.02% | 0.04853 BTC | 1,062 |

### Strategic Insights

1. **DCA Dominance**: Despite its simplicity, Dollar Cost Averaging achieved the highest returns (224.56%), demonstrating the power of consistent market participation.

2. **Capital Utilization**: DCA's superior performance stems largely from its 100% capital deployment rate. While other strategies accumulated cash waiting for optimal entry points, DCA remained fully invested throughout the bull market.

3. **Market Timing Limitations**: Both timing-based strategies (Moving Average and ATH Dip) underperformed DCA during this strong uptrend period, as cash accumulation periods reduced their exposure to Bitcoin's appreciation.

4. **Strategy Sensitivity**: 
   - Moving Average strategy showed minimal performance variation across different MA periods (218-220% returns)
   - ATH Dip strategy performance varied significantly with threshold levels (193-292% returns)

### Market Context Considerations

The analyzed period (2020-2025) represents a predominantly bullish market for Bitcoin, with price appreciation of 857.40%. In different market conditions:

- **Bear Markets**: Timing-based strategies might outperform by avoiding sustained drawdowns
- **Sideways Markets**: DCA's consistent buying could be less advantageous than selective accumulation
- **Volatile Markets**: ATH Dip strategy might capture more opportunities during frequent corrections

## Development Approach

This project was **vibe coded** using modern AI development tools, specifically leveraging [Claude Code](https://claude.ai/code) for rapid prototyping and implementation. The entire codebase, analysis framework, and documentation were developed through AI-assisted programming, demonstrating the potential for AI tools to accelerate financial research and backtesting projects.

The development process showcased:
- Rapid iteration on strategy implementations
- AI-guided debugging and optimization
- Automated generation of comprehensive analysis and documentation
- Seamless integration of multiple backtesting approaches

## Technical Implementation

### Project Structure
```
├── main.py                     # Entry point
├── load.py                     # Data loading utilities
├── dollar_cost_averaging.py    # DCA strategy implementation
├── moving_average_strategy.py  # Moving average strategy
├── ath_dip_strategy.py        # ATH dip strategy
└── Bitcoin_7_30_2020-8_29_2025_historical_data_coinmarketcap.csv
```

### Running the Analysis

```bash
# Run individual strategies
python dollar_cost_averaging.py
python moving_average_strategy.py
python ath_dip_strategy.py

# Or run all strategies
python main.py
```

## Conclusions

1. **Simplicity Wins**: The straightforward DCA approach outperformed more sophisticated timing-based strategies during this bull market period.

2. **Consistency Matters**: Regular, disciplined investing proved more effective than attempting to time market entries, even with reasonable technical indicators.

3. **Capital Efficiency**: Full capital deployment trumped selective investing in a strongly appreciating asset.

4. **Strategy Suitability**: While DCA excelled in this bull market, investors should consider their risk tolerance, market outlook, and ability to maintain discipline when selecting strategies.

## Future Research Directions

- Analysis across different market cycles (bear markets, sideways trends)
- Integration of additional technical indicators
- Risk-adjusted return metrics (Sharpe ratio, maximum drawdown)
- Transaction cost impact analysis
- Portfolio rebalancing strategies

---

*This analysis is for educational and research purposes only and does not constitute financial advice.*