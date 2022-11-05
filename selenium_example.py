from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import codecs

import re
from sympy import pretty

from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

val = "https://www.g2.com/products/appian/reviews?page=5"

wait = WebDriverWait(driver, 10)

driver.get(val)


get_url = driver.current_url
wait.until(EC.url_to_be(val))


if get_url == val:
    page_source = driver.page_source

soup = BeautifulSoup(page_source,features="html.parser")
print(soup.prettify())