-- main.sql

-- clean up existing data
\i ./clean_up.sql

-- schemas and tables created
\i ./create/schemas.sql

-- locations added
\i ./create/locations.sql

-- employees added
\i ./create/employees.sql

-- junction table for employees and locations added
\i ./create/employee_location.sql