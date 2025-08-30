#!/usr/bin/env python3
"""
Dollar Cost Averaging (DCA) Strategy for Bitcoin Trading
Buys a fixed dollar amount of Bitcoin every day regardless of price.
"""

from load import load_bitcoin_data
from typing import List, Dict


def backtest_dca_strategy(data: List[Dict], daily_investment: float = 10.0) -> Dict:
    """
    Backtest the Dollar Cost Averaging strategy.
    Invests a fixed dollar amount every day regardless of price.
    """
    total_invested = 0.0
    total_bitcoin = 0.0
    purchases = []
    portfolio_values = []

    for day_data in data:
        current_price = day_data["close"]

        # Buy fixed dollar amount
        bitcoin_purchased = daily_investment / current_price
        total_bitcoin += bitcoin_purchased
        total_invested += daily_investment

        purchases.append(
            {
                "date": day_data["date"],
                "price": current_price,
                "amount_invested": daily_investment,
                "bitcoin_purchased": bitcoin_purchased,
                "total_bitcoin": total_bitcoin,
                "total_invested": total_invested,
            }
        )

        # Calculate current portfolio value
        portfolio_value = total_bitcoin * current_price
        portfolio_values.append(portfolio_value)

    # Final calculations
    final_price = data[-1]["close"]
    final_value = total_bitcoin * final_price
    total_return = final_value - total_invested
    return_percentage = (
        (total_return / total_invested) * 100 if total_invested > 0 else 0
    )

    # Calculate average purchase price
    avg_purchase_price = total_invested / total_bitcoin if total_bitcoin > 0 else 0

    return {
        "total_invested": total_invested,
        "final_value": final_value,
        "total_return": total_return,
        "return_percentage": return_percentage,
        "total_bitcoin": total_bitcoin,
        "average_purchase_price": avg_purchase_price,
        "final_bitcoin_price": final_price,
        "daily_investment": daily_investment,
        "number_of_days": len(data),
        "purchases": purchases,
        "portfolio_values": portfolio_values,
    }


def analyze_dca_performance(results: Dict) -> None:
    """Analyze and display DCA strategy performance metrics."""
    print(f"Daily Investment: ${results['daily_investment']:.2f}")
    print(f"Investment Period: {results['number_of_days']} days")
    print(f"Total Invested: ${results['total_invested']:,.2f}")
    print(f"Total Bitcoin Accumulated: {results['total_bitcoin']:.8f} BTC")
    print(f"Average Purchase Price: ${results['average_purchase_price']:,.2f}")
    print(f"Final Bitcoin Price: ${results['final_bitcoin_price']:,.2f}")
    print(f"Final Portfolio Value: ${results['final_value']:,.2f}")
    print(f"Total Return: ${results['total_return']:,.2f}")
    print(f"Return Percentage: {results['return_percentage']:.2f}%")

    # Price appreciation vs DCA performance
    first_price = results["purchases"][0]["price"]
    final_price = results["final_bitcoin_price"]
    bitcoin_appreciation = ((final_price - first_price) / first_price) * 100

    print(f"\nBitcoin Price Appreciation: {bitcoin_appreciation:.2f}%")
    print(
        f"DCA Performance vs Buy & Hold: {results['return_percentage'] - bitcoin_appreciation:.2f}% difference"
    )


def compare_investment_amounts(data: List[Dict], amounts: List[float]) -> None:
    """Compare DCA strategy with different daily investment amounts."""
    print("\n--- DCA Strategy Comparison ---")
    print(
        f"{'Daily Amount':<12} {'Total Return':<15} {'Return %':<12} {'Final Value':<15}"
    )
    print("-" * 60)

    for amount in amounts:
        results = backtest_dca_strategy(data, amount)
        print(
            f"${amount:<11.2f} ${results['total_return']:<14,.2f} {results['return_percentage']:<11.2f}% ${results['final_value']:<14,.2f}"
        )


def main():
    """Run the Dollar Cost Averaging strategy backtest."""
    print("Dollar Cost Averaging (DCA) Trading Strategy Backtest")
    print("=" * 60)

    # Load data
    data = load_bitcoin_data(
        "Bitcoin_7_30_2020-8_29_2025_historical_data_coinmarketcap.csv"
    )
    print(f"Loaded {len(data)} days of Bitcoin price data")
    print(f"Date range: {data[0]['date'].date()} to {data[-1]['date'].date()}")

    # Run DCA backtest with $1/day (no initial amount)
    print("\n--- DCA Strategy Results ---")
    results = backtest_dca_strategy(data, daily_investment=1.0)
    analyze_dca_performance(results)

    # Compare different investment amounts
    investment_amounts = [1.0, 5.0, 10.0, 25.0, 50.0]
    compare_investment_amounts(data, investment_amounts)

    # Show some example purchases
    print("\n--- Sample Purchases (First 10 Days) ---")
    for i, purchase in enumerate(results["purchases"][:10]):
        print(
            f"Day {i + 1}: ${purchase['amount_invested']:.2f} → "
            f"{purchase['bitcoin_purchased']:.8f} BTC at ${purchase['price']:,.2f}"
        )

    print("\n--- Sample Purchases (Last 10 Days) ---")
    for i, purchase in enumerate(
        results["purchases"][-10:], len(results["purchases"]) - 9
    ):
        print(
            f"Day {i}: ${purchase['amount_invested']:.2f} → "
            f"{purchase['bitcoin_purchased']:.8f} BTC at ${purchase['price']:,.2f}"
        )


if __name__ == "__main__":
    main()
