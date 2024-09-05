CREATE TABLE employees (
    id SERIAL PRIMARY KEY, -- Unique employee ID, auto-incremented
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
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);
