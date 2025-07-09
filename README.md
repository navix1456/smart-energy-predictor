# Smart Energy Forecasting Pipeline

A beginner-friendly project to predict smart home electricity consumption using machine learning. The pipeline covers data ingestion, preprocessing, model training, evaluation, and deployment as a real-time API with explainability.

## Features
- Uses public datasets (UCI household power consumption)
- Built with Python, Scikit-learn, MLflow, FastAPI
- Real-time prediction API with feature importance and explanations
- Containerized with Docker
- CI/CD with GitHub Actions
- Deployable to AWS Cloud

## Project Structure
```
AI-Powered Energy Predictor/
├── data/                # Raw and processed data
├── notebooks/           # Jupyter notebooks for exploration
├── src/                 # Source code (modules, training, API)
│   ├── data_ingestion.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── api.py
├── models/              # Saved models
├── mlruns/              # MLflow experiment tracking
├── tests/               # Unit and integration tests
├── Dockerfile           # Containerization
├── requirements.txt     # Python dependencies
├── README.md            # Project overview and instructions
├── PROJECT_PLAN.md      # Step-by-step plan
├── REQUIREMENTS.md      # Project requirements
├── ARCHITECTURE.md      # Pipeline architecture
└── .github/workflows/ci.yml # CI/CD workflow
```

## How It Works
1. **Data Ingestion:** Download and load the UCI dataset.
2. **Preprocessing:** Clean data, handle missing values, create time-based features.
3. **Model Training:** Train a regression model to predict electricity consumption.
4. **Evaluation:** Assess model performance and visualize results.
5. **API Deployment:** Serve predictions and explanations via FastAPI.
6. **Containerization:** Package the app with Docker for easy deployment.
7. **CI/CD:** Automated testing and Docker build with GitHub Actions.

## Getting Started
### 1. Clone the repository
```
git clone https://github.com/your-username/smart-energy-predictor.git
cd smart-energy-predictor
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the pipeline locally
- Data ingestion: `python src/data_ingestion.py`
- Preprocessing: `python src/preprocessing.py`
- Training: `python src/train.py`
- Evaluation: `python src/evaluate.py`
- Start API: `uvicorn src.api:app --reload`
- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API

### 4. Run with Docker
```
docker build -t smart-energy-predictor .
docker run -p 8000:8000 smart-energy-predictor
```
- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5. CI/CD
- On every push to `main`, GitHub Actions will run the pipeline and build the Docker image.

## API Usage
- **POST /predict**: Get a prediction and explanation for your input features.
- **GET /feature-importance**: See which features most influence the model.

## Deployment
- Ready for deployment to AWS (Elastic Beanstalk, ECS, etc.)

---
This project is designed for learning and can be extended for real-world smart home energy applications. 