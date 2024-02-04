-- This script that lists all the cities of California
SELECT cities.id, cities.name FROM cities
WHERE (SELECT name FROM states WHERE name = "California ")
