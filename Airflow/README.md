# Airflow
* Apache Airflow is an open-source platform used to schedule, organize, and monitor workflows—especially data pipelines.

### Initialization
```
export AIRFLOW_HOME=.
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:////home/user/airflow/airflow.d
airflow db migrate
```
