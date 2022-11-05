# Step 1: Go to the product review page 1, 2, ....
# Step 2: Go to each full review and extract the review


import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

import re
from time import sleep
from random import randint


#declare global variables
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

mendix_url = "https://www.gartner.com/reviews/market/rapid-mobile-app-development-tools/vendor/zoho/product/zoho-creator/review/view/1130330"

r = requests.get(mendix_url, headers=headers)
print(f"code: {r}")
soup = BeautifulSoup(r.text, 'html.parser')
#soup = BeautifulSoup(r.text, 'html5lib')

#print(soup.prettify())
txt = soup.prettify()
with open("scrape_1_review.txt", "w") as f:
    f.write(txt)


# script id="__NEXT_DATA__" type="application/json"
# review_bodies = soup.find_all("script", attrs={"id": "__NEXT_DATA__"})
# print(len(review_bodies))
# print(type(review_bodies))
# print(type(review_bodies[0]))
# print(review_bodies[0].attrs)
# print(dir(review_bodies[0]))
# print(type(review_bodies[0].string))
# review_summaries = review_bodies[0].findAll("reviewSummary")
# print(review_summaries)
#print(review_bodies[0])
data = soup.find_all("p", attrs={"class": "small answer key"})
# data = json.loads(soup.find("div" , 'page-container'))
print(type(data))
print(dir(data))
print(data)

exit(0)

def find_my_key(d, my_key, result_list, parent_key=None):
    # print(f"parent key: {parent_key}")
    # print(d.keys())
    keys = list(d.keys())
    flag = False
    for k in keys:
        if k == my_key:
            print("Found it")
            flag = True
            result_list.append(d[k])
            return flag, result_list

        new_v = d[k]
        if isinstance(new_v, dict):
            flag, result_list = find_my_key(new_v, my_key, result_list, k)
            
    
    return flag, result_list


my_key = "reviewSummary"
review_list = []
final_results = find_my_key(data, my_key, review_list)
print(final_results[1])

temp_id = 1296192