import requests
import json

"""
Getting Data
"""
# Linear comments

req = requests.get("https://api.poloniex.com/markets/ticker24h") 
# print (req.text)

limit = '10'
symbol = "BTC_USDT" 
scale = '1'
req2 = requests.get("https://api.poloniex.com/markets/"+symbol+"/orderBook?scale="+scale+"&limit="+limit)
# print (req2.text)
# print (req2.text[0]["asks"])

# METHOD
def get_api_data(url):
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.text)
    else: 
        return 0

orderBooks =  get_api_data("https://api.poloniex.com/markets/"+symbol+"/orderBook?scale="+scale+"&limit="+limit)
print(orderBooks)