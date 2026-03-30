import yfinance as yf
import pandas as pd

def load_data():
    data = yf.download("^NSEI", start="2022-01-01", end="2025-01-01")
    data.to_csv("data/nifty_data.csv")
    return data