SELECT * 
FROM order_items oi
JOIN order_item_notes oin
-- 	ON oi.product_id AND oin.product_id 
-- the code above does the same thing as the code below
-- we can use the clause USING only when the tables that we want to join have the same name
	USING (product_id) 