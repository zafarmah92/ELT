# """Definitions that provide Dagster code locations."""

from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_package_module,
)
from dagster_dbt import DbtCliClientResource

from . import assets
from .io.pg_db_io_manager import DbIOManager
from .io import  db_io_manager  
from .utils.constants import DBT_CONFIG

defs = Definitions(
    assets=load_assets_from_package_module(assets),
    resources={
        "dbt": DbtCliClientResource(**DBT_CONFIG),
        "db_io": db_io_manager.postgres_pandas_io_manager.configured(
            {
             "pwd":"secret",
              "uid":"postgres",
              "server":"host.docker.internal",
              "db":"postgres",
              "port":5432 
            }
         )
    },
    schedules=[
        ScheduleDefinition(
            job=define_asset_job("all_assets", selection='*'), cron_schedule="@daily"
        ),
    ],
)
