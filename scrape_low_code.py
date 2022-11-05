import requests
import pandas as pd
from bs4 import BeautifulSoup

import re
from time import sleep
from random import randint


#declare global variables
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

mendix_url = "https://www.gartner.com/reviews/market/rapid-mobile-app-development-tools/vendor/zoho/product/zoho-creator/reviews"

r = requests.get(mendix_url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

#print(soup.prettify())
review_bodies = soup.find_all("li")
print(len(review_bodies))