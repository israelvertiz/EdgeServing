import os
import json
import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from typing import Dict, Any
import uvicorn

from modules.api_generator import ApiGenerator
from modules.dockerfile_generator import DockerfileGenerator
from modules.k8s_generator import K8sGenerator
from modules.container_builder import ContainerBuilder

app = FastAPI(title="ML Deployment Generator API", version="1.0", description="API to generate ML deployment files dynamically.")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.post("/generate", summary="Generate ML Deployment Files", description="Generates FastAPI code, Dockerfile, and Kubernetes YAML dynamically based on input JSON requirements.")
def generate_model_deployment(model_requirements: Dict[str, Any]):
    """
    Generates FastAPI code, Dockerfile, and Kubernetes YAML dynamically based on input JSON requirements.
    - **model_path**: Path to the model file.
    - **framework**: ML framework (e.g., scikit-learn, tensorflow).
    - **input_schema**: Input schema for prediction.
    - **output_schema**: Output schema for prediction.
    - **compute_type**: Type of compute required (CPU/GPU).
    """
    try:
        # Parse model requirements
        model_info = model_requirements

        print("\n=== Generating API Code ===")
        api_generator = ApiGenerator(model_info)
        api_generator.generate()

        print("\n=== Generating Dockerfile ===")
        dockerfile_generator = DockerfileGenerator(model_info)
        dockerfile_generator.generate()

        print("\n=== Building Docker Image and Running ===")
        container_builder = ContainerBuilder()
        container_builder.build_and_run()

        print("\n=== Generating Kubernetes YAML ===")
        k8s_generator = K8sGenerator(model_info)
        k8s_generator.generate()

        return {"status": "success", "message": "Deployment files generated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print("\n=== Starting REST API for ML Deployment Generation ===")
    uvicorn.run(app, host="0.0.0.0", port=5001)

