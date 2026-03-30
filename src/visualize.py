import matplotlib.pyplot as plt

def plot_results(data):
    # Price + Moving Average
    plt.figure(figsize=(10,5))
    plt.plot(data['Close'], label='Price')
    plt.plot(data['MA20'], label='MA20')
    plt.plot(data['MA50'], label='MA50')
    plt.legend()
    plt.title("Price with Moving Averages")
    plt.savefig("outputs/performance.png")
    plt.show()

    # Strategy performance
    plt.figure(figsize=(10,5))
    data['Strategy_Returns'].cumsum().plot()
    plt.title("Strategy Performance")
    plt.show()