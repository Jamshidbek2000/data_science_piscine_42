SELECT event_type, COUNT(*) as qty
FROM customers
GROUP BY event_type
ORDER BY qty DESC;