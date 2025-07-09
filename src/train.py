import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import os

# Paths
DATA_PATH = r'D:\AI-Powered Energy Predictor\data\preprocessed_power_consumption.csv'
MODEL_PATH = r'D:\AI-Powered Energy Predictor\models\linear_regression_model.joblib'

# Load preprocessed data
print('Loading preprocessed data...')
df = pd.read_csv(DATA_PATH)

# Features and target
y = df['Global_active_power']
X = df.drop(['Global_active_power', 'Datetime'], axis=1)

# Split into train and test sets
print('Splitting data...')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print('Training Linear Regression model...')
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
print('Evaluating model...')
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error on test set: {mse:.4f}')

# Save the model
print(f'Saving model to {MODEL_PATH}')
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)
print('Done!') 