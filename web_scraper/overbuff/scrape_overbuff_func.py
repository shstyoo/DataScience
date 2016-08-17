from bs4 import BeautifulSoup
from collections import defaultdict
from HTMLParser import HTMLParser
import requests
import re
import json
import time
import sys

######### GET LIST OF HEROES #########
def update_hero_list():
	# Get hero list
	page = requests.get('https://www.overbuff.com/heroes')
	c = page.content
	soup = BeautifulSoup(c, 'lxml')
	# Initialize hero list
	hero_list = []
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
		
def get_hero_data(hero_val):
	string = hero_val
	print('Getting ' + string + ' data')
	
def get_all_data():
	print('Getting all data')
	
	
	
