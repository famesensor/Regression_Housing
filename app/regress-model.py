import pandas as pd
import pickle
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('Melbourne_housing_FULL.csv')
df = df.drop(['Address', 'Postcode', 'Propertycount', 'Landsize',
            'Suburb', 'Longtitude', 'Lattitude', 
            'Method', 'SellerG'], axis=1)

my_imputer = SimpleImputer()
df[['Bedroom2']] = my_imputer.fit_transform(df[['Bedroom2']])
df[['Bathroom']] = my_imputer.fit_transform(df[['Bathroom']])
df[['Car']] = my_imputer.fit_transform(df[['Car']])

# Add age variable
df['Age'] = 2019 - df['YearBuilt']
df = df.drop(['YearBuilt'], axis=1)

df = df.dropna()
df = df.astype({'Price': 'int', 'Bedroom2': 'int', 'Bathroom': 'int', 
                'Car': 'int', 'BuildingArea': 'int', 'Age': 'int'})
df = df.drop_duplicates()
df = df.reset_index(drop=True)

import datetime
def to_year(date_str):
    return datetime.datetime.strptime(date_str.strip(),'%d/%m/%Y').year
df['Date'] = df.Date.apply(to_year)
df = df.astype({'Date': 'int'})

dic={'Banyule City Council':1,
'Bayside City Council':2,
'Boroondara City Council':3,
'Brimbank City Council':4,
'Cardinia Shire Council':5,
'Casey City Council':6,
'Darebin City Council':7,
'Frankston City Council':8,
'Glen Eira City Council':9,
'Greater Dandenong City Council':10,
'Hobsons Bay City Council':11,
'Hume City Council':12,
'Kingston City Council':13,
'Knox City Council':14,
'Macedon Ranges Shire Council':15,
'Manningham City Council':16,
'Maribyrnong City Council':17,
'Maroondah City Council':18,
'Melbourne City Council':19,
'Melton City Council':20,
'Mitchell Shire Council':21,
'Monash City Council':22,
'Moonee Valley City Council':23,
'Moorabool Shire Council':24,
'Moreland City Council':25,
'Nillumbik Shire Council':26,
'Port Phillip City Council':27,
'Stonnington City Council':28,
'Whitehorse City Council':29,
'Whittlesea City Council':30,
'Wyndham City Council':31,
'Yarra City Council':32,
'Yarra Ranges Shire Council':33 }
df['CouncilArea'] = df.CouncilArea.map(dic)

type_dummies = pd.get_dummies(df[['Type']])
regionname_dummies = pd.get_dummies(df[['Regionname']])
df = df.drop(['Type', 'Regionname'],axis=1).join(type_dummies)
df = df.join(regionname_dummies)

train, test = train_test_split(df, test_size = 0.3, random_state=1060)

X_train = train.loc[:, df.columns != 'Price']
y_train = train.Price

X_test = test.loc[:, df.columns != 'Price']
y_test = test.Price

model = LinearRegression()
model.fit(X_train.values, y_train.values)

# poly_reg = PolynomialFeatures(degree=2)
# X_poly = poly_reg.fit_transform(X_train)
# model = LinearRegression()
# model.fit(X_poly, y_train)

predict_test = model.predict(X_test)
result = r2_score(y_test, predict_test)
print("Accuracy: %.2f%%" % (result*100.0))

# Export model
# pickle.dump(model, open('model.pkl','wb'))

# Plot result
#fig, ax = plt.subplots()

#ax.scatter(y_test, predict_test)
#ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
#ax.set_xlabel('Measured')
#ax.set_ylabel('Predicted')
#plt.show()