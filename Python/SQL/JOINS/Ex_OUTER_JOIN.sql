SELECT 
	c.customer_id,
    c.first_name,
    o.order_id,
    o.shipper_id AS o_sh_id,
    sh.shipper_id AS sh_sh_id,
    sh.name AS shipper
FROM customers c
LEFT JOIN orders o
	ON c.customer_id = o.customer_id
LEFT JOIN shippers sh
	ON o.shipper_id = sh.shipper_id
ORDER BY c.customer_id