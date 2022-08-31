import requests
from bs4 import BeautifulSoup

ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
ItemPage = requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"]))
HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
Properties = {}
ws = 0
wd = len(HTMLResult.select(".content"))
for item in HTMLResult.select(".content"):
    if wd == ws:
        break
    if item.select(".content") == []:
        if wd == ws:
            break
        Properties[((item.find('th')).text).strip()] = (str(((BeautifulSoup(((str(item.select('td')).replace("</td>", "space")).replace("</li>", "space")).replace("<span>", "space"), "html.parser").get_text(' ', strip=True)).replace("space", "")).replace("\n", "")).strip())
        ws +=1
    else:
        meh = ((item.find('th')).text).strip()
        Properties[meh] = {}
        if item.select(".content"):
            wd -= 1
            for mes in item.select(".content"):
                Properties[meh][((mes.find('th')).text).strip()] = (str(((BeautifulSoup(((str(mes.select('td')).replace("</td>", "space")).replace("</li>", "space")).replace("</span>", "space"), "html.parser").get_text(' ', strip=True)).replace("space", "")).replace("\n", "")).strip())
                ws +=1