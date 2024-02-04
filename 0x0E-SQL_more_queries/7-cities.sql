-- This script that creates the database hbtn_0d_usa and the table cities
CREATE DATABSASE IF NOT EXISTS hbtn_0d_usa
CREATE TABLE IF NOT EXISTS cities(
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT FOREIGN KEY(id) REFERENCES states(id),
name VARCHAR(256) NOT NULL
)
