SELECT *
FROM customers c
CROSS JOIN orders o
-- "CROSS JOIN" will combine every culomn from one tabale with every column from the other table
-- it can be written like this in the FROM clause too, "FROM customers c, orders o" without
-- specifing a CROSS JOIN
ORDER BY c.first_name