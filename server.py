from flask import Flask, render_template, request, send_from_directory
from predict_api import predict_price
from sklearn import linear_model
from flask_sqlalchemy import SQLAlchemy
# from server import db
# from static.models.DB import Data
import pickle

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config')
load_model = pickle.load(open("static/models/model.pkl", "rb"))

class Data(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer)
    bedroom = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    buildarea = db.Column(db.Float)
    carspots = db.Column(db.Integer)
    type_p = db.Column(db.String(20))
    distance = db.Column(db.Float)
    region = db.Column(db.String(20))
    councilarea = db.Column(db.Integer)
    age = db.Column(db.Integer)
    year = db.Column(db.Integer)
    price_predict = db.Column(db.Integer)

    def __init__(self, data):
        self.room = data[0]
        self.bedroom = data[1]
        self.bathroom = data[]
        self.buildarea = data[]
        self.carspots = data[2]
        self.type_p = data[3]
        self.distance = data[]
        self.region = data[4]
        self.councilarea = data[]
        self.age = data[]
        self.year = data[5]
        self.price_predict = data[]

@app.route("/", methods=["GET"])
def index() :
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict() :
    data = []
    data.append(request.form['room'])
    data.append(request.form['year'])
    data.append(request.form['distance'])
    data.append(request.form['bedroom'])
    data.append(request.form['bathroom'])
    data.append(request.form['carspots'])
    data.append(request.form['buildarea'])
    data.append(request.form['councilarea'])
    data.append(request.form['age'])
    data.append(request.form['type'])
    data.append(request.form['region'])
    predict_p = predict_price(data, load_model)
    data.append(predict_p)
    data_enter = Data(data = data)
    if request.method == 'POST' :
        try:     
            db.session.add(data_enter)
            db.session.commit()        
            db.session.close()
        except:
            db.session.rollback()
    return render_template("predict.html", prediction = data)

if __name__ == "__main__" :
    app.run(port="3300",debug=True)