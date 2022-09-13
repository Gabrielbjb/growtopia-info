def ItemRecipe(NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        try:
            ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])
            try:
                HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
                require = []
                Result = {}
                def Insert(this,Recipe):
                    if this in Recipe.keys():
                        Recipe[this].append([])
                        for meh in item.select('td'):
                            meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[this][1].append(meh.replace(u'\xa0', u''))                 
                    else:
                        Recipe[this] = [[]]
                        for meh in item.select('td'):
                            meh = ((meh.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[this][0].append(meh.replace(u'\xa0', u'')) 

                def Insert2(this,Recipe):
                    if this in Recipe[meh].keys():
                        Recipe[meh][this].append([])
                        for the in mes.select('td'):
                            the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[meh][this][1].append(the.replace(u'\xa0', u''))                    
                    else:
                        Recipe[meh][this] = [[]]
                        for the in mes.select('td'):
                            the = ((the.get_text(' ',strip=True)).replace('"',"'"))
                            Recipe[meh][this][0].append(the.replace(u'\xa0', u'')) 

                def Title(itemish):
                    try:
                        ItemTitle = ((((itemish.find('span', class_= "mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        ItemTitle = (itemish.find('span', class_= "mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    return ItemTitle
                if Region == "id":
                    ind = HTMLResult.select_one(".tabber.wds-tabber")
                    if len(HTMLResult.select(".gtw-card")) == 1:
                        ws = 0
                        count = 0
                        Recipe = {}
                        for item in HTMLResult.select(".content"):
                            if item.select(".content") == []:
                                if not count in require:
                                    Insert(((item.find('th')).text).strip(), Recipe)
                                ws += 1
                            else:
                                meh = ((item.find('th')).text).strip()
                                Recipe[meh] = {}
                                for mes in item.select(".content"):
                                    Insert2(((mes.find('th')).text).strip(), Recipe)
                                    ws += 1
                                    require.append(ws)
                            count +=1
                        Result[Title(HTMLResult)] = Recipe
                        Result[Title(HTMLResult)]["Title"] = ItemFinder["items"][0]["title"]
                    else:
                        for itemish in ind.select(".wds-tab__content"):
                            ws = 0
                            count = 0
                            Recipe = {}
                            if itemish.select(".content") == []:
                                for item in HTMLResult.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe)
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe)
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
                            else:
                                for item in itemish.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe) 
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe) 
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
                else:
                    if HTMLResult.select(".wds-tab__content") == []:
                        ws = 0
                        count = 0
                        Recipe = {}
                        for item in HTMLResult.select(".content"):
                            if item.select(".content") == []:
                                if not count in require:
                                    Insert(((item.find('th')).text).strip(), Recipe)
                                ws += 1
                            else:
                                meh = ((item.find('th')).text).strip()
                                Recipe[meh] = {}
                                for mes in item.select(".content"):
                                    Insert2(((mes.find('th')).text).strip(), Recipe)
                                    ws += 1
                                    require.append(ws)
                            count +=1
                        Result[Title(HTMLResult)] = Recipe
                        Result[Title(HTMLResult)]["Title"] = ItemFinder["items"][0]["title"]
                    else:
                        for itemish in HTMLResult.select(".wds-tab__content"):
                            ws = 0
                            count = 0
                            Recipe = {}
                            if itemish.select(".content") == []:
                                for item in HTMLResult.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe)
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe)
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
                            else:
                                for item in itemish.select(".content"):
                                    if item.select(".content") == []:
                                        if not count in require: 
                                            Insert(((item.find('th')).text).strip(), Recipe) 
                                        ws += 1
                                    else:
                                        meh = ((item.find('th')).text).strip()
                                        Recipe[meh] = {}
                                        for mes in item.select(".content"):
                                            Insert2(((mes.find('th')).text).strip(), Recipe) 
                                            ws += 1
                                            require.append(ws)
                                    count +=1
                                Result[Title(itemish)] = Recipe
                                Result[Title(itemish)]["Title"] = ItemFinder["items"][0]["title"]
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
