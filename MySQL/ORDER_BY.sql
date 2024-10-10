SELECT first_name, last_name, state, points
FROM customers
ORDER BY points, first_name DESC 
-- defoult it is ordering alphabetically but it orders descending because of  DESC
-- it first orders by the points because we written it first