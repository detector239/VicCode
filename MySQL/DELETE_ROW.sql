DELETE FROM invoices
WHERE clint_id = (
			SELECT *
            FROM clients
            WHERE NAME = 'Myworks'
)