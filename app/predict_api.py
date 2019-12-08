import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def preparation(data) :
    df_type = pd.DataFrame({'Type':['h','t','u'],
        'Type_h':[1,0,0],
        'Type_t':[0,1,0],
        'Type_u':[0,0,1],
    })  
    df_region = pd.DataFrame({'Region':['eastern','eastern-victoria','northern','northern-victoria','south-eastern','southern','western','western-victoria'],
      'Regionname_Eastern Metropolitan':[1,0,0,0,0,0,0,0],
      'Regionname_Eastern Victoria': [0,1,0,0,0,0,0,0],
      'Regionname_Northern Metropolitan':[0,0,1,0,0,0,0,0],
      'Regionname_Northern Victoria':[0,0,0,1,0,0,0,0],
      'Regionname_South-Eastern Metropolitan':[0,0,0,0,1,0,0,0],
      'Regionname_Southern Metropolitan':[0,0,0,0,0,1,0,0],
      'Regionname_Western Metropolitan':[0,0,0,0,0,0,1,0],
      'Regionname_Western Victoria':[0,0,0,0,0,0,0,1]
    })
    df = pd.DataFrame([data], columns=['Room','Date','Distance','Bedroom2','Bathroom','Car','BuildingArea','CouncilArea','Age','Type','Region'])
    df = df.merge(df_type)
    df = df.merge(df_region)
    df = df.drop(['Type','Region'], axis=1)
    return df
    # df.to_csv('d1.csv')

def predict_price(data ,model) :
    poly_reg = PolynomialFeatures(degree=2)
    df_user = preparation(data)
    predict_p = model.predict(poly_reg.fit_transform(df_user))
    return predict_p 