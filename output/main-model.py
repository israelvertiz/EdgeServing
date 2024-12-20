
from fastapi import FastAPI, HTTPException
import joblib
import os
import uvicorn
import json

app = FastAPI(title="ML Model API")

# Load model
MODEL_PATH = "model.pkl"
MODEL = joblib.load(MODEL_PATH)

@app.post("/predict")
def predict(input_data: dict):
    try:
        # Extract input features
        input_features = [input_data[key] for key in ["feature1", "feature2", "feature3"]]
        
        # Predict using the model
        prediction = MODEL.predict([input_features])[0]

        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
        