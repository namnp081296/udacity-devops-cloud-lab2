[![Lab02 ML Flask App Service](https://github.com/namnp081296/udacity-devops-cloud-lab2/actions/workflows/pythonflaskml.yml/badge.svg)](https://github.com/namnp081296/udacity-devops-cloud-lab2/actions/workflows/pythonflaskml.yml)

# Overview
This project will show you how to completely implement DevOps process in building FlaskML app by using the CI/CD tool include Github Actions and Azure Devops pipeline.
After you finish this project, you'll learn:
* How to install and using python tool like pip, pylint, pytest and create the env for testing app before apply it to process
* How to configure Github Actions to implement CI for checking code score, syntax, bugs,...
* How to configure Azure Devops to implement CD for delivering application to production

## Project Plan
* [Project plan](docs/project-plan.xlsx)
* [Tasks Kanban](https://trello.com/b/6Bz6jB9R/udacity-ml-app)

## Architectural Diagram
![](docs/screenshots/architecture-diagram.png)

## Instructions
### Deploy project with Azure Cloud Shell  
* Clone project into Azure Cloud Shell
```
git clone git@github.com:namnp081296/udacity-devops-cloud-lab2.git
cd udacity-devops-cloud-lab2
```
![](docs/screenshots/git-clone.png)

* Install Python virtual environment
```
python3 -m venv .udacity-devops
source .udacity-devops/bin/activate
```
	
* Run lint and tests
```
make all
```
![](docs/screenshots/lint-test.png)
This steps also be triggered automatically by GitHub Actions when new code is pushed
![](docs/screenshots/github-actions.png)

* Deploy project to Azure App Service
```
make web-app
```
![](docs/screenshots/app-service-deploy.png)

### Deploy project with Azure DevOps
* [Configure project in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops#create-an-azure-devops-project-and-connect-to-azure).

* Run pipeline to deploy project to App Service
![](docs/screenshots/azure-devops-pipeline.png)
![](docs/screenshots/azure-devops-pipeline-2.png)

### Verify application
* Go to Azure Portal confirm created App Service
![](docs/screenshots/app-service.png)
* Call prediction API from Azure Cloud Shell.
The output should look similar to this:
![](docs/screenshots/ml-predict.png)

* Output of streamed log files from deployed application
```
az webapp log tail --resource-group Azuredevops --name flaskmlapp
```
![](docs/screenshots/app-service-tail.png)

## Enhancements
Following item can be done next to improve the project.
* Build application as image and do a containerized deployment
* Add more testing like integration test to the pipelines
* Define user parameters for Azure DevOps pipelines 
* Split build and deploy stages into 2 pipelines so that we can re-use built artifact to deploy to different environment

## Demo
