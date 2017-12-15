#!/usr/bin/env python3
'''Translate JSON text into Python data structures.  
 Get Video information from Youtube

 Prints the titles of the first six top rated videos
'''
import json 
from urllib.request import urlopen

url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = urlopen(url) # Connect to the webserver
contents = response.read()
text = contents.decode('utf8') # decode to a text string in json format
data = json.loads(text) # convert to object(data structure)

for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])