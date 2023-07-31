from dagster import  asset
from dagster_dbt import load_assets_from_dbt_project
import pandas as pd
import logging
import numpy as np
from scipy import optimize
from ..utils.constants import  DBT_PROJECT_DIR
import random
import string
from ownerjobs.utils.constants import N_ROWS


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email():
    domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    username_length = random.randint(5, 10)
    domain_name = random.choice(domain)
    username = generate_random_string(username_length)
    return f'{username}@{domain_name}'


@asset(key_prefix=['dbt_project'],group_name="ProductCategory", compute_kind="pandas", io_manager_key="db_io")
def raw_professional_synthetic_data(context) -> pd.DataFrame:
    """
    Creates synthetic data for professional 
    """
    data = []
    for i in range(N_ROWS):
        row = {
            'professional_id': i,
            'first_Name': generate_random_string(6),
            'last_name': generate_random_string(8),
            'email': generate_random_email()
        }
        data.append(row)
    return pd.DataFrame(data)

@asset(key_prefix=['dbt_project'],group_name="ProductCategory", compute_kind="pandas", io_manager_key="db_io")
def raw_proposal_synthetic_data(context)-> pd.DataFrame:
    """
    creates synthetic data for proposal that joins with house owners.
    """
    data = []
    for i in range(N_ROWS):
        row = {
            'id': random.randint(1, 100),
            'house_owner_id': random.randint(1, 100),
            'professional_id': i,
            'message_text': generate_random_string(20),
            'proposal_amount': random.uniform(1000, 5000)
        }
        data.append(row)
    return pd.DataFrame(data)


@asset(key_prefix=['dbt_project'],group_name="ProductCategory", compute_kind="pandas", io_manager_key="db_io")
def raw_professional_event_log(context) -> pd.DataFrame:
    """
    Reads the raw event log data
    """
    read_df = pd.read_csv('./ownerjobs/raw_data/event_log.csv',delimiter=';')
    context.log.info(read_df.head(5))
    return read_df


dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_DIR, key_prefix=["dbt_project"]
)

