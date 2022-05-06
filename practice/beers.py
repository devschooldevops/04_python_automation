#!/bin/python3

import requests, json

url = "https://api.punkapi.com/v2/beers"

response = requests.request("GET", url)

# this is of list type
list_of_beers_recipies = json.loads(response.text)

ph_for_beer = {}

for recipie in list_of_beers_recipies:
	if "name" in recipie and "ph" in recipie and recipie["ph"] is not None:
		ph_for_beer[recipie["name"]] = recipie["ph"]


sorted_by_ph = {}
names_list_sorted_by_ph = sorted(ph_for_beer, key=ph_for_beer.get)

for name in names_list_sorted_by_ph:
	sorted_by_ph[name] = ph_for_beer[name]

print ("name = " + list(sorted_by_ph.keys())[0]  + " ph = " + str(sorted_by_ph[list(sorted_by_ph.keys())[0]]))
print ("name = " + list(sorted_by_ph.keys())[-1]  + " ph = " + str(sorted_by_ph[list(sorted_by_ph.keys())[-1]]))
