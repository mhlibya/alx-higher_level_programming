-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates a user
CREATE  USER IF NOT EXISTS hbtn_0d_2@localhost IDENTIFIES BY 'hbtn_0d_2pwd';
-- Grants select previlege for the user
GRANT SELECT ON hbtn_0d_2. * TO hbtn_0d_2@localhost;
