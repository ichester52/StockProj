from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
import os
# no keys required.

# keys required
#insert keys from os
stock_client = StockHistoricalDataClient(os.environ.get("API_KEY"), os.environ.get("SECRET"))

#create bar params from alapca api
stock_params = StockBarsRequest(
    symbol_or_symbols=["AAPL"],
    timeframe=TimeFrame.Day,
    start=datetime(2023, 10, 9),
    end=datetime(2023, 11, 15)
)

# learn how to use alpha vantage api

stock_data = stock_client.get_stock_bars(stock_params)

print(stock_data)