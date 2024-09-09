import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_computers():
    computers = driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[2]/a')
    computers.click()
    time.sleep(2)
    for i in range(1,3):
        element = driver.find_element(By.XPATH,f'//*[@id="side-menu"]/li[2]/ul/li[{i}]/a')
        element.click()
        time.sleep(2)
        save_to_file(driver.current_url,'col-md-4 col-xl-4 col-lg-4',"computers.txt")

def scrape_phone():
    phone = driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/a')
    phone.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li/a')
    element.click()
    save_to_file(driver.current_url, 'col-md-4 col-xl-4 col-lg-4', "phone.txt")
def save_to_file(url, class_name, file_name):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features="html.parser")

        with open (file_name, 'a') as file:
                items = soup.find_all(class_ = class_name)
                file.write(str(items))

    except Exception as ex:
        print(ex)



driver = webdriver.Chrome()
driver.get("https://webscraper.io/test-sites/e-commerce/allinone")
scrape_computers()
scrape_phone()
