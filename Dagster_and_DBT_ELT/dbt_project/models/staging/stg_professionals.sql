{{ 
  config(
    materialized='table',
    schema='staging',
  )
}}

select 
    *
from {{ source('dbt_project', 'raw_professional_synthetic_data') }} 
