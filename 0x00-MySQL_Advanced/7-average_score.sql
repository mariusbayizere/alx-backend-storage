-- Script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and stores the average score for a student.

DROP PROCEDURE IF EXISTS ComputeStudentAvgScore;
DELIMITER $$ 
CREATE PROCEDURE ComputeStudentAvgScore(
	IN student_id INT
)
BEGIN
	UPDATE users
	SET average_score = (
		SELECT AVG(score) 
		FROM corrections
		WHERE corrections.user_id = student_id
	)
	WHERE id = student_id;
END$$
DELIMITER ;
