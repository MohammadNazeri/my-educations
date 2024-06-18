# Docker compose
Docker Compose is a tool that simplifies the management of multi-container Docker applications. It allows you to define and run multi-container Docker applications using a YAML file. This file, commonly named docker-compose.yml, specifies the services, networks, and volumes that the application requires.

```
version: '3.8'  # Version of Docker Compose file syntax

services:    # Defines the containers
  my-app:    # the first container
    build: . # when we plan to build an image. The dot shows that the docker file should be in the same path of yaml file.
    ports:
      - 3000:3000
    environment:
      db_username: ${os_variable} # username and password can be variable in os environment
      db_password: $(os_variable)

  web:          # second container
    image: nginx:latest
    ports:
      - "80:80"
    volumes:?    
      - ./html:/usr/share/nginx/html
    depends_on:    # it starts to run whenever the depends on containers are running
      - db

  db:      # second container
    image: postgres:13
    environment:      #environmental variables
      POSTGRES_PASSWORD: example
    volumes:?
      - db-data:/var/lib/postgresql/data
```
## Commands

```
docker-compose -f filename up   #Builds, (re)creates, starts, and attaches to containers for a service.
docker-compose -f filename up -d # run docker containers in detach mode (bachground)
docker-compose -f filename down   #Stops and removes containers, networks, volumes, and images created by up.
docker-compose start   #Starts existing (stopped) containers for a service.
docker-compose stop   #Stops running containers without removing them. The data remain on docker container.
docker-compose build   #Builds or rebuilds services.
docker-compose logs   #Displays log output from services.
```


