import requests
from bs4 import BeautifulSoup

def ItemSprite(NameItem, Region = "en"):
    def body(HTMLResult,NameItem):
        wordcheck = None
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
            Result = Data
            Result["Title"] = ItemTitle
            wordcheck = True
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
            wordcheck = False
        if wordcheck == False:
            NameItem = NameItem.lower()
            word = []
            Result2 = {}
            for item in Result.keys():
                if NameItem in item.lower():
                    word.append(item)
            for item2 in word:
                Result2[item2] = Result[item2]
            if len(Result2) == 1:
                for item3 in Result2.keys():
                    return Result2[item3]
            else:
                return Result2
        elif wordcheck == True:
            return Result
        else:
            return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
    #====================================================================Main Program=============================================================================
    try:
        ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+NameItem).text, "html.parser")
        if ItemPage.select(".gtw-card") == []:
            ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
            try:
                ItemPage = BeautifulSoup(requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"]).text, "html.parser")
            except:
                return {"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"}
        return body(ItemPage,NameItem)
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later","Error Code": "1"})  
