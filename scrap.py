from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://stockx.com/es-es/air-jordan-1-retro-high-og-yellow-toe?size=7"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

talla = soup.find_all("span", class_="css-1baulvz")

print(talla)

