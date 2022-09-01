from bs4 import BeautifulSoup
import requests
import time
import datetime


def search_TRAPSTAR(URL, index ) :
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    page = requests.get(URL, headers=headers).text
    content = BeautifulSoup(page, "html.parser")
    get_URL = content.find_all('div', class_="grid-view-item product-card")

    for x in range(len(get_URL)):
        time.sleep(0.25)
        # s_URL and s_page represent 'smaller' pages for each item diferrentiating them from the main URL and page :\
        s_URL  =  'https://uk.trapstarlondon.com/' + get_URL[x].a['href']
        print(URL)
        s_page = requests.get(s_URL, headers=headers).text
        content = BeautifulSoup(s_page, "html.parser")
        item_name = content.find('h1', class_="product-single__title").text
        query_price = content.find('div', class_="product__price").find(class_="price__regular").find(class_="price-item price-item--regular").text
        print(item_name.strip() + '    =>     ' + query_price.strip())
        if x == (len(get_URL)-1):
            index += 1
            search_TRAPSTAR(f'https://uk.trapstarlondon.com/collections/shop-all?page={index}', index)

search_TRAPSTAR('https://uk.trapstarlondon.com/collections/shop-all', 0)
    
