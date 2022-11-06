SELECT orderNumber AS "order number", ROUND(SUM(quantityOrdered * (priceEach - buyPrice)), 2) AS "net profit"
FROM orderdetails JOIN products ON orderdetails.productCode = products.productCode
GROUP BY orderNumber;