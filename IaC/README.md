# IaC
![image](https://github.com/user-attachments/assets/c8af548e-c285-49d4-a8e8-d63207c11836)
<img src="https://github.com/user-attachments/assets/c8af548e-c285-49d4-a8e8-d63207c11836" alt="image" width="50%">

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
 * It takes two input and figure out a plan of what needs to be done. It compare current state and configuration file(our desire) > make plan
 * It use two input source to do its job:
   * Configuration file: What needs to be created/configured?
   * Terraform State: Current state of setup > It keeps the up-to-date state of how the current set up of the infrustructure looks like.
![image](https://github.com/user-attachments/assets/0a4c8839-834a-4519-a289-7dc4e5f8d135)

