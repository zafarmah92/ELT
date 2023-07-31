
{{ config(
    materialized='table',
    schema='dim_models',
    ) 
}}


WITH active_professionals AS (
  SELECT
    DATE_TRUNC('day', n_created_at) AS day,
    COUNT(DISTINCT n_professional_id_anonymized) AS active_count
  FROM {{ ref('stg_event_log') }}
  WHERE n_event_type = 'become_able_to_propose'
    AND DATE_TRUNC('day', n_created_at) BETWEEN (SELECT MIN(DATE_TRUNC('day', n_created_at)) 
                                                FROM {{ ref('stg_event_log') }})
                                            AND DATE '2020-03-11'
  GROUP BY DATE_TRUNC('day', n_created_at)
)
SELECT
  day,
  COALESCE(active_count, 0) AS active_professionals_count
FROM (
  SELECT GENERATE_SERIES(
           (
            SELECT MIN(DATE_TRUNC('day', n_created_at)) 
            FROM {{ ref('stg_event_log') }}),
            DATE '2020-03-10',
            '1 day'::INTERVAL
         )::DATE AS day
) AS dates
LEFT JOIN active_professionals USING (day)
ORDER BY day
