#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 09:56:21 2017

@author: thiyagab
"""

import json
import requests

headers = {
    'Pragma': "no-cache",
    'Origin': "https://kite.zerodha.com",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    'Content-Type': "application/json;charset=UTF-8",
    'Accept': "application/json, text/plain, */*",
    'Cache-Control': "no-cache",
    'Referer': "https://kite.zerodha.com/dashboard/?login=true",
    'Connection': "keep-alive",
    'If-Modified-Since': "0"
    }


def sendgetrequest (url, querystring):
    response = requests.request("GET", url, headers=headers, params=querystring)
    return  parseresponse( response );

def senddelrequest (url, querystring):
    response = requests.request("DELETE", url, headers=headers, params=querystring)
    return  parseresponse( response );
    
def sendpostrequest (url, payload):
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers) 
    return  parseresponse( response );

def sendpostformrequest (url, payload):
    response = requests.request("POST", url, data=payload, headers=headers) 
    return response;

def parseresponse ( response ):
        text = response.text.strip()
        jsonStr=json.loads(text)
        #print(jsonStr)
        return jsonStr