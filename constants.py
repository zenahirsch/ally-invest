# API Configuration
API_VERSION = 'v1'
BASE_URL = 'https://api.tradeking.com/%s/' % API_VERSION

# Endpoints: Account
PATH_GET_ACCOUNTS = 'accounts.json'
PATH_GET_ACCOUNT_BALANCES = 'accounts/balances.json'
PATH_GET_ACCOUNT_BALANCE = 'accounts/%d.json'
PATH_GET_ACCOUNT_HISTORY = 'accounts/%d/history.json'
PATH_GET_ACCOUNT_HOLDINGS = 'accounts/%d/holdings.json'

# Endpoints: Order/Trade
PATH_ORDERS = 'accounts/%d/orders.json'
PATH_PREVIEW_ORDER = 'accounts/%d/orders/preview.json'
