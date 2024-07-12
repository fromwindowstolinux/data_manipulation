import requests
from bs4 import BeautifulSoup


url = 'https://zuscoffee.com/category/store/melaka/'
response = requests.get(url)
response.raise_for_status() 
soup = BeautifulSoup(response.text, 'html.parser')
store_selector = '#post-9971 > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-af9e841.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > div > div > div > span'  
stores = soup.select(store_selector)

for store in stores:
    store_name_tag = store.find('span', class_='entry-title')
    store_name = store_name_tag.get_text(strip=True) if store_name_tag else "Store name not found"
    store_address_tag = store.find('p')
    store_address = store_address_tag.get_text(strip=True) if store_address_tag else "Address not found"

    print(f"Store Name: {store_name}")
    print(f"Address: {store_address}")
    print('-' * 50)
