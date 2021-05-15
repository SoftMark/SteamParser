import page
from page import Page, PageParser


class Item:
    def __init__(self, url):
        self.url = url
        self.page = Page(url)
        self.name = PageParser.get_item_name(self)
        self.id = PageParser.get_id_from_html(self.page.html)
        self.orders_qnt = PageParser.get_order_qnt(self.id)
        self.min_price = PageParser.get_order_min_price(self.id)

    def show_data(self):
        print("------------------------------")
        print("NAME:", self.name)
        print("URL:", self.url)
        print("ID:", self.id)
        print("ORDERS:", self.orders_qnt)
        print("MIN PRICE:", self.min_price)
        print("------------------------------")
