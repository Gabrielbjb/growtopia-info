import requests
from bs4 import BeautifulSoup
import json

try:
    ItemFinder = BeautifulSoup(requests.get("https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={}".format(NameItem)).text, "html.parser")
    Item =  json.loads(str(ItemFinder))
    sprite = BeautifulSoup(requests.get("https://growtopia.fandom.com/wiki/{}".format(Item["items"][0]["title"])).text, "html.parser")
    images = sprite.find('div', {"class": "card-header"}).img['src'] #result
except:
    print("Sorry! I can't",NameItem,'in Growtopia Fandom')
