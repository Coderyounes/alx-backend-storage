--- SQL File Code , Create Trigger to Track Stock
CREATE TRIGGER IF NOT EXISTS  quantityTrack 
AFTER
INSERT
ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
