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
* Each namespace should have their own configmap/secret. They can't access to each other configmap/secret even they are the same.
* Services (database, Nginx, Elastic) can be shared across namespaces. It means we can address a service from configmap of different namespaces like below: [service].[namespace]

<img src="https://github.com/user-attachments/assets/473e0f46-3c63-4109-bafc-33ba39926efc" style="width: 50%;" />

### Componenets in namespace
Some components can't be created within a namespace and they leave globally in cluster like volume, node.
```
kubectl api-resource --namespaced=false > list of resource can't be within namespace
kubectl api-resource --namespaced=true > list of resource can be within namespace
```

NOTE: It is not needed to use kubernetes for small projects and less than 10 users.

# Ingress
* It is used to connect to a pod through extrnal with domain name and also https protocol.
* The external service can be used just for testing by access through IP address and port

![image](https://github.com/user-attachments/assets/0eca1dd5-36b0-4786-b8d5-cfa6d0304b65)

## Ingress controller
It is a component in Kubernetes that manages and enforces the rules defined in Ingress resources. It is responsible for handling external HTTP(S) traffic and routing it to the appropriate internal services.
It is a pod or set of pods that run in a node or cluster. Hence, ingress controller is entry point to cluster.   
There are many third-party implementation that you should choose which one to install. 
NOTE: If using a cloud provider, they have their own virtualized load balancer. By accessing the address of cloud provider, the load balancer redirect request to ingress controller. If using bare metal, the entry point should be defined with ourself. 

```
minikube addons enable ingress > install ingress controller
kubectl get pod -ns kube-system > to ingress controller pod
```

## Ingress
It is kind of component to define routing rules in a cluster. 
Ingress controller evaluate and manage all the rules.

### Ingress YAML file
```
apiVersion: networking.k8s.io/v1
kind: Ingress 
metadata:
  name: name
  annotations:
    kubernetes.io/ingress.class: "nginx"
spec:
  rules:  >  defing rules
    - host: app.com  >  The host that user enter in browser > Forward all requests to internal service in below 
      http: > it is protocol that incoming request gets forwarded to internal service (it is related to second step)
        paths: > define all possible path after host 
        - path: /
          pathType: Exact
          backend: > where the incoming request redirected 
            service:
              name: my-service > internal service name
              port: 
                number: 8080 > internal service port (not targetport)

```
## Configure TLS certificate
To configure https forwarding in ingress
```
kind: Ingress
...
spec:
 tls:
  - hosts: >  the same host 
   - myapp.com
   secretName: myapp-secret-tls > secret that hold tls certificate
 rules:

...
```
We should create secret componenet like below:
```
apiVersion: v1
kind: Secret
metadata:
  name: myapp-secret-tls
  namespace: default > It should be in the same namespace as ingress component 
data:
  tls.crt: dXNlcm5hbWU=  # base64 encoded "username"
  tls.key: cGFzc3dvcmQ=  # base64 encoded "password"
type: kubernetes.io/tls
```
## Helm
It is package manager for Kubernetes. It is convenient way for packaging collections of kubernetes yaml files and distributing them in private and public registery. 

### Helm chart
* A Helm chart is a package of pre-configured Kubernetes resources that define an application, service, or infrastructure component for deployment in a Kubernetes cluster.
* Deployment of some services are standard and we can use existing yaml file for them. Hence, these written yamle file packaged and push them into registeries.

```
helm search hub/repo <keyword>  > to find your helm chart in repositories
helm install <helm chart name>
```
### Helm templating engine
* A templating engine in Helm allows dynamic generation of Kubernetes resource definitions using templates, variables, and logic. It replaces hardcoded values with configurable inputs, making charts reusable and flexible.
* We can define a common blueprint for microservices (template file) and values of each microservices are replaced by placeholders. These values are stored in values.yaml file.
* We can use these template yamle file in CI/CD pipeline to replace the values on the fly before deploying them.
* Use case: when we have three stages for our project(development, staging, and production), each of them run on a kubernetes cluster. instead of defining three different yaml files, helm templating give us the ability to define one yaml file and change the value for each stage. Hence we should have three different values.yaml file. follow command can install them:
```
helm install --values=my-values.yaml <chartname>
```
![image](https://github.com/user-attachments/assets/14e2f062-6696-45ab-88f1-801055b5ba18)


#### helm chart structure
```
mychart/  >  name of chart
  chart.yaml  >  meta info of chart like name version dependencies
  values.yaml  >  default values for template file. They can be overwrriten
  charts/  >  chart dependencies
  templates/  >  templates files
...
```

### Release management
* In helm version 2, Triller was responsible to run helm yaml file inside kubernetes cluser. Because of security issues, vesion 3 removed Triller.

![image](https://github.com/user-attachments/assets/23546376-0433-4c0e-b5e1-c77fe42dabcd)

## Volume
### Persistent volume (PV)
* Storage that does not depend on pod lifecycle or kuberenets cluster and it should be available on all nodes
* Kuberentes does not care about actual storage. It gives PV componenet as interface to the actual storage

<img src="![image](https://github.com/user-attachments/assets/e5c8779c-4035-4162-9eac-99d73482f91f)" style="width: 50%;" />

  
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
...
```
### Persistent volume claim (PVC)
### Storage Class (SC) 
