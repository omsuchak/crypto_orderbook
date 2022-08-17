# Om Suchak: 8/16/22
#
# FTX project with Chris Chaves

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

        
    
    





