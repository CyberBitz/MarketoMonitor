# Marketo Monitor by CyberBitz
# https://github.com/CyberBitz/MarketoMonitor

import requests
from os import system, name
import os
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
marketto_orgs = []
marketto_orgs_new = []
if not os.path.exists('marketo_orgs.txt'):
    file = open('marketo_orgs.txt', 'w+')
text_file = open("marketo_orgs.txt", "r")
lines = text_file.readlines()
for lns in lines:
    marketto_orgs.append(lns.replace("\n", ""))

valid = 1
pagecount = 1
pages = []
orgs = []

class bcolors:
    STATUS = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    NORMAL = '\033[94m'
    
clear()
print(f"{bcolors.NORMAL}Receiving Page: {bcolors.ENDC}")
def receivingPages():
    print(f"{bcolors.STATUS}" + str(pagecount) + f" {bcolors.ENDC}", end="", flush=True)

while valid > 0:
    url = 'https://marketo.cloud/?page=' + str(pagecount)
    
    receivingPages()

    try:
        response = requests.get(url, verify=False)
        if response.status_code != 200:
            valid = 0
        html_text = response.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

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
        marketto_orgs_new.append(ogz)

file_object = open('marketo_orgs.txt', 'a')
for norg in marketto_orgs_new:
    file_object.write(norg+"\n")
print("\n================================")
print(f"{bcolors.STATUS}Existing Orgs: " + str(len(marketto_orgs)) + f"{bcolors.STATUS}", end="")
print(f"{bcolors.NORMAL}")
print(marketto_orgs)
print(f"{bcolors.NORMAL}")
print(f"{bcolors.STATUS}New Orgs: " + str(len(marketto_orgs_new)) + f"{bcolors.STATUS}", end="")
print(f"{bcolors.NORMAL}")
print(marketto_orgs_new)
print(f"{bcolors.NORMAL}")# print array of new orgs posted
# do any alerting here, I implement a telegram bot I push the new orgs that have been added.

