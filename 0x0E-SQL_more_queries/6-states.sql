-- create new database and n new table inside it with non-null unique, and auto-generated id column
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT
        PRIMARY KEY, name VARCHAR(256));
