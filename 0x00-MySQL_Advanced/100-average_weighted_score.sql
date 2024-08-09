-- This SQL script creates a stored procedure named 'ComputeAverageWeightedScoreForUser.
-- It computes the average weighted score for a user by summing up the product of scores 
-- and weights of the user from the 'corrections' table, summing up the total weight, 
-- and then dividing the total weighted score by the total weight, and then updating 

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN input_user_id INT)
BEGIN
    DECLARE computed_total_weighted_score FLOAT DEFAULT 0;
    DECLARE computed_total_weight INT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight)
        INTO computed_total_weighted_score
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = input_user_id;

    SELECT SUM(projects.weight)
        INTO computed_total_weight
        FROM corrections
            INNER JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = input_user_id;

    IF computed_total_weight = 0 THEN
        UPDATE users
            SET users.average_score = 0
            WHERE users.id = input_user_id;
    ELSE
        UPDATE users
            SET users.average_score = computed_total_weighted_score / computed_total_weight
            WHERE users.id = input_user_id;
    END IF;
END $$
DELIMITER ;
