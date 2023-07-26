# import /home/vitech/Downloads/advertising.csv 

import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('/home/vitech/Downloads/advertising.csv')

# print(df.head(5))
# print(df.head(10))
# print(df.tail(1))


#Extracting the Row
x = df[['Sales']]

y = df[['Newspaper']]

# print("X:", df['Sales'])
# print("Y:", df['Newspaper'])


# y = df[['Sales', 'Newspaper', 'TV']] 

# print("Y:", y)


model = LinearRegression()
model.fit(x, y)

# y_prep = model.predict(x)
# print( y_prep)


# y_pred = model.predict(x.head(5))
# print( y_pred)


# y_pred = model.predict(x.tail(1))
# print( y_pred)

y_pred = model.predict(x)

r2 = r2_score(y, y_pred)
print(( r2) * 100)