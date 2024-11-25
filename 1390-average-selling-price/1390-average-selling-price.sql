# Write your MySQL query statement below
WITH PriceCalculation AS (
    SELECT
        u.product_id,
        u.units,
        p.price * u.units AS total_price
    FROM
        UnitsSold u
    JOIN
        Prices p
    ON
        u.product_id = p.product_id
        AND u.purchase_date BETWEEN p.start_date AND p.end_date
),
TotalUnitsAndPrice AS (
    SELECT
        product_id,
        SUM(units) AS total_units,
        SUM(total_price) AS total_revenue
    FROM
        PriceCalculation
    GROUP BY
        product_id
)
SELECT
    p.product_id,
    ROUND(COALESCE(total_revenue / NULLIF(total_units, 0), 0), 2) AS average_price
FROM
    Prices p
LEFT JOIN
    TotalUnitsAndPrice t
ON
    p.product_id = t.product_id
GROUP BY
    p.product_id;
