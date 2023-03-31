Select Customers.name as Customers
From Customers
where Customers.id not in (select customerId from Orders)