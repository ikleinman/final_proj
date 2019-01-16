from flask import Flask, request, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import json
import os

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = #"mongodb://localhost:27017/wine_app"
mongo = PyMongo(app)

data = #our data set.data()





if __name__ == '__main__':
    app.run(debug=True)
