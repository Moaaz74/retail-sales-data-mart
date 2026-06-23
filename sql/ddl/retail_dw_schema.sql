-- =========================
-- SCHEMA
-- =========================
CREATE SCHEMA IF NOT EXISTS dw;
SET search_path TO dw;

-- =========================
-- DIMENSIONS
-- =========================

-- DimDate
CREATE TABLE dw.dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
    year INT NOT NULL,
    quarter INT NOT NULL,
    month INT NOT NULL,
    month_name VARCHAR(20) NOT NULL,
    day INT NOT NULL,
    day_name VARCHAR(20) NOT NULL,
    week_of_year INT NOT NULL,
    is_weekend BOOLEAN NOT NULL
);

-- DimProduct
CREATE TABLE dim_product (
    product_key SERIAL PRIMARY KEY,
    product_code VARCHAR(50),
    product_line VARCHAR(100),
    msrp NUMERIC(10,2)
);

-- DimCustomer
CREATE TABLE dim_customer (
    customer_key SERIAL PRIMARY KEY,
    customer_name VARCHAR(150),
    contact_first_name VARCHAR(100),
    contact_last_name VARCHAR(100)
);

-- DimGeography
CREATE TABLE dim_geography (
    geography_key SERIAL PRIMARY KEY,
    address_line1 VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    country VARCHAR(100),
    territory VARCHAR(50)
);

-- DimOrderAttributes (Junk Dimension)
CREATE TABLE dim_order_attributes (
    order_attr_key SERIAL PRIMARY KEY,
    status_name VARCHAR(50),
    deal_size VARCHAR(20)
);

-- =========================
-- FACT TABLE
-- =========================

CREATE TABLE fact_sales (
    sales_key SERIAL PRIMARY KEY,

    order_number INT,

    product_key INT,
    customer_key INT,
    geography_key INT,
    order_attr_key INT,
    date_key INT,

    quantity_ordered INT,
    sales NUMERIC(12,2),
    price_each NUMERIC(10,2),

    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (geography_key) REFERENCES dim_geography(geography_key),
    FOREIGN KEY (order_attr_key) REFERENCES dim_order_attributes(order_attr_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);