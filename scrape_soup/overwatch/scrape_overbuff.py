from bs4 import BeautifulSoup
from collections import defaultdict
from HTMLParser import HTMLParser
import requests
import re
import json
import time
import sys

# Initialize hero list
hero_list = []

# Get hero list
page = requests.get('https://www.overbuff.com/heroes')
c = page.content
soup = BeautifulSoup(c, 'lxml')

# Sort by table
table = soup.find_all('table')
for item in table:
    if 'table-data' in item['class']:
        table_values = item.find_all('tr')
# Find table values, and get hero names (for URL)
for item in table_values:
	temp_list = []
	td = item.find_all('td')
	for item2 in td:
		temp_list.append(item2)
	try:
		temp_string = temp_list[1].a['href'].split('/')
		hero_list.append(temp_string[2])
	except:
		pass


