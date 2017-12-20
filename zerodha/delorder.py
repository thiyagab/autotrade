#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:00:47 2017

@author: thiyagab
"""

import common
import sys
import orders

def delorder(sessionid,orderid):    
    url = "https://kite.zerodha.com/api/orders/"
    common.headers['Cookie']='session='+sessionid
    # get only the last order status
    querystring = {"variety":"regular"}
    url = url+orderid    
    response=common.senddelrequest(url,querystring)
    return response;

def dellastorder(sessionid) :
    print ("Fetching the last open order to delete")
    response=orders.orders(sessionid)
    response=response['data']
    output_dict = [x for x in response if x['status'] == 'OPEN']
    if(len (output_dict) > 0) :
        orderid=output_dict[0]['order_id']
        print ('Deleting order',output_dict[0]['tradingsymbol'],output_dict[0]['transaction_type'],"at",
               output_dict[0]['order_timestamp'],"id:",orderid)
        response=delorder(sessionid,orderid)
        return response
    else :
        print ("No open orders to delete" )
    
    
if len (sys.argv) < 2 :
        print("Usage: \n","python delorder.py <session> <orderid>\n","or to delete last order","\npython delorder.py <session>")
        sys.exit(1)
        
    
if(len (sys.argv) ==3):
    response=delorder(sys.argv[1],sys.argv[2])
    print(response)
else :
    response=dellastorder(sys.argv[1])
    print (response)


