from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import os
import requests
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def test_openmetadata_connection():
    """
    Test connection to OpenMetadata server
    """
    openmetadata_server_url = os.getenv('OPENMETADATA_SERVER_URL', 'http://192.168.1.29:8585/api')
    admin_user = os.getenv('OPENMETADATA_ADMIN_USER', 'chiennguyen21092003@gmail.com')
    admin_password = os.getenv('OPENMETADATA_ADMIN_PASSWORD', 'rVJ#00_k')
    
    # Endpoint for authentication
    auth_endpoint = f"{openmetadata_server_url}/v1/users/login"
    
    # Prepare login data
    login_data = {
        "email": admin_user,
        "password": admin_password
    }
    
    try:
        # Authenticate to get JWT token
        response = requests.post(auth_endpoint, json=login_data)
        response.raise_for_status()
        
        token = response.json().get('token')
        if not token:
            return f"Authentication successful but no token received: {response.json()}"
        
        # Test connection to OpenMetadata API with token
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Get list of services to verify connection
        services_endpoint = f"{openmetadata_server_url}/v1/services/databaseServices"
        services_response = requests.get(services_endpoint, headers=headers)
        services_response.raise_for_status()
        
        return f"Successfully connected to OpenMetadata. Found {len(services_response.json().get('data', []))} database services."
    
    except Exception as e:
        return f"Error connecting to OpenMetadata: {str(e)}"

with DAG(
    'openmetadata_connection_test',
    default_args=default_args,
    description='Test connection to OpenMetadata',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['openmetadata', 'test'],
) as dag:

    test_connection = PythonOperator(
        task_id='test_openmetadata_connection',
        python_callable=test_openmetadata_connection,
    )

    test_connection
