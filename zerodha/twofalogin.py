#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:26:53 2017

@author: thiyagab
"""

import requests

url = "https://kite.zerodha.com/"

querystring = {}


headers = {
    'Origin': "https://kite.zerodha.com",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Cache-Control': "no-cache",
    'Referer': "https://kite.zerodha.com/",
    'Connection': "keep-alive",
    'Content-Type': "application/x-www-form-urlencoded"
    }

def loginwith2fa(clientid,sessionid,question1,answer1,question2,answer2):
    headers['Cookie']='session='+sessionid
    payload = 'user_id='+clientid+'&question1='+question1+'&question2='+question2+'+&answer1='+answer1+'&answer2='+answer2+'&twofa='
    print(payload)
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.ok)