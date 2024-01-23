"""
    API Documentation
    https://bybit-exchange.github.io/docs/linear/#t-introduction
"""

# API Imports
from pybit import HTTP

# from pybit.inverse_perpetual import HTTP
# from pybit.spot import HTTP

# from pybit import usdt_perpetual
# from pybit import unified_trading
import websocket

from personal_configuration import mode, api_key_testnet, api_secret_testnet, api_key_mainnet, api_secret_mainnet

# CONFIG VARIABLES
ticker_1 = "ETHUSDT"
ticker_2 = "SOLUSDT"
signal_positive_ticker = ticker_2
signal_negative_ticker = ticker_1
rounding_ticker_1 = 4
rounding_ticker_2 = 3
quantity_rounding_ticker_1 = 0
quantity_rounding_ticker_2 = 1

limit_order_basis = True # will ensure positions (except for Close) will be placed on limit basis

tradeable_capital_usdt = 500 # total tradeable capital to be split between both pairs
stop_loss_fail_safe = 0.15 # stop loss at market order in case of drastic event
signal_trigger_thresh = 1.1 # z-score threshold which determines trade (must be above zero)

timeframe = 60 # make sure matches your strategy
kline_limit = 200 # make sure matches your strategy
z_score_window = 21 # make sure matches your strategy

# SELECTED API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

# SELECTED URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"

# SESSION Activation
session_public = HTTP(
    endpoint=api_url,
    api_key=api_key,
    api_secret=api_secret
)
# private = HTTP(
#     testnet=True if mode == "test" else False, 
#     api_key=api_key,
#     api_secret=api_secret )

# session_private = websocket(
#     testnet=True if mode == "test" else False, 
#     api_key=api_key,
#     api_secret=api_secret,
# )

# ws = websocket.WebSocketApp(
#     url=api_url,
#     api_key=api_key,
#     api_secret=api_secret,
# )