from bs4 import BeautifulSoup
from collections import defaultdict
from HTMLParser import HTMLParser
import requests
import re
import json
import time
import sys

######### GLOBAL VARIABLES #########

prepend_url = 'https://www.overbuff.com/heroes'
d_final = defaultdict(dict)
hero_list = []

######### GET LIST OF HEROES #########

def update_hero_list():
	# Get hero list
	page = requests.get(prepend_url)
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

######### DATA SCRAPING #########

# Wrapper call to update hero data (takes arguments for 'all' or specific hero name)
def update_hero_data(*hero_val):
	# Take arguments
	arg = []
	for val in hero_val:
		arg.append(val)
	# If arguement contains all, get all data and break
	if any('all' in item for item in arg):
		get_all_data()
	# Otherwise fetch data for specific heroes
	else:
		for item in arg:
			get_hero_data(item)
	with open('results.json', 'wb') as f:
		json.dump(d_final, f)
			
# Gets specific hero data
def get_hero_data(hero_val):
	hero_name = hero_val
	page = requests.get(prepend_url + '/' + hero_name)
	c = page.content
	soup_hero = BeautifulSoup(c, 'lxml')
	stats = soup_hero.find_all('div')
	temp_dict = {}
	for item in stats:
		try:
			if 'boxed' in item['class']:
				stat2 = item.find_all('div')
				temp_dict[stat2[2].text] = stat2[1].text
		except:
			pass
	d_final[hero_name] = temp_dict

# Gets all hero data
def get_all_data():
	for item in hero_list:
		get_hero_data(item)
	
	
	
