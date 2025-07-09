from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import pandas as pd

# Use relative paths for Docker compatibility
MODEL_PATH = 'models/linear_regression_model.joblib'
DATA_PATH = 'data/preprocessed_power_consumption.csv'

# Load the trained model and data
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

global_avg = float(df['Global_active_power'].mean())
feature_names = [
    'Global_reactive_power', 'Voltage', 'Global_intensity',
    'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3',
    'hour', 'day', 'weekday', 'month'
]

# Define the input data schema
class PredictionInput(BaseModel):
    Global_reactive_power: float
    Voltage: float
    Global_intensity: float
    Sub_metering_1: float
    Sub_metering_2: float
    Sub_metering_3: float
    hour: int
    day: int
    weekday: int
    month: int

app = FastAPI()

@app.post('/predict')
def predict(input: PredictionInput):
    # Prepare the input for prediction
    input_list = [
        input.Global_reactive_power, input.Voltage, input.Global_intensity,
        input.Sub_metering_1, input.Sub_metering_2, input.Sub_metering_3,
        input.hour, input.day, input.weekday, input.month
    ]
    features = np.array([input_list])
    prediction = float(model.predict(features)[0])

    # Simple explanation: contribution of each feature
    coefs = model.coef_
    contributions = {name: float(val * coef) for name, val, coef in zip(feature_names, input_list, coefs)}
    top_features = sorted(contributions.items(), key=lambda x: abs(x[1]), reverse=True)[:3]
    explanation = {
        'top_contributing_features': top_features,
        'global_average': global_avg,
        'above_average': bool(prediction > global_avg)
    }
    return {
        "predicted_global_active_power": prediction,
        "explanation": explanation
    }

@app.get('/feature-importance')
def feature_importance():
    coefs = model.coef_
    importance = {name: float(coef) for name, coef in zip(feature_names, coefs)}
    sorted_importance = dict(sorted(importance.items(), key=lambda x: abs(x[1]), reverse=True))
    return {"feature_importance": sorted_importance}

@app.get('/')
def root():
    return {"message": "Smart Energy Predictor API is running."} 