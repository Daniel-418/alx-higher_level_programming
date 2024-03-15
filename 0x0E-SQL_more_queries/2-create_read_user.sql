-- Creates a database and a user
-- Creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates the user
CREATE USER IF NOT EXISTS
'user_0d_2'@'localhost'
IDENTIFIED BY
'user_0d_2_pwd';

-- Grant SELECT privileges to the created user
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
