import requests
from bs4 import BeautifulSoup

def ItemSprite(NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        try:
            ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])
            try:
                HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
                Result = {}  
                if len(HTMLResult.select(".gtw-card")) == 1:
                    Data = {
                        "Item" :"",
                        "Tree" :"",
                        "Seed" :""
                    }  
                    images = HTMLResult.find('div', {"class": "gtw-card"})
                    Data["Item"]= (images.find('div', {"class": "card-header"})).img['src']
                    Data["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
                    Data["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
                    try:
                        ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    Result[ItemTitle] = Data
                    Result[ItemTitle]["Title"] = ItemTitle
                else:
                    for HTMLResultTabber in HTMLResult.select(".wds-tab__content"):
                        Data = {
                            "Item" :"",
                            "Tree" :"",
                            "Seed" :""
                        }  
                        images = HTMLResultTabber.find('div', {"class": "gtw-card"})
                        Data["Item"]= (images.find('div', {"class": "card-header"})).img['src']
                        Data["Tree"] = (((((((images.find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).find_next('td')).img['src']
                        Data["Seed"] = (images.find('td', {"class": "seedColor"})).img['src']
                        try:
                            ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                        except:    
                            ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                        Result[ItemTitle] = Data
                        Result[ItemTitle]["Title"] = ItemTitle
                try:
                    return Result[ItemFinder["items"][0]["title"]]
                except:
                    if NameItem in Result.keys():
                        return Result[NameItem]
                    else:
                        return Result
            except:
                return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 3"})            
        except IndexError:
            return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region+" Error Code 2"})
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later. Error Code 1"})
