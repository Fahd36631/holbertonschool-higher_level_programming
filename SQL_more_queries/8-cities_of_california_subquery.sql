--  that lists all the cities of California that can be found --
SELECT cities.id, cities.name FROM cities , states
WHERE cities.id = states.id
ORDER BY cities.id ASC;