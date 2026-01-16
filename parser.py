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
    

def write_in_csv(mobiles):
    with open('mobile_catalog.csv', 'w', encoding='utf8') as ff:
        for mobile in mobiles:
            mobile_url = mobile.get('href')
            ff.write(f'{mobile.text}: {mobile_url}\n')

URL = 'https://catalog.onliner.by/mobile'

soup = fetch_onliner_catalog(url=URL)

mobiles = soup.find_all('a', href=True, class_='catalog-form__link catalog-form__link_primary-additional catalog-form__link_base-additional catalog-form__link_font-weight_semibold catalog-form__link_nodecor')
print(f'Всего спарсилось {len(mobiles)} телефонов')

write_in_csv(mobiles=mobiles)

    
