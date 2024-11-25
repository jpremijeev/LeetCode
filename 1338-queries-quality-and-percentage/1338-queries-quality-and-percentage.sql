# Write your MySQL query statement below
WITH QueryStats AS (
    SELECT
        query_name,
        CAST(rating AS DECIMAL(10, 2)) / position AS quality_ratio,
        CASE WHEN rating < 3 THEN 1 ELSE 0 END AS is_poor_query
    FROM
        Queries
    WHERE
        query_name IS NOT NULL
),
AggregatedStats AS (
    SELECT
        query_name,
        AVG(quality_ratio) AS avg_quality,
        SUM(is_poor_query) * 100.0 / COUNT(*) AS poor_query_percentage
    FROM
        QueryStats
    GROUP BY
        query_name
)
SELECT
    query_name,
    ROUND(avg_quality, 2) AS quality,
    ROUND(poor_query_percentage, 2) AS poor_query_percentage
FROM
    AggregatedStats;
