import argparse
import datetime
import json

from datetime_utils import format_date
from menu import build_menu
from filter_recipes import filter_recipes
from sort_list import sort_recipes
from read_recipes import get_recipes

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Generate a menu from recipes data.")
parser.add_argument("--start", "-s", required=True, help="Start date (format: dd/mm/yyyy)")
parser.add_argument("--max-persons", "-p", type=int, default=4, help="Maximum number of persons for recipes")
args = parser.parse_args()

# Load recipes data from recipes_data.json
with open("recipes_data.json", "r") as recipes_file:
    recipes_data = json.load(recipes_file)

# Parse the start date
start_date = format_date(args.start)

# Sort recipes by title
sorted_recipes = sort_recipes(recipes_data, "title")

# Filter recipes by maximum persons
filtered_recipes = filter_recipes(sorted_recipes, args.max_persons)

# Generate the menu
menu = build_menu(start_date, filtered_recipes)

# Write the menu to menu.txt
with open("menu.txt", "w") as menu_file:
    menu_file.write(menu)
