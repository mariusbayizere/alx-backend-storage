-- Task: Create a view named 'need_meeting' that lists all students
-- with a score below 80 and either have no recorded last meeting or

CREATE VIEW need_meeting AS SELECT name from students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
