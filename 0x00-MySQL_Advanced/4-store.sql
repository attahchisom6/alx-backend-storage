-- script that creates a trigger that decreases the quantity of an item after adding a new order.

DELIMITER $$
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
-- for each row in the items table, update  the quantity atrribute to quanity - order where order is a number inserted newly into the orders table
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
	END
DELIMITER ;
