CREATE VIEW ReadingHistory
AS
SELECT clientId,  CAST(substr(dateOut, 1, 4) AS INTEGER) AS yr,  genre, COUNT(*) AS numLoans
    FROM BookEdition
    LEFT JOIN BookCopy USING (ISBN)
    LEFT JOIN loan USING(ISBN, copyNumber)
    LEFT JOIN Client USING(clientId)
    WHERE clientId IS NOT NULL
GROUP BY clientId, genre, yr;



