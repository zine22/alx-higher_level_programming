-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE states.id = cities.state_id
ORDER BY cities.id;
