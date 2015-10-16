import pandas as pd
import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean

def moving_average(data):
    return mean(data)

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = web.DataReader("T", 'yahoo', start, end)
describe = att.describe()
print(describe['Open']['std'])

att['50MA'] = pd.rolling_mean(att['Close'], 50)
att['10MA'] = pd.rolling_mean(att['Close'], 10)
att['50STD'] = pd.rolling_std(att['Close'], 50)
att['MA_with_apply'] = pd.rolling_apply(att['Close'], 50, moving_average)

print(att.head())

att2 = att.dropna()
print(att2.head())

#att.dropna(inplace=True)

#att.dropna(how='all', inplace=True)
#att.fillna(method='bfill', inplace=True) #ffill for forward
#att.fillna(value=-99999, inplace=True)

one_pct = len(att)*0.01
print(att.isnull().values.sum())
att.fillna(value=-99999, inplace=True, limit=one_pct)
print(att.head())

if att.isnull().values.sum() > 1:
    print(att.isnull().values.sum())
    print('Found remaining NA, more than 1% is not a number')
