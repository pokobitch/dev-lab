import streamlit as st
import pandas as pd

# タイトル
st.title("ニュースビューア")

# csvファイル読み込み
df = pd.read_csv("news.csv")

# キーワード入力ボックス
keyword = st.text_input("タイトルに含まれるキーワードで検索")

# キーワードが含まれていればフィルタ
if keyword:
    df = df[df["タイトル"].str.contains(keyword, na=False)]

#データ表示
st.dataframe(df)