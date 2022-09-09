import requests
from bs4 import BeautifulSoup

try:
    ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
    HTMLResult = BeautifulSoup(requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"])).text, "html.parser")
    try:
        Data = {}  
        if HTMLResult.select(".wds-tab__content") == []:
            Data = {
                "Item" :"",
                "Tree" :"",
                "Seed" :""
            }  
            images = HTMLResult.find('div', {"class": "gtw-card"})
            Data["Item"]= (images.find('div', {"class": "card-header"})).img['src']
            Data["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
            Data["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
        else:
            for HTMLResultTabber in HTMLResult.select(".wds-tab__content"):
                Data2 = {
                    "Item" :"",
                    "Tree" :"",
                    "Seed" :""
                }  
                images = HTMLResultTabber.find('div', {"class": "gtw-card"})
                Data2["Item"]= (images.find('div', {"class": "card-header"})).img['src']
                Data2["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
                Data2["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
                try:
                    ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                except:    
                    ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                Data[ItemTitle] = Data2
    except:
        print("Sorry! I can't find",NameItem,"in Growtopia Fandom")
except:
    print("It looks like we can't reach fandom.com") 
