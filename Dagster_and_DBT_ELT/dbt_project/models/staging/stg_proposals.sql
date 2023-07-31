{{ 
  config(
    materialized='table',
    schema='staging',
  )
}}

select 
    *
from {{ source('dbt_project', 'raw_proposal_synthetic_data') }} 
