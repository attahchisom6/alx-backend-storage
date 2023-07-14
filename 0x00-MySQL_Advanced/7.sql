DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE num_scores INT;

    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    SELECT COUNT(*) INTO num_scores
    FROM corrections
    WHERE user_id = user_id;

    IF num_scores > 0 THEN
        SET total_score = total_score / num_scores;
    END IF;

    UPDATE users
    SET average_score = total_score
    WHERE id = user_id;
END //

DELIMITER ;
