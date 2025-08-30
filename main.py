from moving_average_strategy import main as moving_average
from dollar_cost_averaging import main as dca
from ath_dip_strategy import main as ath_dip


def main():
    moving_average()
    dca()
    ath_dip()


if __name__ == "__main__":
    main()
