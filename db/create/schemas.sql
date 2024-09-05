-- schemas.sql

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER,
    role VARCHAR(255)
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    zip_code VARCHAR(20) NOT NULL
);

CREATE TABLE employee_location (
    employee_id INT REFERENCES employees(id),
    location_id INT REFERENCES locations(id),
    PRIMARY KEY (employee_id, location_id)
);