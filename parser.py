import requests
from bs4 import BeautifulSoup

def fetch_onliner_catalog(url, params=None):
    headers = {
        'User-agent': 'Mozilla/5.0 Chrome/143.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10 )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as exc:
        print(f'Ошибка при запросе к API: {exc}')
        return None
    

url = 'https://catalog.onliner.by/mobile'

soup = fetch_onliner_catalog(url=url)

names = soup.find_all('h3', class_='catalog-form__description catalog-form__description_primary catalog-form__description_base-additional catalog-form__description_font-weight_semibold catalog-form__description_condensed-other')
print(f'Всего спарсилось {len(names)} названий телефонов')
for name in names:
    print(name.text)