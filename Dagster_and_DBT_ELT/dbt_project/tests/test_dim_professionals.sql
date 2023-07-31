SELECT COUNT(*) AS record_count
FROM {{ ref('dim_professionals') }}
