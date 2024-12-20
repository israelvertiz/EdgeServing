import json
from typing import Dict, Any

class ApiGenerator:
    def __init__(self, model_info: Dict[str, Any]):
        self.model_info = model_info

    def generate(self):
        api_code = f'''
from fastapi import FastAPI, HTTPException
import joblib
import os
import uvicorn
import json

app = FastAPI(title="ML Model API")

# Load model
MODEL_PATH = "{self.model_info['model_path']}"
MODEL = joblib.load(MODEL_PATH)

@app.post("/predict")
def predict(input_data: dict):
    try:
        # Extract input features
        input_features = [input_data[key] for key in {json.dumps(list(self.model_info['input_schema'].keys()))}]
        
        # Predict using the model
        prediction = MODEL.predict([input_features])[0]

        return {{"prediction": prediction}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
        '''
        with open("./output/main-model.py", "w") as f:
            f.write(api_code)
