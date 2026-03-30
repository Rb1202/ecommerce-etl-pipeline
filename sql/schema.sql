CREATE DATABASE ecommerce_db;

CREATE TABLE customers (
    customer_id TEXT,
    customer_unique_id TEXT,
    customer_city TEXT
);

CREATE TABLE products (
    product_id TEXT,
    product_category_name TEXT,
    product_weight_g INT
);

CREATE TABLE orders (
    order_id TEXT,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TIMESTAMP
);