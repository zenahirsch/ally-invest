import requests
import constants


def get(path, auth):
    url = constants.BASE_URL + path
    return requests.get(url, auth=auth)


def post(path, auth):
    url = constants.BASE_URL + path
    return requests.post(url, auth=auth)
