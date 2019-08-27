import os
import numpy as np
from flask import Flask, render_template, request
import pickle

#Prediction function

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, -1)
    loaded_model = pickle.load(open("tues_model2.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_presict_list))

        result = ValuePredictor(to_predict_list)
    return render_template("results.html", prediction=result)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
    