DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'employee_location') THEN
        DROP TABLE employee_location;
    END IF;

    IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'employees') THEN
        DROP TABLE employees;
    END IF;
    
    IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'locations') THEN
        DROP TABLE locations;
    END IF;
END $$;