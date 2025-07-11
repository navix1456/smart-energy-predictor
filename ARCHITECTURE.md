# Pipeline Architecture – Smart Energy Forecasting Pipeline

## Overview
This architecture describes the flow of data and processing steps for predicting smart home electricity consumption.

## Stages and Tools

1. **Data Ingestion**
   - Download and load the public dataset (e.g., from UCI repository)
   - Tool: Python (pandas)

2. **Data Preprocessing**
   - Clean missing values, handle outliers
   - Feature engineering: create time-based features (hour, day, etc.)
   - Tool: pandas, numpy

3. **Model Training**
   - Train regression models to predict electricity consumption
   - Tool: Scikit-learn
   - Track experiments and parameters
   - Tool: MLflow

4. **Model Evaluation**
   - Evaluate model performance (e.g., RMSE)
   - Select the best model
   - Tool: Scikit-learn, MLflow

5. **Model Deployment**
   - Serve the trained model via a web API
   - Tool: FastAPI

6. **Containerization**
   - Package the application for easy deployment
   - Tool: Docker

7. **CI/CD**
   - Automate testing and deployment pipeline
   - Tool: GitHub Actions (CI/CD)

8. **Cloud Deployment (Future/Optional)**
   - Deploy to AWS Cloud or other providers (future step)

## Data Flow
Dataset → Preprocessing → Model Training → Evaluation → Deployment (API) → Real-time Predictions

---

We have completed all local, Docker, and CI/CD steps. Cloud deployment can be done in the future as needed. 