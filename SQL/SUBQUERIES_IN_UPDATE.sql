UPDATE invoices
SET 
	payment_total = invoice_total*50/100, 
    payment_date = due_date
WHERE client_id IN
			(SELECT client_id
			FROM clients
			WHERE state IN ('CA', 'NY'))