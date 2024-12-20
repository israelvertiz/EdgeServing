## Overview
The **ML Deployment Generator** is a tool designed to simplify the deployment of machine learning models by generating the required infrastructure and serving code. The application dynamically generates:

- **FastAPI code** for model serving
- **Dockerfile** for containerizing the application
- **Kubernetes deployment files** for scaling the application

### Features:
- Accepts model details and requirements via a REST API.
- Automatically generates all necessary files for deployment.
- Supports both CPU and GPU environments.

---

## Installation Guide

### Prerequisites:
1. **Python 3.9 or higher**
2. **Docker** installed and running
3. **Kubernetes** (optional, for advanced scaling)

### Steps to Install:

1. Clone the repository:
   ```bash
   git clone https://github.com/israelvertiz/EdgeServing.git
   cd EdgeServing
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

### Starting the REST API
Once the application is running, the REST API will be available at:
```
http://localhost:5001
```

### Endpoints:
#### `POST /generate`
Generates deployment files based on the provided JSON payload.

- **Payload**:
```json
{
  "model_path": "model.pkl",
  "framework": "scikit-learn",
  "input_schema": {
    "feature1": "float",
    "feature2": "float",
    "feature3": "int"
  },
  "output_schema": {
    "prediction": "float"
  },
  "compute_type": "CPU"
}
```

- **Response**:
```json
{
  "status": "success",
  "message": "Deployment files generated successfully."
}
```

### Swagger UI
The Swagger UI for the API is available at:
```
http://localhost:5001/docs
```

---

## Generated Files

### Output Directory Structure
All generated files will be saved in the `output` directory:

- `output/main-model.py`: FastAPI code for serving the model.
- `output/Dockerfile`: Dockerfile for containerizing the application.
- `output/k8s-deployment.yaml`: Kubernetes deployment configuration.

### Running the Generated Docker Container
To build and run the Docker container:
```bash
cd output
docker build -t ml-model-api -f Dockerfile .
docker run -p 8000:8000 ml-model-api
```

---

## Example Workflow

1. Save your machine learning model as a pickle file (`model.pkl`).
2. Send a `POST` request to `/generate` with the model details (use the payload example above).
3. Check the `output` directory for the generated files.
4. Build and run the Docker container or deploy using Kubernetes.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
