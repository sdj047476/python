# library - 5

import yfinance

apple = yfinance.Ticker("AAPL")
current_price = apple.info['currentPrice']
print(f"애플 주식의 현재 가격: {current_price}")

MicroSoft = yfinance.Ticker("MSFT")
current_price = MicroSoft.info['currentPrice']
print(f"마소 주식의 현재 가격: {current_price}")
