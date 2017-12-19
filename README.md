# autotrade
Simple scripts to get realtime quote from NSE, and trade in zerodha

Note: This is NOT a Stable script, NSE may anytime change the way quote is fetched.


# GET QUOTE
Usage:

EQUITY:

python quotefromnse.py \<symbol\>

FUTURES:

python quotefromnse.py \<symbol\> \<expiry\>

# Trade

Login to zerodha in desktop, and get the sessionid from the cookie by inspecting in dev tools

Run the scripts to know the usage
