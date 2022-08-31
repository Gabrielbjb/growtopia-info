import requests
from bs4 import BeautifulSoup

Result = {}
try:
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
        ItemPage = requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"]))
    except:
        print("It looks like we can't reach fandom.com")
    HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
    Properties = HTMLResult.find_all('div',  class_= "card-text")
    Data = HTMLResult.find('table', class_= "card-field")
    Rarity = BeautifulSoup((str((HTMLResult.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
    try:
        Result.update({"Rarity": int(Rarity)})
    except:
        Result.update({"Rarity": "None"})

    PropertiesResult = []
    for add in Properties:
        hum = BeautifulSoup(str(add).replace("<br/>", "\n"), "html.parser")
        PropertiesResult.append(((hum)).text)
    Result.update({"Description": PropertiesResult[0].strip()})
    Result.update({"Properties": PropertiesResult[1].strip()})

    DataResult = []
    for typ in Data:
        mus = BeautifulSoup((str(typ).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
        DataResult = (((mus.text).split(",")))

    res = 0 
    while res <= (len(DataResult)-3):
        Result.update({DataResult[res].strip(): DataResult[res+1].strip()})
        res = res+2
except:
    print("Sorry! I can't find",NameItem,'in Growtopia Fandom")

# All data will be saved to (Result)
