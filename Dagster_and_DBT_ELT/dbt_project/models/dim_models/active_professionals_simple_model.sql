
{{ config(
    materialized='table',
    schema='dim_models',
    ) 
}}


SELECT DATE(n_created_at) AS n_created_at, COUNT(DISTINCT n_professional_id_anonymized) AS n_active_professionals_count
FROM  {{ ref('stg_event_log') }}
WHERE n_event_type = 'became_able_to_propose'
GROUP BY DATE(n_created_at)
ORDER BY DATE(n_created_at)
