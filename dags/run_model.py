import requests
import pandas as pd
import boto3
import awswrangler as wr 
import os
from dotenv import load_dotenv


load_dotenv()


url = "https://randomuser.me/api/?results=10"

def results_df():

    url = 'https://randomuser.me/api/?results=10'
    response = requests.get(url)

    if response.status_code == 200:
        response_url = response.json()
        results = response_url["results"]
        
    else:
        print("Error: Unable to fetch data from the API")

    results_df = pd.DataFrame(results)

    return results_df



"""
This function defines the parameters for the aws_session connection
"""
def aws_session():
    session = boto3.Session(
    aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key= os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name = os.getenv('AWS_DEFAULT_REGION'))
    return session

"""
defining the function to export the results in the dataframe
into the defined bucket path in aws
"""

def upload_to_aws():
    wr.s3.to_csv(
    df=results_df(),
    path="s3://chizoba-airflow-docker/airflow_docker/",
    boto3_session=aws_session(),
    mode="append",
    dataset=True
    )
    return



