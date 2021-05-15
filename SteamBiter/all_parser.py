from tool import careful
import requests
from bs4 import BeautifulSoup
import json


class HtmlParser:
    @classmethod
    @careful
    def get_dict_from_html(cls, html):
        try:
            return json.loads(html)
        except:
            # print("Cannot parse HTML to JSON ERROR!!")
            return {}

    @classmethod
    @careful
    def get_id_from_html(cls, html):
        start_text = "Market_LoadOrderSpread( "
        end_text = " );\t// initial load"
        return cls.get_segment(html, start_text, end_text)

    @classmethod
    def get_segment(cls, html, start_text, end_text):
        start_i = html.find(start_text) + len(start_text)
        end_i = html.find(end_text)
        return html[start_i:end_i]
