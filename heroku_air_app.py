import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

#Define a prediction function.

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, -1)
    loaded_model = pickle.load(open("wednesday_model_1_random_forest.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))

        result = ValuePredictor(to_predict_list)
    return render_template("results.html", prediction=round(int(result)))

if __name__ == '__main__':
    app.run(port = 4500, debug = True)
