from flask import Flask, request, render_template, redirect, jsonify
import os
import pandas as pd
import json
import numpy as np
import pickle
# create instance of Flask app
app = Flask(__name__)

#model = #model from python

@app.route("/data")
def data_load():

    return render_template("data.html")

# Connect to a database. Will create one if not already available.

# Set route to homepage
@app.route("/")
def home():
    #data = model.data()
    return render_template("index.html") #prediction=prediction)

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    # jsondata = request.get_json()
    # data = json.loads(jsondata)

    # #stuff happens here that involves data to obtain a result

    # result = {'escalate': True}
    # return json.dumps(result)
    return tmp("/", code=302)

@app.route("/response", methods = ["POST"])
def predict():
    # if request.method == "POST":
    #     try:
    user_submission = request.get_data()
    values = user_submission[:]
    user_data = json.loads(user_submission)
    array = []
    for d in user_data:
        for key in d:
            if key == 'value':
                array.append(d['value'])
    print(type(user_data))
    print(user_data)
    print(array)
    # prediction = model.predict(user_submission)
    # res = dict()
    # for value in user_submission.value():
    #     res[value] = 
    # array = np.array(user_submission['value'])
        # except ValueError:
        #     return jsonify("Please try again.")
    #print(user_data)
    #print(jsonify(user_data))
    return (jsonify(user_data))

if __name__ == '__main__':
    model = pickle.load(open('original_csv_files/LogRegression.sav', 'rb'))
    app.run(debug=True)
