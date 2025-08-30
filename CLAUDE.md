# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Bitcoin trading strategy analysis project that uses historical data to backtest various trading strategies. The project analyzes three main trading approaches:

1. **Moving Average Strategy**: Buy when price is above the moving average
2. **Dollar Cost Averaging**: Buy every day regardless of price
3. **ATH Dip Strategy**: Buy when price is X% below all-time high

## Data Source

The project uses historical Bitcoin price data from CoinMarketCap stored in `Bitcoin_7_30_2020-9_29_2020_historical_data_coinmarketcap.csv`. The CSV contains:
- Timestamp data (timeOpen, timeClose, timeHigh, timeLow)
- OHLC price data (open, high, low, close)
- Volume and market cap data
- Data is semicolon-delimited

## Development Environment

- **Python Version**: Requires Python >= 3.13 (specified in pyproject.toml)
- **Virtual Environment**: Uses `.venv/` directory (already set up)
- **Dependencies**: Currently no external dependencies defined in pyproject.toml

## Commands

### Running the Project
```bash
python main.py
```

### Virtual Environment
The project uses a virtual environment in `.venv/`. To activate:
```bash
source .venv/bin/activate  # On macOS/Linux
```

### Package Management
This project uses pyproject.toml for configuration. To install in development mode:
```bash
pip install -e .
```

## Project Structure

- `main.py`: Entry point (currently just prints "Hello from btc!")
- `Bitcoin_7_30_2020-8_29_2025_historical_data_coinmarketcap.csv`: Historical Bitcoin price data
- `pyproject.toml`: Project configuration and dependencies
- `.python-version`: Specifies Python version requirement
