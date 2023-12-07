# infinidat-exercise
## Introduction
This repository contains a simple Flask application that is containerized using Docker and deployable on a Kubernetes cluster. The application includes basic endpoints and demonstrates how to set up a Flask app in a k8s environment.

## Prerequisites
- Docker installed on your machine.
- Access to a Kubernetes cluster.
- kubectl command-line tool installed and configured

## Instructions
### 1. Clone the repository and move to the directory.
```
git clone https://github.com/shaharshurki/infinidat-exercise.git
cd infinidat-exercise
```
### 2. Set up the Docker Environment:
If you're using Minikube, you can use its Docker daemon by running:
```
eval $(minikube docker-env)
```
### 2. Build the Docker Image in Minikube's Docker Daemon:
```
docker build -t my-flask-app:latest .
```
### 3. Deploying to Kubernetes
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

## Assumptions 
# Deploying on a minikube cluster and accessing the image locally.
If you are using a multi-node cluster and want to access the image locally you can load it to each node's Docker Daemon:
```
docker save my-flask-app:latest > my-flask-app.tar
docker load < my-flask-app.tar
```
You can also push the image to a remote repository and change the path of the image in the deployment file.

