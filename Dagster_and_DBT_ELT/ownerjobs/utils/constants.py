from dagster._utils import file_relative_path
from dagster_postgres.utils import get_conn_string

# =========================================================================
# To get this value, run `python -m assets_modern_data_stack.setup_airbyte`
# and grab the connection id that it prints at the end
# =========================================================================


PG_CONFIG = {
             "pwd":"secret",
              "uid":"postgres",
              "server":"host.docker.internal",
              "db":"postgres",
              "port":5432 
}

PG_DESTINATION_CONFIG = {
    "username": "postgres",
    "password": "secret",
    "host": "host.docker.internal",
    "port": 5432,
    "database": "postgres",
}

N_ROWS = 10

DBT_PROJECT_DIR = file_relative_path(__file__, "../../dbt_project")
DBT_PROFILES_DIR = file_relative_path(__file__, "../../dbt_project/config")
DBT_CONFIG = {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROFILES_DIR}
POSTGRES_CONFIG = {
    "con_string": get_conn_string(
        username=PG_DESTINATION_CONFIG["username"],
        password=PG_DESTINATION_CONFIG["password"],
        hostname=PG_DESTINATION_CONFIG["host"],
        port=str(PG_DESTINATION_CONFIG["port"]),
        db_name=PG_DESTINATION_CONFIG["database"],
    )
}
