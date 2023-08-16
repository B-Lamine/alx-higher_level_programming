-- display list of records with a name in descending order of scores
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score
DESC;
