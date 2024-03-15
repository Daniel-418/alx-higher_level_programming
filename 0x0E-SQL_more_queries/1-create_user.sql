-- Creates user in the current server
CREATE USER IF NOT EXISTS
'user_0d_1'@'localhost'
IDENTIFIED BY
'user_0d_1_pwd';

-- Grants privileges to the newly created user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
