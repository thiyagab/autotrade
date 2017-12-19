#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 08:57:58 2017

@author: thiyagab
"""

import requests
import sys
import json

url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp"

if len (sys.argv)!=2 :
    print("Usage: python quotefromnse <symbol>")
    sys.exit(1)
    
querystring = {"symbol":sys.argv[1]}

headers = {
    'Cookie': "ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; pointerfo=1; underlying1=CGPOWER; instrument1=FUTSTK; optiontype1=-; expiry1=28DEC2017; strikeprice1=-; pointer=1; sym1=CGPOWER",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    'Accept': "*/*",
    'Referer': "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=CGPOWER",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Cache-Control': "no-cache",
    'Postman-Token': "c1e877de-74f5-5b4f-d06d-53b436a77dcb"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

text = response.text.strip()
jsonStr=json.loads(text)

print(jsonStr)