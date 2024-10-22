-- schemas.sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


CREATE TABLE employees (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY, -- Unique employee ID, auto-incremented
    name VARCHAR(255) NOT NULL, -- Employee name
    gender BOOLEAN NOT NULL, -- Gender (Male, Female)
    position VARCHAR(255), -- Employee's job title or position
    contract_type VARCHAR(50), -- Employment type (e.g., Full-time, Part-time, Contractor)
    email VARCHAR(255) UNIQUE NOT NULL, -- Employee email address
    phone_number VARCHAR(20), -- Employee phone number
    date_joined DATE, -- Date when the employee joined the company
    date_of_birth DATE, -- Employee's date of birth
    nationality VARCHAR(100), -- Employee's nationality
    address TEXT, -- Employee's full address
    emergency_contact_name VARCHAR(255), -- Name of the emergency contact
    emergency_contact_phone VARCHAR(20), -- Phone number of the emergency contact
    emergency_contact_relationship VARCHAR(50), -- Relationship with the emergency contact
    salary NUMERIC(12, 2), -- Employee's salary, up to 999,999,999.99
    salary_currency VARCHAR(3) DEFAULT 'EUR', -- Salary currency ISO 4217 standard
    vacation_balance INT DEFAULT 0, -- Remaining vacation days balance
    warnings INT DEFAULT 0, -- Number of warnings the employee has received
    photo TEXT, -- Employee photo will contain a link to an S3 bucker url
    permission_level SMALLINT CHECK (permission_level >= 0 AND permission_level <= 6), -- Employee permission level (0-6)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record update timestamp
    status_active BOOLEAN DEFAULT false -- The status can be active = true or inactive = false, an inactive person may be someone who's data we store but doesn't work for the company anymore
);

CREATE TABLE locations (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    zip_code VARCHAR(20) NOT NULL
);

CREATE TABLE employee_location (
    employee_id UUID REFERENCES employees(id),
    location_id UUID REFERENCES locations(id),
    PRIMARY KEY (employee_id, location_id)
);
