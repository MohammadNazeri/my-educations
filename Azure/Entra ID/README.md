# Microsoft Entra ID:
Microsoft Entra ID (formerly known as Azure Active Directory or Azure AD) is Microsoft's identity and access management (IAM) service, offering a range of solutions for managing users, groups, devices, and resources securely across cloud and on-premises environments. It provides centralized authentication, authorization, and security management for users, apps, and devices within an organization.

## Entra ID Features
* Identity Management: It allows for managing user identities and groups, providing tools for user lifecycle management (e.g., creating, updating, and deleting accounts).
* Access Management: This covers role-based access control (RBAC) and policies for controlling access to resources based on roles or attributes.
* Authentication: Supports various authentication mechanisms, including multi-factor authentication (MFA), passwordless authentication, and conditional access policies.
* Single Sign-On (SSO): Users can sign in once and gain access to multiple apps and services without having to authenticate again.
* Identity Protection: This feature helps detect and mitigate risks to user identities by identifying suspicious sign-in attempts and implementing automated policies like requiring MFA for high-risk sign-ins.
* External Identities (B2B/B2C): Enables collaboration with external users (via B2B) or supports customer-facing applications (via B2C).

## Identity
* User: Human identity with credentials (email/password).
* Group: Collection of users, simplifies permission management.
* Service Principal: Used by applications or services to authenticate and access resources, needs a client ID and secret or certificate.
* Managed Identity: Automatically created for Azure resources to authenticate securely to other Azure resources, no credentials required.

## Access Control mechanism
* Role-Based Access Control (RBAC): it is used to assign roles to identities (users, groups, or service principals) that define what actions they can perform on which resources. While RBAC itself is not an identity, it's often used in conjunction with the identities listed above.

```
azd auth login
az account show
```
