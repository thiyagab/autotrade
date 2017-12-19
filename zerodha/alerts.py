#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:48:38 2017

@author: thiyagab
"""

import common
import sys



def alerts(sessionid) :
    url = "https://kite.zerodha.com/api/alerts"
    
    # get only the last order status
    querystring = {"index":"-1"}
    
    
        
    
    common.headers['Cookie']='session='+sessionid
    
    response=common.sendgetrequest(url,querystring)
    return response


if __name__ == '__main__':
    if len (sys.argv) < 2 :
            print("Usage: \n","python alerts <session>")
            sys.exit(1)
            
    response=alerts(sys.argv[1])
    
    print(response['data'])
