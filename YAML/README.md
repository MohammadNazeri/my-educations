# YAML
* YAML is a human-readable data serialization format used for data storage and transmission.
* Application use standard format to send data to each other such as YAML, JSON, XML.

<img src="https://github.com/user-attachments/assets/923f1032-9fa6-4ca6-820c-15d3ddb4f91b" style="width: 50%;" />


### YAML vs JSON 
While YAML is similar to JSON in that both are data serialization formats, YAML offers:
  * Supports comments (JSON doesn't).
  * Supports multi-line strings and complex data types.
  * Has a cleaner syntax (no need for quotes around strings or commas between items in lists).
  * However, YAML's syntax can be more prone to errors due to reliance on indentation, whereas JSON is simpler and more rigid, which can sometimes make it more predictable in terms of parsing and handling.

## Format
* line separation
* Spaces with indentations

## Syntax of YAML
  * key:value pairs (NOTE: for string value, using quote is optional)
  * comments > with # sign
  * object > by using indentation
    * it has key with (probably) some attributes

```
# All of lines below are one object in which has multi attributes
microservices:
  app: user-auth
  port: 9000
  version: 1.7
```
  * list > by adding - to first of line
```
# list of objects
microservices:
  -  app: user-auth
     port: 9000
     version: 1.7
  - app: shopping-cart
    port: 9002
    version: 1.9

# list of simple value
microservices:
  - user-auth
  - shopping cart

# alternative way of defining list
microservice: [user-auth, shopping-cart]
```
  * boolean value > ```deploy: false```
  * multi line strings > lines after | will be interpreted  as a multi lines string
```
mulltilinestring:|
this is multi line string
this is multi line string
this is multi line string
```
The screenshot shows shell command with multiple lines  
<img src="https://github.com/user-attachments/assets/9f76613b-0da0-4cf2-9acd-f66f37dbbaf6" style="width: 30%;" />

  * Enviromental variable > $ shows value of variables
  * Placeholder: {{.value.service.app}} it find the value inside "value object">service object > app
    * NOTE: mostly it uses in helm or ansible
    * To pass the value there are two way:
      * assign values in value.yaml file > helm install mychart ./mychart -f values.yaml
      * pass them as CLI argument > helm install mychart ./mychart --set value.service.app=myapp
  * Multiple yaml documents: separate component by ---


<img src="https://github.com/user-attachments/assets/1c5830ce-0d20-4aff-aae2-f0fbc75412c6" style="width: 30%;" />


