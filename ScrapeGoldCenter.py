from bs4 import BeautifulSoup
from selenium import webdriver
import csv
def scrape_gold(html):
    soup = BeautifulSoup(html, 'html.parser')
    elements = []
    table = soup.select_one('table.exchange-table')
    if table:
        for row in table.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            elements.append(row_data)
    return elements

def scrape_silver(html):
    soup = BeautifulSoup(html, 'html.parser')
    elements = []
    new_ls = []
    tables = soup.select('table.exchange-table')

    for table in tables:

        for row in table.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            elements.append(row_data)
    new_ls.append(elements[14])
    new_ls.append(elements[15])

    return new_ls

def scrape_prices(html):
    soup = BeautifulSoup(html, 'html.parser')
    elements = []
    new_ls2 = []
    tables = soup.select('table.exchange-table')

    for table in tables:

        for row in table.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            elements.append(row_data)
    new_ls2.append(elements[17])
    new_ls2.append(elements[18])
    new_ls2.append(elements[19])
    new_ls2.append(elements[20])

    return new_ls2

def save_to_csv(golds):
    with open('metal.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['GOLD', 'BUY', 'SELL', '+/-', 'TIME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for gold in golds[1:]:
            gold_dict = dict(zip(fieldnames, gold))
            writer.writerow(gold_dict)

def save_to_csv2(silvers):
    with open('metal.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['SILVER', 'BUY', 'SELL', '+/-', 'TIME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for silver in silvers:
            silver_dict = dict(zip(fieldnames, silver))
            writer.writerow(silver_dict)

def save_to_csv3(world_prices):
    with open('metal.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['METALS', 'PRICE', '+/-', 'TIME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for prices in world_prices:
            price_dict = dict(zip(fieldnames, prices))
            writer.writerow(price_dict)


driver = webdriver.Chrome()
url = "https://goldcenter.am/en/buyer-account/"
driver.get(url)

gold_data = scrape_gold(driver.page_source)
save_to_csv(gold_data)

silver_data = scrape_silver(driver.page_source)
save_to_csv2(silver_data)

world_data = scrape_prices(driver.page_source)
save_to_csv3(world_data)


