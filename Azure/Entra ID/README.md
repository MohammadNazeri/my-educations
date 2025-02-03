# Microsoft Entra ID:
## Identity
* User: Human identity with credentials (email/password).
* Group: Collection of users, simplifies permission management.
* Service Principal: Used by applications or services to authenticate and access resources, needs a client ID and secret or certificate.
* Managed Identity: Automatically created for Azure resources to authenticate securely to other Azure resources, no credentials required.

```
azd auth login
az account show
```
