from flask import Flask, render_template, request, send_from_directory, send_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index() :
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict() :
    

if __name__ == "__main__" :
    app.run(port="3300",debug=True)