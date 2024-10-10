USE sql_store;

SELECT *
FROM customers
WHERE last_name LIKE '%b%' 

-- % any number of characters
-- _ single character