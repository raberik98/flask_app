-- seed.sql

-- clean up existing data
\i ./db/clean_up.sql

-- schemas and tables created
\i ./db/create/schemas.sql

-- locations added
\i ./db/create/locations.sql

-- employees added
\i ./db/create/employees.sql

-- junction table for employees and locations added
-- \i ./db/create/employee_location.sql