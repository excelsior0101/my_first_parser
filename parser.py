import requests
from bs4 import BeautifulSoup

def fetch_onliner_catalog(url, params=None):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10 )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as exc:
        print(f'Ошибка при запросе к API: {exc}')
        return None
    

url = 'https://catalog.onliner.by/mobile/apple'

soup = fetch_onliner_catalog(url=url)


