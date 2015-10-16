import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

bridge_readings = {'Distance_mm':
                   [50000, 50013, 50015, 50009,
                    5024012, 50007, 50016, 50014]}

df = pd.DataFrame(bridge_readings)
df.plot().
plt.show()

stats = df.describe()
print(stats)
print(stats.Distance_mm['std'])

df['std'] = pd.rolling_std(df['Distance_mm'], 2)

print(df.head())

df = df[ (df['std'] < stats.Distance_mm['std']) ]
#df = df[ (df['std'] < 50) ]

df['Distance_mm'].plot()
plt.show()
