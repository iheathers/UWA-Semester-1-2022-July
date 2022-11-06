SELECT orderNumber AS "order number", 
productLine AS "product line", 
COUNT(productLine) AS number, 
ROUND(SUM(quantityOrdered * priceEach), 2) AS "total cost"
FROM orderdetails 
JOIN products ON (orderdetails.productCode = products.productCode)
GROUP BY orderNumber, productLine;
