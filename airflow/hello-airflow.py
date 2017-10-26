from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta


dag = DAG('hello-airflow',description='Hello airflow DAG',
        schedule_interval = '*/5 0 * * *',
        start_date=datetime(2017,7,1),
        catchup=False)


def print_hello():
    return 'Hello Airflow'


python_task = PythonOperator(
                    task_id='python_operator',
                    python_callable = print_hello,
                    dag = dag)


bash_task = BashOperator(
        task_id='print_date',
        bash_command='date',
        dag=dag)


bash_task.set_downstream(python_task)


