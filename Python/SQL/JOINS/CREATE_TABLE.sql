-- CREATE TABLE open_archived AS 
-- SELECT * FROM orders
-- WHERE order_date < '2019-01-01'
--  We write this code if the table doesn't exist (creatiing it)
-- NOTE: the table needs to be deleted (droped) so this code can run

INSERT INTO open_archived 
SELECT * FROM orders
WHERE order_date < '2019-01-01'