import requests
from bs4 import BeautifulSoup, Tag
import csv

def scrape_news():
    #スクレイピング先のURL
    url = "https://news.yahoo.co.jp/"

    #webページを取得
    res = requests.get(url)
    res.encoding = res.apparent_encoding #文字化け対策

    #HTMLを解析
    soup = BeautifulSoup(res.text, "html.parser")

    news = []
    for a in soup.find_all("a"):
        title = a.get_text().strip()
        link = a.get("href")
        if title and link and "news.yahoo.co.jp/pickup" in link:
            news.append([title, link])

    return news