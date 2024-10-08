-- Script that creates a trigger to decrease the quantity of an item
-- after adding a new order.

DROP TRIGGER IF EXISTS decrease_quantity_after_order;

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the item in the items table
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
