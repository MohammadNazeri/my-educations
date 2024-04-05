
# Docker
## Commands
* docker images > to list all images in the system
* docker run [image]
* docker run --name [container name] [image] > use the image to make a container with a specific name
> image: an executable software package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and configuration files.   
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
* docker run -p[image port]:[system port] [image name] > to run image with connecting specific image port to specific system port
## Volume 
> each time "docker run [image]" run a new copy of image and make a new container.   
> How to save modification inside the container? On the docker hub, the author writes how to run docker to save modifications inside the container.
* docker run --name redis -p 6379:6379 redis redis-server --appendonly yes > appendonly save the modification on the container based on documentation written by the author.
> Use volume(-v or --mount) to save modification in system. by running image, the modification get from system and affect on container.
* docker run -v [system path]:[path inside container based on documentation] [image] [requirement command to save modification inside container]
* docker run --name redis -p 6379:6379 -v /tmp/data/redis:/data redis redis-server --appendonly yes
## n
