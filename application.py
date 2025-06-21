from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

model = pickle.load(open('model/Netflix Stock Prediction Model.pkl','rb'))
scaler = pickle.load(open('model/Scaler model.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)