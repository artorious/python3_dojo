#!/usr/bin/env python3
'''Translate JSON text into Python data structures.  
 Get Video information from Youtube

 Prints the titles of the first six top rated videos
'''

import requests

url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = requests.get(url) # Connect to the webserver
data = response.json()

for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])