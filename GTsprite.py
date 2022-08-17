import requests
from bs4 import BeautifulSoup
import json

try:
    soup = BeautifulSoup(requests.get("https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={}".format(NameItem)).text, "html.parser")
    soup2 =  json.loads(str(soup))
    soup = BeautifulSoup(requests.get("https://growtopia.fandom.com/wiki/{}".format(soup2["items"][0]["title"])).text, "html.parser")
    images = soup.find('div', {"class": "card-header"}).img['src']
    print(images)
except:
    print("Sorry! I can't",NameItem,'in Growtopia Fandom')
