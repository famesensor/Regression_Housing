from flask import Flask, render_template, request, send_from_directory
from predict_api import predict_price
from sklearn import linear_model
from flask_sqlalchemy import SQLAlchemy
from server import db
from static.models.DB import Data
import pickle

app = Flask(__name__)
app.config.from_object('config')
load_model = pickle.load(open("static/models/model.pkl", "rb"))

@app.route("/", methods=["GET"])
def index() :
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict() :
    data = []
    data.append(request.form['room'])
    data.append(request.form['bedroom'])
    data.append(request.form['carspots'])
    data.append(request.form['type'])
    data.append(request.form['region'])
    data.append(request.form['year'])
    data_enter = Data(notes = data)
    if request.method == 'POST' :
        try:     
            db.session.add()
            db.session.commit()        
            db.session.close()
        except:
            db.session.rollback()
    # predict_p = predict_price(data, load_model)
    return render_template("predict.html", prediction = data)

if __name__ == "__main__" :
    app.run(port="3300",debug=True)