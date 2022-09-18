# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 01:15:12 2022

@author: Yu Jen
"""

import pandas_datareader as DR
import pandas as pd
import dateutil.parser as psr
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False


stock=input('請輸入股票代號(如果非美國股票請加國碼ex:.TW or .JP):')

startDate = psr.parse(input("請輸入查詢起始日期："))
endDate=psr.parse(input("請輸入查詢截止日期："))

data=DR.DataReader(stock,'yahoo',startDate.date(),endDate.date())
close_price=data["Close"] #也可以選High=當日最高價、Low=當日最低價、Volume=當日成交量、Close=當日收盤價
pic1=close_price.plot(label='收盤價')
pic2=close_price.rolling(window=20).mean().plot(label="20MA")
pic3=close_price.rolling(window=60).mean().plot(label="60MA")
plt.title(str(stock)+str(startDate.date())+'~'+str(endDate.date())+'close price')
plt.xlabel("Date")
plt.ylabel("price")
plt.show()