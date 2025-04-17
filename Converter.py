import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def get_currency():
    url = f"https://api.currencyapi.com/v3/latest?apikey={os.getenv('API_KEY')}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"data was not retrieved {response.status_code}")


def main():
    configure()
    data = get_currency()
    print(data)

main()