# Demo
* The deme creates the configuration as below
* Mongo Express use DB URL in configmap to find Mongo DB internal service. Internal service use username and password in secret to log into Mongo DB. 

![image](https://github.com/MohammadNazeri/my-educations/assets/109389707/b86c1019-09f8-4d75-a522-fe1f1f8c23fb)

### mongodb DB and service internal yaml
We plan to use mongo docker image. By checking page of mongo in dockerhub, we configured below.
```
...
     spec:
      containers:
      - name: mongodb
        image: mongo
        ports:
        - containerPort: 27017 > default port for mongo based on dockerhub
        env: The config file is checked into repository. Hence, it is better not to put password here.
        - name: MONGO_INITDB_ROOT_USERNAME
          valueFrom:
            secretKeyRef:
              name: mongodb-secret > secret name
              key: mongo-root-username
        - name: MONGO_INITDB_ROOT_PASSWORD
          valueFrom: 
            secretKeyRef:
              name: mongodb-secret
              key: mongo-root-password
---  > new document started. The deployment and servie are in the same file bacause they belong together.
apiVersion: v1
kind: Service
metadata:
  name: mongodb-service
spec:
  selector:
    app: mongodb > connecting this service to pod with app:mongodb label. Service will find the pod and attach to
  ports:
    - protocol: TCP
      port: 27017 > service port
      targetPort: 27017 > pod port of deployment 
```

### Secret
```
...
type: Opaque > It is default. we can change to other types.
```
to fill username and password in a secret file, it is needed to encrypt them:
* echo -n '[username]'|base64
* echo -n '[password]'|base64

### mongo express and external service yaml file
```
spec:
      containers:
      - name: mongo-express
        image: mongo-express
        ports:
        - containerPort: 8081 > default port of mongo express based on dockerhub
        env:
        - name: ME_CONFIG_MONGODB_ADMINUSERNAME > username and password are in secret file
          valueFrom:
            secretKeyRef:
              name: mongodb-secret
              key: mongo-root-username
        - name: ME_CONFIG_MONGODB_ADMINPASSWORD
          valueFrom: 
            secretKeyRef:
              name: mongodb-secret
              key: mongo-root-password
        - name: ME_CONFIG_MONGODB_SERVER > mongo db address
          valueFrom: 
            configMapKeyRef:
              name: mongodb-configmap
              key: database_url
--- > it makes new document
apiVersion: v1
kind: Service
metadata:
  name: mongo-express-service
spec:
  selector:
    app: mongo-express
  type: LoadBalancer  > To have a external access, there is two step: 1. define type as loadbalancer 2. nodePort for external access
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
      nodePort: 30000 > port for external IP address
```
Type of services can be internal(Cluster IP) or external (LoadBalancer). Internal and External services both have internal IP address and port number. Only external service has enxternal IP address and port number(internalport:externalport). 
By default, Internal service get Internal Ip address. We need to set external IP address with below command:
```
minikube service [external service name]
```
The difference of port, targetPort, and nodePort is as follows:

<img src="https://github.com/user-attachments/assets/ca21b106-7162-42a6-a303-17eb45513645" style="width: 50%;" />


### config map
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: mongodb-configmap
data:
  database_url: mongodb-service > it is the name of service
```
