import pickle
import flask, requests, app, jsonify, url_for, render_template
import numpy
import pandas as pd

app = Flask(__name__)  # starting point of flask

model = pickle.load(open("regression.pkl","rb")) #Loading the model

@app.route("/")
def home():
    return render_template("home.html")  #Once I hit the flask app, it redirects to html page

@app.route("/predict_api", methods = ["POST"])

def predict_api():
    data= request.json["data"]  #when I hit the api, json input given 
    print(data)
