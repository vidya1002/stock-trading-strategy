def apply_strategy(data):
    data['Signal'] = 0

    for i in range(1, len(data)):
        if (
            data['MA20'].iloc[i] > data['MA50'].iloc[i] and
            data['MA20'].iloc[i-1] <= data['MA50'].iloc[i-1] and
            data['RSI'].iloc[i] < 70
        ):
            data.loc[data.index[i], 'Signal'] = 1  # BUY

        elif (
            data['MA20'].iloc[i] < data['MA50'].iloc[i] and
            data['MA20'].iloc[i-1] >= data['MA50'].iloc[i-1]
        ):
            data.loc[data.index[i], 'Signal'] = -1  # SELL

    return data