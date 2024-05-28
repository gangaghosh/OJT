import pandas as pd
# Serires with 1 dimension
# wecan create a series with in a list, array , dictionaries
# #each series value have an index which will start from 0
data=[10,20,30,40]
series=pd.Series(data)
print(series)

# access the element seperately by using indexing 
print(series[3])

# arithametical operation
series_add=series+10
print(series_add)

# filter elements in the series
filtered_series=series[series>20]
print(filtered_series)

# statical methos

mean=series.mean()
print(f"the mean value of the series is {mean}")

