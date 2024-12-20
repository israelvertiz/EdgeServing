from typing import Dict, Any

class K8sGenerator:
    def __init__(self, model_info: Dict[str, Any]):
        self.model_info = model_info

    def generate(self):
        k8s_yaml = f'''
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-model-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ml-model-api
  template:
    metadata:
      labels:
        app: ml-model-api
    spec:
      containers:
      - name: ml-model-api
        image: ml-model-api
        resources:
          limits:
            {"nvidia.com/gpu": 1 if self.model_info['compute_type'] == 'GPU' else ''}
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: ml-model-service
spec:
  type: LoadBalancer
  selector:
    app: ml-model-api
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
        '''
        with open("k8s-deployment.yaml", "w") as f:
            f.write(k8s_yaml)