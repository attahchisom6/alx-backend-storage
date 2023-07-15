-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE weighted_values FLOAT;
  DECLARE sum_weights INTEGER;
  DECLARE weighted_avg FLOAT;

  SELECT user_id, SUM(weight * score) INTO weighted_values
  FROM projects JOIN corrections
  ON projects.id = corrections.project_id
  GROUP BY user_id;

  SELECT SUM(weight) into sum_weights
  FROM projects;

  IF sum_weights != 0 THEN
    SET weighted_avg = weighted_values / sum_weights;
  ELSE
    SET weighted_avg = 0;
  END IF;

  UPDATE users
  SET average_score = weighted_avg
  WHERE users.id IN (
    SELECT user_id
    FROM corrections);
END $$
DELIMITER ;
