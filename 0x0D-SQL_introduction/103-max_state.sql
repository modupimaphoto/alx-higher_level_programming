-- This script that displays the max temperature of each state
SELECT state, MAX(value) AS FROM temperatures
GROUP BY state
ORDER BY state
