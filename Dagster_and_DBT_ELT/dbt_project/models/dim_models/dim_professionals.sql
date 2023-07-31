{{ config(
    materialized='table',
    schema='dim_models',
    indexes=[
      {'columns': ['n_professional_id'], 'unique': True},
    ],
    ) 
}}

SELECT
      professional_id         as n_professional_id
    , "first_Name"            as p_first_name
    , last_name               as p_last_name
    , email                   as p_email
FROM {{ ref('stg_professionals') }}