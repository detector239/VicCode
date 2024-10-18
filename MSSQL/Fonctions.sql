SELECT count(*) FROM KCC.dbo.Orders -- this is a function <<count()>>(it will return nnothing because the current date is way in the future and there is no orders from this time)
WHERE OrderDate >= Dateadd(month, -1, getdate()) -- this is also a function
-- for all the functions: https://learn.microsoft.com/en-us/sql/t-sql/functions/