import requests
from bs4 import BeautifulSoup

def parse_html_result(html_result, result):
    properties_result = []
    properties = html_result.find_all('div', class_="card-text")
    data_fields = html_result.select(".card-field")
    rarity_text = BeautifulSoup((str((html_result.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
    
    for property in properties:
        parsed_property = BeautifulSoup(str(property).replace("<br/>", "--split--"), "html.parser")
        properties_result.append(parsed_property.text)
    
    properties_list = (properties_result[1].strip()).split("--split--")
    result.update({"Description": properties_result[0].strip()})
    result.update({"Properties": "None" if properties_list == ['None'] else properties_list})
    
    try:
        result.update({"Rarity": int(rarity_text)})
    except:
        result.update({"Rarity": "None"})
    
    data_result = []
    for data_field in data_fields:
        parsed_data = BeautifulSoup((str(data_field).replace("</tr>", ",")).replace("</th>", ","), "html.parser")
        data_result = (((parsed_data.text).split(",")))
    
    index = 0 
    while index <= (len(data_result) - 3):
        result.update({data_result[index].strip().replace(" ", ""): data_result[index + 1].strip()})
        index += 2
    
    check = 0
    for key in result.keys():
        if check == 3:
            result[key] = result[key].split(" - ")
        if check == 8:
            result[key] = result[key].split(" ")
        if check == 7:
            restore = []
            for number in result[key].split(" "):
                digits = ""
                for char in number:
                    if char.isdigit():
                        digits += char
                if digits != "":
                    restore.append(digits)
            result[key] = {
                "Fist": restore[0],
                "Pickaxe": restore[1],
                "Restore": restore[2]
            }
        check += 1

def get_item_data(item_name, region="en"):
    try:
        search_response = requests.get(f"https://growtopia.fandom.com/{region}/api/v1/SearchSuggestions/List?query={item_name}").json()
        try:
            item_page_response = requests.get(f"https://growtopia.fandom.com/{region}/wiki/{search_response['items'][0]['title']}")
            try:
                result = {}
                html_result = BeautifulSoup(item_page_response.text, "html.parser")
                if len(html_result.select(".gtw-card")) == 1:
                    parse_html_result(html_result, result)
                    try:
                        item_title = ((((html_result.find('span', class_="mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                    except:    
                        item_title = (html_result.find('span', class_="mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                    result["Title"] = item_title
                else:
                    for html_result_tabber in html_result.select(".gtw-card"):   
                        tabber_result = {}   
                        parse_html_result(html_result_tabber, tabber_result)
                        try:
                            item_title = ((((html_result_tabber.find('span', class_="mw-headline")).small).decompose()).get_text(strip=True)).replace(u'\xa0', u' ')
                        except:    
                            item_title = (html_result_tabber.find('span', class_="mw-headline").get_text(strip=True)).replace(u'\xa0', u' ')
                        result[item_title] = tabber_result
                        result[item_title]["Title"] = item_title
                try:
                    return result[search_response["items"][0]["title"]]
                except:
                    if item_name in result.keys():
                        return result[item_name]
                    else:
                        return result
            except:
                return {"Error": f"Sorry! I can't find {item_name} in Growtopia Fandom {region} Error Code 3"}            
        except IndexError:
            return {"Error": f"Sorry! I can't find {item_name} in Growtopia Fandom {region} Error Code 2"}
    except:
        return {"Error": f"It looks like we can't reach fandom.com {region}! Try again later. Error Code 1"}

# Example usage
if __name__ == "__main__":
    item = get_item_data("dirt")
    print(item)