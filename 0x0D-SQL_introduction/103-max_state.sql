-- This script that displays the max temperature of each state
USE hbtn_0c_0
SELECT state, MAX(value) AS FROM temperatures
GROUP BY state
ORDER BY state
