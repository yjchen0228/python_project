# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:07:23 2022

@author: Yu Jen
"""

import pandas_datareader as DR
import pandas as pd
import dateutil.parser as psr
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import sys

plt.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False

stockdata=pd.read_csv('TaiwanStockID.csv',index_col=0,squeeze=True).to_dict()
stock=input('請輸入台灣股票名稱或代號:')

startDate = psr.parse(input("請輸入查詢起始日期："))
endDate=psr.parse(input("請輸入查詢截止日期："))


    
if stock.isdigit()==True:
    word=str(stock) + ".tw"
    try:
        data=DR.DataReader(word,'yahoo',startDate.date(),endDate.date())
    except RemoteDataError:
        print("股票代號錯誤")
        sys.exit()
    except ValueError:
        print('起始日期必須早於截止日期')
        sys.exit()
    newdic={v:k for k, v in stockdata.items()}
    stock=newdic [int(stock)]
   
    
elif stock.isdigit()==False:
    word=stockdata[stock]
    word=str(word)+".tw"
    try:
        data=DR.DataReader(word,'yahoo',startDate.date(),endDate.date())
    except RemoteDataError:
        print("股票代號錯誤")
        sys.exit()
    except ValueError:
        print('起始日期必須早於截止日期')
        sys.exit()




    
data=DR.DataReader(word,'yahoo',startDate.date(),endDate.date())
close_price=data["Close"]
pic1=close_price.plot(label='收盤價')
pic2=close_price.rolling(window=20).mean().plot(label="20MA")
pic3=close_price.rolling(window=60).mean().plot(label="60MA")
plt.title(str(stock)+str(startDate.date())+'~'+str(endDate.date())+'收盤價')
plt.xlabel("Date")
plt.ylabel("指數")
plt.show()

