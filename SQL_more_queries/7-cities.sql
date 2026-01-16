-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) --
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT UNIQUE AUTO_INCREMENT NOT null PRIMARY KEY,
    state_id INT NOT null, 
    FOREIGN KEY(state_id) REFERENCES states (id),
    name VARCHAR(256) NOT null
);