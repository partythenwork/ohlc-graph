import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

#for data download
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=PIS5KN1SIW74TFZE&datatype=csv 

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = pd.read_csv('MSFT.txt')
period = 100
EMA_name = 'EMA'+str(period)

df['EMA'] = df['close'].ewm(span=period,min_periods=0,adjust=False).mean()


fig = go.Figure(data=[go.Candlestick(x=df['timestamp'], open=df['open'], high=df['high'], low=df['low'], close=df['close'], name='MSFT'),
                    go.Scatter(x=df['timestamp'], y=df['EMA'],name=EMA_name)
                     ])
                
fig.show()

print(df)
