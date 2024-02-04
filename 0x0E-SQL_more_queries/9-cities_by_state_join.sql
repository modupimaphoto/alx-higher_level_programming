-- This script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.state_id
ORDER BY cities.id
