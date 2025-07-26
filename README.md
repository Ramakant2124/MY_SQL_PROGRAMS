# MY_SQL_PROGRAMS

## You can find different My Sql programs in this repository.

This are the programs performed by me during the learning of Core Python and anyone who is learning Python as beginner or has already learned My Sql Program can use this program for practice. If you have any questions or doubts regarding the program you can contact me:)

Thank You!!

 # My Sql Syntax
 
## DDL Statements: 
< 1. Create database database_name; 

< 2. Drop database database_name;

## DDL Statements: 
1. Create table table_name; 
2. Drop table table_name; 
3. Describe table; 
4. Truncate table table_name; 
5. Alter table table_name add column_name datatype(size); 
6. Alter table table_name change oldColumnName newColumnName datatype(size); 
7. Alter table table_name drop column column_name; 
8. Alter table table_name rename to newTablename;
   
## DML Statements: 
1. Insert into table_name(col1, col2, … colN) values(val1, val2, 
…. valN); 
2. Update table_name set column_name = newValue where 
condition; 
3. Delete from table_name where condition; 
4. Select * from table_name; 
5. Select col1, col2 from table_name;
    
## Aggregate Functions: 
1. Select sum(colName) from table_name; 
2. Select max(colName) from table_name; 
3. Select min(colName) from table_name; 
4. Select avg(colName) from table_name; 
5. Select count(colName) from table_name;
   
## Joins: 
1. Select table1.col1, table2.col2 from table1 left join table2 on table1.colX=table2.colX; 
2. Select table1.col1, table2.col2 from table1 right join table2 on table1.colX=table2.colX; 
3. Select table1.col1, table2.col2 from table1 inner join table2 on table1.colX=table2.colX; 
