from app import app, db
from flask import Flask, render_template, request, redirect, url_for, jsonify, get_template_attribute
from app.predict_api import predict_price
from sklearn import linear_model
from app.Db import Data
import pickle

model = pickle.load(open("app/static/models/model.pkl", "rb"))

@app.route("/", methods=["GET"])
def index() :
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict() :
    if request.method == "POST" :
        df_user = request.form.to_dict()
        df_user = list(df_user.values())
        # df_user = request.form['room']
        # df_user = request.form['date']
        # df_user = request.form['distance']
        # df_user = request.form['bedroom']
        # df_user = request.form['bathroom']
        # df_user = request.form['parkinglots']
        # df_user = request.form['buildingarea']
        # df_user = request.form['councilarea']
        # df_user = request.form['age']
        # df_user = request.form['type']
        # df_user = request.form['region']
        predict_p = predict_price(df_user, model)
        # predict_p = 10000
        df_user.append(predict_p)
        # print(df_user)
        data_enter = Data(detail = df_user)
        try : 
            db.session.add(data_enter)
            db.session.commit()        
            db.session.close()
            print("Success")
        except:
            db.session.rollback()
    return render_template("predict.html", predict = df_user)

if __name__ == "__main__" :
    app.run(port="3300",debug=True)