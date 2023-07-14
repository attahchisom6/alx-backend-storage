-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. while noting An average score can be a decimal

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE IF NOT EXISTS ComputeAverageScoreForUser (
  IN user_id INTEGER
  )
  BEGIN
    DECLARE total FLOAT;
    DECLARE student_avg FLOAT;
    DECLARE num_scores INT;
    SELECT INTO total SUM(score)
    FROM corrections
    WHERE user_id = user_id;

    SELECT INTO num_scores COUNT(*)
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users
    SET student_avg = total / num_scores
    SELECT id, name, (average_score as student_avg)
    WHERE user_id = user_id
  END $$
  DELIMITER $$
