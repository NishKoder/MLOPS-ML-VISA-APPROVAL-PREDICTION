# MLOPS-ML-VISA-APPROVAL-PREDICTION

![ML-Project-Structure.png](flowchart%2FML-Project-Structure.png)

This project uses [Conda](https://docs.conda.io/en/latest/) to manage the environment.

## Setup

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution).

2. Clone the project repository.

3. Navigate to the project directory.

4. Create a new conda environment. Replace `envname` with your preferred name for the environment and `python=3.9` with your preferred python version:5. Activate the environment:6. Install the project dependencies:## Usage

Before running the project scripts, ensure that the conda environment is activated. You can do this using the command:Thanks for using this application!# Clone the repository
git clone https://github.com/username/repo.git
# Navigate to the project's directory
`cd repo`

# Create Project Structure
`python template.py`
# Create conda environment
`conda create -p myenv python=3.9`
# Activate the environment
`activate myenv`
# Install the project dependencies
`python install -r requirements.txt`

## Workflow

1. constant
2. config_entity
3. artifact_entity
4. conponent
5. pipeline
6. app.py / demo.py

### Export the  environment variable
```bash


export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets: