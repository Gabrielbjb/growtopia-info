import requests
from bs4 import BeautifulSoup

def ItemData(NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        try:
            ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])
            try:
                Result = {}
                HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
                if len(HTMLResult.select(".gtw-card")) == 1:
                    Properties = HTMLResult.find_all('div',  class_= "card-text")
                    Data = HTMLResult.select(".card-field")
                    Rarity = BeautifulSoup((str((HTMLResult.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
                    PropertiesResult = []
                    for add in Properties:
                        hum = BeautifulSoup(str(add).replace("<br/>", "--split--"), "html.parser")
                        PropertiesResult.append(hum.text)
                    properties = (PropertiesResult[1].strip()).split("--split--")
                    Result.update({"Description": PropertiesResult[0].strip()})
                    Result.update({"Properties": "None" if properties == ['None'] else properties})

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
                        Result.update({DataResult[res].strip().replace(" ", ""): DataResult[res+1].strip()})
                        res = res+2
                    check = 0
                    for fix in Result.keys():
                        if check == 3:
                            Result[fix] = Result[fix].split(" - ")
                        if check == 8:
                            Result[fix] = Result[fix].split(" ")
                        if check == 7:
                            restore = []
                            for number in Result[fix].split(" "):
                                input = ""
                                for number2 in number:
                                    if number2.isdigit():
                                        input = input+number2
                                if input != "":
                                    restore.append(input)
                            Result[fix] = {
                                    "Fist":restore[0],
                                    "Pickaxe":restore[1],
                                    "Restore":restore[2]
                            }
                        check +=1
                    try:
                        ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    Result["Title"] = ItemTitle
                else:
                    for HTMLResultTabber in HTMLResult.select(".gtw-card"):   
                        Result2 = {}   
                        PropertiesResult = []
                        Properties = HTMLResultTabber.find_all('div',  class_= "card-text")
                        Data = HTMLResultTabber.select(".card-field")
                        Rarity = BeautifulSoup((str((HTMLResultTabber.find('small'))).replace("(Rarity: ","")).replace(")", ""), "html.parser").text
                        for add in Properties:
                            hum = BeautifulSoup(str(add).replace("<br/>", "--split--"), "html.parser")
                            PropertiesResult.append(hum.text)
                        properties = (PropertiesResult[1].strip()).split("--split--")
                        Result2.update({"Description": PropertiesResult[0].strip()})
                        Result2.update({"Properties": "None" if properties == ['None'] else properties})

                        try:
                            Result2.update({"Rarity": int(Rarity)})
                        except:
                            Result2.update({"Rarity": "None"})
                        DataResult = []
                        for typ in Data:
                            mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
                            DataResult = (mus.get_text(" ",strip=True)).split(",")

                        res = 0 
                        while res <= (len(DataResult)-3):
                            Result2.update({DataResult[res].strip().replace(" ", ""): DataResult[res+1].strip()})
                            res = res+2  

                        check = 0
                        for fix in Result2.keys():
                            if check == 3:
                                Result2[fix] = Result2[fix].split(" - ")
                            if check == 8:
                                Result2[fix] = Result2[fix].split(" ")
                            if check == 7:
                                restore = []
                                for number in Result2[fix].split(" "):
                                    input = ""
                                    for number2 in number:
                                        if number2.isdigit():
                                            input = input+number2
                                    if input != "":
                                        restore.append(input)
                                Result2[fix] = {
                                        "Fist":restore[0],
                                        "Pickaxe":restore[1],
                                        "Restore":restore[2]
                                }
                            check +=1
                        try:
                            ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                        except:    
                            ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                        Result[ItemTitle] = Result2
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
