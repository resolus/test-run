# Pythonランタイムを親イメージとして使用
FROM python:3.12

# 作業ディレクトリを/appに設定
WORKDIR /app

# 現在のディレクトリの内容をコンテナ内の/appにコピー
COPY . /app

# requirements.txtで指定された必要なパッケージをインストール
RUN pip install -r requirements.txt

CMD gunicorn --workers=1 --bind=0.0.0.0:8080 app:app

# CMD ["gunicorn", "--workers=2", "app:app"]
## ポートの公開
#EXPOSE 5000
#CMD ["flask", "run", "--host=0.0.0.0"]

## コンテナ起動時にapp.pyを実行
#CMD ["python", "app.py"]
