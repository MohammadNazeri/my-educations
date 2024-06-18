# Docker compose
Docker Compose is a tool that simplifies the management of multi-container Docker applications. It allows you to define and run multi-container Docker applications using a YAML file. This file, commonly named docker-compose.yml, specifies the services, networks, and volumes that the application requires.

```
version: '3.8'  # Version of Docker Compose file syntax

services:
  web:          # Defines the containers
    image: nginx:latest
    ports:
      - "80:80"
    volumes:    
      - ./html:/usr/share/nginx/html
    networks:      
      - webnet

  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - webnet

volumes:      #Defines custom volumes
  db-data:

networks:    #Defines custom networks
  webnet:




```
