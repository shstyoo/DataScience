from collections import defaultdict
import json
import time
import sys

# Set list of values to keep
core_vals = ['ELMINATIONS', 'OBJ KILLS', 'OBJ TIME', 'WEAPON ACC', 'CRITICAL HITS', 'SOLO KILLS', 'DAMAGE', 'HEALING', 'DEATHS', 'MEDALS', 'GOLD MEDALS', 'SILVER MEDALS', 'BRONZE MEDALS', 'E:D RATIO', 'VOTING CARDS']

# Get only core values
def get_core(output_dict):
	pre_dict = output_dict
	core_dict = defaultdict(dict)
	for k in pre_dict.keys():
		temp_dict = {}
		for k1 in pre_dict[k].keys():
			for item in core_vals:
				if k1 == item:
					temp_dict[k1] = pre_dict[k][k1]
				else:
					pass
		core_dict[k] = temp_dict
	with open('results_core.json', 'wb') as f:
		json.dump(core_dict, f)

	
