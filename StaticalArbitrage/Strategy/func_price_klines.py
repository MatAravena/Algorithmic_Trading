"""
    interval: 60, "D"
    from: integer from timestamp in seconds
    limit: max size of 200
"""
from config_strategy_api import timeframe
from config_strategy_api import kline_limit
from httpClient_HMAC import GET
import datetime
import time

from pybit import HTTP 

# Get start times
time_start_date = 0
if timeframe == 60:
    time_start_date = datetime.datetime.now() - datetime.timedelta(hours=kline_limit)
if timeframe == "D":
    time_start_date = datetime.datetime.now() - datetime.timedelta(days=kline_limit)

time_start_seconds = int(time_start_date.timestamp())

# Get historical prices (klines)
def get_price_klines(symbol):

    # https://bybit-exchange.github.io/docs/v5/market/mark-kline
    # Get prices
    payload = "category={}&symbol={}&interval={}&start={}&end={}&limit={}".format('linear',symbol,timeframe,time_start_seconds, datetime.datetime.now().timestamp(),kline_limit)
    prices =  GET('/v5/market/mark-price-kline',payload )
    # print('/v5/market/mark-price-kline'+'?'+payload)

     # Manage API calls
    time.sleep(0.1)

    # Return output
    if 'result' not in prices and  'list' not in prices["result"] and len(prices["result"]['list']) != kline_limit:
        return []

    return prices["result"]
