# Helm Chart
* Helm is a package manager for Kubernetes — often described as “apt/yum for Kubernetes.”
* They are distributed in public and private repositories
* For example: To add a new Elastic Stack for logging, several Kubernetes components—such as StatefulSets, ConfigMaps, Secrets, Kubernetes users, and Services—need to be created, which is a tedious task. Since the deployment is fairly standard, a packaged solution can be used to simplify and automate the deployment process.
* Helm repositories contain various charts for different service deployment. The step by step process is as follows:
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install elastic bitnami/elasticsearch
```
