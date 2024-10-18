SELECT OrderID,
OrderDate,
OrderTotal,
CustomerName,
Phone
FROM KCC.dbo.Orders AS Orders
Join KCC.dbo.Customers AS Customers ON Orders.CustomerID = Customers.CustomerID