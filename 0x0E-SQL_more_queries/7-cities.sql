-- This script that creates the database hbtn_0d_usa and the table cities
CREATE DATABSASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT FOREIGN KEY(id) REFERENCES states(id),
name VARCHAR(256) NOT NULL
);
