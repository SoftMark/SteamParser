from tool import careful
from bs4 import BeautifulSoup
from page import Page, PageLoader
from all_parser import HtmlParser


class Item:
    def __init__(self, url):
        self.url = url
        self.page = Page(url)
        self.name = self.get_item_name(self.page)
        self.id = self.get_item_id(self.page)
        self.orders_qnt_forsell = self.get_order_qnt(self.id, "sell_order_summary")
        self.min_price_forsell = self.get_order_min_price(self.id, "sell_order_summary")
        self.orders_qnt_buyrequests = self.get_order_qnt(self.id, "buy_order_summary")
        self.min_price_buyrequests = self.get_order_min_price(self.id, "buy_order_summary")

    def show_data(self):
        print("------------------------------")
        print("NAME:", self.name)
        print("URL:", self.url)
        print("ID:", self.id)
        print("ORDERS FORSELL:", self.orders_qnt_forsell)
        print("MIN PRICE:", self.min_price_forsell)
        print("ORDERS BUYREQUESTS:", self.orders_qnt_buyrequests)
        print("MIN PRICE:", self.min_price_buyrequests)
        print("------------------------------")

    @classmethod
    @careful
    def get_item_id(cls, page):
        try: return HtmlParser.get_id_from_html(page.html)
        except: pass

    @classmethod
    def get_item_data(cls, id, _stat_trade):
        data_dict = PageLoader.get_item_data_page(id).dict
        return BeautifulSoup(data_dict[_stat_trade], "html.parser")

    @classmethod
    def get_item_main_data(cls, id, _stat_trade):
        return cls.get_item_data(id, _stat_trade).findAll("span", class_="market_commodity_orders_header_promote")

    @classmethod
    @careful
    def get_order_qnt(cls, id, _stat_trade):
        return cls.get_item_main_data(id, _stat_trade)[0].text

    @classmethod
    @careful
    def get_order_min_price(cls, id, _stat_trade):
        return cls.get_item_main_data(id, _stat_trade)[1].text

    @classmethod
    @careful
    def get_item_name(cls, page):
            soup = BeautifulSoup(page.html, "html.parser")
            return soup.find("span", class_="market_listing_item_name").text
