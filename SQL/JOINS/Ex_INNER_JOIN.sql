SELECT order_id, oi.product_id, quantity, oi.unit_price
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id