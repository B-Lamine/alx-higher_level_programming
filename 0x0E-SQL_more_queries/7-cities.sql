-- create new table with non-null unique, and auto-generated id column
CREATE TABLE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT
        PRIMARY KEY, FOREIGN KEY(state_id) REFEERENCES states(id), name VARCHAR(256));
