import pandas as pd

# read the csv file into the dataframe
df=pd.read_csv('data.csv',
               dtype={'Age':int, 'salary':float},
               usecols=['Name','Age','Salary']) #read the specific column which we mention

print(df)