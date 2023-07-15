-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE weighted_value FLOAT;
  DECLARE sum_weights INTEGER;
  DECLARE weighted_avg FLOAT;

  SELECT (score * weight) INTO weighted_value
  FROM corrections JOIN projects
  ON corrections.project_id = projects.id;

  SELECT SUM(weight) INTO sum_weights
  FROM  projects;

  IF sum_weights != 0 THEN
    SET weighted_avg = weighted_value / sum_weights;
  ELSE
    SET weighted_avg = 0;
  END IF;

  UPDATE users
  SET average = weighted_average;

END $$
DELIMITER ;
