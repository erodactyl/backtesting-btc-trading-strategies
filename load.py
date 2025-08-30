import csv
from datetime import datetime
from typing import List, Dict


def load_bitcoin_data(filename: str) -> List[Dict]:
    """Load Bitcoin price data from CSV file."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            data.append(
                {
                    "date": datetime.fromisoformat(
                        row["timeOpen"].strip('"').replace("Z", "+00:00")
                    ),
                    "open": float(row["open"]),
                    "high": float(row["high"]),
                    "low": float(row["low"]),
                    "close": float(row["close"]),
                    "volume": float(row["volume"]),
                }
            )
    # Sort by date (oldest first for backtesting)
    data.sort(key=lambda x: x["date"])
    return data
