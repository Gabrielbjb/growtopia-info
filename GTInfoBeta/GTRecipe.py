import requests
from bs4 import BeautifulSoup

try:
    ItemFinder = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={NameItem}").json()
    ItemPage = requests.get("https://growtopia.fandom.com/wiki/{}".format(ItemFinder["items"][0]["title"]))
    try:
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
                        if ((item.find('th')).text).strip() in Recipe.keys():
                            Recipe[((item.find('th')).text).strip()].append([])
                            for meh in item.select('td'):
                                meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                                Recipe[((item.find('th')).text).strip()][1].append(meh.replace(u'\xa0', u''))                 
                        else:
                            Recipe[((item.find('th')).text).strip()] = [[]]
                            for meh in item.select('td'):
                                meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                                Recipe[((item.find('th')).text).strip()][0].append(meh.replace(u'\xa0', u'')) 
                    ws += 1
                else:
                    meh = ((item.find('th')).text).strip()
                    Recipe[meh] = {}
                    for mes in item.select(".content"):
                        if ((mes.find('th')).text).strip() in Recipe[meh].keys():
                            Recipe[meh][((mes.find('th')).text).strip()].append([])
                            for the in mes.select('td'):
                                the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                                Recipe[meh][((mes.find('th')).text).strip()][1].append(the.replace(u'\xa0', u''))                    
                        else:
                            Recipe[meh][((mes.find('th')).text).strip()] = [[]]
                            for the in mes.select('td'):
                                the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                                Recipe[meh][((mes.find('th')).text).strip()][0].append(the.replace(u'\xa0', u'')) 
                        ws += 1
                        require.append(ws)
                count +=1
            try:
                ItemTitle = ((((HTMLResult.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
            except:    
                ItemTitle = (HTMLResult.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
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
                                if ((item.find('th')).text).strip() in Recipe.keys():
                                    Recipe[((item.find('th')).text).strip()].append([])
                                    for meh in item.select('td'):
                                        meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[((item.find('th')).text).strip()][1].append(meh.replace(u'\xa0', u''))                   
                                else:
                                    Recipe[((item.find('th')).text).strip()] = [[]]
                                    for meh in item.select('td'):
                                        meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[((item.find('th')).text).strip()][0].append(meh.replace(u'\xa0', u'')) 
                            ws += 1
                        else:
                            meh = ((item.find('th')).text).strip()
                            Recipe[meh] = {}
                            for mes in item.select(".content"):
                                if ((mes.find('th')).text).strip() in Recipe[meh].keys():
                                    Recipe[meh][((mes.find('th')).text).strip()].append([])
                                    for the in mes.select('td'):
                                        the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[meh][((mes.find('th')).text).strip()][1].append(the.replace(u'\xa0', u''))                  
                                else:
                                    Recipe[meh][((mes.find('th')).text).strip()] = [[]]
                                    for the in mes.select('td'):
                                        the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[meh][((mes.find('th')).text).strip()][0].append(the.replace(u'\xa0', u'')) 
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
                                if ((item.find('th')).text).strip() in Recipe.keys():
                                    Recipe[((item.find('th')).text).strip()].append([])
                                    for meh in item.select('td'):
                                        meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[((item.find('th')).text).strip()][1].append(meh.replace(u'\xa0', u''))             
                                else:
                                    Recipe[((item.find('th')).text).strip()] = [[]]
                                    for meh in item.select('td'):
                                        meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[((item.find('th')).text).strip()][0].append(meh.replace(u'\xa0', u'')) 
                            ws += 1
                        else:
                            meh = ((item.find('th')).text).strip()
                            Recipe[meh] = {}
                            for mes in item.select(".content"):
                                if ((mes.find('th')).text).strip() in Recipe[meh].keys():
                                    Recipe[meh][((mes.find('th')).text).strip()].append([])
                                    for the in mes.select('td'):
                                        the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[meh][((mes.find('th')).text).strip()][1].append(the.replace(u'\xa0', u''))                    
                                else:
                                    Recipe[meh][((mes.find('th')).text).strip()] = [[]]
                                    for the in mes.select('td'):
                                        the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                                        Recipe[meh][((mes.find('th')).text).strip()][0].append(the.replace(u'\xa0', u'')) 
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
except:
    print("It looks like we can't reach fandom.com")

