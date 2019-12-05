from flask import Flask, render_template, request, send_from_directory, send_file
from predict_api import predict_price
import pickle

app = Flask(__name__)
load_model = pickle.load(open("static/models/model.pkl", "rb"))

@app.route("/", methods=["GET"])
def index() :
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict() :
    data = 0 
    predict_price(data, load_model)
    return render_template("predict.html")

if __name__ == "__main__" :
    app.run(port="3300",debug=True)