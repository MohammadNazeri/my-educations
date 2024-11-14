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

## Demo Python Application
1. Test the code in local
``` make test ```

2. Create CI/CD pipeline code in YAML format
  * .gitlab-ci.yml file name

<img src="https://github.com/user-attachments/assets/4fddb94d-b5a0-4063-acad-cd596143099b" style="width: 50%;" />

```
variables: # variables in code
  IMAGE_NAME: nanajanashia/demo-app
  IMAGE_TAG: python-app-1.0

stages:
  - test
  - build
  - deploy

run_tests:
  stage: test
  image: python:3.9-slim-buster
  before_script:
    - apt-get update && apt-get install make
  script:
    - make test


build_image:
  stage: build
  image: docker:20.10.16
  services:
    - docker:20.10.16-dind
  variables:
    DOCKER_TLS_CERTDIR: "/certs"
  before_script:
    - docker login -u $REGISTRY_USER -p $REGISTRY_PASS
  script:
    - docker build -t $IMAGE_NAME:$IMAGE_TAG .
    - docker push $IMAGE_NAME:$IMAGE_TAG


deploy:
  stage: deploy
  before_script:
    - chmod 400 $SSH_KEY
  script:
    - ssh -o StrictHostKeyChecking=no -i $SSH_KEY root@161.35.223.117 "
        docker login -u $REGISTRY_USER -p $REGISTRY_PASS &&
        docker ps -aq | xargs docker stop | xargs docker rm &&
        docker run -d -p 5000:5000 $IMAGE_NAME:$IMAGE_TAG"

```






4. In pipeline three command have to be available: make 
