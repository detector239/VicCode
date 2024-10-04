SELECT order_id, c.customer_id, first_name, last_name
FROM orders o -- the "o" is an alias for orders, thats what it means when we write it after orders
INNER JOIN customers c -- default it is INNER JOIN, even if we don't write INNER-- the "c" is also an alias 
	ON o.customer_id = c.customer_id