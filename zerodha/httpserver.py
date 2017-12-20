#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 01:09:40 2017

@author: thiyagab
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse,parse_qs
import placeorder
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        print (self.path)
        params= parse_qs(urlparse(self.path).query)
        message=''
        
        if len (params) >0:
            try:
                clientid= params['clientid'][0]
                sessionid= params['sessionid'][0]
                symbol= params['symbol'][0]
                transactiontype= params['transactiontype'][0]
                qty= params['qty'][0]
                price= params['price'][0]
                message=placeorder.placeorder(clientid,sessionid,symbol,transactiontype,qty,price)
                self.wfile.write(bytes(str(message),"utf8"))
            except:
                message = "Error!"
                self.wfile.write(bytes(str(message), "utf8"))
 
        # Send message back to client
        # Write content as utf-8 data
        #self.wfile.write(bytes(str(message), "utf8"))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('localhost', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()

def test():
    print (parse_qs('a=b&c=d').get('dd') )
 
run()








