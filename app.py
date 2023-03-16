import pickle
from flask import Flask, jsonify, render_template, request, url_for
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder="templates")

#app = Flask(__name__)  # starting point of flask

#Loading the model
model = pickle.load(open("regressionModel.pkl","rb")) 
scalar = pickle.load(open("scaling.pkl","rb")) 



@app.route("/")
def home():
    return render_template("home.html")  #Once I hit the flask app, it redirects to html page

@app.route("/predict_api", methods = ["POST"])

def predict_api():
    data= request.json["data"]  #when I hit the api, json input given and data is returned by api
    print(list(data.values()))
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route("/predict", methods = ["POST"])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input  = scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = model.predict(final_input)[0]
    return render_template("home.html", Prediction_text = "The House Price Prediction is $ {}".format(round(output*1000,2)))

if __name__ == "__main__":
    app.run(debug = True)

