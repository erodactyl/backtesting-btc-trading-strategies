#!/usr/bin/env python3
"""
All-Time High (ATH) Dip Buying Strategy for Bitcoin Trading
Buys when the current price is X% below the all-time high seen so far.
"""

from typing import List, Dict
from load import load_bitcoin_data


def backtest_ath_dip_strategy(
    data: List[Dict],
    dip_percentage: float = 20.0,
    daily_budget: float = 1.0,
) -> Dict:
    """
    Backtest the ATH Dip Buying strategy.
    Accumulates $1 per day, buys when price is dip_percentage% below ATH.

    Args:
        data: Historical price data
        dip_percentage: Percentage below ATH to trigger buy (e.g., 20 for 20%)
        daily_budget: Dollar amount accumulated per day
    """
    all_time_high = 0.0
    accumulated_cash = 0.0
    total_invested = 0.0
    total_bitcoin = 0.0
    purchases = []
    portfolio_values = []
    purchase_count = 0

    for day_data in data:
        current_price = day_data["close"]
        current_high = day_data["high"]

        # Accumulate daily budget
        accumulated_cash += daily_budget

        # Update all-time high
        all_time_high = max(all_time_high, current_high)

        # Calculate dip threshold
        dip_threshold = all_time_high * (1 - dip_percentage / 100)

        # Check if current price is at or below dip threshold
        buy_signal = current_price <= dip_threshold and accumulated_cash > 0

        if buy_signal and all_time_high > 0:
            # Buy signal: price is X% below ATH, invest all accumulated cash
            bitcoin_purchased = accumulated_cash / current_price
            total_bitcoin += bitcoin_purchased
            total_invested += accumulated_cash
            purchase_count += 1

            dip_from_ath = ((all_time_high - current_price) / all_time_high) * 100

            purchases.append(
                {
                    "date": day_data["date"],
                    "price": current_price,
                    "amount_invested": accumulated_cash,
                    "bitcoin_purchased": bitcoin_purchased,
                    "all_time_high": all_time_high,
                    "dip_percentage": dip_from_ath,
                    "total_bitcoin": total_bitcoin,
                    "total_invested": total_invested,
                    "purchase_number": purchase_count,
                }
            )

            # Reset accumulated cash after purchase
            accumulated_cash = 0.0

        # Calculate current portfolio value
        portfolio_value = accumulated_cash + (total_bitcoin * current_price)
        portfolio_values.append(
            {
                "date": day_data["date"],
                "price": current_price,
                "ath": all_time_high,
                "portfolio_value": portfolio_value,
                "total_invested": total_invested,
                "accumulated_cash": accumulated_cash,
                "unrealized_return": portfolio_value - total_invested - accumulated_cash
                if total_invested > 0
                else 0,
            }
        )

    # Final calculations
    final_price = data[-1]["close"]
    final_value = accumulated_cash + (total_bitcoin * final_price)
    total_return = final_value - total_invested - accumulated_cash
    return_percentage = (
        (total_return / total_invested) * 100 if total_invested > 0 else 0
    )

    # Calculate average purchase price
    avg_purchase_price = total_invested / total_bitcoin if total_bitcoin > 0 else 0

    return {
        "dip_percentage": dip_percentage,
        "daily_budget": daily_budget,
        "total_invested": total_invested,
        "final_value": final_value,
        "total_return": total_return,
        "return_percentage": return_percentage,
        "total_bitcoin": total_bitcoin,
        "average_purchase_price": avg_purchase_price,
        "final_bitcoin_price": final_price,
        "final_ath": all_time_high,
        "accumulated_cash": accumulated_cash,
        "number_of_purchases": len(purchases),
        "number_of_days": len(data),
        "purchases": purchases,
        "portfolio_values": portfolio_values,
    }


def analyze_ath_dip_performance(results: Dict) -> None:
    """Analyze and display ATH Dip strategy performance metrics."""
    print(f"Dip Threshold: {results['dip_percentage']:.1f}% below ATH")
    print(f"Daily Budget: ${results['daily_budget']:.2f}")
    print(f"Number of Purchases: {results['number_of_purchases']}")
    print(f"Total Invested: ${results['total_invested']:,.2f}")
    print(f"Cash Still Accumulating: ${results['accumulated_cash']:,.2f}")
    print(f"Total Bitcoin Accumulated: {results['total_bitcoin']:.8f} BTC")
    print(f"Average Purchase Price: ${results['average_purchase_price']:,.2f}")
    print(f"Final Bitcoin Price: ${results['final_bitcoin_price']:,.2f}")
    print(f"Final All-Time High: ${results['final_ath']:,.2f}")
    print(f"Final Portfolio Value: ${results['final_value']:,.2f}")
    print(f"Total Return: ${results['total_return']:,.2f}")
    print(f"Return Percentage: {results['return_percentage']:.2f}%")

    if results["purchases"]:
        print(
            f"First Purchase: {results['purchases'][0]['date'].date()} at ${results['purchases'][0]['price']:,.2f}"
        )
        print(
            f"Last Purchase: {results['purchases'][-1]['date'].date()} at ${results['purchases'][-1]['price']:,.2f}"
        )


def compare_dip_thresholds(data: List[Dict], thresholds: List[float]) -> None:
    """Compare ATH Dip strategy with different dip thresholds."""
    print("\n--- ATH Dip Strategy Comparison ---")
    print(
        f"{'Dip %':<8} {'Purchases':<10} {'Total Return':<15} {'Return %':<12} {'Final Value':<15}"
    )
    print("-" * 70)

    for threshold in thresholds:
        results = backtest_ath_dip_strategy(data, threshold, daily_budget=1.0)
        print(
            f"{threshold:<7.1f}% {results['number_of_purchases']:<9} "
            f"${results['total_return']:<14,.2f} {results['return_percentage']:<11.2f}% "
            f"${results['final_value']:<14,.2f}"
        )


def main():
    """Run the ATH Dip Buying strategy backtest."""
    print("All-Time High (ATH) Dip Buying Strategy Backtest")
    print("=" * 60)

    # Load data
    data = load_bitcoin_data(
        "Bitcoin_7_30_2020-8_29_2025_historical_data_coinmarketcap.csv"
    )
    print(f"Loaded {len(data)} days of Bitcoin price data")
    print(f"Date range: {data[0]['date'].date()} to {data[-1]['date'].date()}")

    # Run ATH Dip backtest with 20% dip threshold and $1/day budget
    print("\n--- ATH Dip Strategy Results (20% dip) ---")
    results = backtest_ath_dip_strategy(data, dip_percentage=20.0, daily_budget=1.0)
    analyze_ath_dip_performance(results)

    # Compare different dip thresholds
    dip_thresholds = [10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0]
    compare_dip_thresholds(data, dip_thresholds)

    # Show purchase history for 20% dip strategy
    if results["purchases"]:
        print("\n--- Purchase History (20% Dip Strategy) ---")
        for purchase in results["purchases"]:
            print(
                f"{purchase['date'].date()}: Bought {purchase['bitcoin_purchased']:.8f} BTC "
                f"at ${purchase['price']:,.2f} ({purchase['dip_percentage']:.1f}% below ATH of "
                f"${purchase['all_time_high']:,.2f})"
            )

    # Analysis of missed opportunities vs timing
    print("\n--- Strategy Analysis ---")
    if results["purchases"]:
        best_purchase = min(results["purchases"], key=lambda x: x["price"])
        worst_purchase = max(results["purchases"], key=lambda x: x["price"])

        print(
            f"Best Purchase: {best_purchase['bitcoin_purchased']:.8f} BTC at ${best_purchase['price']:,.2f} "
            f"on {best_purchase['date'].date()}"
        )
        print(
            f"Worst Purchase: {worst_purchase['bitcoin_purchased']:.8f} BTC at ${worst_purchase['price']:,.2f} "
            f"on {worst_purchase['date'].date()}"
        )

    # Compare to buy-and-hold
    if data:
        initial_price = data[0]["close"]
        final_price = data[-1]["close"]
        buy_hold_return = ((final_price - initial_price) / initial_price) * 100

        print(f"\nBuy and Hold Return: {buy_hold_return:.2f}%")
        if results["total_invested"] > 0:
            equivalent_buy_hold = (
                results["total_invested"] / initial_price * final_price
            )
            print(f"Buy & Hold with same total investment: ${equivalent_buy_hold:,.2f}")
            print(
                f"ATH Dip Strategy vs Buy & Hold: {results['final_value'] - equivalent_buy_hold:+,.2f}"
            )


if __name__ == "__main__":
    main()
