# Docker compose
Docker Compose is a tool that simplifies the management of multi-container Docker applications. It allows you to define and run multi-container Docker applications using a YAML file. This file, commonly named docker-compose.yml, specifies the services, networks, and volumes that the application requires.

```
version: '3.8'  # Version of Docker Compose file syntax

services:    # Defines the containers 
  web:          # first container
    image: nginx:latest
    ports:
      - "80:80"
    volumes:    
      - ./html:/usr/share/nginx/html
    networks:?
      - webnet

  db:      # second container
    image: postgres:13
    environment:      #environmental variables
      POSTGRES_PASSWORD: example
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:?
      - webnet

volumes:      #Defines custom volumes
  db-data:

networks:    #Defines custom networks
  webnet:

```
## Commands

```
docker-compose up   #Builds, (re)creates, starts, and attaches to containers for a service.
docker-compose down   #Stops and removes containers, networks, volumes, and images created by up.
docker-compose start   #Starts existing containers for a service.
docker-compose stop   #Stops running containers without removing them.
docker-compose build   #Builds or rebuilds services.
docker-compose ps   #Lists containers.
docker-compose logs   #Displays log output from services.
```