from bs4 import BeautifulSoup

def parse_html_content(html_content: BeautifulSoup, result: dict):
    properties_result = []
    properties = html_content.find_all('div', class_="card-text")
    data_fields = html_content.select(".card-field")

    rarity_text = BeautifulSoup((str((html_content.find('small'))).replace("(Rarity: ", "")).replace(")", ""), "html.parser").text
    try: result.update({"Rarity": int(rarity_text)})
    except: result.update({"Rarity": "None"})
    
    for property in properties:
        parsed_property = BeautifulSoup(str(property).replace("<br/>", "--split--"), "html.parser")
        properties_result.append(parsed_property.text)
    properties_list = (properties_result[1].strip()).split("--split--")
    result.update({"Description": properties_result[0].strip()})
    result.update({"Properties": "None" if properties_list == ['None'] else properties_list})
        
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
    
    result["Sprite"] = get_item_sprites(html_content)

def get_item_sprites(html_content: BeautifulSoup) -> dict:
    return {
        "Item": html_content.select_one('div.card-header img')['src'],
        "Tree": html_content.select_one('th:-soup-contains("Grow Time") + td img')['src'],
        "Seed": html_content.select_one('td.seedColor img')['src']
    }

# Used to get tabber title
def get_item_title(html_content: BeautifulSoup) -> str:
    title_tag = html_content.find('span', class_="mw-headline")
    try: title_tag.small.decompose()
    except AttributeError: pass
    return title_tag.get_text(strip=True).replace(u'\xa0', u' ')
