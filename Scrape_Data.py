import requests
from bs4 import BeautifulSoup

def scrap_data(url):
    try:
        r = requests.get(url, auth=('user', 'pass'))
        soup = BeautifulSoup(r.text, features="html.parser")

        with open ('created_file', 'w+') as file:
            for item in soup.find_all(class_=['title','description card-text','ratings','caption']):
                file.write(str(item))

    except Exception as ex:
        print(ex)

scrap_data('https://webscraper.io/test-sites/e-commerce/allinone')

