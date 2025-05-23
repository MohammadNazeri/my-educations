# Oauth2
* In simple example, the scenario cosists of user, application, and API(Authentication server+Resource server)
* Authentication server is only responsible for authorizing Sarah as a user and providing proper access token that will eventually alow application to retrieve info from Resource server.
* Access token send to application. This token will be included in request from application to Resource server. Application can access to limited things that user granted.
* Oauth2 is a authorization framework. Authentication occurs with OpenID Connect through the use of ID tokens( two arrow with Access Token).

![image](https://github.com/user-attachments/assets/d776c823-50c7-4c6d-9381-56cef96f7e63)

* Application should be registered in Resource server. To do so, API is provided with :
  * Name, website, and Callback URL
  * Callback URL: Resource server authorization will redirect the user after they have authorized access to their account
* After that, Resource server send back Client ID and Client Secret. THey are used to authenticate application when it makes request for an access token.
  * Client ID: public and unique identifier
  * Client Secret: private identifier between app and API
![image](https://github.com/user-attachments/assets/7aac2ce2-e867-4302-972b-48dfd24b8bec)

## Microsoft Entra ID
![image](https://github.com/user-attachments/assets/0a136a78-44ef-4e16-8142-0446198c7bb5)

## Tokens
* Access Tokens are used to access resources and have scopes and expiry times.
* ID Tokens provide user identity information and are used in authentication processes.
* Refresh Tokens are used to get new access tokens without re-authenticating.
* Authorization Codes are intermediate tokens used in OAuth 2.0 flows to get access and ID tokens.
* Bearer Tokens are a general term for tokens used in HTTP authorization headers.
