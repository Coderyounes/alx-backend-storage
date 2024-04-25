--- SQL File Code , Create Trigger to Track Stock
DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE current_quantity INT;

    SELECT quantity INTO current_quantity
    FROM items
    WHERE name = NEW.item_name;

    UPDATE items
    SET quantity = current_quantity - NEW.number
    WHERE name = NEW.item_name;
END//

DELIMITER ;
