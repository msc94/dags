from airflow import DAG
from airflow.operators.bash_operator import BashOperator

def task_1(dag: DAG):
    return BashOperator(task_id="bash_task", bash_command="echo 'Hello World!'", dag=dag)