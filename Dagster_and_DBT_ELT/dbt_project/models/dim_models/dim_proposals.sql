{{ config(
    materialized='table',
    schema='dim_models',
    indexes=[
      {'columns': ['n_id'] },
      {'columns': ['n_professional_id'], 'unique': True},
    ],
    ) 
}}
SELECT
      id                     as n_id
    , house_owner_id         as n_house_owner_id
    , professional_id        as n_professional_id  
    , message_text           as n_message_text
    , proposal_amount        as n_proposal_amount
FROM {{ ref('stg_proposals') }}