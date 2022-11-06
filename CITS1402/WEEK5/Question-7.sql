SELECT DISTINCT orderdetails.orderNumber FROM products 
JOIN orderdetails ON products.productCode=orderdetails.productCode
WHERE products.productLine="Planes";
