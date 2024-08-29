# Application Architecture
## Monolith
* All code in one codebase
  * App must be in single language with one technology stack and single runtime.
  * to scale specific service, we can only scale the entire app. (which needs more resource)
  * All services should use the same version of code. By using different version, there would be different dependencies.
  * After chaning parts of code, realse process is long because it needs to test wholes app
   <img src="https://github.com/user-attachments/assets/249654d7-7e08-4ff3-b551-de6de8c20e38" alt="image" width="50%">



## Microservices
* App is converted into several micro app
* How to break down applications?
  * Beak down based on the buisiness functionalities not technical functionalities
  * Like products, shopping cart, user, and checkout for online website.
  * one microservice does one specific job
  * Microservices should be self-contained and independant from each other.
  * Lose coupled: They should be developed, deployed and scaled separately
* How do they connect to each other?
  1. API (Sync): Each service has an endpoint on which it accept Http requests from other services.
  2. Message Broker (Asynch): Services send their message first into intermediary message service or broker such as rabbitmq then broker forward that message to respctive service.
  ![image](https://github.com/user-attachments/assets/77e778ed-97f2-4d33-b870-a63dd963bc69)
  3. Service mesh (Kurbenets): there is helper service which takes over complete communication logic.
  <img src="https://github.com/user-attachments/assets/f5e2aef6-00dd-4d5c-95eb-3820e00d1e90" alt="image" width="50%">

 
