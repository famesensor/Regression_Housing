import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

df = pd.read_csv('Melbourne_housing_FULL.csv')
df = df.drop(['Address', 'Postcode', 'Propertycount', 'Landsize',
            'BuildingArea', 'Lattitude', 'Longtitude', 'YearBuilt', 
            'CouncilArea', 'Method', 'SellerG', 'Distance'], axis=1)

my_imputer = SimpleImputer()
df[['Price']] = my_imputer.fit_transform(df[['Price']])
df[['Bedroom2']] = my_imputer.fit_transform(df[['Bedroom2']])
df[['Bathroom']] = my_imputer.fit_transform(df[['Bathroom']])
df[['Car']] = my_imputer.fit_transform(df[['Car']])

df = df.dropna()

df = df.astype({'Price': 'int', 'Bedroom2': 'int', 
                'Bathroom': 'int', 'Car': 'int'})
df = df.drop_duplicates()
df = df.reset_index(drop=True)

df

import datetime
def to_year(date_str):
    return datetime.datetime.strptime(date_str.strip(),'%d/%m/%Y').year
df['Date'] = df.Date.apply(to_year)
df = df.astype({'Date': 'object'})
df.Date.value_counts()

suburb_dummies = pd.get_dummies(df[['Type']])
regionname_dummies = pd.get_dummies(df[['Regionname']])
date_dummies = pd.get_dummies(df[['Date']])
df = df.drop(['Suburb', 'Type', 'Regionname', 'Date'],axis=1).join(suburb_dummies)
df = df.join(regionname_dummies)
df = df.join(date_dummies)

from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.metrics import mean_squared_error

train, test = train_test_split(df, test_size = 0.2, random_state=512)

X_train = train.loc[:, df.columns != 'Price']
y_train = train.Price

X_test = test.loc[:, df.columns != 'Price']
y_test = test.Price

lm = LinearRegression()
lm.fit(X_train.values, y_train.values)

# predictions = lm.predict(X_test)

predict_train = lm.predict(X_train.values)
mean_squared_error(y_train, predict_train)

predict_test = lm.predict(X_test.values)
mean_squared_error(y_test, predict_test)

fig, ax = plt.subplots()
ax.scatter(y_test, predict_test)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
