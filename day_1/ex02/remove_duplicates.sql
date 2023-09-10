CREATE TEMPORARY TABLE tmp_customers AS SELECT DISTINCT * FROM customers;
TRUNCATE customers;
INSERT INTO customers SELECT * FROM tmp_customers;