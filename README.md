# infinidat-exercise
# My Flask App on Kubernetes
## Introduction
This repository contains a simple Flask application that is containerized using Docker and deployable on a Kubernetes (k8s) cluster. The application includes basic endpoints and demonstrates how to set up a Flask app in a k8s environment.

## Prerequisites
- Docker installed on your machine.
- Access to a Kubernetes cluster.
- kubectl command-line tool installed and configured

## Instructions
1. Build the Docker Image:
'''
docker build -t my-flask-app:latest .
'''
2. Deploying to Kubernetes
Set up the Docker Environment:
If you're using Minikube, you can use its Docker daemon by running:

```
eval $(minikube docker-env)
```
Build the Docker Image in Minikube's Docker Daemon:

```
docker build -t my-flask-app:latest .
```

Create Kubernetes Deployment and Service:
Apply the deployment and service YAML files to your Kubernetes cluster:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
Check the Deployment:
Verify that the deployment was successful:
```
kubectl get deployments
kubectl get pods
```
## Access the Application:
Minikube: Use the following command to get the URL:
Copy code
minikube service flask-app-service
Cloud-based or other Kubernetes Clusters: Access the application via the external IP of your cluster's node combined with the node port defined in flask-service.yaml.
Troubleshooting
Ensure Docker is running before building the image.
Verify that kubectl is correctly configured to interact with your Kubernetes cluster.
Check the logs of the Kubernetes pods if the application is not running as expected:
php
Copy code
kubectl logs <pod-name>
