# Ansible
* It is a tool to automate IT tasks.
* The tasks could be repetitive tasks such as updates, back ups, create user, assign group, etc.

  ![image](https://github.com/user-attachments/assets/ba38ac35-bf7d-413e-bf80-d03897b2788f)

### Advantages
* Execute tasks from your own machine (agentless)
  * benefit: No deployment effort in beginning and No upgrade effort needs
* Configuration /installation/Deployment steps in a single YAML file
* Re-use same file multiple times and for different environment
* More reliable and less likely for errors
* supporting all insfrastructures like different OS and cloud platform

## Ansible Architecture
### Modules
* Module is Small programs that do the specific task such as create/copy file, install Nginx, start docker containers, etc.
* It gets pushed to the target server and does its work and get removed.
* list of prepared modules is in Ansible Official Documentation.

![image](https://github.com/user-attachments/assets/5072fd34-4947-46b5-8fd2-9a517afec8a5)

## Ansible Playbook
* Sequential module groups to tasks
* a play is a single set of instructions (tasks) that you want to run on a group of hosts (like code below). A playbook is made up of one or more plays.

```
- name: instal and start nginx server > play name
- hosts: webservers  >  target machine in which tasks should be executed
  remote_user: root  >  with which user those tasks should be executed
  vars:
    tablename: foo
    tableowner: someuser

  tasks:
    - name: Rename table {{tablename}} to bar  > description of task
      postgresql_table: > Module name
        table: {{tablename}}  >  arguments
        rename: bar  >  arguments
    - name: set owner to someuser
      postgresql_table:
        name: {{tablename}}
        owner: someuser
    - name: Truncate table
      postgresql_table:
        name: {{tablename}}
        truncate: yse

```

### Ansible inventory list 
* Ansible has host file which contains list of machine (inventory)
* The IP address or host names could be a group 

![image](https://github.com/user-attachments/assets/d3256076-2dcf-4e14-8f10-f9faa9f9973c)

NOTE: 
* Ansible alows you to reproduce application across many enviroment like docker contianer, cloud instance, bare metal, etc.
* Ansible can manage docker container, its host, and the all services like network and storage.
### Ansible Tower
It is UI dashboard from redhat to automate task, configure permissions, manage inventory
