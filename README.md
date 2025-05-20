
# Python Pipeline Orchestrated with Airflow (Containerized using Docker)
This repository contains a Python-based data pipeline that is orchestrated using Apache Airflow. The tasks in the pipeline are executed as part of a Directed Acyclic Graph (DAG) and are containerized using Docker to ensure a reproducible and isolated execution environment.

# Table of Contents
Overview

Requirements

Installation

Pipeline Structure

Running Airflow with Docker

Example Pipeline Tasks

Notes


# Overview
This project demonstrates how to:

Define a data pipeline using Apache Airflow in Python.

Containerize both the pipeline and Airflow environment using Docker.

Orchestrate and schedule tasks to run on Apache Airflow.

Interact with external systems such as APIs or S3 buckets.

The pipeline includes several tasks:

Fetch data from an external API (e.g., https://randomuser.me).

Process and clean the data.

Store the results in an external storage service (e.g., AWS S3).

# Requirements
To run this pipeline, you need the following:

Docker installed on your system.

Python 3.9 installed.

Airflow version 2.8.0

An active AWS account if using AWS services.

Optional
Docker Compose to simplify managing the Airflow containers.

Installation
1. Clone the Repository
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-username/airflow-pipeline.git
cd airflow-pipeline
2. Set Up Environment Variables
Create a .env file in the project root to store your sensitive credentials and configurations:

bash
Copy
Edit


# .env file example
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=us-eu-central-1

3. Build the Docker Containers
We use Docker Compose to set up the Airflow containers. The repository contains a docker-compose.yml file, which defines the Airflow web server, scheduler, and worker.

Build and start the containers with:

bash
Copy
Edit
docker-compose up --build
This will build and start all necessary containers for the Airflow environment.

# Pipeline Structure
DAG Definition
The pipeline consists of an Airflow DAG defined in the dags/ directory. The DAG includes several tasks that can be executed in parallel or sequentially. Here's an overview of the DAG's tasks:

Fetch Data: Makes a request to the external API to retrieve random user data.

Process Data: Cleans and processes the retrieved data.

Store Data: Uploads the processed data to AWS S3.

# Docker Configuration
Dockerfile: Contains instructions to create a custom Docker image with Airflow installed and the necessary Python dependencies.

docker-compose.yml: Defines how Airflow components (Web Server, Scheduler, Workers, etc.) are set up in Docker.

Each task is defined as a Python operator in Airflow, and the tasks are orchestrated using Python code.

Running Airflow with Docker
After building the Docker containers with docker-compose up --build, follow these steps:


# Example Pipeline Tasks
Here are the brief descriptions of the tasks in the pipeline:

1. Fetch Data:
This task makes an HTTP request to an API (e.g., randomuser.me) to fetch random user data and stores it in a Pandas DataFrame.

2. Process Data:
This task processes and cleans the data from the API response. For example, it might clean names, format addresses, or remove unwanted fields.

3. Store Data:
After the data is processed, this task uploads it to a destination, such as an AWS S3 bucket. This can be done using libraries like boto3 or awswrangler.

![Image Alt](https://github.com/Chizobaeze/Airflow_docker_pipeline/blob/main/IMG_4830.JPG?raw=true)

Notes
Make sure to replace the AWS credentials and region in the .env file with your actual AWS details.
The Docker environment is set up to run with Airflow's LocalExecutor by default. If you're deploying to Kubernetes or another environment, you may need to adjust the executor configuration.
The docker-compose.yml file is pre-configured for development. For production, you should customize it based on your infrastructure.
