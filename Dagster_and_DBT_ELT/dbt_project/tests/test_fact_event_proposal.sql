-- This test checks if the fact_proposal_event model has data
SELECT COUNT(*) AS record_count
FROM {{ ref('fact_event_proposal') }}
