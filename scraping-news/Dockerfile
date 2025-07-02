# Python公式の軽量イメージをベースに
FROM python:3.11-slim

# 作業ディレクトリを作る
WORKDIR /app

# 依存関係のファイルを先にコピー
COPY requirements.txt .

# ライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリのソースコードをコピー
COPY . .

# Streamlitが使うポートを開ける
EXPOSE 8501

# コンテナ起動時に実行するコマンド
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]