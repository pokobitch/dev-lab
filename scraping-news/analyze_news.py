import pandas as pd

#csvファイルの読み込み
df = pd.read_csv("news.csv")

#タイトルに"ガソリン"が含まれるデータだけを抽出
df_filtered = df[df["タイトル"].str.contains("ガソリン", na=False)]

#結果を出力
print(df_filtered)

#別のcsvとして保存
df_filtered.to_csv("filtered_news.csv", index=False, encoding="utf-8")