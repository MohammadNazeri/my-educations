# GitLab CI/CD
* Continuous Integration/ Continuous Deployment
* Gitlab is trying to become the devops platform. 
* They are integerating and creating new features to give everything in one platform to build devops process.
* One big part of process is CI/CD.

<img src="https://github.com/user-attachments/assets/c446bb77-3672-45a0-83ff-e4a5705fcc81" style="width: 50%;" />

## Other CI/CD Tools

<img src="https://github.com/user-attachments/assets/65696fbc-e63a-4b94-8c38-3a043c6acc69" style="width: 50%;" />


## GitLab CI/CD Architecture
* Gitlab instance or Gitlab server: It host application codes and pipeline
* Gitlab runners: They are executing the pipelines. They are connected to Gitlab servers.
 * It could run pipeline on OS or docker 

## Demo Python Application
1. Test the code in local
``` make test ```

2. Create CI/CD pipeline code in YAML format and store it in ```.gitlab-ci.yml``` file name
   * By creating the file and on "commit the code" button, gitlab start to run the current CI/CD pipeline

<img src="https://github.com/user-attachments/assets/4fddb94d-b5a0-4063-acad-cd596143099b" style="width: 50%;" />

```
variables: 
  IMAGE_NAME: nanajanashia/demo-app
  IMAGE_TAG: python-app-1.0

stages: > running jobs in order
  - test
  - build
  - deploy

run_tests: > name of job
  stage: test
  image: python:3.9-slim-buster > gitlab runner
  before_script: > run the command before running scripts
    - apt-get update && apt-get install make > The python code needs python, pip (to install libraries) and make (to run). The python image misses make. Hence we should install it.
  script: > list of commands should be run 
    - make test


build_image:
  stage: build
  image: docker:20.10.16
  services: > It is a container which start at the same time as job container. Job container uses the container in build time like mysql, daemon, etc.
    - docker:20.10.16-dind
  variables:
    DOCKER_TLS_CERTDIR: "/certs" > docker creates certificate in this location. The certificate will share between service and job container
  before_script:
    - docker login -u $REGISTRY_USER -p $REGISTRY_PASS > login to dockerhub(private repository) > define variable in gitlab>settings> CI/CD>variables : these variables are availabe in pipeline code > Also the dockerhub is default. If another docker registery exist we can specify it by its address at the end of command: [register_url]
  script:
    - docker build -t $IMAGE_NAME:$IMAGE_TAG . > build docker image by using DOCKERFILE which exist in root of gitlab > IMAGE_NAME=repository location+image name>e.g. hub.docker.com/nanajanashia/demo-app > dockerhub is default
    - docker push $IMAGE_NAME:$IMAGE_TAG > the default repository is dockerhub


deploy: > Deployment server: To connect to server, here uses ssh command. It needs ssh key. It needs to set ssh private and public key. Assume the server is pure OS, it needs docker to be installed. 
  stage: deploy
  before_script:
    - chmod 400 $SSH_KEY > Because the ssh_key stored in file type, it needs to set permission for the file.
  script:
    - ssh -o StrictHostKeyChecking=no -i $SSH_KEY root@161.35.223.117 " > define ssh_key in gitlab>setting>CI/CD>variable > we should disable interactive step by stictho... option > by connecting to server run commands:
        docker login -u $REGISTRY_USER -p $REGISTRY_PASS && > login to pull the image
        docker ps -aq | xargs docker stop | xargs docker rm && > by running each time, it needs to remove previous version and run new one
        docker run -d -p 5000:5000 $IMAGE_NAME:$IMAGE_TAG" >  pull and run the app in specific port

```

### Check Pipeline 
In gitlab>CI/CD:
* Pipeline: show the list view of all pipeline execution and their state (passed)
* Jobs: show list of jobs. Also, the logs of jobs can be checked here.

![image](https://github.com/user-attachments/assets/9d56574f-9231-4af5-8f06-5dd964a2c230)


### Define Scretry in Setting
gitlab>settings> CI/CD > Variable to store passwords which should not be included in repository. 
![image](https://github.com/user-attachments/assets/d8d3aba9-1660-4dc9-a6c8-35d3df66dd87)


### Add SSH key of server to setting
gitlab>settings> CI/CD > Variable to create a file to store SSH key. It is stored in file because we are going to reference it as a file.
![image](https://github.com/user-attachments/assets/d3781434-78c6-4736-8626-9f4a3fae172e)



4. In pipeline three command have to be available: make 
