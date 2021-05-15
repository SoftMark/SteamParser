import requests
from bs4 import BeautifulSoup
import json


class Page:
    def __init__(self, url):
        self.html = PageLoader.get_html_from_url(url)

    def dict(self):
        try:
            return PageLoader.get_dict_from_html(self.html)
        except:
            print("Cannot parse to json ERROR!!")
            return None


class PageLoader:
    # Request
    @classmethod
    def get_html_from_url(cls, url):
        page = requests.get(url)
        if page.status_code == 200:
            print("Page loaded!")
            return page.text
        else:
            print("Page loading ERROR!")
            return None

    @classmethod
    def get_dict_from_html(cls, html):
        return json.loads(html)


class PageParser:
    # Collect
    @classmethod
    def get_id_from_html(cls, html):
        # Start of ID
        start_text = "Market_LoadOrderSpread( "
        start_i = html.find(start_text) + len(start_text)
        # End of ID
        end_text = " );\t// initial load"
        end_i = html.find(end_text)
        # Got it!
        return html[start_i:end_i]

    @classmethod
    def get_order_data(cls, id):
        url = f"https://steamcommunity.com/market/itemordershistogram?country=RU&language=russian&currency=5&item_nameid={id}&two_factor=0"
        data_dict = Page(url).dict()
        return BeautifulSoup(data_dict["sell_order_summary"], "html.parser")

    @classmethod
    def get_order_main_data(cls, id):
        return cls.get_order_data(id).findAll("span", class_="market_commodity_orders_header_promote")

    @classmethod
    def get_order_qnt(cls, id):
        return cls.get_order_main_data(id)[0].text

    @classmethod
    def get_order_min_price(cls, id):
        return cls.get_order_main_data(id)[1].text

    @classmethod
    def get_item_name(cls, item):
        soup = BeautifulSoup(item.page.html, "html.parser")
        return soup.find("span", class_="market_listing_item_name").text
