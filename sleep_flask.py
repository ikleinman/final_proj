from flask import Flask, request, render_template, redirect, jsonify
import os
import pandas as pd

# create instance of Flask app
app = Flask(__name__)

@app.route("/data")
def data_load():

    #data = model.data()
    return render_template("data.html")

# Connect to a database. Will create one if not already available.

# Set route to homepage
@app.route("/")
def home():

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
