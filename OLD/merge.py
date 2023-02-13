import pandas as pd

data = pd.read_csv('data.csv')
data2 = pd.read_csv('data2.csv')

merged_data = pd.merge(data, data2, on='filename')

merged_data.to_csv('merged_data.csv', index=False)
