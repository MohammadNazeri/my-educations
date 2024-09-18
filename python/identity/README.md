# Identity
* A digital identity is a collection of unique identifiers or attributes that represent a human, software component, etc
* Identities are used to authenticate and authorize access to resources, etc
* Types of Identity: Human identities, Workload identities, Device identities
* Authentication proves the identity of a user, machine, or software component.
* Authorization grants or denies the user, machine, or software component access to certain resources.
* the IAM system acts as the source of identity truth for the other resources available to the user. It removes the need for signing on to multiple, separate target systems.
* An identity provider creates, maintains, and manages identity information while offering authentication, authorization, and auditing services.
* With modern authentication, all services, including all authentication services, are supplied by a central identity provider.
* Microsoft Entra is an example of a cloud-based identity provider.
# Token
Three types of bearer tokens are used by the identity platform as security tokens:
* Access tokens - Access tokens are issued by the authorization server to the client application. The client passes access tokens to the resource server. Access tokens contain the permissions the client has been granted by the authorization server.
* ID tokens - ID tokens are issued by the authorization server to the client application. Clients use ID tokens when signing in users and to get basic information about them.
* Refresh tokens - The client uses a refresh token, or RT, to request new access and ID tokens from the authorization server. 
