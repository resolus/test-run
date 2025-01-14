# save this as app.py
from flask import Flask
import requests
import asyncio
import httpx

app = Flask(__name__)

@app.route("/")
def fast():
    x = get_sync()
    return x

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

async def get_ext():
    try:
        url = 'https://ai.resolus.co.jp/fast'
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            # app.logger.error(response.text)
            return response.text
    except Exception as e:
        app.logger.error(f'{e}', exc_info=True)
        return 'failed'

def get_sync():
    try:
        url = 'https://0ut9kgutfe.execute-api.ap-northeast-1.amazonaws.com/default/mytest'
        with httpx.Client() as client:
            response = client.get(url)
            return response.text
    except Exception as e:
        app.logger.error(f'{e}', exc_info=True)
        return 'failed'
