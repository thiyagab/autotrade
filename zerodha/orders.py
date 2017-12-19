#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:37:59 2017

@author: thiyagab
"""
import sys,common



def orders(sessionid):
    url="https://kite.zerodha.com/api/orders"   
    common.headers['Cookie']='session='+sessionid  
    response=common.sendgetrequest(url,{})
    return response


if __name__ == '__main__':
    if len (sys.argv) < 2 :
            print("Usage: \n","python orders <session>")
            sys.exit(1)
          
    response=orders(sys.argv[1])  
    print(response['data'][0])