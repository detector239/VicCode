-- Operators >, >=, <, <=, =, (!=, <>)(both mean not equal)
SELECT *
FROM customers
WHERE birth_date > '1988-01-01' AND state != 'tx'