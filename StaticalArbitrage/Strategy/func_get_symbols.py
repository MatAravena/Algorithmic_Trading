from config_strategy_api import session
import httpClient_HMAC as http


# Get symbols that are tradeable
def get_tradeable_symbols():

    # Get available symbols
    sym_list = []
    symbols = http.GET_DirectUrl('https://api.bybit.com/v2/public/symbols')

    if "ret_msg" in symbols.keys():
        if symbols["ret_msg"] == "OK":
            symbols = symbols["result"]
            for symbol in symbols:
                if symbol["quote_currency"] == "USDT" and symbol["status"] == "Trading" and float(symbol["maker_fee"]) <= 0.005 and float(symbol["taker_fee"]) <= 0.005 and '1000' not in symbol["name"]:
                    sym_list.append(symbol)
    return sym_list
