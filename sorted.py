import pandas as pd

df = pd.read_csv('formated.csv')
df2 = df.sort_values(by=['StationId'])

turbines = []
for station, df3 in df2.groupby('StationId'):
    turbines.append(df3.sort_index())

print(len(turbines))