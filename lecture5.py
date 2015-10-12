import pandas as pd

starting = {'Col_1':[5,2,4,7,2,4],
            'Col_2':[7,8,2,1,5,6],
            'Col_3':[10,4,2,1,8,2],
            'Col_4':[5,6,7,1,1,4],
            'Col_5':[9,9,2,1,5,2],
            'Col_6':[7,8,2,1,7,8]}
            
df = pd.DataFrame(starting)

print(df.head()) #first five rows
print(df.tail()) #last five rows

print(df.head(2)) #first two rows
print(df.tail(2)) #last two rows

print(df['Col_1'][2])