-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. while noting An average score can be a decimal

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INTEGER
  )
  BEGIN
    DECLARE total FLOAT;
    DECLARE student_avg FLOAT;
    DECLARE num_scores FLOAT;

    SELECT SUM(score) INTO total
    FROM corrections
    WHERE corrections.user_id = user_id;

    SELECT COUNT(*) INTO num_scores
    FROM corrections
    WHERE corrections.user_id = user_id;

    IF num_scores > 0 THEN
      SET student_avg = total / num_scores;
    ELSE
      SET student_avg = 0
    END IF;

    UPDATE users
    SET average_score = student_avg
    WHERE id = user_id;
END $$
DELIMITER ;
