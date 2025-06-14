import yfinance as yf
data = yf.download("NVDA", start="2020-01-01", end="2023-03-01", interval="1d")

print(type(data))

