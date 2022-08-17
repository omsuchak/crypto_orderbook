#from xml.etree.ElementTree import TreeBuilder
#from aiohttp import TraceDnsResolveHostEndParams
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
import csv
import os
import time
import json
from datetime import datetime
from pathlib import Path
from datetime import datetime
import random
# custom imports
#import logger
import requests
from websocket import create_connection
import websockets
import websocket
import asyncio
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
        print(f"OB Info, Received : {datetime.now()}")
        print(message)

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
        print(f"Trades Info, Received : {datetime.now()}")
        print(message)

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


# print('starting')
# ws = create_connection('wss://ftx.us/ws/')

# print('connected')

# ws.send(json.dumps({'op':'subscribe', 'channel':'orderbook', 'market':'BTC/USD'}))

# while True:
#     result = ws.recv()
#     result = json.loads(result)
#     print(result)

if __name__ == '__main__':
    #print('hi')
    # import multiprocessing as mp

    # p1 = mp.Process(target=get_ob())
    # p2 = mp.Process(target=get_trades())
    # p1.start()
    # p2.start()
    #p1.join() # wait for completion
    #p2.join()

    import threading
    # import concurrent.futures

    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.map([get_ob, get_trades], range(2))

    # x = threading.Thread(target=get_ob)
    t1 = threading.Thread(target=get_ob, daemon=True)
    t2 = threading.Thread(target=get_trades, daemon=True)
    t1.start()
    t2.start()
    input('Hit enter to terminate...\n')
