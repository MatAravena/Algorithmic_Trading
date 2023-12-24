# Documentation Bybit
# https://bybit-exchange.github.io/docs/v5/intro


# API Imports
# import http
# from pybit import HTTP
from pybit import usdt_perpetual

# CONFIG
mode = "test"
# Could it be within another timeframe like days or more hours
timeframe = 60
# Limit data return
kline_limit = 200
# Moving average
z_score_window = 21

# LIVE API
api_key_mainnet = ""
api_secret_mainnet = ""

# TEST API
api_key_testnet = "lSl4CqPIT1PS6l9Cl9"
api_secret_testnet = "3IQbhwDO2iVHrAQ2wAfHhl69OKtTrDqOOB8y"

# SELECTED API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

# SELECTED URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"

# Account rsa private_key
rsa_private_key_path = '/Users/XXXXXXXXXX/private.pem'

# SESSION Activation
session = usdt_perpetual.HTTP(
    endpoint=api_url,
    api_key=api_key,
    api_secret=api_secret
)
