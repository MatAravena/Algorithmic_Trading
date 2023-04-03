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
    triangular_pair_list = []
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
                            combine_all = [pair_a,pair_b,pair_c]
                            pair_box = [a_base , a_quote ,b_base , b_quote, c_base , c_quote]

                            counts_c_base = 0
                            for i in pair_box:
                                if i == c_base:
                                    counts_c_base +=1

                            counts_c_quote = 0
                            for i in pair_box:
                                if i == c_quote:
                                    counts_c_quote +=1

                            # Determining Triangular Match
                            if counts_c_base == 2 and counts_c_quote == 2 and c_base != c_quote:
                                combined = pair_a + "," + pair_b + "," + pair_c
                                unique_item = ''.join(sorted(combine_all))
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

                                    remove_duplicate_list.append(unique_item)
                                    triangular_pair_list.append(match_dict)
    return triangular_pair_list

def get_price_for_t_pair(t_pair, prices_json):
    # Extrac pair into
    par_a = t_pair["pair_a"]
    par_b = t_pair["pair_b"]
    par_c = t_pair["pair_c"]
    
    # Extract Price information for given pairs
    par_a_ask = float(prices_json[par_a]["lowestAsk"])
    par_a_bid = float(prices_json[par_a]["highestBid"])

    par_b_ask = float(prices_json[par_b]["lowestAsk"])
    par_b_bid = float(prices_json[par_b]["highestBid"])

    par_c_ask = float(prices_json[par_c]["lowestAsk"])
    par_c_bid = float(prices_json[par_c]["highestBid"])
    
    # Output Dictionary
    return {
        "pair_a_ask": par_a_ask,
        "pair_a_bid": par_a_bid,
        "pair_b_ask": par_b_ask,
        "pair_b_bid": par_b_bid,
        "pair_c_ask": par_c_ask,
        "pair_c_bid": par_c_bid       
    }

# Calculation Surface Rate Arbitrafe Opportunity
def calc_triangular_arb_surface_rate(t_pair ,prices_dict):
    
    # Set Variables
    starting_amount = 1000
    min_surface_rate = 0
    surface_dict = {}
    contract_2 = ""
    contract_3 = ""
    direction_trade_1 =''
    direction_trade_2 =''
    direction_trade_3 =''
    acquired_coin_t2 = 0
    acquired_coin_t3 = 0
    calculated = 0
    
    # Extract Pair Variables    
    a_base = t_pair["a_base"]
    a_quote = t_pair["a_quote"]
    b_base = t_pair["b_base"]
    b_quote = t_pair["b_quote"]
    c_base = t_pair["c_base"]
    c_quote = t_pair["c_quote"]
    
    pair_a = t_pair["pair_a"]
    pair_b = t_pair["pair_b"]
    pair_c = t_pair["pair_c"]

    # Extract prices json
    a_ask = float(prices_dict["pair_a_ask"])
    a_bid = float(prices_dict["pair_a_bid"])
    b_ask = float(prices_dict["pair_b_ask"])
    b_bid = float(prices_dict["pair_b_bid"])
    c_ask = float(prices_dict["pair_c_ask"])
    c_bid = float(prices_dict["pair_c_bid"])

    # Set directions and loop through
    direction_list = ["forward", "reverse"]
    for direction in direction_list:
        if a_ask == 0 or a_bid == 0 or b_ask == 0 or b_bid == 0 or c_ask == 0 or c_bid == 0:
            continue
        
        # Set aditional variables for swap information
        swap_1 = ""
        swap_2 = ""
        swap_3 = ""
        swap_1_rate = 0
        swap_2_rate = 0
        swap_3_rate = 0
        
        """ 
            Exchange Poloniex rules
            If we are swapping the coin on the left (Base) to the right (Quote) then 1/
            If we are swapping the coin on the right (Quote) to the left (Base) then * Bid
        """
    
        # Assume starting with a_base and swaaping for a_quote
        if direction == "forward":
            swap_1 = a_base
            swap_2 = a_quote
            swap_1_rate = 1 / a_ask
            direction_trade_1 = "baseToQuote"

        
        # Assume starting with a_base and swaaping for a_quote
        if direction == "reverse":
            swap_1 = a_quote
            swap_2 = a_base
            swap_1_rate = a_bid
            direction_trade_1 = "quoteToBase"
            
        # Place fist trade
        contract_1 = pair_a
        acquired_coin_t1 = starting_amount * swap_1_rate
        # print(direction, pair_a, starting_amount, adquired_coin_1)

        """ Forward """
        if direction == "forward":
            # Check if a_quote (adquired_coin) matches b_quote
            if a_quote == b_quote and calculated == 0:
                swap_2_rate = b_bid
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "quoteToBase"
                contract_2 = pair_b

                # if b_base (adquired coin) matches c_base
                if b_base == c_base:
                    swap_3 = c_base
                    swap_3_rate = 1 / c_ask
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_c

                # if b_base (adquired coin) matches c_base
                if b_base == c_quote:
                    swap_3 = c_quote
                    swap_3_rate = c_bid
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_c

                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1

            # Check if a_quote (adquired_coin) matches b_base
            if a_quote == b_base and calculated == 0:
                swap_2_rate =  1 / b_ask
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "baseToQuote"
                contract_2 = pair_b

                # if b_quote (adquired coin) matches c_base
                if b_quote == c_base:
                    swap_3 = c_base
                    swap_3_rate = 1 / b_ask
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_c

                # if b_base (adquired coin) matches c_quote
                if b_quote == c_quote:
                    swap_3 = c_quote
                    swap_3_rate = c_bid
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_c

                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1

            # Check if a_quote (adquired_coin) matches c_base
            if a_quote == c_quote and calculated == 0:
                swap_2_rate = c_bid
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "quoteToBase"
                contract_2 = pair_c
                
                # if c_base (adquired coin) matches b_base
                if c_base == b_base:
                    swap_3 = b_base
                    swap_3_rate = 1 / c_ask
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_c
                    
                # if c_base (adquired coin) matches b_base
                if c_base == b_quote:
                    swap_3 = b_quote
                    swap_3_rate = c_bid
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_c
                    
                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1
                
            # Check if a_quote (adquired_coin) matches c_base
            if a_quote == c_base and calculated == 0:
                swap_2_rate =  1 / c_ask
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "baseToQuote"
                contract_2 = pair_c

                # if c_quote (adquired coin) matches b_base
                if c_quote == b_base:
                    swap_3 = c_base
                    swap_3_rate = 1 / c_ask
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_b

                # if b_base (adquired coin) matches b_quote
                if c_quote == b_quote:
                    swap_3 = b_quote
                    swap_3_rate = b_bid
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_b

                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1

        """ Reverse """
        if direction == "Reverse":
            # Check if a_base (adquired_coin) matches b_quote
            if a_base == b_quote and calculated == 0:
                swap_2_rate = b_bid
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "quoteToBase"
                contract_2 = pair_b

                # if b_base (adquired coin) matches c_base
                if b_base == c_base:
                    swap_3 = c_base
                    swap_3_rate = 1 / c_ask
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_c

                # if b_base (adquired coin) matches c_base
                if b_base == c_quote:
                    swap_3 = c_quote
                    swap_3_rate = c_bid
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_c

                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1

            # Check if a_base (adquired_coin) matches b_base
            if a_base == b_base and calculated == 0:
                swap_2_rate =  1 / b_ask
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "baseToQuote"
                contract_2 = pair_b

                # if b_quote (adquired coin) matches c_base
                if b_quote == c_base:
                    swap_3 = c_base
                    swap_3_rate = 1 / b_ask
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_c

                # if b_base (adquired coin) matches c_quote
                if b_quote == c_quote:
                    swap_3 = c_quote
                    swap_3_rate = c_bid
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_c

                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1

            # Check if a_base (adquired_coin) matches c_base
            if a_base == c_quote and calculated == 0:
                swap_2_rate = c_bid
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "quoteToBase"
                contract_2 = pair_c
                
                # if c_base (adquired coin) matches b_base
                if c_base == b_base:
                    swap_3 = b_base
                    swap_3_rate = 1 / c_ask
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_c
                    
                # if c_base (adquired coin) matches b_base
                if c_base == b_quote:
                    swap_3 = b_quote
                    swap_3_rate = c_bid
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_c
                    
                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1
                
            # Check if a_base (adquired_coin) matches c_base
            if a_base == c_base and calculated == 0:
                swap_2_rate =  1 / c_ask
                acquired_coin_t2 = acquired_coin_t1 * swap_2_rate
                direction_trade_2 = "baseToQuote"
                contract_2 = pair_c

                # if c_quote (adquired coin) matches b_base
                if c_quote == b_base:
                    swap_3 = c_base
                    swap_3_rate = 1 / c_ask
                    direction_trade_3 = "quoteToBase"
                    contract_3 = pair_b

                # if b_base (adquired coin) matches b_quote
                if c_quote == b_quote:
                    swap_3 = b_quote
                    swap_3_rate = b_bid
                    direction_trade_3 = "baseToQuote"
                    contract_3 = pair_b

                acquired_coin_t3 = acquired_coin_t2 * swap_3_rate
                calculated = 1


        """ Profit loss output """
        # Profit and loss calculations
        profit_loss = acquired_coin_t3 - starting_amount
        profit_loss_perc = (acquired_coin_t3 - starting_amount) * 100 if profit_loss != 0 else 0
        
          # Trade Descriptions
        trade_description_1 = f"Start with {swap_1} of {starting_amount}. Swap at {swap_1_rate} for {swap_2} acquiring {acquired_coin_t1}."
        trade_description_2 = f"Swap {acquired_coin_t1} of {swap_2} at {swap_2_rate} for {swap_3} acquiring {acquired_coin_t2}."
        trade_description_3 = f"Swap {acquired_coin_t2} of {swap_3} at {swap_3_rate} for {swap_1} acquiring {acquired_coin_t3}."

        if profit_loss > 0:            
            print("New Trade")
            print (trade_description_1 )
            print (trade_description_2 )
            print (trade_description_3 )
            print( acquired_coin_t3 / swap_1_rate )
            break

        # if acquired_coin_t3 > starting_amount:
        #     print(direction, pair_a , pair_b, pair_c, starting_amount, acquired_coin_t3)
