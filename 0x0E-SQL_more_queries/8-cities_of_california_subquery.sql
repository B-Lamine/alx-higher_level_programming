-- list all cities of California that can be found in the given database
SELECT * FROM cities WHERE state_id=(SELECT id FROM states WHERE name='California') ORDER BY id ASC;
