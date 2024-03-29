#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:05:55 2022

@author: aditya
"""

from flask import  Flask,render_template,url_for,request
import pandas as pd
import pickle

## Load the Modal from Disk
loaded_model=pickle.load(open('random_forest_regression_model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('real_2018.csv')
    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction=my_prediction)


if __name__=='__main__':
    app.run(debug=True)