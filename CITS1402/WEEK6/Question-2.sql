SELECT city AS name, COUNT(*)AS "number of employees"
FROM offices JOIN employees USING(officeCode)
GROUP BY officeCode;