-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student

CREATE OR REPLACE PROCEDURE ComputeAverageWeightedScoreForUser (
  user_id INTEGER
)
BEGIN
  DECLARE data INTEGER;
  DECLARE weights INTEGER;
  DECLARE weigted_value INTEGER;
  DECLARE sum_weight INTEGER;
  DECLARE weighted_avg INTEGER;

  SELECT score INTO data
  FROM corrections
  WHERE user_id = user_id;

  SELECT weight INTO weights
  FROM projects
  where id = user_id;

  SELECT SUM(weight) into sum_weight
  FROM projects
  WHERE id = user_id;

  SET weighted_value = data * weights
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
