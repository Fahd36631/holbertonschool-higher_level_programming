-- creates a table second_table AND create these records --
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
insert INTO second_table(id,name,score)values(1,"John",10);
insert INTO second_table(id,name,score)values(2,"Alex",3);
insert INTO second_table(id,name,score)values(3,"Bob",14);
insert INTO second_table(id,name,score)values(4,"George",8);