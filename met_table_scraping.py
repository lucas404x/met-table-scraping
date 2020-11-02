import json
import requests
from bs4 import BeautifulSoup

URL = 'https://golf.procon.org/met-values-for-800-activities/'

html_content = requests.get(URL).content
html_content = BeautifulSoup(html_content, features='html.parser')

# the second value is the correct table
html_content = html_content.find_all('tbody')[1]

# dict object with exercise (key) and METs points (value)
met_values = {}

# extracting the values of html document
for tr in html_content.find_all('tr')[1::]:
    td = tr.find_all('td')[1::]
    met_values[td[0].string] = td[1].string

# Making a json file with these info
with open('met_values.json', mode='w') as fp:
    json.dump(met_values, fp, ensure_ascii=False)
