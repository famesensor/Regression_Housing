from app import app, db
from flask import Flask, render_template, request, send_from_directory
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
    data = []
    data.append(request.form['room'])
    data.append(request.form['date'])
    data.append(request.form['distance'])
    data.append(request.form['bedroom'])
    data.append(request.form['bathroom'])
    data.append(request.form['parkinglots'])
    data.append(request.form['buildingarea'])
    data.append(request.form['councilarea'])
    data.append(request.form['age'])
    data.append(request.form['type'])
    data.append(request.form['region'])
    predict_p = predict_price(data, model)
    data.append(predict_p[0])
    data_enter = Data(detail = data)
    if request.method == "POST":
        try : 
            db.session.add(data_enter)
            db.session.commit()        
            db.session.close()
            print("Inset success")
        except:
            db.session.rollback()
    
    return render_template("predict.html", prediction = data)

if __name__ == "__main__" :
    app.run(port="3300",debug=True)