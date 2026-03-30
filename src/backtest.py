def backtest(data):
    data['Returns'] = data['Close'].pct_change()
    data['Strategy_Returns'] = data['Returns'] * data['Signal'].shift(1)

    total_return = data['Strategy_Returns'].sum()

    # Save results
    data.to_csv("outputs/results.csv")

    print("Total Return:", total_return)
    print("Max Drawdown:", data['Strategy_Returns'].min())
    print("Win Rate:", (data['Strategy_Returns'] > 0).mean())

    return data