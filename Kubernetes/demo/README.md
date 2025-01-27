# Demo
* The deme creates the configuration as below
* Mongo Express use DB URL in configmap to find Mongo DB internal service. Internal service use username and password in secret to log into Mongo DB. 

![image](https://github.com/MohammadNazeri/my-educations/assets/109389707/b86c1019-09f8-4d75-a522-fe1f1f8c23fb)

to fill username and password in a secret file, it is needed to encrypt them:
* echo -n '[username]'|base64
* echo -n '[password]'|base64
>  Then, Copy them in the secret file. 
