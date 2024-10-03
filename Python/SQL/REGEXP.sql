USE sql_store;

SELECT *
FROM customers
WHERE last_name REGEXP '%b%'