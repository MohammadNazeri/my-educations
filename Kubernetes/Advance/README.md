# Kubernetes Advance
## Namespace
* namespace is used to organize resources. It likes virtual cluster in kubernetes cluster.
* By default, each cluster has four namespace: > ```kubectl get namespace```
  * kubernetes-dashboard > it is specific to minikube not in standard cluster
  * kube-system > it contains system process and does not need to be modified. It typically includes components like kube-dns, kube-proxy, kube-scheduler, kube-controller-manager, etc
  * kube-public > It contains publicly accessible data like configmap which contains cluster information: ```kubectl cluster-info```
  * kube-node-lease > It contains the most important data of nodes
  * default > It uses at beginning when there is not any new namespace 
### Create Namespace
They can be created through ```kubeclt create namespace [name]``` or in config files:
  ```
  ...
  metadata:
   name: mysql-configmap
   namespace: my-namespace
  ...
  ```
### Usage of Namespace
The use case of namespace is follows:
* Organizing components (deployment, replicasets, services, configmaps)
* Having multiple teams: Maybe they create projects with same name which overwrite each other files
* Service sharing: Using common Service (Elasti,Nginx) in different project(cluster)
* Resource sharing: Having two different versions of the same project
* Access and resource limits on Namespace: each team limits to access to their namespace. Also, we can limit the resources(CPU,RAM, etc) that each namespace can use.

<img src="https://github.com/user-attachments/assets/f004aa08-971c-457d-946f-8a3151692331" style="width: 50%;" />

We can group the components based on:
* Different application: Database, Monitoring, etc
* Different project of each different team

We can't access most resources from another Namespace
* Each namespace should have their own configmap. They can't access to each other configmap even they are the same

NOTE: It is not needed to use kubernetes for small projects and less than 10 users.
