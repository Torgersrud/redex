# -*- coding: utf-8 -*-
"""

@author: Oskar Torgersrud
"""
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time as t


# We are using the coinmarketcap api to get up to date data on price

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


# Start and limit refer to which currencies to include in the request
parameters = {
  'start':'1',
  'limit':'5000',
  'convert': 'USD'
}

headers = {
  'Accepts': 'application/txt',
  'X-CMC_PRO_API_KEY': '51964cdd-cfc6-433c-8394-47bfdc7245e0',
}

session = Session()
session.headers.update(headers)
    
def getCoinData():
  try:
    livedata = {}
    response = session.get(url, params=parameters)
  except (ValueError, ConnectionError) as fail_msg:
    return fail_msg
  
  data = json.loads(response.text)
  for i in range(160):
    livedata[(data["data"][i]["name"])] = data["data"][i]["quote"]["USD"]["market_cap"]
  return livedata


