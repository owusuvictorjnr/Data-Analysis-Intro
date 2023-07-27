import pandas as pd
import numpy as np



df = pd.read_csv('/home/vitech/Downloads/Data2Cleanups2.csv')



#Finding missing values

# print(df.isna().sum()) #this list all colums that have missing values

# print(df.isna().sum().sum()) this list the total number of missing values



# removing missing values
# df2 = df
# df2 = df2.dropna() 
# print( df2.dropna().isna().sum().sum())
# print( df2)
# print(df2.dropna()) 


# summerinsing by exploring basic stats
# print(df.describe())


#finding data information
# print(df.info)

# reset
# data transformation


# Renaming column by fixing confusing header names
# df3 = df
# print(df3)

# df3.rename(columns={'Duration in minutes': 'Duration'}, inplace=True)
# print(df3)


# finding  rows and columns
# print(df.shape)


# finding duplicates
# df4 = df

# print(df4.duplicated())
# print(df4.drop_duplicates())
# print(df4.reset_index())
# print(df4.compare)
# print(df4)


# Find out if data contains outlers
# df5 = df
# z_scores = np.abs(df5["Duration in minutes"] - df5["Duration in minutes"].mean()) / df5["Duration in minutes"].std()

# # # Identify the outliers
# outliers = df5[z_scores > 3]

# # # Print the outliers
# print(outliers)


# Finding wrong format
# df6 = df
# wrong_format =df6[df6["Duration in minutes"].apply(lambda x: not isinstance(x, float))]
# print(wrong_format)



# Finding wrong value or data
df7 = df
wrong_values = df7[df7["Calories"].apply(lambda x: x > 9 or x < 0)]
print(wrong_values)

# print(df)