import requests
from bs4 import BeautifulSoup, Tag
import csv

#スクレイピング先のURL
url = "https://news.yahoo.co.jp/"

#webページを取得
res = requests.get(url)
res.encoding = res.apparent_encoding #文字化け対策

#HTMLを解析
soup = BeautifulSoup(res.text, "html.parser")

#csvに書き出す
with open("news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["タイトル", "リンク"])
    
    for a in soup.find_all("a"):
        title = a.get_text().strip()
        link = a.get("href")
        if title and link and "news.yahoo.co.jp/pickup" in link:
            writer.writerow([title, link])
