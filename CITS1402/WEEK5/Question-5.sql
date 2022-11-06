SELECT customerNumber FROM customers 
EXCEPT
SELECT customerNumber FROM orders;