import requests
from bs4 import BeautifulSoup

try:
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
        sprite = BeautifulSoup(requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"])).text, "html.parser")
    except:
        print("It looks like we can't reach fandom.com")
    images = sprite.find('div', {"class": "card-header"}).img['src'] #result
except:
    print("Sorry! I can't find",NameItem,'in Growtopia Fandom")

#put item name in (NameItem)
