from page import PageLoader
from bs4 import BeautifulSoup as BS

class NewParserItems:
    def __init__(self):
        self.bs4 = self.get_bs4_html("https://steamcommunity.com/market/recent?country=RU&language=russian&currency=1")

    def get_names_links(self):
        tag_a = self.bs4.findAll("a", class_="market_listing_item_name_link")
        names = [name.text.strip() for name in tag_a]
        links = [link.get("href") for link in tag_a]
        return names, links

    def get_names(self):
        names, links = self.get_names_links()
        return names

    def get_links(self):
        names, links = self.get_names_links()
        return links

    def get_prices(self):
        tag_span = self.bs4.findAll("span", class_="market_listing_price market_listing_price_with_fee")
        return [price.text.strip() for price in tag_span]


    @classmethod
    def get_bs4_html(cls, _url_news):
        items_dict = PageLoader().get_html_from_url(_url_news, "json")
        return BS(items_dict["results_html"], "html.parser")
        