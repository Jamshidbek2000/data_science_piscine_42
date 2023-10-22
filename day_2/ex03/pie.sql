SELECT user_id, COUNT(*) as qty_of_purchase
FROM customers
WHERE event_type = 'purchase'
GROUP BY user_id
HAVING COUNT(*) <= 40
ORDER BY qty_of_purchase;