-- SQL Code Update email
DELIMITER //

CREATE TRIGGER reset_valid_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        IF NEW.valid_email = 1 THEN
            SET NEW.valid_email = 0;
        END IF;
    END IF;
END;
//

DELIMITER ;