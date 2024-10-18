SELECT OrderID,
OrderDate,
OrderTotal,
CustomerName,
Customers.CustomerID,
Phone
FROM KCC.dbo.Orders Orders -- <<Orders>> is an alias for <<KCC.dbo.Orders>>
Join KCC.dbo.Customers Customers ON Orders.CustomerID = Customers.CustomerID
ORDER BY Orders.CustomerID
-- by defoult is INNER JOIN