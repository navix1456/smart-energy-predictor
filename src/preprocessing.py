import pandas as pd
import numpy as np

# Path to the sample data
DATA_PATH = r'D:\AI-Powered Energy Predictor\data\sample_power_consumption.csv'
OUTPUT_PATH = r'D:\AI-Powered Energy Predictor\data\preprocessed_power_consumption.csv'

# Load the data
print('Loading data...')
df = pd.read_csv(DATA_PATH, sep=',')

# Combine Date and Time into a single datetime column
print('Converting date and time...')
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M:%S', errors='coerce')
df = df.drop(['Date', 'Time'], axis=1)

# Handle missing values: replace '?' with NaN, then convert columns to float
print('Handling missing values and converting numerics...')
df = df.replace('?', np.nan)
for col in df.columns:
    if col != 'Datetime':
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with any missing values (for simplicity)
df = df.dropna()

# Create time-based features
print('Creating time-based features...')
df['hour'] = df['Datetime'].dt.hour
df['day'] = df['Datetime'].dt.day
df['weekday'] = df['Datetime'].dt.weekday
df['month'] = df['Datetime'].dt.month

df = df.reset_index(drop=True)

# Save the preprocessed data
print(f'Saving preprocessed data to {OUTPUT_PATH}')
df.to_csv(OUTPUT_PATH, index=False)
print('Done!') 