from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
from airflow.models import Variable

#SRC=Variable.get("SRC")
SRC='./'
#COUNTRY=Variable.get("COUNTRY")
COUNTRY='PL'

dag = DAG('project-workflow',description='Project Workflow DAG',
        schedule_interval = '*/5 0 * * *',
        start_date=datetime(2017,7,1),
        catchup=False)

xlsx_to_csv_task = BashOperator(
        task_id='xlsx_to_csv',
        bash_command='"$src"/test.sh "$country" 2nd_param_xlsx',
        env={'src': SRC, 'country': COUNTRY},
        dag=dag)

merge_command = SRC + '/test.sh ' + COUNTRY + ' 2nd_param_merge'
merge_task = BashOperator(
        task_id='merge',
        bash_command=merge_command ,
        dag=dag)

my_templated_command = """
{{ params.src }}/test.sh {{ params.country}} 2nd_param_cleansing
"""
cleansing_task = BashOperator(
        task_id='cleansing',
        bash_command=my_templated_command, 
        params={'src': SRC, 'country': COUNTRY},
        dag=dag)

x1_task = BashOperator(
        task_id='x1',
        bash_command='sleep 1 && echo [x1 start]',
        dag=dag)

x2_task = BashOperator(
        task_id='x2',
        bash_command='sleep 2 && echo [x2 start]',
        dag=dag)

x3_task = BashOperator(
        task_id='x3',
        bash_command='sleep 3 && echo [x3 start]',
        dag=dag)

y1_task = BashOperator(
        task_id='y1',
        bash_command='sleep 1 && echo [y1 start]',
        dag=dag)

y2_task = BashOperator(
        task_id='y2',
        bash_command='sleep 2 && echo [y2 start]',
        dag=dag)

segmentation_task = BashOperator(
        task_id='segmentation',
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


