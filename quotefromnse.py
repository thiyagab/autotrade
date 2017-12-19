#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 08:57:58 2017

@author: thiyagab
"""
import sys
import common

if len (sys.argv) < 2 :
    print("Usage: \n","python quotefromnse <symbol>\n","or\n","python quotefromnse <symbol> <expiry>")
    sys.exit(1)


symbol=sys.argv[1].upper()
expiry = ''
if len (sys.argv) == 3 :
    expiry=sys.argv[2].upper()
    


    
quoteurl = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp"
futquoteurl=  "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxFOGetQuoteJSON.jsp"

querystring = ''

if  expiry :
    querystring =  {"underlying":symbol,"instrument":"FUTSTK","expiry":expiry,"type":"SELECT","strike":"SELECT"}
    url = futquoteurl

else :
    querystring = {"symbol":sys.argv[1]}
    url=quoteurl



response = common.sendrequest( url= url,querystring=querystring)