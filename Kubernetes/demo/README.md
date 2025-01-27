# Demo
* The deme creates the configuration as below
* Mongo Express use DB URL in configmap to find Mongo DB internal service. Internal service use username and password in secret to log into Mongo DB. 

![image](https://github.com/MohammadNazeri/my-educations/assets/109389707/b86c1019-09f8-4d75-a522-fe1f1f8c23fb)

### mongodb.yaml service-internal.yaml
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
