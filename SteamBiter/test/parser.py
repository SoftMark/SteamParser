import requests
from bs4 import BeautifulSoup
import steam_market as sm

url = "https://steamcommunity.com/market/listings/753/322170-Dovahkiin"
page_html = requests.get(url).text

soup = BeautifulSoup(page_html, 'html.parser')
orders_qnt = soup.find("div", class_="market_commodity_orders_header")

print(sm.get_csgo_item("AK-47 | Frontside Misty (Field-Tested)", currency='EUR'))