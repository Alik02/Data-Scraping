import csv
from selenium import webdriver
from bs4 import BeautifulSoup

def extract_gold_info(gold):
    td_elements = gold.find_all('td', class_='exchange-table__item')

    result_string = ''
    for element in td_elements:
        result_string += element.get_text()
    chlp = result_string.split("\n")
    for key in range(len(chlp)):
        chlp[key] = chlp[key].strip()
    for key in chlp:
        if key == '':
            chlp.remove(key)

    data = []
    smData = []
    for key in range(0,len(chlp)):
        if key % 5 == 0 and key != 0:
                data.append(smData)
                smData = []
        smData.append(chlp[key])
    data.append(smData)
    first_set = data.pop(0)
    data.insert(0, first_set)

    res = []
    for key in range(len(data)):
        dic = dict()
        dic['GOLD'] = data[key][0]
        dic['BUY'] = data[key][1]
        dic['SELL'] = data[key][2]
        dic['+/-'] = data[key][3]
        dic['TIME'] = data[key][4]
        res.append(dic)

    return res
def scrape_gold(html):
    scraped_data = []
    soup = BeautifulSoup(html, 'html.parser')
    scraped_data.append(soup.find('table', class_='exchange-table'))

    return [extract_gold_info(gold) for gold in scraped_data][0]


def save_to_csv(golds):
    with open('gold.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['GOLD', 'BUY', 'SELL', '+/-', 'TIME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for gold in golds:
            writer.writerow(gold)

driver = webdriver.Chrome()
url = "https://goldcenter.am/en/buyer-account/"
driver.get(url)
golds = scrape_gold(driver.page_source)
save_to_csv(golds)

