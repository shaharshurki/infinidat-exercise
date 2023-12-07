# Infinidat Exercise
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
### Deploying on a minikube cluster and accessing the image locally.
If you are using a multi-node cluster and want to access the image locally you can load it to each node's Docker Daemon:
```
docker save my-flask-app:latest > my-flask-app.tar
docker load < my-flask-app.tar
```
You can also push the image to a remote repository and change the path of the image in the deployment file.
## Challenges
### 1. My Environment - 
I am working with a not-so-new laptop with Windows as my OS, so I needed to use a VM. I chose to use AWS EC2 and encountered little issues along the way.      First I Launched a t2.micro machine but as I tried to install minikube on it I found that it doesn't have 2 vCPUs so I needed to launche a new Machine with sufficiient resources. I launched the new machine and installed minikube. Finally,  as I tried to build the image it failed with a "no space left on device" error. to fix that I added more volume space to the EC2. 
