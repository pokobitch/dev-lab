import streamlit as st
import pandas as pd
import csv
from scrape_yahoo_news import scrape_news


# タイトル
st.title("ニュースビューア")

# スクレイピング実行
news_data = scrape_news()
    
# データフレームに変換
df = pd.DataFrame(news_data, columns=["タイトル", "リンク"])
    
# キーワード入力ボックス
keyword = st.text_input("タイトルに含まれるキーワードで検索")

# キーワードが含まれていればフィルタ
if keyword:
    df = df[df["タイトル"].str.contains(keyword, na=False)]

#データ表示
st.dataframe(df)

# CSVダウンロード
if st.button("CSVダウンロード"):
    df.to_csv("/app/data/news.csv", index=False, encoding="utf-8")
    st.success("CSVファイルをダウンロードしました。")
