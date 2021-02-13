import argparse
import glob
import simplejson as json
import os
from datetime import date

import requests
from selectorlib import Extractor


argparser = argparse.ArgumentParser(description='Amazon URL Tracker/Scraper')
argparser.add_argument(
    '-url', dest='url', action='store_true', help='Insert a url for scraping')
argparser.add_argument('-search', dest='search', action='store_true',
                       help='Insert a Name and a keyword to search')
args = argparser.parse_args()

if args.url:
    URL = input('insert a url: ')
    todayDate = date.today()
    extractor = Extractor.from_yaml_file('search.yml')
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    headers = {'User-Agent': user_agent}

    r = requests.get(URL, headers=headers)
    array = extractor.extract(r.text)
    nameFile = 'data' + (todayDate.strftime('%d%m%Y')) + '.json'
    with open(nameFile, 'w') as outfile:
        json.dump(array, outfile, sort_keys=True, indent=4)
    pass


if args.search:
    name = input('Name of Product: ')
    value = input('What do you want to search?')
    os.chdir(".")
    for file in glob.glob("*.json"):
        print(file)
        data_input = json.loads(file)
        sale_price = 0
        i = 0
        if name == data_input['name']:
            parameter_found = data_input[value]
            print(parameter_found)
            if value == 'sale_price':
                i += 1
                sale_price += parameter_found
        sale_price = sale_price / i
        print(sale_price)

'''
with open(nameFile) as fileInput:
    data = json.load(fileInput)
'''
