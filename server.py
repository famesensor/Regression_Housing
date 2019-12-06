from flask import Flask, render_template, request, send_from_directory, send_file
from predict_api import predict_price
from sklearn import linear_model
import pickle

app = Flask(__name__)
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
    # predict_p = predict_price(data, load_model)
    return render_template("predict.html", prediction = data)

if __name__ == "__main__" :
    app.run(port="3300",debug=True)