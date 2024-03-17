-- Creates a database and a table
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    state_id INTEGER NOT NULL,
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL
);
