#################################################################
http://bcho.tistory.com/1184

pip install airflow

airflow initdb
airflow webserver -p 8080


airflow list_dags
airflow list_tasks -t project-workflow
airflow scheduler

airflow run --force project-workflow segmentation_operator 2017-7-1
airflow run --force project-workflow xlsx_to_csv_operator 2017-7-1

airflow clear project-workflow -s 2017-7-1 -e 2017-12-31


airflow test project-workflow xlsx_to_csv_operator 2017-07-02
airflow test project-workflow merge_operator 2017-07-02
airflow test project-workflow cleansing_operator 2017-07-02
airflow test project-workflow x1_operator 2017-07-02
airflow test project-workflow y1_operator 2017-07-02
airflow test project-workflow segmentation_operator 2017-07-02


airflow backfill project-workflow -s 2017-07-01 -e 2017-07-07
#################################################################
git clone https://github.com/apache/incubator-airflow
cd incubator-airflow/airflow/example_dags

