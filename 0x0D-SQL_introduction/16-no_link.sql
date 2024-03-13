-- a script that lists all records of the table "second_table" of the database "hbtn_0c_0" in your MySQL server.
-- Results should display the score and the name
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
