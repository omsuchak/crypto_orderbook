# Om Suchak: 8/16/22
#
# FTX project with Chris Chaves

#from selectors import EpollSelector
import pandas as pd
import numpy as np

"""
OrderBook class:
Inputs:
- initial_bids, a 2D list of bids and sizes
- initial_asks, a 2D list of asks and sizes
"""
class OrderBook():
    def __init__(self, initial_bids: list, initial_asks: list):
        self.bids = initial_bids
        self.asks = initial_asks

    """
    orders are formatted as such: [price_level, size]
    """
    

    def limitUpdate(self, bids: list, asks: list):
        if bids:
            #bid_cols = zip(*bids)
            #prices = bid_cols[0]
            print('bids')
            
            curr_bids = list(zip(*self.bids))
            curr_bid_prices = curr_bids[0]

            #sizes = cols[1]
            for order in bids:
                if order[0] in curr_bid_prices:
                    idx = curr_bid_prices.index(order[0])
                    if order[1] == 0:
                        self.bids.pop(idx)
                    else:
                        self.bids[idx] = order
                else:
                    self.bids.append(order)
                    self.bids = sorted(self.bids,key=lambda x: (x[0],x[1]))
        if asks:
            #cols = zip(*asks)
            #prices = cols[0]

            print('asks')

            curr_asks = list(zip(*self.asks))
            curr_ask_prices = curr_asks[0]

            #sizes = cols[1]
            for order in asks:
                if order[0] in curr_ask_prices:
                    idx = curr_ask_prices.index(order[0])
                    if order[1] == 0:
                        self.asks.pop(idx)
                    else:
                        self.asks[idx] = order
                else:
                    self.asks.append(order)
                    self.asks = sorted(self.asks,key=lambda x: (x[0],x[1]))

    def tradeUpdate(self, trades: list):
        for trade in trades:
            price = trade['price']
            size = trade['size']
            side = (trade['side'] == 'buy')
            if side:
                curr_asks = list(zip(*self.asks))
                curr_ask_prices = curr_asks[0]
                idx = curr_ask_prices.index(price)
                self.asks[idx][1] = self.asks[idx][1] - size
            else:
                curr_bids = list(zip(*self.bids))
                curr_bid_prices = curr_bids[0]
                idx = curr_bid_prices.index(price)
                self.bids[idx][1] = self.bids[idx][1] - size

    

    
    
    
    
    
    def addLimitOrder(self, order: list, is_bid: bool):
        if is_bid: 
            self.bids.append(order)
            self.bids = sorted(self.bids,key=lambda x: (x[0],x[1]))
        else:
            self.asks.append(order)
            self.asks = sorted(self.asks,key=lambda x: (x[0],x[1]))



    def marketOrder(self, size: float, is_bid: bool):
        if is_bid:
            book_depth = self.bids[0][0]

            #find out how many levels of the order book the order wiped out and sweep accordingly
            while(book_depth < size):
                self.bids.pop(0)
                book_depth += self.bids[0][0]

            self.bids[0][1] = book_depth - size
        
        else:
            book_depth = self.asks[0][0]

            #find out how many levels of the order book the order wiped out and sweep accordingly
            while(book_depth < size):
                self.asks.pop(0)
                book_depth += self.asks[0][0]

            self.asks[0][1] = book_depth - size


                
    def removeOrder(self, order: list, is_bid: bool):
        #store index of value to pop
        idx = None

        if is_bid:
            #search for value to pop
            for count, value in enumerate(self.bids):
                if value == order:
                    idx = count
            self.bids = self.bids.pop(idx)

        else:
            #search for value to pop
            for count, value in enumerate(self.asks):
                if value == order:
                    idx = count
            self.asks = self.asks.pop(idx)

        
    
#trades = [{"id":39638614,"price":2,"size":0.5,"side":"sell","liquidation":false,"time":"2022-08-18T05:17:36.059948+00:00"}]

#ob = OrderBook([[1, 1], [2, 2]], [[3, 3], [4, 4]])
#print('bids', ob.bids, 'asks', ob.asks)

# ob.limitUpdate([[1, 2]], [])
# print('bids', ob.bids, 'asks', ob.asks)

# ob.limitUpdate([[1, 0]], [])
# print('bids', ob.bids, 'asks', ob.asks)

# ob.limitUpdate([[1, 2]], [[4, 5]])
# print('bids', ob.bids, 'asks', ob.asks)

# ob.limitUpdate([], [[4, 0]])
# print('bids', ob.bids, 'asks', ob.asks)

#ob.tradeUpdate([{"id":39638614,"price":2,"size":0.5,"side":"sell","liquidation":False,"time":"2022-08-18T05:17:36.059948+00:00"}])
#print('bids', ob.bids, 'asks', ob.asks)








