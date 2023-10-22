
SELECT DATE_TRUNC('day', event_time) AS purchase_date, COUNT(*) AS qty
FROM customers
WHERE event_type = 'purchase'
GROUP BY purchase_date
ORDER BY purchase_date;