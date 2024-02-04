-- This script that lists all the cities of California
USE hbtn_0d_usa
SELECT cities.id, cities.name FROM cities
WHERE (SELECT name FROM states WHERE cities.name == states.name)
