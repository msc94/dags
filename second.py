import random
import os

from airflow import DAG
from airflow.operators.python import PythonOperator

from minio import Minio
from io import BytesIO


def print_hello():
    client = Minio("k3s1:32000", "rootuser", "rootpass123", secure=False)

    bucket_name = "hello"
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    # Create random filename
    object_name = format(random.getrandbits(256), "x")
    content = os.urandom(1024)
    io = BytesIO(content)

    client.put_object(bucket_name, object_name, io, len(content))

    return object_name


def task_2(dag: DAG):
    return PythonOperator(task_id="python_task", python_callable=print_hello, dag=dag)
