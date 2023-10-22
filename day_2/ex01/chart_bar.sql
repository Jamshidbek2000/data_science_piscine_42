SELECT DATE_TRUNC('month', event_time) AS purchase_month, SUM(price) AS sum
FROM customers
WHERE event_type = 'purchase'
GROUP BY purchase_month
ORDER BY purchase_month;
