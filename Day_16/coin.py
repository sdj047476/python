# coin - 1

import ccxt



exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USD')
current_price = ticker['last']
last_price = current_price

while True:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USD')
    current_price = ticker['last']
    if current_price - last_price > last_price * 0.00001:
        print(f"BTC/USD의 현재 가격: {current_price}")
        print("드가자")
    elif current_price - last_price < -last_price * 0.00001:
        print(f"BTC/USD의 현재 가격: {current_price}")
        print("도망가")
    else:
        print(f"BTC/USD의 현재 가격: {current_price}")
        print("버텨")
    last_price = current_price