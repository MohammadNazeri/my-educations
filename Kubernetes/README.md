# Kubernetes
* Master
  * API server: Clients use UI, API, or CLI to connect to Kubernet through YAML or JSON format. Also, It contains all configurations.
  * Controller manager
  * Scheduler
  * etcd
* Virtual Network
* Worker node: It consists of multiple pods.
* Pod: It is a wrapper of a container or containers. The smallest unit that is configured and interacted with. There is one pod per application. Each pod gets one IP address to communicate with other pods.
* Service: Two functionalities: keep permanent IP address  and load balancer. When a pod crashes and dies its service remains unchanged until a new pod restart.
* Ingress: It manages external access to services within a cluster. It acts as a gateway, allowing external traffic to reach the appropriate services within the Kubernetes cluster.
