import pandas as pd

values = [9, 5, 10, 16, 5, 15, 25, 50, 51, 53, 75, 100, 121, 123, 114, 140, 150]
EMA_periods = [2,5,10]


df = pd.DataFrame({'close':values})

#go through each EMA period and create an EMA col for each
for x in range(len(EMA_periods)):
    period = int(EMA_periods[x])
    #creates an 'EMA field'
    field_name = 'EMA'+str(EMA_periods[x])
    df[field_name] = df['close'].ewm(span=period,min_periods=period,adjust=False).mean()

print(df)