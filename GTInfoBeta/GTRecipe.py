import requests
from bs4 import BeautifulSoup

try:
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
        ItemPage = requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"]))
    except:
        print("It looks like we can't reach fandom.com")
        exit()
    HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
    require = []
    Item = {}
    if HTMLResult.select(".wds-tab__content") == []:
            ws = 0
            count = 0
            Recipe = {}
            for item in HTMLResult.select(".content"):
                if item.select(".content") == []:
                    if not count in require: 
                        Recipe[((item.find('th')).text).strip()] = (str(((BeautifulSoup(((str(item.select('td')).replace("</td>","space")).replace("</li>","space")).replace("<span>","space"), "html.parser").get_text(' ', strip=True)).replace("space","")).replace("\n","")).strip()).replace(u'\xa0', u' ')
                    ws += 1
                else:
                    meh = ((item.find('th')).text).strip()
                    Recipe[meh] = {}
                    for mes in item.select(".content"):
                        Recipe[meh][((mes.find('th')).text).strip()] = (str(((BeautifulSoup(((str(mes.select('td')).replace("</td>", "space")).replace("</li>","space")).replace("</span>","space"), "html.parser").get_text(' ', strip=True)).replace("space", "")).replace("\n","")).strip()).replace(u'\xa0', u' ')
                        ws += 1
                        require.append(ws)
                count +=1
            try:
                ItemTitle = ((((itemish.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
            except:    
                ItemTitle = (itemish.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
            Item[ItemTitle] = Recipe
    else:
        for itemish in HTMLResult.select(".wds-tab__content"):
            ws = 0
            count = 0
            Recipe = {}
            if itemish.select(".content") == []:
                for item in HTMLResult.select(".content"):
                    if item.select(".content") == []:
                        if not count in require: 
                            Recipe[((item.find('th')).text).strip()] = (str(((BeautifulSoup(((str(item.select('td')).replace("</td>","space")).replace("</li>","space")).replace("<span>","space"), "html.parser").get_text(' ', strip=True)).replace("space","")).replace("\n","")).strip()).replace(u'\xa0', u' ')
                        ws += 1
                    else:
                        meh = ((item.find('th')).text).strip()
                        Recipe[meh] = {}
                        for mes in item.select(".content"):
                            Recipe[meh][((mes.find('th')).text).strip()] = (str(((BeautifulSoup(((str(mes.select('td')).replace("</td>","space")).replace("</li>","space")).replace("</span>","space"), "html.parser").get_text(' ', strip=True)).replace("space","")).replace("\n","")).strip()).replace(u'\xa0', u' ')
                            ws += 1
                            require.append(ws)
                    count +=1
                try:
                    ItemTitle = ((((itemish.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                except:    
                    ItemTitle = (itemish.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                Item[ItemTitle] = Recipe
            else:
                for item in itemish.select(".content"):
                    if item.select(".content") == []:
                        if not count in require: 
                            Recipe[((item.find('th')).text).strip()] = (str(((BeautifulSoup(((str(item.select('td')).replace("</td>","space")).replace("</li>","space")).replace("<span>","space"), "html.parser").get_text(' ', strip=True)).replace("space","")).replace("\n","")).strip()).replace(u'\xa0', u' ')
                        ws += 1
                    else:
                        meh = ((item.find('th')).text).strip()
                        Recipe[meh] = {}
                        for mes in item.select(".content"):
                            Recipe[meh][((mes.find('th')).text).strip()] = (str(((BeautifulSoup(((str(mes.select('td')).replace("</td>","space")).replace("</li>","space")).replace("</span>","space"), "html.parser").get_text(' ', strip=True)).replace("space","")).replace("\n","")).strip()).replace(u'\xa0', u' ')
                            ws += 1
                            require.append(ws)
                    count +=1
                try:
                    ItemTitle = ((((itemish.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                except:    
                    ItemTitle = (itemish.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                Item[ItemTitle] = Recipe
except:
    print("Sorry! I can't find",NameItem,"in Growtopia Fandom")
