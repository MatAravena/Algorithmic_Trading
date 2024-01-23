from config_execution_api import signal_positive_ticker  
from config_execution_api import signal_negative_ticker
from httpClient_HMAC import GET,POST
# from config_execution_api import ws

# Get position information
def get_position_info(ticker):

    # Declare output variables
    side = 0
    size = ""

    # https://bybit-exchange.github.io/docs/v5/position
    # Extract position info
    position = GET( '/v5/position/list', 'category=linear&symbol='+ticker)
    print('position',position)
    if len(position["result"]) == 2:
        if position["result"][0]["size"] > 0:
            size = position["result"][0]["size"]
            side = "Buy"
        else:
            size = position["result"][1]["size"]
            side = "Sell"

    # Return output
    return side, size

#  Place market close order
def place_market_close_order(ticker, side, size):

    # https://bybit-exchange.github.io/docs/v5/position/close-pnl
    # Close position
    # POST('/contract/v3/private/copytrading/order/close',  'category=linearsymbol='+ticker)

    # https://api2-1-testnet.bybit.com/contract/v5/order/create?_sp_category=fbu&_sp_business=usdt&_sp_response_format=portugal
    # {"category": "linear", "symbol": "BTCUSDT", "side": "Sell", "orderType": "Limit", "qty": "1", "price": "30000", 
    # "timeInForce": "GTC", "positionIdx": 0, "orderLinkId": "usdt-test-02", "reduceOnly": true}

    POST('/v5/order/create',
        {
            "category": "linear",
            "symbol": "XRPUSDT",
            "side": "Sell",
            "orderType": "Market",
            "qty": "13530",
            "timeInForce": "GTC",
            "positionIdx": 0,
            "reduceOnly": 'false',
            "closeOnTrigger": 'false'
        }
    )

    # ws.close_all_positions()

        # {
        #     "category": "linear", 
        #     "symbol": "XRPUSDT",
        #     "side": "Sell", 
        #     "orderType": "Limit", 
        #     "qty": "0", 
        #     "price": "30000", 
        #     "timeInForce": "GTC",
        #     "positionIdx": 0,
        #     "reduceOnly": True
        # }
    
    # ws.place_order(
    # category='linear',
    # symbol=ticker,
    # side=side,
    # order_type="Market",
    # qty=size,
    # time_in_force="GoodTillCancel",
    # reduce_only=True,
    # close_on_trigger=False)


    # POST('/unified/v3/private/order/create',
    #     '&symbol='+ticker+
    #     '&side='+side+
    #     '&orderType=Market'+
    #     '&qty='+size+
    #     # '&qty=0' # +size+
    #     '&timeInForce=GTC'+
    #     '&category=linear'+
    #     '&createType=CreateByClosing'+
    #     '&action=PositionClose'+
    #     '&reduceOnly=True'+
    #     '&closeOnTrigger=true'+
    #     '&smpType=true'
    # )

    

    # https://api2-testnet.bybit.com/contract/v5/order/create?_sp_category=fbu&_sp_business=usdt&_sp_response_format=portugal
    # action:"PositionClose"
    # closeOnTrigger:true
    # createType:CreateByClosing
    # leverage:"10"
    # leverageE2:"1000"
    # orderType:"Market"
    # positionIdx:"0"
    # price:"0"
    # qty:"11605"
    # qtyX:"1160500000000"
    # side:"Sell"
    # symbol:"MATICUSDT"
    # timeInForce:"GoodTillCancel"
    # type:"Activity"

    # session_private.place_active_order(
    # category=linear
    # symbol=ticker,
    # side=side,
    # order_type="Market",
    # qty=size,
    # time_in_force="GoodTillCancel",
    # reduce_only=True,
    # close_on_trigger=False

    return

# Close all positions for both tickers
def close_all_positions(kill_switch):

    # Cancel all active orders
    # session_private.cancel_all_active_orders(symbol=signal_positive_ticker)
    # session_private.cancel_all_active_orders(symbol=signal_negative_ticker)

    # GET( '/contract/v3/private/copytrading/position/close','symbol=MATICUSDT&positionIdx=1' )
    POST('/v5/order/cancel-all', 'category=linear&symbol='+ signal_positive_ticker)
    POST('/v5/order/cancel-all', 'category=linear&symbol='+ signal_negative_ticker)

    # Get position information
    # side_1, size_1 = get_position_info(signal_positive_ticker)
    # side_2, size_2 = get_position_info(signal_negative_ticker)

    # if size_1 > 0:
    #     place_market_close_order(signal_positive_ticker, side_2, size_1) # use side 2

    # if size_2 > 0:
    #     place_market_close_order(signal_negative_ticker, side_1, size_2) # use side 1

    # # Output results
    # kill_switch = 0
    # return kill_switch

# TEST
# get_position_info("MATICUSDT")
# close_all_positions('MATICUSDT')
place_market_close_order('XRPUSDT','Sell','13530')
# POST('/v5/order/cancel-all', 'category=linear&symbol=MATICUSDT')
