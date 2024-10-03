# IaC
Difference of IaC tools:
* declarative vs procedural
  * Declarative = Define WHAT end result you want
* mutable vs immutable
* agent vs agentless

Common example is using 
* Terraform to provision and configure infrustructure
* Ansible to install and deploy applications

<img src="https://github.com/user-attachments/assets/c8af548e-c285-49d4-a8e8-d63207c11836" alt="image" width="50%">

## Terraform
* Automate and manage infrustracture, platform, services thar run on that platform
* Declarative
* Open source
### Terraform Architecture
It has two main components:
1. Core   
  1.1 It takes two input and figure out a plan of what needs to be done. It compare current state and configuration file(our desire) > make plan   
  1.2 It use two input source to do its job:   
    * Configuration file: What needs to be created/configured?
    * Terraform State: Current state of setup > It keeps the up-to-date state of how the current set up of the infrustructure looks like.
2. Provider for specific technology   
2.1 It works in different levels:   
  * infrustracture as a Service: AWS, Azure > Cloud provider
  * Platform as a Service: Kubernetes
  * Software as a Service: Fastly
  
<img src="https://github.com/user-attachments/assets/0a4c8839-834a-4519-a289-7dc4e5f8d135" alt="image" width="50%">

### Terraform command
1. refresh > query infrustructure provider to get current state
2. plan > Core creates an execution plan by comparing two files
3. apply > execute the plan
4. destroy > destroy the resource/infrastructure
### Terraform code

* The Terraform language uses a limited number of top-level block types, which are blocks that can appear outside of any other block in a configuration file. Most of Terraform's features (including resources, input variables, output values, data sources, etc.) are implemented as top-level blocks.
  
```
[block type] [label (provision)] [lable(instance name]{

[further arguments and blocks may be nested]

}
```
```
resource "aws_instance" "example" {
  ami = "abc123"

  network_interface {
    # ...
  }
}
```

### Terraform file structure
* main.ft: define the primary resources for your infrastructure.
* variables.tf: variable definitions
* outputs.tf: outputs of your Terraform configuration, allowing you to return data after your resources are created.
* terraform.tfvars: to set the values of the variables defined in variables.tf. It allows you to provide specific configurations without hardcoding them.
* provider.tf: to configure the provider(s) you are using (e.g., AWS, Azure, Google Cloud).
* modules/: This directory contains reusable modules. Each module has its own subdirectory with its own main.tf, variables.tf, and outputs.tf files. This keeps your code DRY (Don't Repeat Yourself) and organized.

## [Terraformer](https://github.com/GoogleCloudPlatform/terraformer?tab=readme-ov-file)

### current state for terraform in azure
https://www.youtube.com/watch?v=V53AHWun17s
https://www.youtube.com/watch?v=YcJ9IeukJL8
https://medium.com/expert-thinking/mastering-azure-search-with-terraform-a-how-to-guide-7edc3a6b1ee3
https://registry.terraform.io/providers/Mastercard/restapi/latest
