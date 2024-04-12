# Kubernetes
## Components
* Master
  * API server: Clients use UI, API, or CLI to connect to Kubernet through YAML or JSON format. Also, It contains all configurations.
  * Controller manager
  * Scheduler
  * etcd
*Each Worker node contains:
  * pods
  * container runtime
  * kubelet
  * kube proxey
 
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
