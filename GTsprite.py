import requests
from bs4 import BeautifulSoup

def get_item_sprite(item_name, region="en"):
    try:
        search_response = requests.get(f"https://growtopia.fandom.com/{region}/api/v1/SearchSuggestions/List?query={item_name}").json()
        try:
            item_page_response = requests.get(f"https://growtopia.fandom.com/{region}/wiki/{search_response['items'][0]['title']}")
            try:
                html_content = BeautifulSoup(item_page_response.text, "html.parser")
                result = {}
                if len(html_content.select(".gtw-card")) == 1:
                    sprite = {
                        "Item": "",
                        "Tree": "",
                        "Seed": ""
                    }
                    images = html_content.find('div', {"class": "gtw-card"})
                    sprite["Item"] = images.find('div', {"class": "card-header"}).img['src']
                    sprite["Tree"] = images.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').img['src']
                    sprite["Seed"] = images.find('td', {"class": "seedColor"}).img['src']
                    try:
                        item_title = html_content.find('span', class_="mw-headline").small.decompose().get_text(strip=True).replace(u'\xa0', u' ')
                    except:
                        item_title = html_content.find('span', class_="mw-headline").get_text(strip=True).replace(u'\xa0', u' ')
                    result[item_title] = sprite
                    result[item_title]["Title"] = item_title
                else:
                    for tab_content in html_content.select(".wds-tab__content"):
                        sprite = {
                            "Item": "",
                            "Tree": "",
                            "Seed": ""
                        }
                        images = tab_content.find('div', {"class": "gtw-card"})
                        sprite["Item"] = images.find('div', {"class": "card-header"}).img['src']
                        sprite["Tree"] = images.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').img['src']
                        sprite["Seed"] = images.find('td', {"class": "seedColor"}).img['src']
                        try:
                            item_title = tab_content.find('span', class_="mw-headline").small.decompose().get_text(strip=True).replace(u'\xa0', u' ')
                        except:
                            item_title = tab_content.find('span', class_="mw-headline").get_text(strip=True).replace(u'\xa0', u' ')
                        result[item_title] = sprite
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
    print(get_item_sprite("ancestral tesseract"))