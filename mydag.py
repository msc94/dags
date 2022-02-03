from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 4, 30),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    "my_dag",
    description="My first DAG",
    schedule_interval="0 12 * * *",
    default_args=default_args,
    catchup=False,
) as dag:
    t1 = BashOperator(task_id="task1", bash_command="echo 'Hello World?'")
    t2 = BashOperator(task_id="task2", bash_command="echo 'Hello World!'")

    # sets downstream for t1
    t1 >> t2
