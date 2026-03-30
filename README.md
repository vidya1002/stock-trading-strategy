# 📈 Stock Trading Strategy (NIFTY 50)

## 📌 Overview
This project builds and backtests a trading strategy using historical NIFTY 50 data.

## ⚙️ Strategy Logic
- Buy when:
  - MA20 crosses above MA50
  - RSI < 70
- Sell when:
  - MA20 crosses below MA50

## 📊 Indicators Used
- Moving Averages (MA20, MA50)
- Relative Strength Index (RSI)

## 📈 Results
- Total Return: XX%
- Win Rate: XX%
- Max Drawdown: XX%

## 📷 Output
<img width="1000" height="500" alt="Trade" src="https://github.com/user-attachments/assets/8089da8c-89d5-4052-a85a-fbc066a0da31" />


## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Matplotlib
- yfinance

## 🚀 How to Run
pip install -r requirements.txt  
python main.py
