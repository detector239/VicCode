SELECT *
FROM customers c
LEFT JOIN orders o 
-- the LEFT JOIN means that it will create a line for c.customer_id even though it has no value for 
-- o.customer_id so we will see all the customers and see if they have no orders or one or more orders orders
-- But the RIGHT JOIN does the same thing but for o.customer_id because we written it after c.customer_id
	ON c.customer_id = o.customer_id
ORDER BY c.customer_id