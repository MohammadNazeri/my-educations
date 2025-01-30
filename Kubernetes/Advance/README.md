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
* 
* 
