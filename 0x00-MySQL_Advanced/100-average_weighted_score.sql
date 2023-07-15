-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
  IN user_id INTEGER
)
BEGIN
  DECLARE weighted_value FLOAT;
  DECLARE sum_weight INTEGER;
  DECLARE weighted_avg FLOAT;

  SELECT SUM(weight * score) INTO weighted_value
  FROM projects JOIN corrections
  ON projects.id = corrections.project_id
  WHERE corrections.user_id = user_id;

  SELECT SUM(weight) INTO sum_weight
  FROM projects;

  IF sum_weight != 0 THEN
    SET weighted_avg = weighted_value / sum_weight;
  ELSE
    SET weighted_avg = 0;
  END IF;

  UPDATE users
  SET average_score = weighted_avg
  WHERE id = user_id;
END $$
DELIMITER ;
