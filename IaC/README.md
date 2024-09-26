# IaC
![image](https://github.com/user-attachments/assets/c8af548e-c285-49d4-a8e8-d63207c11836)

Common example is using 
* Terraform to provision and configure infrustructure
* Ansible to install and deploy applications

Difference of IaC tools:
* declarative vs procedural
  * Declarative = Define WHAT end result you want
* mutable vs immutable
* agent vs agentless

## Terraform
* Automate and manage infrustracture, platform, services thar run on that platform
* Declarative
* Open source
### Terraform Architecture
It has two main components:
1. Core
 * It use two input source to do its job:
  > Configuration file: What needs to be created/configured?
  > 
![image](https://github.com/user-attachments/assets/0a4c8839-834a-4519-a289-7dc4e5f8d135)

