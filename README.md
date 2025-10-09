# MY_SQL_PROGRAMS

## You can find different My Sql programs in this repository.

This are the programs performed by me during the learning of Core Python and anyone who is learning Python as beginner or has already learned My Sql Program can use this program for practice. If you have any questions or doubts regarding the program you can contact me:)

Thank You!!

# To Install Modul From CMD :
>python -m pip install mysql-connector-python

# My Sql Syntax
 
## DDL Statements: 
>Create database database_name; 

>Drop database database_name;

>show databases;

>show Tables;


## DDL Statements: 
>Create table table_name;

>Drop table table_name;
 
>Describe table;

>Truncate table table_name;

>Alter table table_name add column_name datatype(size);

>Alter table table_name change oldColumnName newColumnName datatype(size);

>Alter table table_name drop column column_name;

>Alter table table_name rename to newTablename;
   
## DML Statements: 
>Insert into table_name(col1, col2, … colN) values(val1, val2, …. valN);
 
>Update table_name set column_name = newValue where condition;

>Delete from table_name where condition;

>Select * from table_name;

>Select col1, col2 from table_name;
    
## Aggregate Functions: 
>Select sum(colName) from table_name;

>Select max(colName) from table_name;

>Select min(colName) from table_name;

>Select avg(colName) from table_name;
 
>Select count(colName) from table_name;
   
## Joins: 
>Select table1.col1, table2.col2 from table1 left join table2 on table1.colX=table2.colX;
 
>Select table1.col1, table2.col2 from table1 right join table2 on table1.colX=table2.colX;

>Select table1.col1, table2.col2 from table1 inner join table2 on table1.colX=table2.colX;




## SQL Syntax Reference


>SHOW DATABASES;

>USE database_name;

>SHOW TABLES;

>CREATE TABLE table_name (col1 DATATYPE(size), col2 DATATYPE(size), ...);

>SELECT * FROM table_name;

>INSERT INTO table_name VALUES (val1, val2, ...);

>SELECT col FROM table_name;

>SELECT col1, col2, ... FROM table_name;

>SELECT * FROM table_name WHERE condition;
  Example condition: col OPERATOR value (e.g., age > 30)

>SELECT * FROM table_name ORDER BY col ASC;

>SELECT * FROM table_name ORDER BY col;

>SELECT * FROM table_name ORDER BY col DESC;

>SELECT * FROM table_name ORDER BY col1, col2;

>SELECT * FROM table_name WHERE col LIKE 'prefix%';

>SELECT * FROM table_name WHERE col LIKE '%suffix';

>SELECT * FROM table_name WHERE col LIKE '%substring%';

>DESC table_name;

>DROP TABLE table_name;

>DROP DATABASE database_name;

>ALTER TABLE table_name ADD col DATATYPE(size);

>UPDATE table_name SET col = value WHERE condition;

>ALTER TABLE table_name DROP COLUMN col;

>ALTER TABLE table_name RENAME COLUMN old_col TO new_col;

>ALTER TABLE table_name MODIFY COLUMN col DATATYPE(size);

>SELECT * FROM table_name WHERE condition1 AND condition2;

>SELECT * FROM table_name WHERE condition1 OR condition2;

>SELECT * FROM table_name WHERE NOT condition;


>DELETE FROM tbl_name WHERE condition;


>DELETE FROM tbl_name;


>SELECT MAX(col) FROM tbl_name;


>SELECT MIN(col) FROM tbl_name;

 
>SELECT COUNT(col) FROM tbl_name;


>SELECT AVG(col) FROM tbl_name;


>SELECT SUM(col) FROM tbl_name;


>INSERT INTO tbl_name (col1, col2, ...) VALUES (val1, val2, ...);


>SELECT AGG_FUN(col) AS alias_col FROM tbl_name;


>SELECT AGG_FUN(col) FROM tbl_name WHERE condition;

>SELECT * FROM tbl_name WHERE col BETWEEN val1 AND val2;


>SELECT * FROM tbl_name WHERE col NOT BETWEEN val1 AND val2;

>SELECT * FROM tbl_name WHERE col NOT BETWEEN val1 AND val2;

>ALTER TABLE tbl name MODIFY COLUMN col coldt (size) NOT NULL;

>ALTER TABLE tbl name MODIFY COLUMN col colDT (Size) DEFAULT val;

>ALTER TABLE tbl name MODIFY COLUMN col colDT (size) UNIQUE;

>ALTER TABLE tbl name MODIFY COLUMN col colDT (size) PRIMARY KEY;

>CREATE TABLE tbl name(col colDT(s) UNIQUE);

>CREATE TABLE tbl name(col colDT(s) NOT NULL);

>CREATE TABLE tbl_name(col colDT(s) DEFAULT val);

>CREATE TABLE tbl_name(col colDT(s) PRIMARY KEY);

>DATE:-"YYYY-MM-DD"

>DATETIME:-"YYYY-MM-DD hh:mm:ss"

>SELECT tbll.coli, tbli.col2,...tbl2.coll, tbl2.co12,... FROM tb11 INNER JOIN tb12 ON tbli.col tbl2.col; 58) SELECT tbli.coll, tbll.col2....tbl2.coll, tbl2.col2,... FROM tb11 LEFT JOIN tb12 ON tbll.col = tbl2.col;

>SELECT tbl1.coll, tbl1.col2,...tbl2.coll, tbl2.col2,... FROM tb11 RIGHT JOIN tb12 ON tbli.col tbl2.col;

>SELECT tbll.coll, tbl1.col2....tbl2.coll, tbl2.col2.... FROM tb11 LEFT JOIN tb12 ON tbli.coltbl2.col UNION SELECT tbli.coll, tbll.col2,...tbl2.coll,

>tb12.col2,... FROM tb11 RIGHT JOIN tb12 ON tbll.col= tbl2.col;


>CREATE TABLE parent tbl(coll colDT(size) PRIMARY KEY, col colDT(size), ....);

>CREATE TABLE child tbl (coli colDT UNIQUE, col colDT (size),..., FOREIGN KEY(col1) REFERENCES parent_tbl(coll) ON DELETE CASCADE ON UPDATE CASCADE);

>CREATE TABLE parent tbl(coli colDT(size) PRIMARY KEY, col colDT(size), ....);

>CREATE TABLE child tbl (coll colDT, col colDT (size),...., FOREIGN KEY(col1) REFERENCES parent_tbl(coll) ON DELETE CASCADE ON UPDATE CASCADE);

>CREATE TABLE parent tbl(coll colDT(size) PRIMARY KEY, col colDT(size), ....);

>CREATE TABLE child_tbl (col2 colDT (size) PRIMARY KEY, col colDT(size), ....);

>CREATE TABLE junction_tbl (coll colDT(size), col2 colDT(size), FOREIGN KEY (coll) REFERENCES parent_tbl(coll),FOREIGN KEY(co12) REFERENCES child_tbl(col2),

### Ramakant Chaudhari
