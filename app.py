# save this as app.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def fast():
    try:
        r = requests.get('https://ai.resolus.co.jp/fast')
        return r.text
    except Exception as e:
        app.logger.error(f'{e}', exc_info=True)
        return 'failed'

@app.route("/slow")
def slow():
    try:
        r = requests.get('https://ai.resolus.co.jp/slow')
        return r.text
    except Exception as e:
        app.logger.error(f'{e}', exc_info=True)
        return 'failed'

@app.route("/myip")
def myip():
    try:
        r = requests.get('https://api.ipify.org/?format=json')
        return r.text
    except Exception as e:
        app.logger.error(f'{e}', exc_info=True)
        return 'failed'
