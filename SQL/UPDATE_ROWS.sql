UPDATE invoices
SET 
	payment_total = invoice_total*50/100, 
    payinvoicesment_date = due_date
WHERE client_id IN (3, 4)
-- the same as client_id=3 AND cliient_id=4
