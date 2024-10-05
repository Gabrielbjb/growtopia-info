import requests
from bs4 import BeautifulSoup

def parse_html_result(html_result: BeautifulSoup, result: dict):
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
    
    for i in range(0, len(data_result) - 2, 2):
        key = data_result[i].strip().replace(" ", "")
        value = data_result[i + 1].strip()
        result[key] = value

    for idx, (key, value) in enumerate(result.items()):
        if idx == 3:
            result[key] = value.split(" - ")
        elif idx == 8:
            result[key] = value.split(" ")
        elif idx == 7:
            digits_list = ["".join(filter(str.isdigit, part)) for part in value.split(" ") if any(char.isdigit() for char in part)]
            result[key] = {
                "Fist": digits_list[0] if len(digits_list) > 0 else None,
                "Pickaxe": digits_list[1] if len(digits_list) > 1 else None,
                "Restore": digits_list[2] if len(digits_list) > 2 else None
            }

def get_item_title(html_result: BeautifulSoup) -> str:
    title_tag = html_result.find('span', class_="mw-headline")
    try: title_tag.small.decompose()
    except AttributeError: pass
    return title_tag.get_text(strip=True).replace(u'\xa0', u' ')
    
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
                    result["Title"] = get_item_title(html_result)
                else:
                    for html_result_tabber in html_result.select(".gtw-card"):   
                        tabber_result = {}   
                        parse_html_result(html_result_tabber, tabber_result)
                        item_title = get_item_title(html_result_tabber)
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
    item = get_item_data("ancestral tesseract")
    print(item)