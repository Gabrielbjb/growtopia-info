import asyncio
import requests

from GTItemData import ItemData
from GTSearchItem import SearchItem


class GrowtopiaItem:
    def __init__(self, item_name, region="en"):
        try:
            query_result = SearchItem(item_name)[0]
            self.title = query_result["title"]
            self.url = query_result["url"]
            self.__item_page = requests.get(f"https://growtopia.fandom.com/{region}/wiki/{self.title}")
            self.data = ItemData(self.__item_page, item_name, self.title)
            print(self.data)
        except:
            return ({"Error": "It looks like we can't reach fandom.com! Try again later."})

# Example usage
if __name__ == "__main__":
    item = GrowtopiaItem("dirt")