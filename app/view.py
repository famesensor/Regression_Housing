from app import app, db
from flask import Flask, render_template, request, redirect, url_for, jsonify, get_template_attribute
from app.predict_api import predict_price, changedata
from sklearn import linear_model
from app.Db import Data
import pickle

model = pickle.load(open("app/static/models/model.pkl", "rb"))

@app.route("/", methods=["GET"])
def index() :
    return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict() :
#     if request.method == "POST" :
#         df_user = []
#         # df_user = request.form.to_dict()
#         # df_user = list(df_user.values())
#         df_user.append(request.form['room'])
#         df_user.append(request.form['date'])
#         df_user.append(request.form['distance'])
#         df_user.append(request.form['bedroom'])
#         df_user.append(request.form['bathroom'])
#         df_user.append(request.form['parkinglots'])
#         df_user.append(request.form['buildingarea'])
#         df_user.append(request.form['councilarea'])
#         df_user.append(request.form['age'])
#         df_user.append(request.form['type'])
#         df_user.append(request.form['region'])
#         predict_p = predict_price(df_user, model)
#         # predict_p = 10000
#         df_user.append(predict_p)
#         df_user = changedata(df_user)
#         print(df_user)
#         data_enter = Data(detail = df_user)
#         try : 
#             db.session.add(data_enter)
#             db.session.commit()        
#             db.session.close()
#             print("Success")
#         except:
#             db.session.rollback()

#     # return jsonify({'price' : predict_p})
#     return render_template("predict.html", predict = df_user)

@app.route('/process', methods=['POST'])
def process():
    df_user = []
    df_user.append(request.form['room'])
    df_user.append(request.form['date'])
    df_user.append(request.form['distance'])
    df_user.append(request.form['bedroom'])
    df_user.append(request.form['bathroom'])
    df_user.append(request.form['parkinglots'])
    df_user.append(request.form['buildingarea'])
    df_user.append(request.form['coun'])
    df_user.append(request.form['age'])
    df_user.append(request.form['type'])
    df_user.append(request.form['region'])
    if request.method == "POST" : 
        predict_p = predict_price(df_user, model)
        df_user.append(predict_p)
        df_user = changedata(df_user)
        data_enter = Data(detail = df_user)
        try : 
            db.session.add(data_enter)
            db.session.commit()        
            db.session.close()
            print("Success")
        except:
            db.session.rollback()
        return jsonify({'price' : predict_p})
    else :
	    return jsonify({'error' : 'Fail!'})

if __name__ == "__main__" :
    app.run(port="3300",debug=True)