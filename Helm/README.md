# Helm Chart
* Helm is a package manager for Kubernetes — often described as “apt/yum for Kubernetes.”
* They are distributed in public and private repositories
* For example: To add a new Elastic Stack for logging, several Kubernetes components—such as StatefulSets, ConfigMaps, Secrets, Kubernetes users, and Services—need to be created, which is a tedious task. Since the deployment is fairly standard, a packaged solution can be used to simplify and automate the deployment process.
* Helm repositories contain various charts for different service deployment. The step by step process is as follows:
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install <release name> <chart name>
```
* When a chart is installed, Helm creates a release with a unique release name to track that installation. Installing the same chart multiple times requires different release names, each representing a separate instance with its own configuration and lifecycle.
## Helm Chart Features
### First Feature: Sharing Helm Charts
* It allows teams to package, reuse, version, and distribute Kubernetes applications easily.
```bash
helm search <keyword>
```
* Helm Hub also avaialbe to search desired chart.

### Second Feature: Templating Engine
* A templating engine in Helm allows Kubernetes YAML files to be dynamic and reusable instead of static.
  1. Define a common blueprint
  2. Dynamic values are replaced by placeholders. logic that are filled using values from values.yaml and release information.

<img width="1765" height="623" alt="image" src="https://github.com/user-attachments/assets/6dcfb05e-7ab4-4634-afe7-92d5b16b9e8c" />

* Template YAML config file with {{.values...}}
* Those values come from external configuration like values.yaml file
* Values is an object which is created by yaml file or --set flag
* the --set flag is used to override chart values directly from the command line without editing values.yaml
```bash
helm install my-app bitnami/nginx --set replicaCount=3
```
* It uses in CI/CD pipeline by adding value.yaml, they can replaced on the fly.

#### Same Applications Across Different Enviroments
* It uses when we plan to deploy the same application in development, staging, producetion, etc enviroments.
* Package the yaml files and make new chart

## Helm Chart Structure
* my-chart: name of chart
* Chart.yaml: meta info about chart e.g. name, version, etc
* values.yaml: values for the template files. It is default value which can be override later.
* chart folder: chart dependencies
* templates folder: the actual template files
my-chart/
├── Chart.yaml
├── values.yaml
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── _helpers.tpl
│   └── NOTES.txt
└── .helmignore
* By running `helm install` to install yamle file to kubernetes, the process will be as follows:
  1. template files will be filled with the value from values.yaml
  2. Produce valid kubernetes manifests
  3. deploy in kubernetes

#### Value into Template files
Helm merges values in this order:
  1. Chart default values.yaml> `helm install my-app ./my-chart`
  2. Values from -f values.yaml> `helm install my-app ./my-chart -f values-prod.yaml`
  3. Values from --set (highest priority)> `helm install my-app bitnami/nginx --set replicaCount=3`

<img width="1669" height="465" alt="image" src="https://github.com/user-attachments/assets/44f988e1-3d0c-41cc-bcf1-0c6e83851fb9" />

### Third Feature: Release Management
