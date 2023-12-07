# infinidat-exercise
## Introduction
This repository contains a simple Flask application that is containerized using Docker and deployable on a Kubernetes (k8s) cluster. The application includes basic endpoints and demonstrates how to set up a Flask app in a k8s environment.

## Prerequisites
- Docker installed on your machine.
- Access to a Kubernetes cluster.
- kubectl command-line tool installed and configured

## Instructions
1. Clone the repository and move to the directory.
```
git clone https://github.com/shaharshurki/infinidat-exercise.git
cd infinidat-exercise
```
2. Build the Docker Image:
```
docker build -t my-flask-app:latest .
```
3. Deploying to Kubernetes
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
*Minikube*: Use the following command to get the URL:
```
minikube service flask-app-service
```
*Cloud-based or other Kubernetes Clusters*: Access the application via the external IP of your cluster's node combined with the node port defined in service.yaml.

