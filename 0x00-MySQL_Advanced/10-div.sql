-- Task: Create a function named 'SafeDiv' that performs 
-- division and handles division by zero.
-- This function divides the first number by the second number

DELIMITER $$ ;
CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE division_result FLOAT;
    IF b = 0 THEN
        RETURN 0;
    END IF;
    SET division_result = (a * 1.0) / b;
    RETURN division_result;
END;$$
DELIMITER ;
