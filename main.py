# https://api.coinbase.com/v2/prices/buy?currency=USD

import requests

def inform_AfiaBTC(price):
    print(f"Hello there, the price of bitcoin is good now and the price is {price}")

my_good_price = 110090.085 # Set your desired price here

response = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")
price = float(response.json()['data']['amount'])
if (price < my_good_price):
    inform_AfiaBTC(price)
print(price)