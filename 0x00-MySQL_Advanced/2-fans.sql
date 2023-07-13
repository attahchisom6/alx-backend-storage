-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) as nb_fans GROUP BY origin ORDER by nb_fans DESC;