from typing import Tuple
from bs4 import BeautifulSoup
import requests

def search_item(item_name, allow_partial_match=True, show_url=True):
    try:
        if allow_partial_match: #Experimental
            params = {
                "action": "query",
                "srlimit": 20,
                "list": "search",
                "srsearch": item_name,
                "format": "json"
            }
            data = requests.get("https://growtopia.fandom.com/api.php", params=params).json()
            items = [
                {
                    "Title": item['title'],
                    **({"Url": f"https://growtopia.fandom.com/wiki/{item['title'].replace(' ', '_')}"} if show_url else {})
                } for item in data['query']['search']
                # Filter out items that are not actual items
                if not any(kw in item['title'].lower() for kw in ['category:', 'update', 'disambiguation', 'week', 'mods/'])
                and item_name.lower() in item['title'].lower()
            ]
            return items
        else:
            data = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={item_name}").json()
            items = [{
                "Title": item['title'],
                **({"Url": f"https://growtopia.fandom.com/wiki/{item['title'].replace(' ', '_')}"} if show_url else {})
            } for item in data['items']]
            return items
    except requests.RequestException as error:
        raise Exception(f"Wiki search fetch failed: {error}")

def get_raw_html(item_name) -> Tuple[BeautifulSoup, dict]:
    try:
        found_item = search_item(item_name, allow_partial_match=False)[0]
        item_page_response = requests.get(f"https://growtopia.fandom.com/wiki/{found_item['Title']}")
        return BeautifulSoup(item_page_response.text, "html.parser"), found_item
    except requests.RequestException as error:
        raise Exception(f"Wiki page fetch failed: {error}")
    except IndexError:
        raise Exception(f"No search results found for item: {item_name}")
