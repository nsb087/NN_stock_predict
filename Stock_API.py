# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:54:14 2017

@author: CYBERPOWER
"""

import pandas_datareader as web   
import datetime
import matplotlib.pyplot as plt 
from urllib.request import Request, urlopen 


def GetStockPrice(chosen_stock,start_year,start_month,start_day):

    plt.close("all")


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

def get_google_data(symbol, period, window):
 

 url_root = 'http://www.google.com/finance/getprices?i=['
 url_root += str(period) + ']&p=[' + str(period)
 url_root += ']d&f=d,o,h,l,c,v&df=cpct&q=['+str(symbol) + ']'
 response = urlopen(url_root)
 data = response.read()
 
 #actual data starts at index = 7
 #first line contains full timestamp,
 #every other line is offset of period from timestamp
 parsed_data = []
 anchor_stamp = ''
 end = len(data)
 for i in range(7, end):
     cdata = data[i].split(',')
 if 'a' in cdata[0]:
 #first one record anchor timestamp
     anchor_stamp = cdata[0].replace('a', '')
     cts = int(anchor_stamp)
 else:
     try:
         coffset = int(cdata[0])
         cts = int(anchor_stamp) + (coffset * period)
         parsed_data.append((dt.datetime.fromtimestamp(float(cts)), float(cdata[1]), float(cdata[2]), float(cdata[3]), float(cdata[4]), float(cdata[5])))
     except:
         pass # for time zone offsets thrown into data
 df = pd.DataFrame(parsed_data)
 df.columns = ['ts', 'o', 'h', 'l', 'c', 'v']
 df.index = df.ts
 del df['ts']
 return df
