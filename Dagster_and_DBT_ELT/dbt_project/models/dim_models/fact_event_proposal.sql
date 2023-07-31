
{{ config(
    materialized='table',
    schema='dim_models',
    ) 
}}

SELECT
     el.n_event_id 
    , el.n_event_type
    , el.n_professional_id_anonymized
    , el.n_created_at
    , el.n_meta_data
    , el.n_payment_to_instapro
    , dp.n_id                          AS n_proposal_id
    , dp.n_house_owner_id
    , dp.n_message_text
    , dp.n_proposal_amount
    , dpf.p_first_name
    , dpf.p_last_name
    , dpf.p_email
FROM {{ ref('stg_event_log') }} AS el
LEFT JOIN {{ ref('dim_proposals') }} AS dp 
    ON el.n_professional_id_anonymized = dp.n_professional_id
LEFT JOIN {{ ref('dim_professionals') }} as dpf 
    ON el.n_professional_id_anonymized = dpf.n_professional_id