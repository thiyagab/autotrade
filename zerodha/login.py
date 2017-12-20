#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:24:14 2017

@author: thiyagab
"""


import requests
import lxml.html
import twofalogin
import configparser



filename='config.ini'
config = configparser.ConfigParser()
config.read(filename)

url = "https://kite.zerodha.com/"
payload = "user_id="+config['user']['clientid']+"&password="+config['user']['password']+"&login="


response = requests.request("POST", url, data=payload, headers=twofalogin.headers)

newsession=response.cookies['session']
print(newsession)
#print (response.text)
parser=lxml.html.fromstring(response.text)
inputtag=parser.xpath('//*[@id="twofaform"]/input[2]')
#for inputtag in parser.iter('input'):
#    inputtag.

question1=inputtag[0].value
inputtag=parser.xpath('//*[@id="twofaform"]/input[3]')
question2=inputtag[0].value
print(question1,question2)

twofalogin.loginwith2fa(config['user']['clientid'],newsession,question1,config['twofa'][question1],question2,config['twofa'][question2])


config['user']['sessionid']=newsession
with open(filename, 'w') as configfile:
    config.write(configfile)