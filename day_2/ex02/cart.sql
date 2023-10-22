SELECT user_id, avg(price) FROM
	(
		SELECT 
			user_id,
			user_session,
			SUM(price) AS price
		FROM customers
		WHERE event_type = 'purchase'
		GROUP BY user_id, user_session
	) AS i
GROUP BY user_id