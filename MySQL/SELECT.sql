
SELECT DISTINCT first_name, 
	last_name, 
	points, 
    (points + 10) * 100 AS 'discount points'
FROM customers 
