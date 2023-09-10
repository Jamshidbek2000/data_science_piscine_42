CREATE TABLE data_2023_feb (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2023_feb FROM '/tmp/data_2023_feb.csv' CSV HEADER;