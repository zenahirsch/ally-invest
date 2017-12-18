from requests_oauthlib import OAuth1
import request
import constants


class AllyClient:
    def __init__(self, credentials):
        self.auth = OAuth1(*credentials)

    def get_accounts(self):
        r = request.get(constants.PATH_GET_ACCOUNTS, self.auth)
        return r.content

    def get_account_balances(self):
        r = request.get(constants.PATH_GET_ACCOUNT_BALANCES, self.auth)
        return r.content

    def get_account_balance(self, account_id):
        r = request.get(constants.PATH_GET_ACCOUNT_BALANCE % account_id,
                        self.auth)
        return r.content

    def get_account_history(self, account_id):
        r = request.get(constants.PATH_GET_ACCOUNT_HISTORY % account_id,
                        self.auth)
        return r.content

    def get_account_holdings(self, account_id):
        r = request.get(constants.PATH_GET_ACCOUNT_HOLDINGS % account_id,
                        self.auth)
        return r.content
    
    def get_account_orders(account_id):
        r = request.get(constants.PATH_ORDERS, self.auth)
        return r.content

    def place_order(account_id):
        pass

    def preview_order(account_id):
        pass
