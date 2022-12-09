import pickle
from flask import Flask,request,app,jsonify,url_for,render_template

import numpy
import pandas

app = Flask(__name__)

# Load the model

regmodel = pickle(open('regmodel.pkl','rb'))

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    
