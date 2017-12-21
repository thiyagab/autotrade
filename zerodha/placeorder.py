#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:18:25 2017

@author: thiyagab
"""

import sys
import common
import configparser

url = "https://kite.zerodha.com/api/orders"

def placeorder(clientid,sessionid,symbol,transactiontype,qty,price):  
    common.headers['Cookie']='session='+sessionid
    payload = {
            "exchange":"NSE","order_type":"LIMIT",
            "product":"CNC","validity":"DAY","disclosed_quantity":"0",
            "trigger_price":"0","squareoff_value":"0","squareoff":"0","stoploss_value":"0",
            "stoploss":"0","trailing_stoploss":"0","variety":"regular"
            }
    symbol = symbol.upper().strip()
    payload['tradingsymbol']= symbol
    payload['transaction_type']= transactiontype
    payload['quantity']= qty
    payload['price']= price
    payload['client_id']= clientid 
    
    if symbol.endswith('FUT'):
        payload['exchange']='NFO'
        payload['product']='NRML'
    print ('payload',payload)
    response=common.sendpostrequest(url,payload)  
    print( response )
    return response


if __name__ == '__main__':  
    if len(sys.argv) ==2 :
        filename=sys.argv[1]
        config = configparser.ConfigParser()
        config.read(filename)
        symbol=config['trade']['symbol']
        qty=config['trade']['qty']
        price=config['trade']['price']
        clientid=config['user']['clientid']
        transactiontype=config['trade']['transactiontype']
        sessionid=config['user']['sessionid']
        placeorder(clientid,sessionid,symbol,transactiontype,qty,price)
    elif len (sys.argv) < 7 :
        print("Usage: \n","python placeorder.py <clientid> <session> <symbol> <transactiontype BUY|SELL> <qty> <price>")
        sys.exit(1)
    else:
        symbol=sys.argv[3]
        qty=sys.argv[5]
        price=sys.argv[6]
        clientid=sys.argv[1]
        transactiontype=sys.argv[4]
        sessionid=sys.argv[2]
        placeorder(clientid,sessionid,symbol,transactiontype,qty,price)
        
        
        
