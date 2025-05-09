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

```
- name: instal and start nginx server
  hosts: webservers
  remote_user: root
  vars:
    tablename: foo
    tableowner: someuser

  tasks:
    - name: Rename table {{tablename}} to bar
      postgresql_table:
        table: {{tablename}}
        rename: bar
    - name: set owner to someuser
      postgresql_table:
        name: {{tablename}}
        owner: someuser
    - name: Truncate table
      postgresql_table:
        name: {{tablename}}
        truncate: yse

```

![image](https://github.com/user-attachments/assets/a044f027-15da-4997-8ddf-0f0400a1da49)
