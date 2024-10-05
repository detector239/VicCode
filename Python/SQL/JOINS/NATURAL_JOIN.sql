SELECT
	o.order_id,
    c.first_name AS name,
    c.address
FROM orders o
NATURAL JOIN customers c
-- mysql will join the columns automatically that seem to him that it can be joined