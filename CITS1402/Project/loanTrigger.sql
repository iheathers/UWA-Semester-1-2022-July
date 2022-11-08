CREATE TRIGGER DaysLoanedLogger 
    AFTER UPDATE
    ON loan
    FOR EACH ROW
        WHEN OLD.dateBack IS NULL
BEGIN
    UPDATE BookCopy 
    SET daysLoaned =( 
        COALESCE(daysLoaned, 0) + 
        julianday(NEW.dateBack) - 
        julianday(NEW.dateOut) +
        1
    ) 
    WHERE 
    (ISBN == OLD.ISBN AND copyNumber == OLD.copyNumber);
END;


CREATE TABLE gives (
    donorId INTEGER,
    charityName TEXT,
    amount INTEGER,
    date TEXT
    PRIMARY KEY (   
        donorId,
        charityName
    )
    FOREIGN KEY(donorId) REFERENCES Donor(donorId),
    FOREIGN KEY(charityName) REFERENCES Charity(CharityName),
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

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