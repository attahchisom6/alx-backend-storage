-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student

XELIMITER $$
CREATE OR REPLACE PROCEDURE ComputeAverageWeightedScoreForUser (
  user_id INTEGER
)
BEGIN
  DECLARE weights INTEGER;
  DECLARE weigted_value FLOAT;
  DECLARE sum_weight INTEGER;
  DECLARE weighted_avg FLOAT;

  SELECT SUM(weight * score) INTO weighted_value
  FROM projects JOIN corrections
  ON project.id = project_id
  WHERE user.id = user_id;

  SELECT SUM(weight) into sum_weight
  FROM projects

  IF sum_weights != 0 THEN
    SET weighted_avg = weighted_value / sum_weight;
  ELSE
    SET weighted_avg = 0;
  END IF;

  UPDATE users
  SET average_score = weighted_avg
  WHERE id = user_id;
END $$
DELIMITER ;
