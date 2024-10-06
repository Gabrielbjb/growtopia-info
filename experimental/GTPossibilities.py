def Possibilities(self, NameItem, Region = "en"):
    try:
        ItemFinder = requests.get(f"https://growtopia.fandom.com/"+Region+"/api/v1/SearchSuggestions/List?query="+NameItem).json()
        ItemPage = requests.get("https://growtopia.fandom.com/"+Region+"/"+"wiki/"+ItemFinder["items"][0]["title"])

        HTMLResult = BeautifulSoup(ItemPage.text, "html.parser")
        try:
            table = HTMLResult.find("h2").find_next("h3").find_next("table")
            for row in table.find_all('tr')[1:]:
                item_cell = row.find('td').find('a').text.replace(u'\xa0', '').replace(u'\n', '')
        except:
            table = HTMLResult.find("h2").find_next("h2").find_next("h3").find_next("h3").find_next("h3").find_next("table")
            if NameItem.lower() == "cutting board":
                table = HTMLResult.find("h2").find_next("h3").find_next("table").find_next("table")
        
        try:
            for row in table.find_all('tr')[1:]:
                item_cell = row.find('td').find('a').text.replace(u'\xa0', '').replace(u'\n', '')
        except:
            return None

        output = []

        for row in table.find_all('tr')[1:]:
            #print(row)
            # TODO: to anyone reading this, args and kwargs may be really helpful here c:
            item_cell = row.find('td').find('a').text.replace(u'\xa0', '').replace(u'\n', '')
            if "splicing" in row.find('td').find_next('td').text:
                recipe_cell = row.find('td').find_next('td').text.split('•')[1].replace(u'\xa0', '').replace(u'\n', '')
            elif "combining" in row.find('td').find_next('td').text:
                recipe_cell = row.find('td').find_next('td').text.split('combining:')[1].replace(u'\xa0', '').replace(u'\n', '').replace(".", "")                
            #elif "harmonic" in row.find('td').find_next('td').text: # or cooking here
            #    recipe
            elif "sliced" in row.find('td').find_next('td').text:
                recipe_cell = row.find('td').find_next('td').text.split('•')[1].replace(u'\xa0', '').replace(u'\n', '').replace(".", "")
                numbers = re.findall(r'\d+', row.find('td').find_next('td').text)                    
                recipe_cell = f"{numbers[0]}x {recipe_cell}"
            elif "burnt" in row.find('td').find_next('td').text:
                recipe_cell = row.find('td').find_next('td').text.split('•')[1].replace(u'\xa0', '').replace(u'\n', '').replace(".", "").replace(")", ") ")
            elif "chance to be dropped from breaking" in row.find('td').find_next('td').text:
                recipe_cell = row.find('td').find_next('td').text.split(':')[1].replace(u'\xa0', '').replace(u'\n', '').replace(".", "")                                        
                recipe_cell = f"Chance to drop from breaking: {recipe_cell}"
            elif "grinding" in row.find('td').find_next('td').text:
                recipe_cell = row.find('td').find_next('td').text.split(':')[1].replace(u'\xa0', '').replace(u'\n', '').replace(".", "")
            else:
                recipe_cell = None

            #recipe_cell = row.find('td').find_next('td').text.split('•')[1].replace(u'\xa0', '').replace(u'\n', '')
            #output += {item_cell} : {recipe_cell}
            #output[item_cell] = recipe_cell.split("+")
          
            # NOTE: the output is altered to Shiina's presentation of outputs, if you would like other forms of presentation, change the below statement

            if recipe_cell is not None:
                output += [f"- **[{item_cell}]({self.GetLink(item_cell)})** = {recipe_cell}"]

        return output
    except Exception as e:
        print(e)