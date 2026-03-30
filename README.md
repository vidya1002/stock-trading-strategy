# 📈 Stock Trading Strategy (NIFTY 50)

## 📌 Overview

This project builds and backtests a rule-based trading strategy using historical data of the **NIFTY 50** index.
The strategy uses technical indicators to identify trends and generate buy/sell signals.

---

## ⚙️ Strategy Logic

* **Buy Signal:**

  * MA20 crosses above MA50 (uptrend)
  * RSI < 70 (not overbought)

* **Sell Signal:**

  * MA20 crosses below MA50 (downtrend)

---

## 📊 Indicators Used

* Moving Averages (MA20, MA50)
* Relative Strength Index (RSI)

---

## 📊 Results (Backtesting)

* **Total Return:** 3.21%
* **Max Drawdown:** -1.52%
* **Win Rate:** 33.33%

📅 Tested on historical NIFTY 50 data (2022–2025)

---

## 📷 Output

<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/df709bd3-8ce2-47a8-b21f-d2e192c0c47e" />
<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/035137bc-05af-4ad6-bb8d-fb3142541b24" />

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* yfinance

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📁 Project Structure

```
stock-trading-strategy/
│
├── data/                  # Stores downloaded market data
│   └── nifty_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── indicators.py
│   ├── strategy.py
│   ├── backtest.py
│   └── visualize.py
│
├── outputs/               # Stores results and graphs (generated)
│   ├── results.csv
│   └── performance.png
│
├── main.py
├── requirements.txt
└── README.md
```

> Note: The `data/` and `outputs/` folders are generated during runtime and may not be included in the repository.

---

## ⚠️ Limitations

* Does not include transaction costs or brokerage
* Does not consider slippage or execution delays
* Based on historical data (no guarantee of future performance)

---

## 🔮 Future Improvements

* Add transaction cost and slippage
* Implement multiple trading strategies
* Build a Streamlit dashboard
* Add live market data integration

---

## 💡 Key Learnings

* Implemented financial indicators using Python
* Built a backtesting pipeline for trading strategies
* Evaluated performance using metrics like return, drawdown, and win rate
* Worked with real-world financial data

---

## 👩‍💻 Author

**Vidyashree K J**

🔗 GitHub: https://github.com/vidya1002/stock-trading-strategy
