from bs4 import BeautifulSoup
from collections import defaultdict
from HTMLParser import HTMLParser
import requests
import re
import json
import time
import sys

hero_list = []

page = requests.get('https://www.overbuff.com/heroes')
c = page.content
soup = BeautifulSoup(c, 'lxml')

table = soup.find_all('table')
for item in table:
    if 'table-data' in item['class']:
        tableValues = item.find_all('tr')
