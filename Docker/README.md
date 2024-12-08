
# Docker
## Commands
* docker images > to list all images in the system
* docker run [image]
* docker run --name [container name] [image] > use the image to make a container with a specific name
> * image: an executable software package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and configuration files.
  > * It is based on a base-layer and also multi-layers on top of that
  > Images are stored in a Docker registry, such as Docker Hub or a private registry.
  > It is built thorugh Docker file.
> container is a running instance of a Docker image.
  > It is built and run through a commmand.
> dockerhub: it contains various images
* docker pull [image] > download image from dockerhub
* docker ps > shows running docker container
* docker run [image] [command with arguments] > run the command inside the image. First, it creates a new container from the image and then starts it.
* docker ps -a > shows all running docker previously > these images take space from disk
* docker rm [container ID] > to remove the container from the system. 
* docker rmi [image] > to remove the image
* docker container prune > remove all exited containers 
* docker run --rm [image] > automatically remove the container when it exits
* docker run -it [image] > Keep stdin open even if not attached and tty
> Each image contains some files and takes some requirement files from the upper layer like OS
* docker exec [container] [command with arguments] > run command inside the existing container
* docker run -p[image port]:[system port] [image name] > to run an image by connecting a specific image port to a specific system port
## Volume 
> each time "docker run [image]" run a new copy of image and make a new container.   
> How to save modification inside the container? On the docker hub, the author writes how to run docker to save modifications inside the container.
* docker run --name redis -p 6379:6379 redis redis-server --appendonly yes > appendonly save the modification on the container based on documentation written by the author.
> Use volume(-v or --mount) to save modification in system. by running image, the modification get from system and affect on container.
* docker run -v [system path]:[path inside container based on documentation] [image] [requirement command to save modification inside container]
* docker run --name redis -p 6379:6379 -v /tmp/data/redis:/data redis redis-server --appendonly yes
## Dockerfile
> How to make a new image from an existing image?
> dockerfile makes a new image from an existing image or a fresh one. To do so, read docker hub of the existing image.

```
FROM [image] > FROM tiangolo/uwsgi-nginx-flask
COPY [system file] [image path] > COPY ./reqirements.txt /tmp/requirements.txt
RUN [linux command] > RUN pip install -r /tmp/requirements.txt
COPY [my app] [image path]  > docker hub shows the path of the image
```
> docker build . > It makes a new image based on docker file.
> docker build -t [app name]:[version] . : making new image with name and tag
### Push to Docker Hub
* docker login --username=mjrod > connect CLI to Docker Hub account
* docker tag hello-py mjrod/hello-py > tag the image with your Docker Hub username: <username>/<image-name>
* docker push mjrod/hello-py > to push a new repository to Docker Hub to store the image
* docker pull mjrod/hello-py:latest to pull the previously uploaded image from Docker Hub
## Docker Network
* docker network ls >  shows the list of existing network
* docker network create [name] > creates a network with name
* docker run --network [network name] [image]  > The new container belongs to network name
> Run all containers in the same network to see each other. It works like DNS. It means that all containers can see each other through the name of the containers e.g. redis:8080. Read docker network documentation for various kinds of networks.
>
## Build system:
> By modifying a system, it is needed to modify other parts also.

## Container orchestration platforms
> Docker Swarm
> Kubernetes 
