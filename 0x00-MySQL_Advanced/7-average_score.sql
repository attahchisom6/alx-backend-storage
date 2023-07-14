-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. while noting An average score can be a decimal

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INTEGER
  )
  BEGIN
    DECLARE total FLOAT;
    DECLARE student_avg FLOAT;
    DECLARE num_scores INT;

    SELECT SUM(score) INTO total
    FROM corrections
    WHERE user_id = user_id;

    SELECT COUNT(*) INTO num_scores
    FROM corrections
    WHERE user_id = user_id;

    SET student_avg = total / num_scores;

    UPDATE users
    SET average_score = student_avg
    WHERE id = user_id;
  END $$
  DELIMITER ;
