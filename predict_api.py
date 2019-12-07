def dummy(data) :

    return result
    
def predict_price(data ,model) :
    data = dummy(data)
    predict_p = model.predict(poly_reg.fit_transform(data))
    return predict_p 