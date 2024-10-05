SELECT 
	sh.shipper_id,
    sh.name,
    p.product_id
FROM products p
CROSS JOIN shippers sh
ORDER BY sh.shipper_id