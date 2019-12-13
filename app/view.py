from app import app, db
from flask import Flask, render_template, request, redirect, url_for, jsonify, get_template_attribute
from app.predict_api import predict_price, changedata
from sklearn import linear_model
from app.Db import Data
import pickle

model = pickle.load(open("app/static/models/model.pkl", "rb"))

@app.route("/", methods=["GET"])
def index() :
    query_db = Data.query.order_by(Data.id.desc()).limit(10)
    # for q in query_db :
    #     print(q.room)
    return render_template("index.html", query = query_db)

@app.route("/predict", methods=["POST"])
def predict() :
    if request.method == "POST" :
        df_user = []
        # df_user = request.form.to_dict()
        # df_user = list(df_user.values())
        df_user.append(request.form['room'])
        df_user.append(request.form['date'])
        df_user.append(request.form['distance'])
        df_user.append(request.form['bedroom'])
        df_user.append(request.form['bathroom'])
        df_user.append(request.form['parkinglots'])
        df_user.append(request.form['buildingarea'])
        df_user.append(request.form['councilarea'])
        df_user.append(request.form['age'])
        df_user.append(request.form['type'])
        df_user.append(request.form['region'])
        predict_p = predict_price(df_user, model)
        print(predict_price(df_user, model))
        # predict_p = 10000
        df_user.append(int(predict_p))
        df_user = changedata(df_user)
        # print(df_user)
        # data_enter = Data(detail = df_user)
        # try : 
        #     db.session.add(data_enter)
        #     db.session.commit()        
        #     db.session.close()
        #     print("Success")
        # except:
        #     db.session.rollback()
    query_db = Data.query.order_by(Data.id.desc()).limit(10)

    # return jsonify({'price' : predict_p})
    return render_template("predict.html", predict = df_user, query = query_db)

# @app.route('/process', methods=['POST'])
# def process():

# 	email = request.form['room']
# 	name = request.form['date']

# 	if name and email:
# 		newName = name[::-1]

# 		return jsonify({'name' : newName})

# 	return jsonify({'error' : 'Missing data!'})

if __name__ == "__main__" :
    app.run(port="3300",debug=True)