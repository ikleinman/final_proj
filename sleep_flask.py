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
    encoder.fit(array)
    new_array = encoder.transform(array)
    print(new_array)
    # array = map(int, array)
    # new_array = np.array(new_array)
    # new_array = [new_array]
    new_array = new_array.reshape(1, -1)
    print(new_array)
    prediction = model.predict(new_array)
    print(prediction)
    print(prediction[0])
    data = {"prediction": str(prediction[0])}
    print(data)
    # res = dict()
    # for value in user_submission.value():
    #     res[value] =
    # array = np.array(user_submission['value'])
        # except ValueError:
        #     return jsonify("Please try again.")
    # return jsonify(data)
    return render_template("index.html", data=data)

if __name__ == '__main__':
    encoder = pickle.load(open('original_csv_files/Encoder.sav', 'rb'))
    model = pickle.load(open('original_csv_files/LogRegression.sav', 'rb'))
    app.run(debug=True)
