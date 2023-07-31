{{ 
  config(
    materialized='table',
    schema='staging',
    indexes=[
      {'columns': ['n_event_id'], 'unique': True},
      {'columns': ['n_professional_id_anonymized']},
    ]
  )
}}

select
      event_id                                  as n_event_id               
    , event_type                                as n_event_type       
    , professional_id_anonymized                   as n_professional_id_anonymized
    , TO_TIMESTAMP(created_at,'YYYY-MM-DD HH24:MI:SS')       as n_created_at   
    , meta_data         as n_meta_data
    , SPLIT_PART(meta_data , '_', -1)  as n_payment_to_instapro         
from {{ source('dbt_project', 'raw_professional_event_log') }}
