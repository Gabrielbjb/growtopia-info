import requests

def SearchItem(ItemName):
    try:
        params = {
            "action": "query",
            "srlimit": 20,
            "list": "search",
            "srsearch": ItemName,
            "format": "json"
        }

        response = requests.get("https://growtopia.fandom.com/api.php", params=params)
        data = response.json()

        items = [
            {
                "title": item['title'],
                "url": f"https://growtopia.fandom.com/wiki/{item['title'].replace(' ', '_')}"
            } for item in data['query']['search']
            # Filter out items that are not actual items
            if not any(kw in item['title'].lower() for kw in ['category:', 'update', 'disambiguation', 'week'])
            and ItemName.lower() in item['title'].lower()
        ]

        return items
    except requests.RequestException as error:
        raise Exception(f"Wiki fetch failed: {error}")
