SELECT days, AVG(user_spent_per_day)
FROM 
	(
		SELECT DATE_TRUNC('day', event_time) AS days, user_id, SUM(price) AS user_spent_per_day
		FROM customers
		WHERE event_type = 'purchase'
		GROUP BY days, user_id
		ORDER BY days
	) as table_users_spent_per_day
GROUP BY days
ORDER BY days;
