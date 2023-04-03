import func_arbitrage
import json

# Set Variables
coin_price_url = 'https://api.poloniex.com/public?command=returnTicker'

"""
    Step 0 Gather correct coins 
    Finding couns which can be traded
    Exchange Poloniex 
    https://docs.poloniex.com/
"""
def step0():
    coin_json = func_arbitrage.get_coin_tickers(coin_price_url)
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
    with open("Arbitrage/structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)

""" Step 2
    Calculate Surface  Arbitrage Opportunities
    Exchange Poloniex 
    https://docs.poloniex.com/
"""
def step2():
    
    # Get Structurated Pairs
    with open("Arbitrage/structured_triangular_pairs.json") as json_file:
        structurated_paris = json.load(json_file)
    
    # Get latests Surfaces prices
    prices_json = func_arbitrage.get_coin_tickers(coin_price_url)
    
    # Loop trough and Structurate price information
    for t_pair in structurated_paris:
        prices_dict = func_arbitrage.get_price_for_t_pair(t_pair ,prices_json)
        surface_arb = func_arbitrage. calc_triangular_arb_surface_rate(t_pair ,prices_dict)

""" MAIN """
if __name__ == "__main__":
    # coin_list = step0()
    # structured_pairs = step1(coin_list)
    step2()
