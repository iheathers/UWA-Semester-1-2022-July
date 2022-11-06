SELECT productLine AS "product line", buyPrice AS "price paid" 
FROM products
GROUP BY productLine
HAVING MAX(buyPrice);