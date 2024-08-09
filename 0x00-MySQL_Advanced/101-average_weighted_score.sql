-- This SQL script creates a stored procedure named 'ComputeAverageWeightedScoreForUsers'

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE total_weighted_score FLOAT DEFAULT 0;
  DECLARE total_weight INT DEFAULT 0;

  UPDATE users AS U
  JOIN (
    SELECT U.id AS user_id, SUM(C.score * P.weight) / SUM(P.weight) AS weighted_avg
    FROM users U
    JOIN corrections C ON U.id = C.user_id
    JOIN projects P ON C.project_id = P.id
    GROUP BY U.id
  ) AS AvgTable
  ON U.id = AvgTable.user_id
  SET U.average_score = AvgTable.weighted_avg;
END |
DELIMITER ;
