# Kubernetes
## Components
* Master
  * API server: Clients use UI, API, or CLI to connect to Kubernet through YAML or JSON format. Also, It contains all configurations.
  * Controller manager: It Detects dead pods and asks the scheduler to make new ones.
  * Scheduler: The scheduler is a component responsible for assigning new pods to nodes in the cluster based on resources. 
  * etcd: It is a key-value store of a cluster state, configuration, and coordination (cluster brain). it keeps all data and every change in a cluster except application data like data base that is in another storage. 
* Each Worker node contains:
  * pods
  * container runtime
  * kubelet
  * kube proxey

 ![image](https://github.com/MohammadNazeri/my-educations/assets/109389707/cf4d2676-544b-4dbb-bc82-dcee70458dde)

* Virtual Network
* Worker node: It consists of multiple pods.
* Pod: It is a wrapper of a container or containers. The smallest unit that is configured and interacted with. There is one pod per application. Each pod gets one IP address to communicate with other pods.
* Service: Two functionalities: keep permanent IP address  and load balancer. When a pod crashes and dies its service remains unchanged until a new pod restart.
* Ingress: It manages external access to services within a cluster. It acts as a gateway, allowing external traffic to reach the appropriate services within the Kubernetes cluster.
* Configmap: ConfigMap is an API object used to store non-sensitive configuration data that can be consumed by pods or other resources in the cluster.
* Secret: It is kind of ConfigMap that is used to store sensitive configuration data e.g. username and password
* Volume: It is data storage to keep pods' data. Kubernetes cluster does not manage any data persistence.
* Deployment: Deployment is an API object that provides declarative updates to applications running within a cluster. It manages the deployment and scaling of replica sets, ensuring that a specified number of identical pods are running at any given time.
* Stateful set:  While Deployments manage stateless applications, a StatefulSet manages stateful applications, such as databases, where each instance requires stable, persistent storage and unique network identifiers.

## Minikube 
* Minikube sets up a lightweight Kubernetes cluster on your local system, allowing you to experiment with Kubernetes features and deploy applications without needing access to a full-scale production cluster.
## YAML file
There are three parts for configuration file of service and deployment:
1. metadata > Determine the kind of components e.g. service, deployment, etc.
2. specification > features of component
3. status > It is related to runtime. Kubernetes always compares the specification part with the current status and if there is a difference (e.g. number of pods) it tries to fit it (self-healing). These data comes from etcd.
### pod configuration
It is inside of the specification(spec) part with the title "template". It has its own metadata and spec parts. 
