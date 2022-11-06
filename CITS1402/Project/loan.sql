CREATE TABLE loan (
    clientId INTEGER,
    ISBN TEXT,
    copyNumber INTEGER,
    dateOut TEXT,
    dateBack TEXT,
    FOREIGN KEY(ISBN, copyNumber) REFERENCES BookCopy(ISBN, copyNumber),
    FOREIGN KEY(clientId) REFERENCES Client(clientId)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);