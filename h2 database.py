create database h2;
use h2;

create table student(id int primary key auto_increment,name varchar(25) not null,marks int);
desc student;
insert into student values('0','Shivam',80),('0','Amit',75),('0','Sneha',90),('0','Rahul',60),('0','Pooja',85);
select * from student;

select sum(marks) from student;
select avg(marks) from student;
select count(marks) from student;
select min(marks) from student;
select max(marks) from student;

select count(id) from student where marks>70;
