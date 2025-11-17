
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Funkcja, którą wykona zadanie
def hello_world():
    print("Dag executer from --feature02--")

# Definicja DAG
with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2025, 11, 14),
    schedule_interval="@daily",  # uruchamiane codziennie
    catchup=False,
    tags=["example"]
) as dag:

    # Zadanie
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=hello_world
    )

    hello_task
