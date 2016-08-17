from scrape_overbuff_func import *
from get_core_values import *

# Get the updated hero list (works even if new heroes are added)
update_hero_list()

# Get data for all heroes
all_dict = update_hero_data('all')

# Get core data from output
get_core(all_dict)
