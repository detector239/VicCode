CREATE TABLE open_archived AS
SELECT * FROM orders
WHERE order_date < '2019-01-01'
-- NOTE: the table needs to be deleted (droped) so this code can run