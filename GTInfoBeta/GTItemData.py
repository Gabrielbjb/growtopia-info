from unittest import result
import requests
from bs4 import BeautifulSoup

NameItem= "User:Gabrielbjb/Sandbox"
ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
ItemPage = requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"]))
Result = {}
HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
if HTMLResult.select(".wds-tab__content") == []:
        Properties = HTMLResult.find_all('div',  class_= "card-text")
        Data = HTMLResult.select(".wds-tab__content")
        Rarity = BeautifulSoup((str((HTMLResult.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
        PropertiesResult = []
        for add in Properties:
            hum = BeautifulSoup(str(add).replace("<br/>", "\n"), "html.parser")
            PropertiesResult.append(((hum)).text)
        Result.update({"Description": PropertiesResult[0].strip()})
        Result.update({(HTMLResult.find('b', class_= "card-title").get_text(strip=True)).replace(u'\xa0', u' '): PropertiesResult[1].strip()})
        try:
            Result.update({"Rarity": int(Rarity)})
        except:
            Result.update({"Rarity": "None"})
        DataResult = []
        for typ in Data:
            mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
            DataResult = (((mus.text).split(",")))
        res = 0 
        while res <= (len(DataResult)-3):
            Result.update({DataResult[res].strip(): DataResult[res+1].strip()})
            res = res+2
else:
        Result = {}
        for HTMLResultTabber in HTMLResult.select(".wds-tab__content"):   
                Result2 = {}   
                Properties = HTMLResult.find_all('div',  class_= "card-text")
                Data = HTMLResultTabber.select(".wds-tab__content")
                Rarity = BeautifulSoup((str((HTMLResultTabber.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
                PropertiesResult = []
                for add in Properties:
                    hum = BeautifulSoup(str(add).replace("<br/>", "\n"), "html.parser")
                    PropertiesResult.append(((hum)).text)
                Result2.update({"Description": PropertiesResult[0].strip()})
                Result2.update({"Properties": PropertiesResult[1].strip()})
                try:
                    Result2.update({"Rarity": int(Rarity)})
                except:
                    Result2.update({"Rarity": "None"})
                DataResult = []
                for typ in Data:
                    mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
                    DataResult = (((mus.text).split(",")))
                res = 0 
                while res <= (len(DataResult)-3):
                    Result2.update({DataResult[res].strip(): DataResult[res+1].strip()})
                    res = res+2  
                try:
                    ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                except:    
                    ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                Result[ItemTitle] = Result2
print(Result)
