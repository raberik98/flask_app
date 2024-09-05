-- SELECT name FROM employees WHERE  role LIKE '%Manager%' AND age > 40;

-- SELECT 
--     e.name AS employee_name,
--     e.role AS employee_role,
--     l.city AS city_name
-- FROM 
--     employees e
-- JOIN
--     employee_location el ON e.id = el.employee_id 
-- JOIN
--     locations l ON el.location_id = l.id
-- WHERE e.role LIKE '%Engineer%' OR ( e.role LIKE '%Manager%' AND l.city LIKE 'Boston')   
;