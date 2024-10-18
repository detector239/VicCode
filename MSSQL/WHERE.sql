SELECT DISTINCT top(3) * 
FROM KCC.dbo.Customers
WHERE State NOT IN('WA', 'NY', 'UT') -- the same as <<State = 'WA' OR State = 'NY' OR State = 'UT'>>
