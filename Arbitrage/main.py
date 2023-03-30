import func_arbitrage
import json
"""
    Step 0 Gather correct coins 
    Finding couns which can be traded
    Exchange Ploloniex 
    https://docs.poloniex.com/
"""
def step0():
    coin_json = func_arbitrage.get_coin_tickers('https://api.poloniex.com/public?command=returnTicker')
    coin_list = func_arbitrage.collectTradeables(coin_json)
    
    # Return tradeable coins
    return coin_list

"""
    Step 1 Structuring Triangular Pairs
    Calculation only
"""
def step1(coin_list):
    expected_pair = 'USDT_BTC'
    
    # Structure the list of triangule arbitrage
    structured_list = func_arbitrage.structure_triangular_pairs(coin_list)
    
    # Save structured list   
    with open("structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)


""" MAIN """
if __name__ == "__main__":
    coin_list = step0()
    structured_pairs = step1(coin_list)
