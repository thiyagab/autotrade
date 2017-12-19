import requests
import json
import sys


url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxFOGetQuoteJSON.jsp"

if len (sys.argv)!=3 :
    print("Usage: python quotefromnse <symbol> <expiry>")
    sys.exit(1)
    
symbol=sys.argv[1]
expiry=sys.argv[2]

querystring = {"underlying":symbol,"instrument":"FUTSTK","expiry":expiry,"type":"SELECT","strike":"SELECT"}

headers = {
    'Cookie': 'ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; pointerfo=1; underlying1={symbol}; instrument1=FUTSTK; optiontype1=-; expiry1={expiry}; strikeprice1=-',
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    'Accept': "*/*",
    'Referer': 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying={symbol}&instrument=FUTSTK&type=-&strike=-&expiry={expiry}',
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'Cache-Control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
text = response.text.strip()
jsonStr=json.loads(text)

print(jsonStr)