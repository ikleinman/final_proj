from flask import Flask, request, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
import os
import pandas as pd
import pymongo

# create instance of Flask app
app = Flask(__name__)

sleep_df = pd.read_csv("final_project.csv")
jsonfiles = json.loads(sleep_df.to_json())

@app.route("/data")
def data_load():

    return jsonify(jsonfiles)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/final_project_test"
#mongo = PyMongo(app)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.final_project_test

# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    data = list(db.final_project_test.find())
    print(data)

    # Return the template with the teams list passed in
    return render_template('index.html', data=data)




if __name__ == '__main__':
    app.run(debug=True)
