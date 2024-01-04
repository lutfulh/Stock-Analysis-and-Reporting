import requests
import os

def get_symbol_from_name(company_name):
    API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
    BASE_URL = "https://www.alphavantage.co/query"

    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": company_name,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    #print("API Response:", response.text)
    if response.status_code == 200:
        data = response.json()
        best_matches = data.get('bestMatches', [])
        if best_matches:
            return best_matches[0].get('1. symbol')
    return None


def get_financial_data(symbol):
    API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
    BASE_URL = "https://www.alphavantage.co/query"
    params = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "apikey": API_KEY}

    response = requests.get(BASE_URL, params=params)
    try:
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    except ValueError:
        print("Invalid JSON response")
        return None
