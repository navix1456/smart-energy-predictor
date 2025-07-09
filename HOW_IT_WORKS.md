# How It Works – Smart Energy Forecasting Pipeline

## End-to-End Flow
1. **Data Ingestion**: Loads the UCI household power consumption dataset.
2. **Preprocessing**: Cleans the data, handles missing values, and creates time-based features (hour, day, weekday, month).
3. **Model Training**: Trains a linear regression model to predict electricity consumption using historical and environmental features.
4. **Evaluation**: Evaluates model performance (MSE, R²) and visualizes actual vs. predicted values.
5. **API Deployment**: Serves predictions and explanations via a FastAPI app.
6. **Explainability**: Each prediction includes the top contributing features and whether the value is above or below the dataset average.
7. **Feature Importance**: The API provides a global view of which features most influence the model.
8. **Containerization & CI/CD**: The app is packaged with Docker and tested/built automatically with GitHub Actions.
9. **Cloud deployment is a future/optional step.**

## API Endpoints
- **POST /predict**
  - Input: JSON with feature values (see docs for schema)
  - Output: Predicted electricity consumption, top contributing features, comparison to average
- **GET /feature-importance**
  - Output: Global feature importance (model coefficients)
- **GET /**
  - Output: Health check message

## How to Interpret Results
- **Prediction**: The estimated electricity consumption for the given input features.
- **Top Contributing Features**: The features that most influenced the prediction (positive or negative impact).
- **Global Average**: The average consumption in the dataset; use this to see if your prediction is high or low.
- **Feature Importance**: Shows which features the model relies on most overall.

## Example Use Cases
- Real-time energy monitoring for smart homes
- Energy-saving recommendations based on feature impact
- Educational tool for learning ML pipelines and explainability

---
For more details, see the API docs at `/docs` after running the app. 