from typing import Dict, Any
import subprocess


class ContainerBuilder:
    def build_and_run(self):
        print("\n=== Building Docker Image - ContainerBuilder ===")
        subprocess.run(["docker", "build", "-t", "ml-model-api", "-f", "Dockerfile", "."], check=True)
        print("\n=== Running Docker Container - ContainerBuilder ===")
        subprocess.run(["docker", "run", "-p", "8000:8000", "ml-model-api"], check=True)