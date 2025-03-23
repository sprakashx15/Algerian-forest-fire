import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify, render_template, Response

application = Flask(__name__)
app = application

# Importing pickle files (ridge_regressor and standard scaler pickle)
ridge_model = pickle.load(open('model/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('model/standard_scaler.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        
        # Extract form data
        temperature = request.form.get('temperature')
        humidity = request.form.get('humidity')
        wind = request.form.get('wind')
        rain = request.form.get('rain')
        ffmc = request.form.get('ffmc')
        dmc = request.form.get('dmc')
        isi = request.form.get('isi')
        classes=request.form.get('classes')
        
        # Check for missing values
        if None in [temperature, humidity, wind, rain, ffmc, dmc, isi,classes]:
            return Response("Error: One or more input values are missing", status=400)
        
        try:
            # Convert values to float
            Temperature = float(temperature)
            RH = float(humidity)
            WS = float(wind)
            Rain = float(rain)
            FFMC = float(ffmc)
            DMC = float(dmc)
            ISI = float(isi)
            Classes=float(classes)

        except ValueError:
            return Response("Error: Invalid input type. Please enter numeric values.", status=400)
        
        # Transform input data
        new_data = standard_scaler.transform([[Temperature,RH, WS, Rain, FFMC, DMC, ISI,Classes]])
        result = ridge_model.predict(new_data)
        
        return render_template('home.html', results=result[0])
    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
