# Application Architecture
## Monolith
* All code in one codebase
  * App must be in single language with one technology stack and single runtime.
  * to scale specific service, we can only scale the entire app. (which needs more resource)
  * All services should use the same version of code. By using different version, there would be different dependencies.
  * After chaning parts of code, realse process is long because it needs to test wholes app
![image](https://github.com/user-attachments/assets/249654d7-7e08-4ff3-b551-de6de8c20e38)



## Microservices
