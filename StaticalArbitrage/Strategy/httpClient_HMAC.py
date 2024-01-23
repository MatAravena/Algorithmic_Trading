import json

from config_strategy_api import mode
from config_strategy_api import api_key
from config_strategy_api import api_secret
from config_strategy_api import api_url

import requests
import time
import hashlib
import hmac 
 
httpClient=requests.Session()
recv_window=str(5000) 

def JsonValidator(JSON):
    newJson = json.loads(JSON.text)
    if mode == "test" and 'retMsg' in newJson and newJson['retMsg'] == 'OK':
        return newJson

    if mode != "test" and 'ret_msg' in newJson and newJson['ret_msg'] == 'OK':
        return newJson

    return []

def POST(endPoint,payload):
    global time_stamp
    time_stamp=str(int(time.time() * 10 ** 3))
    signature=genSignature(payload)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    response = httpClient.request("POST", api_url+endPoint+"?"+payload, headers=headers)
    return JsonValidator(response)

def GET(endPoint,payload=''):
    global time_stamp
    time_stamp=str(int(time.time() * 10 ** 3))
    signature= genSignature(payload)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    # print('result Get', api_url+endPoint+'?'+payload)
    # response = httpClient.request("GET", api_url+endPoint+'?', headers=headers, data=payload)
    response = httpClient.request("GET", api_url+endPoint+'?'+payload, headers=headers)
    
    print('result Get', response)
    return JsonValidator(response)

def GET_DirectUrl(endPoint,payload=''):
    global time_stamp
    time_stamp=str(int(time.time() * 10 ** 3))
    signature= genSignature(payload)
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-SIGN': signature,
        'X-BAPI-SIGN-TYPE': '2',
        'X-BAPI-TIMESTAMP': time_stamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'Content-Type': 'application/json'
    }
    response = httpClient.request("GET", endPoint, headers=headers, data=payload)
    newJson = json.loads(response.text)
    return newJson

def genSignature(payload):
    param_str= str(time_stamp) + api_key + recv_window + payload
    hash = hmac.new(bytes(api_secret, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
    signature = hash.hexdigest()
    return signature

# Examples
# #Create Order
# endpoint="/v5/order/create"
# method="POST"
# orderLinkId=uuid.uuid4().hex
# params='{"category":"linear","symbol": "BTCUSDT","side": "Buy","positionIdx": 0,"orderType": "Limit","qty": "0.001","price": "10000","timeInForce": "GTC","orderLinkId": "' + orderLinkId + '"}'
# POST(endpoint,method,params,"Create")

# #Get unfilled Orders
# endpoint="/v5/order/realtime"
# method="GET"
# params='category=linear&settleCoin=USDT'
# GET(endpoint,method,params,"UnFilled")

# #Cancel Order
# endpoint="/v5/order/cancel"
# method="POST"
# params='{"category":"linear","symbol": "BTCUSDT","orderLinkId": "'+orderLinkId+'"}'
# POST(endpoint,method,params,"Cancel")