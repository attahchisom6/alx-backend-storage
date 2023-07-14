-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. while noting An average score can be a decimal

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INTEGER
  )
  BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score)
      FROM corrections
      WHERE user_id=user_id);
  END $$
  DELIMITER ;
