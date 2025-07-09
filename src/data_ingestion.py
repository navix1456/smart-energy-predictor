import pandas as pd
import os

# Absolute path to the local data file
DATA_PATH = r'D:\AI-Powered Energy Predictor\data\individual+household+electric+power+consumption\household_power_consumption.txt'

# Load the dataset (semicolon-separated, header in first row)
df = pd.read_csv(DATA_PATH, sep=';', low_memory=False)

# Print basic info
print('Data shape:', df.shape)
print('Columns:', df.columns.tolist())
print(df.head())

# Save a small sample (first 10,000 rows) for quick testing
sample_path = r'D:\AI-Powered Energy Predictor\data\sample_power_consumption.csv'
df.head(10000).to_csv(sample_path, index=False)
print(f'Sample saved to {sample_path}') 