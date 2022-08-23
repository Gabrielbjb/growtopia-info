import requests
from bs4 import BeautifulSoup

NameItem = "Dirt"
try:
    ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
    sprite = BeautifulSoup(requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"])).text, "html.parser")
    images = sprite.find('div', {"class": "card-header"}).img['src'] #result
except:
    print("Sorry! I can't find",NameItem,'in Growtopia Fandom')
