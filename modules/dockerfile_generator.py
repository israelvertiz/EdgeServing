from typing import Dict, Any

class DockerfileGenerator:
    def __init__(self, model_info: Dict[str, Any]):
        self.model_info = model_info

    def generate(self):
        dockerfile_content = f'''
# Use lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy API code and model
COPY output/main-model.py ./
COPY {self.model_info['model_path']} ./

# Install dependencies
RUN pip install fastapi uvicorn joblib {self.model_info['framework']}

# Expose port 8000
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main-model:app", "--host", "0.0.0.0", "--port", "8000"]
        '''
        with open("Dockerfile", "w") as f:
            f.write(dockerfile_content)