from distutils import text_file

from bs4 import BeautifulSoup
import requests

import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd

# search area of interest

# 'https://marketo.cloud/?page=1'
marketto_orgs = []
marketto_orgs_new = []

text_file = open("marketto_orgs.txt", "r")
lines = text_file.readlines()
for lns in lines:
    marketto_orgs.append(lns.replace("\n", ""))

valid = 1
pagecount = 1
pages = []
orgs = []
while valid > 0:
    url = 'https://marketo.cloud/?page=' + str(pagecount)
    print(url)
    try:
        response = requests.get(url, verify=False)
        if response.status_code != 200:
            valid = 0
        html_text = response.text
    except:
        print("bad")
    print(response.status_code)
    soup = BeautifulSoup(html_text, 'lxml')

    pgs = soup.find_all('li', class_='page-item')

    for ele in pgs:
        title = ele.find('a', class_='page-link')
        page = title.attrs['href']
        p = page[-1:]
        if p != "1":
            pages.append(p)

    pgs = soup.find_all('a', class_='pl-1')

    for ele in pgs:
        o = ele.text
        orgs.append(o)

    pagecount += 1

for oz in orgs:
    ogz = oz.replace("https://", "").replace("http://", "").replace("www.", "")
    if ogz not in marketto_orgs:
        print("NEW: " + ogz)
        marketto_orgs_new.append(ogz)

file_object = open('marketto_orgs.txt', 'a')
for norg in marketto_orgs_new:
    file_object.write(norg+"\n")


print(marketto_orgs)
print(marketto_orgs_new)
