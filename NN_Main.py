# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:42:57 2017

@author: RABarnes
"""
import Stock_API

chosen_stock=str("BTC-USD")
start_year=2016
start_month=1
start_day=1
 
data=Stock_API.GetStockPrice(chosen_stock,start_year,start_month,start_day)