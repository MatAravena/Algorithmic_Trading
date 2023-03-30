import requests
import json

# Get list coins
def get_coin_tickers(url):
    # https://api.poloniex.com/markets/ticker24h
    # https://api.poloniex.com/public?command=returnTicker
    req = requests.get(url)
    return json.loads(req.text)
    # if (req.status_code == 200):
#      print(coin_json)

# Loop through each object and find the tradeable pairs
def collectTradeables(coin_json):
    coin_list = []
    for coin in coin_json: 
        isFrozen =  coin_json[coin]["isFrozen"]
        isPostOnly = coin_json[coin]["isFrozen"] 

        if isFrozen == "0" or isPostOnly == "0":
            coin_list.append(coin)
    return coin_list

# Structure Arbitrage Pairs
def structure_triangular_pairs(coin_list):
    expected_pair = 'USDT_BTC'
    
    # Declare Variables
    triangular_par_list = []
    remove_duplicate_list = []
    pairs_list = coin_list[0:]
    
    # Get pair A
    for pair_a in pairs_list:
        par_a_split = pair_a.split("_")
        a_base = par_a_split[0]
        a_quote = par_a_split[1]

        # Assign A to a Box
        a_pair_box = [a_base,a_quote]

        # Get pair B
        for pair_b in pairs_list:
            par_b_split = pair_b.split("_")
            b_base = par_b_split[0]
            b_quote = par_b_split[1]
            
            # Check pair B
            if pair_b != pair_a:
                if b_base in a_pair_box or b_quote in a_pair_box:
                    # Check pair C
                    for pair_c in pairs_list:
                        par_c_split = pair_c.split("_")
                        c_base = par_c_split[0]
                        c_quote = par_c_split[1]
                        
                        # Count the number of matching c items
                        if pair_c != pair_a and pair_c != pair_b:
                            compine_all = [pair_a,pair_b,pair_c]
                            pair_box = [a_base , a_quote ,b_base , b_quote, c_base , c_quote]
                            
                            counts_c_base = 0
                            for i in pair_box:
                                if i == c_base:
                                    counts_c_base +=1
                            
                            counts_c_quote = 0
                            for i in pair_box:
                                if i == c_quote:
                                    counts_c_quote +=1
                                    
                            if counts_c_base == 2 and counts_c_quote == 2 and c_base != c_quote:
                                combined = pair_a + "," + pair_b + "," + pair_c
                                unique_item =''.join(sorted(compine_all))
                                if unique_item not in remove_duplicate_list:
                                    match_dict = {
                                        "a_base" : a_base,
                                        "b_base" : b_base,
                                        "c_base" : c_base,
                                        "a_quote" : a_quote,
                                        "b_quote" : b_quote,
                                        "c_quote": c_quote,
                                        "pair_a" : pair_a,
                                        "pair_b" : pair_b,
                                        "pair_c" : pair_c,
                                        "combined" : combined,
                                    }
                                    
                                    triangular_par_list.append(match_dict)
                                    remove_duplicate_list.append(unique_item)
    return triangular_par_list

    # return pairs_list
