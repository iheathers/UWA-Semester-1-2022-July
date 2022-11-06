SELECT products.productName AS "product name", orderdetails.quantityOrdered AS quantity, (orderdetails.quantityOrdered * orderdetails.priceEach) AS "total price" FROM orderdetails
JOIN products ON products.productCode = orderdetails.productCode
WHERE orderdetails.orderNumber=10100;