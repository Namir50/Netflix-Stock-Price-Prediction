from flask import Flask,request,jsonify,render_template,redirect, url_for, session
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application
app.secret_key = 'hello'

model = pickle.load(open('model/Netflix Stock Prediction Model.pkl','rb'))
scaler = pickle.load(open('model/Scaler model.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods = ['GET','POST'])
def predictdatapoint():
    if request.method == 'POST':
        open = float(request.form.get('Open'))
        high = float(request.form.get('High'))
        low = float(request.form.get('Low'))
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        day = int(request.form.get('day'))
        
        scaled_data = scaler.transform([[open,high,low,year,month,day]])
        result = round(model.predict(scaled_data)[0], 2)
        
        session['result'] = result
        return redirect(url_for('predictdatapoint'))
        
    result = session.pop('result','')
    return render_template('home.html',result = result)

    
    

if __name__ == '__main__':
    app.run(debug=True)