from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle
import numpy as np
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/predict',methods = ['POST'])
def predict():
    input_json = request.get_json()
    data = []
    for key,val in input_json.items():
        data.append(val)
    print(data)
    data = np.array(data).reshape(1, -1)
    modelfile = '/var/house_price_prediction/models/rf.pkl'
    model = pickle.load(open(modelfile, 'rb'))

    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')