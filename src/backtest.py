def backtest(data):
    data['Returns'] = data['Close'].pct_change()
    data['Strategy_Returns'] = data['Returns'] * data['Signal'].shift(1)

    data = data.dropna()

    total_return = data['Strategy_Returns'].sum()
    max_drawdown = data['Strategy_Returns'].min()

    # Identify trades (change in signal)
    data['Trade'] = data['Signal'].diff()

    # Only consider entry points
    trades = data[data['Trade'] != 0]

    if len(trades) > 0:
        win_rate = (trades['Strategy_Returns'] > 0).mean()
    else:
        win_rate = 0

    # Convert to %
    print(f"Total Return: {total_return*100:.2f}%")
    print(f"Max Drawdown: {max_drawdown*100:.2f}%")
    print(f"Win Rate: {win_rate*100:.2f}%")

    data.to_csv("outputs/results.csv")

    return data