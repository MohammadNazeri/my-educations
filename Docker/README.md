#Docker
docker images > to list all images in the system
docker run [image]
> image: an executable software package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and configuration files.
> dockerhub: it contains various images
docker pull [image] > download image from dockerhub
docker ps > shows running docker container
docker run [image] [command with arguments] > run the command inside the image. First, it creates a new container from the image and then starts it.
docker ps -a > shows all running docker previously > these images take space from disk
docker rm [container ID] > to remove the container from the system. 
docker rmi [image] > to remove the image
docker container prune > remove all exited containers 
docker run --rm [image] > automatically remove the container when it exits
docker run -it [image] > Keep stdin open even if not attached and tty
> Each image contains some files and takes some requirement files from the upper layer like OS
docker exec [container] [command with arguments] > run command inside the existing container
