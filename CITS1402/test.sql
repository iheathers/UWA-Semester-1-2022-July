CREATE TABLE BookEdition (
    ISBN TEXT PRIMARY KEY 
        CHECK (length(ISBN) == 5) 
        CHECK (ISBN regexp '^[0-9]+$')
        CHECK (
        ((3 * (SUBSTR(ISBN, 1, 1) + SUBSTR(ISBN, 3, 1)) + 7 * (SUBSTR(ISBN, 2, 1) + SUBSTR(ISBN, 4, 1))) % 10) == (ISBN % 10)
        ),
    title TEXT,
    author TEXT,
    publicationDate INTEGER,
    genre TEXT);
    

