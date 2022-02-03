from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from first import task_1
from second import task_2

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
    t1 = task_1(dag)
    t2 = task_2(dag)

    # sets downstream for t1
    t1 >> t2
