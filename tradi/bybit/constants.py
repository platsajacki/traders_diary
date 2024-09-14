from os import getenv

USDT = 'USDT'
LINEAR = 'linear'

BYBIT_API_KEY = getenv('BYBIT_API_KEY', '')
BYBIT_API_SECRET = getenv('BYBIT_API_SECRET', '')
TESTNET = bool(int(getenv('NOT_TESTNET', 1)))
