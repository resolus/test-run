# save this as app.py
from flask import Flask
import requests
import asyncio
import httpx

app = Flask(__name__)

@app.route("/")
def fast():
    return asyncio.run(get_ext())

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
