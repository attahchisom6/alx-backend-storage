-- script that creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus (
	IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER
)
BEGIN
  -- check if the given project_name exist in the projects table
DECLARE project_id INTEGER;
SELECT id INTO project_id FROM projects WHERE name=project_name;

-- if the given project_name does not match any name in projects table name field
IF project_id IS NULL THEN
  INSERT INTO projects (name) VALUES (project_name);
  SET project_id = LAST_INSERT_ID();
END IF;
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id, project_id, score);
END $$
DELIMITER ;
