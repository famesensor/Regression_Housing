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
    # print(df)
    return df

def predict_price(data ,model) :
    poly_reg = PolynomialFeatures(degree=2)
    df_user = preparation(data)
    predict_p = model.predict(poly_reg.fit_transform(df_user))
    return predict_p[0]

def changedata(data) :
    result = data
    df_type = {'h':'House', 't':'Townhouse', 'u':'Unit'}
    df_con = {1:'Banyule City Council',
        2:'Bayside City Council',
        3:'Boroondara City Counci',
        4:'Brimbank City Council',
        5:'Cardinia Shire Council',
        6:'Casey City Council',
        7:'Darebin City Council',
        8:'Frankston City Council',
        9:'Glen Eira City Council',
        10:'Greater Dandenong City Council',
        11:'Hobsons Bay City Council',
        12:'Hume City Council',
        13:'Kingston City Council',
        14:'Knox City Council',
        15:'Macedon Ranges Shire Council',
        16:'Manningham City Council',
        17:'Maribyrnong City Council',
        18:'Maroondah City Council',
        19:'Melbourne City Council',
        20:'Melton City Council',
        21:'Mitchell Shire Council',
        22:'Monash City Council',
        23:'Moonee Valley City Council',
        24:'Moorabool Shire Council',
        25:'Moreland City Council',
        26:'Nillumbik Shire Council',
        27:'Port Phillip City Council',
        28:'Stonnington City Council',
        29:'Whitehorse City Council',
        30:'Whittlesea City Council',
        31:'Wyndham City Council',
        32:'Yarra City Council',
        33:'Yarra Ranges Shire Council'
    }
    for k,v in df_type.items() :
        if result[9] == k :
            result[9] = v
            break
    for k,v in df_con.items() :
        if int(result[7]) == k :
            result[7] = v
            break
    return result