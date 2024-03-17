-- Creates a database and a table
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selece the database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
