import requests
from bs4 import BeautifulSoup

def ItemData(NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        try:
            ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])
            try:
                def checking(Result):
                    check = 0
                    for fix in Result.keys():
                        theresult = Result[fix]
                        if check == 3:
                            Result[fix] = theresult.split(" - ")
                        if check == 8:
                            Result[fix] = theresult.split(" ")
                        if check == 7:
                            restore = []
                            for number in theresult.split(" "):
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
                        if check == 9:
                            time = []
                            growtime = {}
                            for number in theresult.split(" "):
                                input = ""
                                for number2 in number:
                                    if number2.isdigit():
                                        input = input+number2
                                if input != "":
                                    time.append(input)
                            format = ["Month","Week","Day","Hour","Minute","Second"]
                            i = 0
                            while i != len(time):
                                growtime[format[((len(format))-1)-i]] = time[((len(time))-1)-i]
                                i+=1
                            Result[fix] = growtime

                        if check == 10:
                            gems = []
                            if len(theresult.split(" - ")) == 1:
                                gems.append(theresult.split(" - ")[0])
                                gems.append(theresult.split(" - ")[0])
                            else:
                                gems.append(theresult.split(" - ")[0])
                                gems.append(theresult.split(" - ")[1])                        
                            Result[fix] = {
                                    "Max":gems[1],
                                    "Min":gems[0]
                                }                                
                        check +=1
                wordcheck = None
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
                    Result.update({"Description": PropertiesResult[0].strip()})
                    Result.update({"Properties": (PropertiesResult[1].strip()).split("--split--")})
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
                    checking(Result)
                    try:
                        ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    Result["Title"] = ItemTitle
                    wordcheck = True
                elif len(HTMLResult.select(".gtw-card")) > 1:
                    for HTMLResultTabber in HTMLResult.select(".gtw-card"):   
                        Result2 = {}   
                        PropertiesResult = []
                        Properties = HTMLResultTabber.find_all('div',  class_= "card-text")
                        Data = HTMLResultTabber.select(".card-field")
                        Rarity = BeautifulSoup((str((HTMLResultTabber.find('small'))).replace("(Rarity: ","")).replace(")", ""), "html.parser").text
                        for add in Properties:
                            hum = BeautifulSoup(str(add).replace("<br/>", "--split--"), "html.parser")
                            PropertiesResult.append(hum.text)
                        Result2.update({"Description": PropertiesResult[0].strip()})
                        Result2.update({"Properties": (PropertiesResult[1].strip()).split("--split--")})

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
                            Result2.update({DataResult[res].strip(): DataResult[res+1].strip()})
                            res = res+2  
                        checking(Result2)
                        try:
                            ItemTitle = ((((HTMLResultTabber.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                        except:    
                            ItemTitle = (HTMLResultTabber.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                        Result[ItemTitle] = Result2
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
            except:
                return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "3"})            
        except IndexError:
            return({"Error": "Sorry! I can't find "+NameItem+" in Growtopia Fandom "+Region,"Error Code": "2"})
    except:
        return({"Error": "It looks like we can't reach fandom.com "+Region+"! Try again later","Error Code": "1"})
