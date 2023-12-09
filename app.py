from flask import Flask,redirect,url_for,render_template,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import joblib

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')



@app.route('/solar')
def solar(): 
    return render_template('ss.html')

@app.route('/contact')
def contact(): 
    return render_template('contact.html')

@app.route('/explore/<sec>')
def explore(sec):
    return render_template('explore.html', section_id=sec)



# Load the trained model
model = load_model('knn_model.h5')



# FILEPATH: /app.py
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve values from the form
        pl_orbper = request.form['pl_orbper']
        pl_rade = request.form['pl_rade']
        pl_orbeccen = request.form['pl_orbeccen']
        pl_orbincl = request.form['pl_orbincl']
        pl_tranmid = request.form['pl_tranmid']
        pl_imppar = request.form['pl_imppar']
        pl_trandep = request.form['pl_trandep']
        pl_trandur = request.form['pl_trandur']
        pl_ratdor = request.form['pl_ratdor']
        pl_ratror = request.form['pl_ratror']
        sy_vmag = request.form['sy_vmag']
        sy_kmag = request.form['sy_kmag']

        # Perform calculations or processing to determine ttv_flag
        ttv_flag = calculate_ttv_flag(pl_orbper, pl_rade, pl_orbeccen, pl_orbincl, pl_tranmid, pl_imppar, pl_trandep, pl_trandur, pl_ratdor, pl_ratror, sy_vmag, sy_kmag)

        # Pass ttv_flag to the template
        return render_template('explore.html', ttv_flag=ttv_flag)

    # Render the form on initial page load
    return render_template('explore.html')

def calculate_ttv_flag(pl_orbper, pl_rade, pl_orbeccen, pl_orbincl, pl_tranmid, pl_imppar, pl_trandep, pl_trandur, pl_ratdor, pl_ratror, sy_vmag, sy_kmag):
        # Perform calculations or processing to determine ttv_flag
    # For example, you can set ttv_flag based on some conditions
    ttv_flag = 0  # Replace None with your logic

    return ttv_flag


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)