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
    df["food_spend"]= encoder1.transform(df["food_spend"])
    df["interest"]= encoder2.transform(df["interest"])
    df["depression"]= encoder3.transform(df["depression"])
    df["sleep_act"]= encoder4.transform(df["sleep_act"])
    df["energy"]= encoder5.transform(df["energy"])
    df["eating"]= encoder6.transform(df["eating"])
    df["failure"]= encoder7.transform(df["failure"])
    df["concentrate"]= encoder8.transform(df["concentrate"])
    df["wic"]= encoder9.transform(df["wic"])
    df["private_ins"]= encoder10.transform(df["private_ins"])
    df["medicare"]= encoder11.transform(df["medicare"])
    df["govt_ins"]= encoder12.transform(df["govt_ins"])
    df["sleep_hrs"]= encoder13.transform(df["sleep_hrs"])
    df["gender"]= encoder14.transform(df["gender"])
    df["race"]= encoder15.transform(df["race"])

    from scipy import sparse
    df = sparse.coo_matrix(df)
    prediction = model.predict(df)

    #print(type(user_data))
    #print(user_data)
    #print(user_dict)
    #print(df)
    #print(array)
    # encoder.fit(array)
    # new_array = encoder.transform(array)


    # new_array = new_array.reshape(1, -1)
    #print(new_array)
    # prediction = model.predict(new_array)
    #print(prediction)
    #print(prediction[0])
    data = {"prediction": str(prediction)}
    #print(data)

    return jsonify(data)
    # return render_template("index.html", data=data)

if __name__ == '__main__':
    encoder1 = pickle.load(open('original_csv_files/leCBD130.sav', 'rb'))
    encoder2 = pickle.load(open('original_csv_files/leDPQ010.sav', 'rb'))
    encoder3 = pickle.load(open('original_csv_files/leDPQ020.sav', 'rb'))
    encoder4 = pickle.load(open('original_csv_files/leDPQ030.sav', 'rb'))
    encoder5 = pickle.load(open('original_csv_files/leDPQ040.sav', 'rb'))
    encoder6 = pickle.load(open('original_csv_files/leDPQ050.sav', 'rb'))
    encoder7 = pickle.load(open('original_csv_files/leDPQ060.sav', 'rb'))
    encoder8 = pickle.load(open('original_csv_files/leDPQ070.sav', 'rb'))
    encoder9 = pickle.load(open('original_csv_files/leFSQ162.sav', 'rb'))
    encoder10 = pickle.load(open('original_csv_files/leHIQ031A.sav', 'rb'))
    encoder11 = pickle.load(open('original_csv_files/leHIQ031B.sav', 'rb'))
    encoder12 = pickle.load(open('original_csv_files/leHIQ031I.sav', 'rb'))
    encoder13 = pickle.load(open('original_csv_files/leSLD010H.sav', 'rb'))
    encoder14 = pickle.load(open('original_csv_files/leRIAGENDR.sav', 'rb'))
    encoder15 = pickle.load(open('original_csv_files/leRIDRETH1.sav', 'rb'))
    model = pickle.load(open('original_csv_files/LogRegression.sav', 'rb'))
    app.run(debug=True)
