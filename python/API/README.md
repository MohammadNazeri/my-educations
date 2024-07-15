# API
* It is a set of rules, protocols, and tools that allows different software applications to communicate with each other. APIs define the methods and data formats that developers can use to interact with a service or a platform. It provides a way for developers to access certain features or data from a service or application without needing to understand the internal workings of that service.
* It could be run on various protocols.
* The various kinds of data format could be sent e.g. jason.
* "curl" command could be used for HTTP protocol.
* "request" library for requesting a http API
```
 response = request.get("url") > request API
 response.json()['data']['amount'] > extract amount pair in data of response.
 response = request.post('url', payload={'key':'value'})
```
* There are several types of APIs used in web services:
  * RESTful API (Representational State Transfer)
  * SOAP API (Simple Object Access Protocol)
  * GraphQL API
  * WebSocket API
  * JSON-RPC and XML-RPC APIs
* REST API:  is an architectural style for designing networked applications
* RESTfull API: It adheres to the principles of REST. A RESTful API is an API that uses HTTP requests.
* while "REST" defines the architectural style, "RESTful" describes applications or services that conform to this style.
