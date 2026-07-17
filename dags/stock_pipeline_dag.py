from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, '..', 'config.json')
with open(config_path, "r") as f:
    config = json.load(f)

default_args = {
    'owner' : 'airflow',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=2),
    'email_on_failure' : True,
    'email' : config.get("emails")
}
  
with DAG (
    dag_id = "stock_pipeline",
    schedule = '0 6 * * MON-FRI',
    start_date = datetime(2026, 7, 1),
    catchup = False,
    default_args = default_args
) as dag:
    task1 = BashOperator(
        task_id = 'fetch_and_transform',
        bash_command = 'source /home/ubuntu/finance-data-pipeline/venv/bin/activate && python3 /home/ubuntu/finance-data-pipeline/src/fetch_transform.py'
    )

    task2 = BashOperator(
        task_id = 'load_to_rds',
        bash_command = 'source /home/ubuntu/finance-data-pipeline/venv/bin/activate && python3 /home/ubuntu/finance-data-pipeline/src/load_rds.py'
    )

    task3 = BashOperator(
        task_id = 'load_to_snowflake',
        bash_command = 'source /home/ubuntu/finance-data-pipeline/venv/bin/activate && python3 /home/ubuntu/finance-data-pipeline/src/load_snowflake.py'
    )

    task1 >> [task2, task3]