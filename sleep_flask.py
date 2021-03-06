from flask import Flask, request, render_template, redirect, jsonify
import os
import pandas as pd
import json
import numpy as np
import pickle
# create instance of Flask app
app = Flask(__name__)


@app.route("/data")
def data_load():

    return render_template("data.html")



# Set route to homepage
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    # jsondata = request.get_json()
    # data = json.loads(jsondata)

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

    user_dict = pd.DataFrame(user_data)
    print(user_dict)
    ## USE ME! I'M THE RIGHT DATAFRAME! ##
    df = user_dict.transpose()
    print(df)
    # df = df.reset_index(drop=True, inplace=True)
    # df = df.drop(axis=1, label=index)
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    ordered_df = df[["food_spend", "interest", "depression", 
            "sleep_act", "energy", "eating", 
            "failure", "concentrate", "wic", 
            "private_ins", "medicare", "govt_ins", 
            "sleep_hrs", "gender", "race"]]
    print(ordered_df)
    #print(type(user_data))
    #print(user_data)
    #print(user_dict)
    #print(df)
    #print(array)
    encoder.fit(array)
    new_array = encoder.transform(array)


    new_array = new_array.reshape(1, -1)
    #print(new_array)
    prediction = model.predict(new_array)
    #print(prediction)
    #print(prediction[0])
    data = {"prediction": str(prediction[0])}
    #print(data)

    return jsonify(data)
    # return render_template("index.html", data=data)

if __name__ == '__main__':
    encoder = pickle.load(open('original_csv_files/Encoder.sav', 'rb'))
    model = pickle.load(open('original_csv_files/LogRegression.sav', 'rb'))
    app.run(debug=True)
