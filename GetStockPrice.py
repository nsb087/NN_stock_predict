# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:54:14 2017

@author: RABarnes
"""

import pandas_datareader as web   
import datetime
import matplotlib.pyplot as plt  


def GetStockPrice(chosen_stock,start_year,start_month,start_day):

    plt.close("all")

    chosen_stock=str("BTC-USD")
    start_year=2017
    start_month=12
    start_day=1
 

   


    start = datetime.datetime(start_year,start_month,start_day)
    end = datetime.date.today()


    stock = web.DataReader(chosen_stock, "yahoo", start, end)
    stock.reset_index(inplace=True,drop=False)



#    length=len(stock.Date)-1

    #plt.xlim(stock.Date[0],stock.Date[length])
    #plt.plot(stock.Date,stock.Open,'b',stock.Date,stock.Close,'r')
    #plt.show()


    fig, ax1 = plt.subplots()
    plt.title(chosen_stock)
    ax1.plot(stock.Date,stock.Close, 'b-')
    ax1.set_xlabel('Date')

    ax1.set_ylabel('Closing Price ($)', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()

    ax2.plot(stock.Date,stock.Volume/1e9, 'r-')
    ax2.set_ylabel('Volume (Billion)', color='r')
    ax2.tick_params('y', colors='r')

    fig.tight_layout()
    plt.show()

    return stock
