from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta


dag = DAG('project-workflow',description='Project Workflow DAG',
        schedule_interval = '*/5 0 * * *',
        start_date=datetime(2017,7,1),
        catchup=False)

xlsx_to_csv_task = BashOperator(
        task_id='xlsx_to_csv_operator',
        bash_command='sleep 1 && echo [xlsx_to_csv start]',
        dag=dag)

merge_task = BashOperator(
        task_id='merge_operator',
        bash_command='sleep 1 && echo [merge start]',
        dag=dag)

cleansing_task = BashOperator(
        task_id='cleansing_operator',
        bash_command='sleep 1 && echo [cleansing start]',
        dag=dag)

x1_task = BashOperator(
        task_id='x1_operator',
        bash_command='sleep 1 && echo [x1 start]',
        dag=dag)

x2_task = BashOperator(
        task_id='x2_operator',
        bash_command='sleep 2 && echo [x2 start]',
        dag=dag)

x3_task = BashOperator(
        task_id='x3_operator',
        bash_command='sleep 3 && echo [x3 start]',
        dag=dag)

y1_task = BashOperator(
        task_id='y1_operator',
        bash_command='sleep 1 && echo [y1 start]',
        dag=dag)

y2_task = BashOperator(
        task_id='y2_operator',
        bash_command='sleep 2 && echo [y2 start]',
        dag=dag)

segmentation_task = BashOperator(
        task_id='segmentation_operator',
        bash_command='sleep 1 && echo [segmentation start]',
        dag=dag)

merge_task.set_upstream(xlsx_to_csv_task)
cleansing_task.set_upstream(merge_task)
x1_task.set_upstream(cleansing_task)
x2_task.set_upstream(cleansing_task)
x3_task.set_upstream(cleansing_task)
y1_task.set_upstream(cleansing_task)
y2_task.set_upstream(cleansing_task)

x1_task.set_downstream(segmentation_task)
x2_task.set_downstream(segmentation_task)
x3_task.set_downstream(segmentation_task)

y1_task.set_downstream(segmentation_task)
y2_task.set_downstream(segmentation_task)


