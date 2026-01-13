import requests
import json

def fetch_onliner_catalog(url, params=None):
    headers = {
        'User-agent': 'Chrome/120.0.0.0',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as exc:
        print(f'Ошибка при запросе к API: {exc}')
        return None
    

api_url = 'https://counter.mediameter.by/?href=https%3A%2F%2Fcatalog.onliner.by%2Fmobile%2Fapple'
search_params = {
    'query': 'смартфон'
}

data = fetch_onliner_catalog(url=api_url, params=search_params)
if data:
    print(json.dumps(data, indent=2, ensure_ascii=False))