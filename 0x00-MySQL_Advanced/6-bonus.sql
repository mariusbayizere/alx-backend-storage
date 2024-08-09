-- Script that creates a stored procedure AddBonus
-- that adds a new correction for a student.

DELIMITER $$ 
CREATE PROCEDURE AddBonus(
	IN student_id INTEGER,
	IN assignment_name VARCHAR(255),
	IN grade INTEGER
)
BEGIN
	IF NOT EXISTS(SELECT name FROM projects WHERE name = assignment_name) THEN
		INSERT INTO projects (name) VALUES (assignment_name);
	END IF;
	
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (student_id, (SELECT id FROM projects WHERE name = assignment_name), grade);
END$$
DELIMITER ;
