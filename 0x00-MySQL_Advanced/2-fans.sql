-- SQL File Code Aggregate the fans Based on origin
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
