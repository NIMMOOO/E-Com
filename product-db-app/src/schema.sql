CREATE TABLE products (
    id INT PRIMARY KEY,
    cost DECIMAL(10,2),
    category VARCHAR(100),
    name VARCHAR(255),
    brand VARCHAR(100),
    retail_price DECIMAL(10,2),
    department VARCHAR(100),
    sku VARCHAR(100),
    distribution_center_id INT
);

INSERT INTO products (id, cost, category, name, brand, retail_price, department, sku, distribution_center_id) VALUES
(1, 19.99, 'Widgets', 'Widget A', 'Brand X', 24.99, 'Department A', 'SKU001', 1),
(2, 29.99, 'Gadgets', 'Gadget B', 'Brand Y', 34.99, 'Department B', 'SKU002', 2),
(3, 15.99, 'Thingamajigs', 'Thingamajig C', 'Brand Z', 19.99, 'Department C', 'SKU003', 3);