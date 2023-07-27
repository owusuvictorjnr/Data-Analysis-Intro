import pandas as pd
import numpy as np


df = pd.read_csv('/home/vitech/Downloads/EAF_Report.csv', encoding='cp1252')

# print number of rows
# print (df.head(5))

#get information about the dataset
# print (df.info())

#finding missing values
# print (df.isna().sum())

#finding the overall total number of missing values
# print (df.isna().sum().sum()) 


# replacing missing values
# df2 = df.fillna(value=0) #this can be any number or value
# print(df2)


# df3 = df.fillna(method='pad') #this will fill the null value with the previous value
# print(df3)

# df4 = df.fillna(method='bfill') #this will fill the null value with the next value
# print(df4)


# df5 = df.fillna(method='pad', axis=1) #this will fill the null value with the left column value
# print(df5)


# df6 = df.fillna(method='bfill', axis=1) #this will fill the null value with the right column  value
# print(df6)


# df7 = df.fillna({'COMMERCIAL': '2.4', 'BUSH': '40.50'}) #this will fill the null value with 
# the assigned values in dictionary using different column name
# print(df7)


# df8 = df.fillna(value=df['BUSH'].mean()) #this will fill the null value with the mean of a column
# print(df8)





# print(df)



# df.eaf.replace(to_replace=np.nan, value=df.eaf.mean(), inplace=True)
# print("There are {} missing values in the data.".format(df.isna().sum().sum()))