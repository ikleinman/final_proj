from flask import Flask, request, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
import os
import pandas as pd

# create instance of Flask app
app = Flask(__name__)

sleep_df = pd.read_csv("final_project.csv")
jsonfiles = json.loads(sleep_df.to_json())

@app.route("/data")
def data_load():

    return jsonify(jsonfiles)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/"
#mongo = PyMongo(app)


# create our session link to our DataFrame




if __name__ == '__main__':
    app.run(debug=True)
