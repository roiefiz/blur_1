import re
import json
from time import sleep
from DrissionPage import ChromiumPage, ChromiumOptions


# URLs


def scrape_collection_tokens(collection):
    """
    :param collection:
    :return: listed tokens
    """
    # Sketch to scrape a collection from blur , all listed tokens
    tokens_sketch = f"https://core-api.prod.blur.io/v1/collections/{collection}/tokens?filters=%7B%22traits%22%3A%5B%5D%2C%22hasAsks%22%3Atrue%7D"
    tokens_sketch = "https://core-api.prod.blur.io/v1/collections/pixels-farm/tokens?filters=%7B%22traits%22%3A%5B%5D%2C%22hasAsks%22%3Atrue%7D"
    # Use DrissionPage to extract the raw data from the website
    p = ChromiumPage()
    p.get(f"{tokens_sketch}")
    data = p.json
    p.quit()

    # Access the 'tokens' list
    tokens = data['tokens']

    # Print the tokens list to verify
    for token in tokens:
        print(token)
    return tokens


def scrape_collection_general_details(collection):
    """
    :param collection:
    :return: collection general details
    """
    # Sketch to scrape a collection from blur , all listed tokens
    collection_general_sketch = f"https://core-api.prod.blur.io/v1/collections/{collection}"
    # Use DrissionPage to extract the raw data from the website
    p = ChromiumPage()
    p.get(f"{collection_general_sketch}")
    data = p.json
    p.quit()
    # Parse the JSON data
    print(data['collection'])
    return data['collection']


def send_alert(message):
    pass


def open_webpage(url: str):
    p = ChromiumPage()
    p.get(f"{url}")
    p._find_elements()
    input("shalom")
    data = p.json
    p.quit()


pixels_all_traits_dic = {1: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 2: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 3: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 4: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Large', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 5: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 6: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Environment': 'Land'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 7: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 8: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 9: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Environment': 'Land'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 10: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Windmill': 'Yes', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 11: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Water'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 12: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 13: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 14: {
    'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 15: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small',
               'Environment': 'Land', 'Tree Density': 'Dense'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 16: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Windmill': 'Yes',
               'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 17: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 18: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 19: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Land'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 20: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Land'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 21: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Land'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 22: {
    'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 23: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small',
               'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 24: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 25: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Environment': 'Water'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 26: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 27: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Large', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 28: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small',
               'Environment': 'Land'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 29: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Environment': 'Land',
               'Tree Density': 'Dense'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 30: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small',
               'Environment': 'Water'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 31: {
    'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 32: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Windmill': 'Yes', 'Environment': 'Water'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 33: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small',
               'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 34: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Environment': 'Water',
               'Tree Density': 'Dense'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 35: {
    'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Windmill': 'Yes', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 36: {
    'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Windmill': 'Yes', 'Environment': 'Land'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 37: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Environment': 'Water',
               'Tree Density': 'Dense'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 38: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 39: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Large',
               'Environment': 'Land'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 40: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Environment': 'Land',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 41: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Environment': 'Water', 'Tree Density': 'Dense'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 42: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Environment': 'Water',
               'Tree Density': 'Dense'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 43: {
    'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 44: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 45: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 46: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Windmill': 'Yes',
               'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 47: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 48: {
    'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Environment': 'Water', 'Tree Density': 'Dense'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 49: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Large', 'Windmill': 'Yes',
               'Environment': 'Land', 'Tree Density': 'Dense'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 50: {
    'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Environment': 'Land', 'Tree Density': 'Dense'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 51: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 52: {
    'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Water', 'Tree Density': 'Dense'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 53: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Environment': 'Water',
               'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 54: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Land', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 55: {
    'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
               'Environment': 'Water', 'Tree Density': 'Light'},
    'lowest_price': {'price': 100000000, 'token_id': 20000000},
    'second_lowest': {'price': 100000000, 'token_id': 20000000}},
                         56: {'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Environment': 'Land'},
                              'lowest_price': {'price': 100000000, 'token_id': 20000000},
                              'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 57: {
        'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Large',
                   'Windmill': 'Yes', 'Environment': 'Land', 'Tree Density': 'Light'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 58: {
        'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Small', 'Windmill': 'Yes',
                   'Environment': 'Land', 'Tree Density': 'Light'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}},
                         59: {'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Environment': 'Land'},
                              'lowest_price': {'price': 100000000, 'token_id': 20000000},
                              'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 60: {
        'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small',
                   'Environment': 'Water', 'Tree Density': 'Dense'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 61: {
        'traits': {'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Small', 'House': 'Large', 'Windmill': 'Yes',
                   'Environment': 'Land', 'Tree Density': 'Dense'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 62: {
        'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Windmill': 'Yes', 'Environment': 'Land',
                   'Tree Density': 'Light'}, 'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 63: {
        'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Large',
                   'Environment': 'Land', 'Tree Density': 'Light'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 64: {
        'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Windmill': 'Yes',
                   'Environment': 'Water', 'Tree Density': 'Light'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 65: {
        'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Small', 'House': 'Large', 'Environment': 'Land'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}},
                         66: {'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Environment': 'Water'},
                              'lowest_price': {'price': 100000000, 'token_id': 20000000},
                              'second_lowest': {'price': 100000000, 'token_id': 20000000}},
                         67: {'traits': {'Land': 'Standard', 'Size': 'Small', 'House': 'Small', 'Environment': 'Land'},
                              'lowest_price': {'price': 100000000, 'token_id': 20000000},
                              'second_lowest': {'price': 100000000, 'token_id': 20000000}},
                         68: {'traits': {'Land': 'Standard', 'Size': 'Large', 'House': 'Large', 'Environment': 'Water'},
                              'lowest_price': {'price': 100000000, 'token_id': 20000000},
                              'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 69: {
        'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Size': 'Large', 'House': 'Small', 'Windmill': 'Yes',
                   'Environment': 'Water', 'Tree Density': 'Light'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}, 70: {
        'traits': {'Coop': 'Yes', 'Land': 'Standard', 'Silo': 'Yes', 'Size': 'Large', 'House': 'Small',
                   'Windmill': 'Yes', 'Environment': 'Water', 'Tree Density': 'Light'},
        'lowest_price': {'price': 100000000, 'token_id': 20000000},
        'second_lowest': {'price': 100000000, 'token_id': 20000000}}}


