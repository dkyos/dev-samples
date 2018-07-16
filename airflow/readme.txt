#################################################################
http://bcho.tistory.com/1184

export all_proxy=http://172.21.101.204:3128/

pip install apache-airflow
# error uninstall html5lib
pip install apache-airflow --ignore-installed html5lib 

pip list | grep airflow
apache-airflow                     1.9.0      

# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME=.

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080


# add username/pasword
# edit airflow.cfg
# Set to true to turn on authentication:
authenticate = True
auth_backend = airflow.contrib.auth.backends.password_auth


using python add default user


airflow list_dags
airflow list_tasks -t project-workflow
airflow scheduler

airflow run --force project-workflow segmentation 2017-7-1
airflow run --force project-workflow xlsx_to_csv 2017-7-1

airflow clear project-workflow -s 2017-7-1 -e 2017-12-31


airflow test project-workflow xlsx_to_csv 2017-07-02
airflow test project-workflow merge 2017-07-02
airflow test project-workflow cleansing 2017-07-02
airflow test project-workflow x1 2017-07-02
airflow test project-workflow y1 2017-07-02
airflow test project-workflow segmentation 2017-07-02


airflow backfill project-workflow -s 2017-07-01 -e 2017-07-07
#################################################################
git clone https://github.com/apache/incubator-airflow
cd incubator-airflow/airflow/example_dags

