from tool import careful
from bs4 import BeautifulSoup
from page import Page, PageLoader
from parser import HtmlParser


class Item:
    def __init__(self, url):
        self.url = url
        self.page = Page(url)
        self.name = self.get_item_name(self.page)
        self.id = self.get_item_id(self.page)
        self.orders_qnt = self.get_order_qnt(self.id)
        self.min_price = self.get_order_min_price(self.id)

    def show_data(self):
        print("------------------------------")
        print("NAME:", self.name)
        print("URL:", self.url)
        print("ID:", self.id)
        print("ORDERS:", self.orders_qnt)
        print("MIN PRICE:", self.min_price)
        print("------------------------------")

    @classmethod
    @careful
    def get_item_id(cls, page):
        try: return HtmlParser.get_id_from_html(page.html)
        except: pass

    @classmethod
    def get_item_data(cls, id):
        data_dict = PageLoader.get_item_data_page(id).dict
        return BeautifulSoup(data_dict["sell_order_summary"], "html.parser")

    @classmethod
    def get_item_main_data(cls, id):
        return cls.get_item_data(id).findAll("span", class_="market_commodity_orders_header_promote")

    @classmethod
    @careful
    def get_order_qnt(cls, id):
        return cls.get_item_main_data(id)[0].text

    @classmethod
    @careful
    def get_order_min_price(cls, id):
        return cls.get_item_main_data(id)[1].text

    @classmethod
    @careful
    def get_item_name(cls, page):
            soup = BeautifulSoup(page.html, "html.parser")
            return soup.find("span", class_="market_listing_item_name").text
