from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from run_model import upload_to_aws




default_args ={
    'owner': 'zobachukwu',
    'retries': 1,
    'retry_delay': timedelta(seconds=10)


}

run_dag=DAG(
    dag_id="chizoba_cynthia",
    description=" data gotten from response",
    default_args=default_args
)


task_one=PythonOperator(
    dag=run_dag,
    python_callable=upload_to_aws,
    task_id= "task_one"
)

task_one

