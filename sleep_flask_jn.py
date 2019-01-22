from flask import Flask, request, render_template, redirect, jsonify
import os
import pandas as pd

# create instance of Flask app
app = Flask(__name__)

#model = #model from python

@app.route("/data")
def data_load():

    return render_template("data.html")

    #return tmp("/", code=302)
# Connect to a database. Will create one if not already available.

# Set route to homepage
@app.route("/", methods = ['GET'])
def home():
    #data = model.data()
    return render_template("index.html") #prediction=prediction)
    jsondata = request.get_json()
    data = json.loads(jsondata)

    #stuff happens here that involves data to obtain a result

    result = {'escalate': True}
    return json.dumps(result)
#@app.route("/submit", methods = ['GET'])
#def submit():
#    jsondata = request.get_json()
#    data = json.loads(jsondata)

    #stuff happens here that involves data to obtain a result

#    result = {'escalate': True}
#    return json.dumps(result)
    #return tmp("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)
