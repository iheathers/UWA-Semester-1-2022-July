CREATE TRIGGER DaysLoanedLogger 
    AFTER UPDATE ON loan
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