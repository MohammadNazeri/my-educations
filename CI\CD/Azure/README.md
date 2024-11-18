# Azure DevOps

<img src="https://github.com/user-attachments/assets/4079a4ef-bda6-46a6-afdc-ed58c274e7f0" style="width: 50%;" />

## Azure Boards
planning is the first step.
## Azure Repos
Source control management
## Azure pipeline build
Releasing new feature/bug

<img src="https://github.com/user-attachments/assets/cc1a41da-8187-4241-8b5b-58b06e4a0ae3" style="width: 50%;" />

### Syntax Pipeline
* It is Yaml file which is part of git project
* script or task can be use in script. Task is pre-created script offered as a convenience.
* "Show assistance" button shows the list of tasks and template to define them
* Job represents an execution boundary of a set of steps.
* Each job runs on an agent
* All the steps in a job run on the same agent
* With jobs we can run series of steps in different environment.
* Jobs can run in parallel, sequentially, or across different agents.
```
trigger:
- main

variable: 
  var: var

jobs:
- job: PreWork
  pool: 
    vmImage: ubuntu-latest > run tasks on this image
  steps:
  - script: "Do pre-work"

- job: PostWork
  pool: 
    vmImage: windows-latest
  steps:
  - script: "Do post-work using a different hosted image"

```

## Azure Artifacts
* Traditionaly, depending on application programming language, artifact produced will be different such as JAR file, etc
* The produced artifact in the built pipeline, can be stored in azure atrifact(as a repository).
* In modern, we donot use artifact anymore. Instead docker images are created as artifact.

## Azure Pipelines Stages
* stage is logical boundary in the pipeline. Each stage contains one or more jobs. They run one after another.
* Two stages are defined here.

```
stages:
- stage: Build
  jobs:
  -  job: Test and Build
    steps:
    - task:
    ...
    - task:
    ...
- stage: Deploy
  jobs:
  - deployment: Deploy to development
    steps:
    - task:
    ...
```
*A deployment job is a special type of job in Azure Pipelines that is specifically designed for deployment purposes.
* A deployment job ensures that resources like Azure Web Apps, Kubernetes, virtual machines, or other cloud resources are updated with the new version of your application.
* What differentiates a deployment job from a regular job is that it can track deployment history and provide features like approvals, gates, and rollbacks.
