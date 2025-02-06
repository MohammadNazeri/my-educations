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




## YAML file
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
