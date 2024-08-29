# Application Architecture
## Monolith
* All code in one codebase
  * App must be in single language with one technology stack and single runtime.
  * to scale specific service, we can only scale the entire app. (which needs more resource)
  * All services should use the same version of code. By using different version, there would be different dependencies.
  * After chaning parts of code, realse process is long because it needs to test wholes app
![image](https://github.com/user-attachments/assets/249654d7-7e08-4ff3-b551-de6de8c20e38)



## Microservices
* App is converted into several micro app
* How to break down applications?
  * Beak down based on the buisiness functionalities not technical functionalities
  * Like products, shopping cart, user, and checkout for online website.
  * one microservice does one specific job
  * Microservices should be self-contained and independant from each other.
  * Lose coupled: They should be developed, deployed and scaled separately
* 
