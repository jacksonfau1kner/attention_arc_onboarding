import logging
import os
from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from search_pacing.search_pacing import client_config, dag_config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),  # DO NOT CHANGE THIS
    "depends_on_past": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
    "catchup": False,
}

with DAG(
    "search_pacing_dashboards",
    default_args=default_args,
    description="DAG for Search Pacing Dashboards",
    schedule_interval="0 7 * * *",
    tags=["search"],
) as dag:
    client_configs = client_config.CLIENT_CONFIGS
    logging.info(f"Found {len(client_configs)} client configurations")

    # Set up each client in its own task group
    for client_key, client_config_obj in client_configs.items():
        logging.info(f"Setting up TaskGroup for client: {client_key}")

        with TaskGroup(group_id=client_key) as client_process:
            # Set up the client's operators and task dependencies using the new function
            dag_config.setup_client_in_dag(
                client_key, client_config_obj, dag, client_process
            )

    logging.info("DAG setup complete")
