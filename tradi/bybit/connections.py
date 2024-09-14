from pybit.unified_trading import HTTP

from bybit.constants import BYBIT_API_KEY, BYBIT_API_SECRET, TESTNET

http_bybit = HTTP(testnet=TESTNET, api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)
