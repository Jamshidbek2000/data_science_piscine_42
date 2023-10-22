SELECT user_id, SUM(price) as total
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
HAVING SUM(price) <= 250
ORDER BY total;