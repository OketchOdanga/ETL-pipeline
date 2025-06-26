from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'datamart_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',  # Run the pipeline daily
    catchup=False # Do not run past dags
)

# Define the extraction tasks
extract_customer_data = PythonOperator(
    task_id='extract_customer_data',
    python_callable=extract_customer_data_function,  # Replace with your extraction function
    dag=dag,
)

extract_sales_data = PythonOperator(
    task_id='extract_sales_data',
    python_callable=extract_sales_data_function,  # Replace with your extraction function
    dag=dag,
)

extract_website_activity_data = PythonOperator(
    task_id='extract_website_activity_data',
    python_callable=extract_website_activity_data_function,  # Replace with your extraction function
    dag=dag,
)

# Define the transformation task
transform_data = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data_function,  # Replace with your transformation function
    dag=dag,
)

# Define the loading task
load_data = PythonOperator(
    task_id='load_data',
    python_callable=load_data_function,  # Replace with your loading function
    dag=dag,
)

# Define the task dependencies
[extract_customer_data, extract_sales_data, extract_website_activity_data] >> transform_data >> load_data