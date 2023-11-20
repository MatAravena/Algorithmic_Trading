# https://thegraph.com/hosted-service/subgraph/ianlapham/uniswap-v3-subgraph?selected=playground
import requests
import json
import time
import func_triangular_arb

""" Retrieve graphQl mid prices from uniswap """ 
def retrieveUniswapInformation():
    query = """ 
         {   pools(orderBy: totalValueLockedETH, orderDirection: desc, first: 500) 
            {
                feeTier
                feesUSD
                id
                token0 {
                    decimals
                    id
                    name
                    symbol
                }
                tick
                token0Price
                token1Price
                token1 {
                    decimals
                    id
                    name
                    symbol
                }
                totalValueLockedETH
                totalValueLockedToken0
                totalValueLockedToken1
            }
        }
    """

    # Graphql Endpoint
    url ='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    req = requests.post(url, json={ 'query': query} )
    json_dict = json.loads(req.text)
 
    return json_dict
 
if __name__ == "__main__":

    # while True:
        pairs = retrieveUniswapInformation()["data"]["pools"] 
        structured_pairs = func_triangular_arb.structure_trading_pairs(pairs, limit=200)

        #Get surface rates
        surface_rate_list = []

        for t_pair in structured_pairs:
            surface_rate = func_triangular_arb.calc_triangular_arb_surface_rate(t_pair, min_rate=1.5)
            if len(surface_rate) > 0:
                surface_rate_list.append(surface_rate)

        #Save to JSON File
        if len(surface_rate_list) > 0:
            with open('Arbitrage/Uniswap/uniswap_surface_rates.json', 'w') as fp:
                json.dump(surface_rate_list, fp)
                print('new file save')

        # time.sleep(60)
