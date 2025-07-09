# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements (to be created) and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY ./src ./src
COPY ./models ./models
COPY ./data ./data

# Expose port for FastAPI
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"] 