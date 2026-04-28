# Airflow
* Apache Airflow is an open-source platform used to schedule, organize, and monitor workflows—especially data pipelines.
* Workflow: A workflow is simply a sequence of steps or tasks arranged to complete a specific goal, often with rules about the order in which things happen.
* DAG: it’s a way of representing tasks and their relationships, especially in workflows
* Task: A task is one step in a workflow, and many tasks together form a complete process.
* Operator: n operator is the template or building block used to define a task. You use an operator to create a task.
  * PythonOperator → runs Python functions
  * BashOperator → runs shell commands
  * PostgresOperator → runs SQL queries in PostgreSQL
  * HttpOperator → makes API requests
* Execution Date: the execution date is the logical date that a workflow run is associated with, not necessarily the exact time it actually runs.
* Task Instance: a task instance is a specific execution of a task at a specific time (within a specific DAG run).
* Dag Run: a DAG run is one complete execution of a DAG at a specific time (or for a specific logical date).


<img width="1251" height="440" alt="image" src="https://github.com/user-attachments/assets/5d33bfd3-de82-41f0-8cbe-df83543f36c7" />

the task lifecycle describes the sequence of states a task instance goes through from creation to completion (or failure).

<img width="1255" height="53" alt="image" src="https://github.com/user-attachments/assets/f6bfa0b1-61a1-4fc1-bb1e-395654c5f5ce" />

Sequence of tasks stages:

<img width="1264" height="461" alt="image" src="https://github.com/user-attachments/assets/b4af232f-f017-4d92-a97a-539dcb113174" />

## Basic Architecture

Steps to create workflow
1. Data Engineer creates DAG through airflow interface (web)
2. DAG is visible to scheduler and worker
3. Executer to update and recieve info from DAG which is connected to DB

<img width="904" height="469" alt="image" src="https://github.com/user-attachments/assets/8add88ad-2c39-4b90-8940-433103015281" />

## BashOperator

### Installation

[Docker compose](https://example.com](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)


