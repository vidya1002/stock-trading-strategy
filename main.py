from src.data_loader import load_data
from src.indicators import add_indicators
from src.strategy import apply_strategy
from src.backtest import backtest
from src.visualize import plot_results

def main():
    data = load_data()
    data = add_indicators(data)
    data = data.dropna()
    data = apply_strategy(data)
    data = backtest(data)
    plot_results(data)

if __name__ == "__main__":
    main()