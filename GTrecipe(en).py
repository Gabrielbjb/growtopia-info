import requests
from bs4 import BeautifulSoup

try:
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
        ItemPage = requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"]))
    except:
        print("It looks like we can't reach fandom.com")
    HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
    Recipe = {}
    ws = 0
    wd = len(HTMLResult.select(".content"))
    for item in HTMLResult.select(".content"):
        if wd == ws:
            break
        if item.select(".content") == []:
            if wd == ws:
                break
            Recipe[((item.find('th')).text).strip()] = (str(((BeautifulSoup(((str(item.select('td')).replace("</td>", "space")).replace("</li>", "space")).replace("<span>", "space"), "html.parser").get_text(' ', strip=True)).replace("space", "")).replace("\n", "")).strip())
            ws +=1
        else:
            meh = ((item.find('th')).text).strip()
            Recipe[meh] = {}
            if item.select(".content"):
                wd -= 1
                for mes in item.select(".content"):
                    Recipe[meh][((mes.find('th')).text).strip()] = (str(((BeautifulSoup(((str(mes.select('td')).replace("</td>", "space")).replace("</li>", "space")).replace("</span>", "space"), "html.parser").get_text(' ', strip=True)).replace("space", "")).replace("\n", "")).strip())
                    ws +=1
except:
    print("Sorry! I can't find",NameItem,"in Growtopia Fandom")
          
# All data will be saved to (Recipe)
# Put the item name in (NameItem)
# Growtopia Wiki (id) is still not 100% supported
