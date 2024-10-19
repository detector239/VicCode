SELECT sum(OrderTotal) FROM KCC.dbo.Orders -- this is a function <<sum()>>
WHERE OrderDate >= Dateadd(year, -3, getdate()) -- this is also a function
GROUP BY CustomerID -- the list of all the functions: https://learn.microsoft.com/en-us/sql/t-sql/functions/