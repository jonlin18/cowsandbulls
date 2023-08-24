import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download(tickers='MSFT', period='200d', interval='1d')

#plt.figure(figsize=(16,8))
#plt.title('Close Price History', fontsize=18)
#plt.plot(data['Close'])
#plt.xlabel('Date', fontsize=18)
#plt.ylabel('Close Price', fontsize=18)
#plt.show()

def SMA(data, period = 30, column='Close'):
    return data[column].rolling(window=period).mean()

data['SMA20']=SMA(data, 20)
data['SMA50']=SMA(data, 50)

data['Signal'] = np.where(data['SMA20'] > data['SMA50'] , 1, 0)
data['Position'] = data['Signal'].diff()

data['Buy'] = np.where(data['Position'] == 1, data['Close'], np.NAN)
data['Sell'] = np.where(data['Position'] == -1, data['Close'], np.NAN)

plt.figure(figsize=(16,8))
plt.title('Buy and Sell Signals', fontsize=18)
plt.plot(data['Close'], alpha = 0.5, label = 'Close')
plt.plot(data['SMA20'], alpha = 0.5, label = 'SMA20')
plt.plot(data['SMA50'], alpha = 0.5, label = 'SMA50')
plt.scatter(data.index, data['Buy'], alpha = 1, label = 'Buy Signal', marker = '^', color = 'green')
plt.scatter(data.index, data['Sell'], alpha = 1, label = 'Sell Signal', marker = 'v', color = 'red')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price', fontsize=18)
plt.show()
