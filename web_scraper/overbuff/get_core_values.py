import json
import time
import sys

# Set list of values to keep
core_vals = ['eliminations', 'obj kills', 'obj time', 'weapon acc', 'critical hits', 'solo kills', 'damage', 'healing', 'deaths', 'medals', 'gold medals', 'silver medals', 'bronze medals', 'E:D ratio', 'voting cards']

def get_core(output_dict):
	pre_dict = output_dict
	
	
