# save this as app.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def fast():
    r = requests.get('https://ai.resolus.co.jp/fast')
    return r.text

@app.route("/slow")
def slow():
    r = requests.get('https://ai.resolus.co.jp/slow')
    return r.text

@app.route("/myip")
def myip():
    r = requests.get('https://api.ipify.org/?format=json')
    return r.text
