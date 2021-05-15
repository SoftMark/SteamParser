import requests
from bs4 import BeautifulSoup
from tool import careful
from all_parser import HtmlParser
import json


class Page:
    def __init__(self, url):
        self.html = PageLoader.get_html_from_url(url)
        self.dict = HtmlParser.get_dict_from_html(self.html)


class PageLoader:
    # Request
    @classmethod
    @careful
    def get_html_from_url(cls, url):
        page = requests.get(url)
        if page.status_code == 200:
            # print("Page loaded!")
            return page.text
        else:
            # print("Page loading ERROR!")
            return None

    @classmethod
    @careful
    def get_item_data_page(cls, item_id):
        url = f"https://steamcommunity.com/market/itemordershistogram?country=RU&language=russian&currency=5&item_nameid={item_id}&two_factor=0"
        return Page(url)

