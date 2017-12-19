#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 09:56:21 2017

@author: thiyagab
"""

import json
import requests

headers = {
    'Cookie': "ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; pointerfo=1;",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    'Accept': "*/*",
    'Referer': "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Cache-Control': "no-cache",
    }


def sendrequest (url, querystring):
    response = requests.request("GET", url, headers=headers, params=querystring)
    printresponse( response )

def printresponse ( response ):
        text = response.text.strip()
        jsonStr=json.loads(text)
        print(jsonStr)