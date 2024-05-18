'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''

# Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
import requests
import pprint
import time


# while time.sleep(30): 
# Request URL. Repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
url = 'https://rest.coinapi.io/v1/assets/BTC'
headers = {'X-CoinAPI-Key' : '9A1885E7-E117-4E16-8883-E7B1E57231EA'}
response = requests.get(url, headers=headers)
crypto_data = response.json()


# Key Time & Value Price
time_start = (crypto_data[0]["data_trade_start"])
price = (crypto_data[0]["price_usd"])

# Leave time before the second request
time.sleep(10)

# Second request 
response = requests.get(url, headers=headers)
crypto_data_2 = response.json()

# Key2 Time & Value2 Price
trade_end = (crypto_data_2[0]["data_trade_end"])
price_2 = (crypto_data_2[0]["price_usd"])


# Store each value in a dictionary that uses the time of query as a key.
my_cryptodict = {}
my_cryptodict[time_start] = price
my_cryptodict[trade_end] = price_2

print(my_cryptodict)




