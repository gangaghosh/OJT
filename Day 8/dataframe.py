# dataframes is two dimensional which is in atabular format
import pandas as pd

# create a dataframe with a dictionary
data= {
    'Name': ['Ganga','Devika','Dhanya'],
    'Age': [22,24,23],
    'Place': ['TVM','Kollam','CLT']
}

# convert the data in to dataframe
df=pd.DataFrame(data)
# print(df)

# print(df[['Name','Place']])

# for accessing each row from the datframe we need to use the inbuilt use the inbuilt function in pandas 'iloc'
# print(df.iloc[2])

# print(df[df['Age']>23])

# add a new column into the dataframe
df['stiphant']=[15000,5000,5000]
# print(df)

# remove a column
df=df.drop(columns=['stiphant'])
# print(df)

# statical function 
# describe() get the summery of  statics your data frame
print(df.describe())
