
# Use lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy API code and model
COPY output/main-model.py ./
COPY model.pkl ./

# Install dependencies
RUN pip install fastapi uvicorn joblib scikit-learn

# Expose port 8000
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main-model:app", "--host", "0.0.0.0", "--port", "8000"]
        