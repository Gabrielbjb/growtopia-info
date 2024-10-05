import requests

def SearchItem(item_name, allow_partial_match=True, show_url=True):
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
                    "title": item['title'],
                    **({"url": f"https://growtopia.fandom.com/wiki/{item['title'].replace(' ', '_')}"} if show_url else {})
                } for item in data['query']['search']
                # Filter out items that are not actual items
                if not any(kw in item['title'].lower() for kw in ['category:', 'update', 'disambiguation', 'week', 'mods/'])
                and item_name.lower() in item['title'].lower()
            ]
            return items
        else:
            data = requests.get(f"https://growtopia.fandom.com/api/v1/SearchSuggestions/List?query={item_name}").json()
            items = [{
                "title": item['title'],
                **({"url": f"https://growtopia.fandom.com/wiki/{item['title'].replace(' ', '_')}"} if show_url else {})
            } for item in data['items']]
            return items

    except requests.RequestException as error:
        raise Exception(f"Wiki fetch failed: {error}")
