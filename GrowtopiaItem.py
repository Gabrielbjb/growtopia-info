from GTItemData import get_item_title, parse_html_content
from GTSearchItem import get_raw_html


class GrowtopiaItem:
    def __init__(self, item_name):
        self.__item_page, query_found = get_raw_html(item_name)
        self.title = query_found["Title"]
        self.url = query_found["Url"]
    
    def get_item_data(self, include_subitems=False):
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
    
    def get_item_sprite(self):
        return {
            "Title": self.title,
            "Item": self.__item_page.select_one('div.card-header img')['src'],
            "Tree": self.__item_page.select_one('th:-soup-contains("Grow Time") + td img')['src'],
            "Seed": self.__item_page.select_one('td.seedColor img')['src']
        }
