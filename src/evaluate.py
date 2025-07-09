import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Paths
DATA_PATH = r'D:\AI-Powered Energy Predictor\data\preprocessed_power_consumption.csv'
MODEL_PATH = r'D:\AI-Powered Energy Predictor\models\linear_regression_model.joblib'

# Load data and model
print('Loading data and model...')
df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

# Features and target
y = df['Global_active_power']
X = df.drop(['Global_active_power', 'Datetime'], axis=1)

# Split into train and test sets (same as before)
_, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict
y_pred = model.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse:.4f}')
print(f'R^2 Score: {r2:.4f}')

# Plot actual vs predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.3)
plt.xlabel('Actual Global Active Power')
plt.ylabel('Predicted Global Active Power')
plt.title('Actual vs Predicted Global Active Power')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.tight_layout()
plt.show() 