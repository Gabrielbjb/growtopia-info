from pprint import pprint
from GTItemData import get_item_sprites, get_item_title, parse_html_content
from GTSearchItem import get_raw_html

class GrowtopiaItem:
    def __init__(self, item_name):
        self.__item_page, query_found = get_raw_html(item_name)
        self.title = query_found["Title"]
        self.url = query_found["Url"]
    
    def get_item_data(self, include_subitems: bool = False) -> dict:
        result = {}
        if len(self.__item_page.select(".gtw-card")) == 1:
            parse_html_content(self.__item_page, result)
        else:
            for idx, html_content_tabber in enumerate(self.__item_page.select(".gtw-card")):   
                tabber_result = {}   
                parse_html_content(html_content_tabber, tabber_result)
                if idx == 0:
                    result = tabber_result
                    # result["Title"] = self.title
                    if not include_subitems: break
                else:
                    item_title = get_item_title(html_content_tabber)
                    tabber_result["Title"] = item_title
                    result.setdefault("SubItems", []).append(tabber_result)
        result["Title"] = self.title
        result["URL"] = self.url
        return result
    
    def get_item_sprite(self, include_title: bool = False) -> dict:
        item_sprites = get_item_sprites(self.__item_page)
        if include_title: item_sprites["Title"] = self.title
        return item_sprites

# Example usage:
item = GrowtopiaItem("Dirt")
pprint(item.get_item_data())
print(item.get_item_sprite())
