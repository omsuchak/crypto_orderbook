import pandas as pd
import numpy as np
import json
from datetime import datetime
from pathlib import Path
import requests
from websocket import create_connection
import websockets
import websocket
import asyncio
import threading
from Orderbook import OrderBook
"""
abspath = os.path.abspath(os.getcwd())
finpath = Path(abspath).resolve().parent

api_path = str(finpath) + '/ftx_key.txt'

with open(api_path) as f:
    lines = f.readlines()
    API_key = lines[0]
    API_secret = lines[1]
    API_key = API_key.strip('\n')
    API_secret = API_secret.strip('\n')
"""

API_key = "DtbP1YkXB3EsL--x3Gztpn_pbdN-9LnTTPPrSxlD"
API_secret = "mJT4sRJSQfPJR5GED1prOTFqza_w5dXz2-mg8pyT"
API_key = API_key.strip('\n')
API_secret = API_secret.strip('\n')

ob = OrderBook([], [])


#json dumps converts a python object into a json stream
def get_ob():
    def on_open(wsapp):
        print("orderbook opened")
        subscribe_message = {
            'op': 'subscribe',
            'channel': 'orderbook',
            'market': 'BTC/USD'
        }
        ws.send(json.dumps(subscribe_message))

    def on_message(wsapp, message, prev=None):
        global ob
        print(f"OB Info, Received : {datetime.now()}")

        m = json.loads(message)


        bids = m['data']['bids']
        asks = m['data']['asks']
        
        if m['type'] == 'partial':
            ob = OrderBook(bids, asks)
            print('bids', ob.bids, 'asks', ob.asks)
        else:
            ob.limitUpdate(bids, asks)
            #print('BIDS', ob.bids)
            #print('ASKS', ob.asks)


        ###### full json payloads ######
        # pprint.pprint(json.loads(message))

    def on_close(wsapp):
        print("closed connection")

    endpoint = 'wss://ftx.us/ws/'
    ws = websocket.WebSocketApp(endpoint,
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)

    ws.run_forever()


def get_trades():
    def on_open(wsapp):
        print("trades opened")
        subscribe_message = {
            'op': 'subscribe',
            'channel': 'trades',
            'market': 'BTC/USD'
        }
        ws.send(json.dumps(subscribe_message))

    def on_message(wsapp, message, prev=None):
        global ob
        print(f"Trades Info, Received : {datetime.now()}")
        print(message)

        m = json.loads(message)
        trades = m['data']

        ob.tradeUpdate(trades)
        print('TRADE UPDATE', ob.bids)
        print(ob.asks)

        ###### full json payloads ######
        # pprint.pprint(json.loads(message))

    def on_close(wsapp):
        print("closed connection")

    endpoint = 'wss://ftx.us/ws/'
    ws = websocket.WebSocketApp(endpoint,
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)

    ws.run_forever()



if __name__ == '__main__':
    t1 = threading.Thread(target=get_ob, daemon=True)
    t2 = threading.Thread(target=get_trades, daemon=True)
    t1.start()
    t2.start()
    input('Hit enter to terminate...\n')


# msg = {}
# trades = {}

# async def listen():
#     url = 'wss://ftx.us/ws/'
#     global msg
#     global trades

#     async with websockets.connect(url) as ws:
#         await ws.send(json.dumps({'op':'subscribe', 'channel':'orderbook', 'market':'BTC/USD'}))
#         await ws.send(json.dumps({'op':'subscribe', 'channel':'trades', 'market':'BTC/USD'}))

#         while True:
#             #ws.send(json.dumps({'op':'subscribe', 'channel':'orderbook', 'market':'BTC/USD'}))

#             msg = await ws.recv()
#             msg = json.loads(msg)
#             print(msg)

#             trades = await ws.recv()
#             trades = json.loads(trades)
#             print(trades)

# asyncio.get_event_loop().run_until_complete(listen())
