import requests
import os

def exchange_currency(current_currency, current_amount, new_currency):
    url = f"https://api.currencyapi.com/v3/latest?apikey={os.getenv('API_KEY')}"
    response = requests.get(url)
    current_currency_exchange_rate = response.json()["data"][current_currency]["value"]
    new_currency_exchange_rate = response.json()["data"][new_currency]["value"]
    return (new_currency_exchange_rate / current_currency_exchange_rate) * current_amount