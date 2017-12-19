#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:18:25 2017

@author: thiyagab
"""

import sys
import common

url = "https://kite.zerodha.com/api/orders"

if len (sys.argv) < 7 :
    print("Usage: \n","python placeorder <clientid> <session> <symbol> <transactiontype BUY|SELL> <qty> <price>")
    sys.exit(1)

symbol=sys.argv[3]
qty=sys.argv[5]
price=sys.argv[6]
clientid=sys.argv[1]
transactiontype=sys.argv[4]


common.headers['Cookie']='session='+sys.argv[2]

payload = {
        "exchange":"NFO","order_type":"LIMIT",
        "product":"NRML","validity":"DAY","disclosed_quantity":"0",
        "trigger_price":"0","squareoff_value":"0","squareoff":"0","stoploss_value":"0",
        "stoploss":"0","trailing_stoploss":"0","variety":"regular"
        }

payload['tradingsymbol']= symbol
payload['transaction_type']= transactiontype
payload['quantity']= qty
payload['price']= price
payload['client_id']= clientid


response=common.sendpostrequest(url,payload)

print( response )