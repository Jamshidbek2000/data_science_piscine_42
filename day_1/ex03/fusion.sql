--------------------------------------------------------------------------------------------

-- create a new table "items_nodup"
-- without duplicate product_id's
-- removing empty entries:
-- (category_id, category_code and brand)

CREATE TABLE IF NOT EXISTS items_nodup AS
SELECT
    product_id,
    COALESCE(MAX(category_id), NULL) AS category_id,
    COALESCE(MAX(category_code), NULL) AS category_code,
    COALESCE(MAX(brand), NULL) AS brand
FROM
    items
GROUP BY
    product_id;

--------------------------------------------------------------------------------------------

-- add missing 3 columns to table "customers"
-- the new columns will be empty

-- ALTER TABLE customers
-- ADD COLUMN category_id BIGINT,
-- ADD COLUMN category_code VARCHAR(255),
-- ADD COLUMN brand VARCHAR(255);


--------------------------------------------------------------------------------------------


-- fill table "customers" with data received by "items_nodup"

-- UPDATE customers c
-- SET
--     category_id = i.category_id,
--     category_code = i.category_code,
--     brand = i.brand
-- FROM items_nodup i
-- WHERE c.product_id = i.product_id;


--------------------------------------------------------------------------------------------


-- to see result

-- SELECT * FROM customers ORDER BY product_id LIMIT 200;


--------------------------------------------------------------------------------------------