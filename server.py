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
    carspots = db.Column(db.Integer)
    type_p = db.Column(db.String(20))
    region = db.Column(db.String(20))
    year = db.Column(db.Integer)

    def __init__(self, notes):
        self.room = notes[0]
        self.bedroom = notes[1]
        self.carspots = notes[2]
        self.type_p = notes[3]
        self.region = notes[4]
        self.year = notes[5]

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
            db.session.add(data_enter)
            db.session.commit()        
            db.session.close()
        except:
            db.session.rollback()
    # predict_p = predict_price(data, load_model)
    return render_template("predict.html", prediction = data)

if __name__ == "__main__" :
    app.run(port="3300",debug=True)