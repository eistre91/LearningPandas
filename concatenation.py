import pandas as pd

df1 = pd.DataFrame({'Temp':[75,73,72,76],
                   'Humidity':[30,45,32,42],
                   'Precip':[0,0,0,1]},
                  index = [0,1,2,3])

df2 = pd.DataFrame({'Temp':[76,79,77,77],
                   'Humidity':[33,35,37,23],
                   'Precip':[1,0,1,1]},
                  index = [4, 5,6,7])

df3 = pd.DataFrame({'Temp':[77,79,81,76],
                   'Humidity':[40,42,42,43],
                   'Precip':[0,1,1,1]},
                  index = [8,9,10,11])

df4 = pd.DataFrame({'Temp':[77,79,81,76],
                   'Humidity':[40,42,42,43],
                   'wind':[15,11,12,13]},
                  index = [8,9,10,11])

df5 = pd.DataFrame({'Pressure':[77,79,81,76],
                   'Cloudy':[1,0,0,1],
                   'wind':[15,11,12,13]},
                  index = [0,1,2,3])

concat1 = pd.concat([df1, df2, df3])
print(concat1)

concat2 = pd.concat([df1, df2, df4])
print(concat2)

concat3 = pd.concat([df1, df2, df5], axis=1)
print(concat3)

concat4 = pd.concat([df1, df2], axis=0) #axis is row vs column concat
print(concat4)

concat5 = pd.concat([concat4, df5], axis=1)
print(concat5)
