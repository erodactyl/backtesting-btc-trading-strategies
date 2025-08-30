#!/usr/bin/env python3
"""
Moving Average Strategy for Bitcoin Trading
Buys when the current price is above the moving average and sells when below.
"""

from load import load_bitcoin_data
from typing import List, Dict


def calculate_moving_average(data: List[Dict], window: int = 20) -> List[float]:
    """Calculate moving average for the given data."""
    moving_averages = []
    for i in range(len(data)):
        if i < window - 1:
            # Not enough data points for moving average
            moving_averages.append(None)
        else:
            avg = sum(data[j]["close"] for j in range(i - window + 1, i + 1)) / window
            moving_averages.append(avg)
    return moving_averages


def backtest_moving_average_strategy(
    data: List[Dict], ma_window: int = 20, daily_budget: float = 1.0
) -> Dict:
    """
    Backtest the moving average strategy.
    Accumulates $1 per day, buys when price is below MA, never sells.
    """
    moving_averages = calculate_moving_average(data, ma_window)

    accumulated_cash = 0.0
    bitcoin_held = 0.0
    trades = []
    portfolio_values = []
    total_invested = 0.0

    for i, day_data in enumerate(data):
        current_price = day_data["close"]
        ma = moving_averages[i]

        # Accumulate $1 per day
        accumulated_cash += daily_budget

        if ma is None:
            # Not enough data for moving average yet
            portfolio_value = accumulated_cash + (bitcoin_held * current_price)
            portfolio_values.append(portfolio_value)
            continue

        # Trading logic - only buy when price is below moving average, never sell
        if current_price < ma and accumulated_cash > 0:
            # Buy signal: price below moving average, invest all accumulated cash
            bitcoin_bought = accumulated_cash / current_price
            bitcoin_held += bitcoin_bought
            total_invested += accumulated_cash
            trades.append(
                {
                    "date": day_data["date"],
                    "action": "BUY",
                    "price": current_price,
                    "amount": bitcoin_bought,
                    "cash_used": accumulated_cash,
                }
            )
            accumulated_cash = 0.0

        # Calculate portfolio value
        portfolio_value = accumulated_cash + (bitcoin_held * current_price)
        portfolio_values.append(portfolio_value)

    # Final portfolio value
    final_value = accumulated_cash + (bitcoin_held * data[-1]["close"])

    return {
        "total_invested": total_invested,
        "final_value": final_value,
        "total_return": final_value - total_invested,
        "return_percentage": ((final_value - total_invested) / total_invested) * 100
        if total_invested > 0
        else 0,
        "trades": trades,
        "portfolio_values": portfolio_values,
        "moving_average_window": ma_window,
        "bitcoin_held": bitcoin_held,
        "accumulated_cash": accumulated_cash,
        "daily_budget": daily_budget,
        "number_of_days": len(data),
    }


def main():
    """Run the moving average strategy backtest."""
    print("Moving Average Trading Strategy Backtest")
    print("=" * 50)

    # Load data
    data = load_bitcoin_data(
        "Bitcoin_7_30_2020-8_29_2025_historical_data_coinmarketcap.csv"
    )
    print(f"Loaded {len(data)} days of Bitcoin price data")
    print(f"Date range: {data[0]['date'].date()} to {data[-1]['date'].date()}")

    # Run backtest with different moving average windows
    windows = [10, 20, 50]

    for window in windows:
        print(f"\n--- Moving Average Strategy (MA-{window}) ---")
        results = backtest_moving_average_strategy(data, window)

        print(f"Daily Budget: ${results['daily_budget']:.2f}")
        print(f"Total Invested: ${results['total_invested']:,.2f}")
        print(f"Bitcoin Held: {results['bitcoin_held']:.8f} BTC")
        print(f"Cash Still Accumulating: ${results['accumulated_cash']:,.2f}")
        print(f"Final Value: ${results['final_value']:,.2f}")
        print(f"Total Return: ${results['total_return']:,.2f}")
        print(f"Return Percentage: {results['return_percentage']:.2f}%")
        print(f"Number of Purchases: {len(results['trades'])}")

        if results["trades"]:
            print(
                f"First Purchase: {results['trades'][0]['date'].date()} at ${results['trades'][0]['price']:,.2f}"
            )
            print(
                f"Last Purchase: {results['trades'][-1]['date'].date()} at ${results['trades'][-1]['price']:,.2f}"
            )

    # Compare to buy-and-hold
    initial_price = data[0]["close"]
    final_price = data[-1]["close"]
    buy_hold_return = ((final_price - initial_price) / initial_price) * 100

    print("\n--- Buy and Hold Comparison ---")
    print(f"Buy and Hold Return: {buy_hold_return:.2f}%")


if __name__ == "__main__":
    main()
