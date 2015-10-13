import pandas as pd

df = pd.read_csv('FBI-CRIME11.csv')

#print(df.head())

df.to_csv('newcsv.csv')
df['Violent Crime Rate'].to_csv('newcsv2.csv')

df.set_index('Year', inplace = True)

print(df.head())