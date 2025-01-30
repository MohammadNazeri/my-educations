# Kubernetes Advance
## Namespace
* namespace is used to organize resources.
* There could be multiple namespace in a cluster.
* They can be created in config files.
  ```
  ...
  metadata:
   name: mysql-configmap
   namespace: my-namespace
  ...
  ```
* By default, each cluster has four namespace:
 * kubernetes-dashboard > it is specific to minikube
 * kube-system > it is used for system-level components and resources. It typically includes components like kube-dns, kube-proxy, kube-scheduler, kube-controller-manager, etc
 * kube-public > It contains publicly accessible data like configmap
 * kube-node-lease > It contains the most important data of nodes
 * default > It uses at beginning when there is not any new namespace 
* kubectl get namespace
* kubeclt create namespace [name]
* 
