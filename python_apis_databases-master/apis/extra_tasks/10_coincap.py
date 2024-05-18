'''
Sign up for an API key with the coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.

'''
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint


url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ca80e6b7-8cf6-4f23-9468-075366394cdd',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  pprint.pprint(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


cmc_rank = (data['data'][0]['cmc_rank'])
name = (data['data'][0]['name'])
symbol = (data['data'][0]['symbol'])
platform = (data['data'][0]['platform'])
quote = (data['data'][0]['quote'])

# Creating JSON. Adding data to json_obj
json_obj = {}
json_obj['cmc_rank'] = []
json_obj['name'] = []
json_obj['symbol'] = []
json_obj['platform'] = []
json_obj['quote'] = []

json_obj['cmc_rank'].append(cmc_rank)
json_obj['name'].append(name)
json_obj['symbol'].append(symbol)
json_obj['platform'].append(platform)
json_obj['quote'].append(quote)
print(json_obj)

#Write the object to file.
with open('example.json','w') as jsonFile:
    json.dump(json_obj, jsonFile)