# Kubernetes
## Components
* Master
  * API server: Clients use UI, API, or CLI to connect to Kubernet through YAML or JSON format. Also, It contains all configurations.
  * Controller manager: It Detects dead pods and asks the scheduler to make new ones.
  * Scheduler: The scheduler is a component responsible for assigning new pods to nodes in the cluster based on resources. 
  * etcd: It is a key-value store of a cluster state, configuration, and coordination (cluster brain). it keeps all data and every change in a cluster except application data like data base that is in another storage. 
* Node (Worker node can be virtual or physical machine) contains:
  * pods:  It is a wrapper of a container or containers. The smallest unit that is configured and interacted with. There is one pod per application. Each pod gets one IP address to communicate with other pods.
  * container runtime
  * kubelet
  * kube proxey

 ![image](https://github.com/MohammadNazeri/my-educations/assets/109389707/cf4d2676-544b-4dbb-bc82-dcee70458dde)

* Virtual Network
* Service: When a pod crashes and dies its service remains unchanged until a new pod restart. Two functionalities: 1. keep permanent IP address  2. load balancer. 
![image](https://github.com/user-attachments/assets/b8f2abbb-9fad-4a6a-8730-938afccde77a)

* Ingress: It manages external access to services within a cluster. It acts as a gateway, allowing external traffic to reach the appropriate services within the Kubernetes cluster.

<img src="https://github.com/user-attachments/assets/221b81c7-f05e-465d-b5e2-6ef32a1c58cd" style="width: 50%;" />



* Configmap: ConfigMap is an API object used to store non-sensitive configuration data that can be consumed by pods or other resources in the cluster.
* Secret: It is kind of ConfigMap that is used to store sensitive configuration data e.g. username and password
* Volume: It is data storage to keep pods' data. Kubernetes cluster does not manage any data persistence.

![image](https://github.com/user-attachments/assets/fc344f6a-1b2a-491a-93ac-4ed2cf8ea14b)


* Deployment: Deployment is an API object that provides declarative updates to applications running within a cluster. It manages the deployment and scaling of replica sets, ensuring that a specified number of identical pods are running at any given time.
* Stateful set:  While Deployments manage stateless applications, a StatefulSet manages stateful applications, such as databases, where each instance requires stable, persistent storage and unique network identifiers.

## Minikube 
* Minikube sets up a lightweight Kubernetes cluster on your local system, allowing you to experiment with Kubernetes features and deploy applications without needing access to a full-scale production cluster.
* kubectl:  It is a command-line tool for interacting with Kubernetes clusters.
### Installation:
* sudo apt install docker.io
* sudo systemctl enable docker
* sudo systemctl start docker
* install minikube
* install kubectl
### Commands
* minikube start
* minikube status
* minikube delete
* minikube service [service name] > Minikube will open a tunnel to the specified service, allowing you to access it via a local URL. This is particularly useful during development and testing phases when you need to interact with services running inside your Kubernetes cluster.
* kubectl get nodes > shows all nodes
* kubectl get pod
* kubectl get services
* kubectl get deployment
* kubectl create deployment NAME --image=image [--dry-run] [options]
* kubectl create deployment nginx-depl --image=nginx > get nginx from dockerhub and create deployment
* kubectl logs [podname] > debug pods
* kubectl describe pod [podname]
* kubectl exec -it [podname] --bin/bash > it gives the terminal of application container
* kubectl delete deployment [deployment name]
* kubectl apply -f [configuration file].yaml 

## YAML file
There are three parts for configuration file of service and deployment:
1. metadata > Determine the kind of components e.g. service, deployment, etc.
2. specification > features of component
3. status > It is related to runtime. Kubernetes always compares the specification part with the current status and if there is a difference (e.g. number of pods) it tries to fit it (self-healing). These data comes from etcd.
### pod configuration
It is inside of the specification(spec) part with the title "template". It has its own metadata and spec parts. 

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
