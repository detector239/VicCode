SELECT OrderID,
OrderDate,
OrderTotal,
CustomerName,
Phone
FROM KCC.dbo.Orders Orders -- <<Orders>> is an alias for <<KCC.dbo.Orders>>
Join KCC.dbo.Customers Customers ON Orders.CustomerID = Customers.CustomerID
-- by defoult is INNER JOIN