create database school;
use school;
create table students(
	id int primary key auto_increment,
    name varchar(50),
    age int,
    grade varchar(10)
);
insert into students(name,age,grade) 
values ('alice',14,'A');
insert into students(name,age,grade) 
values ('bob',15,'A');
insert into students(name,age,grade) 
values ('charlie',14,'A');

insert into students(name,age,grade) 
values ('Nishu',14,'B'), ('Akshu',15,'B');
select * from students;
select name,grade from students where grade = 'B';
select name,grade from students where grade = 'A';
select id,name,grade from students;

set sql_safe_updates = 0;
update students set grade = 'A+' where name = 'Bob';
select * from students;
delete from students where name ='charlie';
drop table students;
drop database school;
create  database movie_db;
use movie_db;

CREATE TABLE movies ( 
movie_id INT PRIMARY KEY AUTO_INCREMENT, 
title VARCHAR(100), 
director VARCHAR(100), 
release_year INT, 
genre VARCHAR(50)
 );

drop table movies;

CREATE TABLE movies ( movie_id INT PRIMARY KEY AUTO_INCREMENT,
 title VARCHAR(100), 
 director VARCHAR(100), 
 release_year YEAR, 
 genre VARCHAR(50) 
 );

insert into movies (title, director, release_year, genre)
values
('3 Idiots', 'Rajkumar Hirani', 2009, 'Comedy/Drama'),
('Devdas', 'Sanjay Leela Bhansali', 2002, 'Romance/Drama'),
('Kabhi Khushi Kabhie Gham', 'Karan Johar', 2001, 'Family/Drama'),
('Nayakan', 'Mani Ratnam', 1987, 'Crime/Drama'),
('12th Fail', 'Vidhu Vinod Chopra', 2023, 'Drama');

select * from movies;
select title,genre from movies;
select title,genre from movies where director= 'Mani Ratnam';
select * from movies where release_year >= 2009;

create table departments(
	dept_id int primary key,
    dept_name varchar(50)
);

insert into departments values (101,'IT');
insert into departments values (102,'HR');
insert into departments values (103,'Finance');




create table employees (
	emp_id int primary key,
    emp_name varchar(50),
    salary int,
    dept_id int,
    foreign key (dept_id) references 
    departments(dept_id)
);


insert into employees values (1, 'Raj', 50000, 
101);

insert into employees values (2, 'Simran', 55000, 
102);

insert into employees values (3, 'Karan', 60000, 
101);


create database collage_db;
use collage_db;

create table departments(
	dept_id int primary key,
    dept_name varchar(50)
);

insert into departments values (101,'IT');
insert into departments values (102,'HR');
insert into departments values (103,'Finance');

create table employees (
	emp_id int primary key,
    emp_name varchar(50),
    salary int,
    dept_id int,
    foreign key (dept_id) references 
    departments(dept_id)
);
insert into employees values (1, 'Raj', 50000, 
101);

insert into employees values (2, 'Simran', 55000, 
102);

insert into employees values (3, 'Karan', 60000, 
101);
select * from employees;

Inner joint
select employees.emp_name, departments.dept_name
from employees
inner join departments
on employees.dept_id = departments.dept_id;


insert into employees values (4, 'Pooja', 45000, 
Null);
left join

select employees.emp_name, departments.dept_name
from employees
left join departments
on employees.dept_id = departments.dept_id;

select employees.emp_name, departments.dept_name
from employees
right join departments
on employees.dept_id = departments.dept_id;

select employees.emp_name, departments.dept_name
from employees
left join departments
on employees.dept_id = departments.dept_id
union
select employees.emp_name, departments.dept_name
from employees
right join departments
on employees.dept_id = departments.dept_id;

Built-in function
Aggregate functions :
count 
select count(*) from employees;
sum 
select sum(salary) from employees;
avg
select avg(salary) from employees;

max min
select min(salary) from employees;

group by 

select dept_id, avg(salary)
from employees
group by dept_id;

having 
select dept_id, avg(salary) as avg_salary
from employees
group by dept_id
having avg(salary) > 45000


distinct 
select distinct city from student;

Normalization

create database normamalization_demo;
use normamalization_demo;

create table student_course(
student_id int,
student_name varchar(50),
course_id int, 
course_name varchar(50),
instructor_name varchar(50),
instructor_phone varchar(50)
);

insert into student_course values
(1, 'Amit', 101, 'SQL', 'Rahul', '9999988888'),
(1, 'Amit', 102, 'Python', 'Neha', '9999966666'),
(2, 'Priya', 101, 'SQL', 'Rahul', '9999988888'),
(3, 'Rohit', 101, 'SQL', 'Rahul', '9999988888');

select * from student_course;

create table students (
	student_id int primary key,
    student_name varchar(50)
);
insert into students values
(1, 'Amit'),
(2, 'Priya'),
(3, 'Rohit');




create table courses (
	course_id int primary key,
    course_name varchar(50),
    instructor_name varchar (50),
    instructor_phone varchar (15)
);
insert into courses values
(101, 'SQL', 'Rahul', '9999988888'),
(102, 'Python', 'Neha', '9999966666');

create table enrollment (
	student_id int,
    course_id int,
    primary key (student_id, course_id),
    foreign key (student_id) references 
    students(student_id),
    foreign key (course_id) references 
    courses(course_id)
    );
    insert into enrollment values
    (1,101),
    (1,102),
    (2,101),
    (3,101);
select * from enrollment;
select * from courses;
select * from students;

create table instructors(
    instructor_id int primary key,
    instructor_name varchar(50),
    instructor_phone varchar(15)
    );
insert into instructors values
(1, 'Rahul', '9999988888'),
(2, 'Neha', '9999966666');

select * from instructors;

create table courses_3nf(
	course_id int primary key,
    course_name varchar(50),
    instructor_id int,
    foreign key (instructor_id) references instructors(instructor_id )    
);
insert into courses_3nf values 
(101,'SQL',1),
(102,'python',2);




create database CompanyDB;
use companydb;

create table employees (
	emp_id int auto_increment primary key,
    name varchar(100),
    department varchar(50),
    salary decimal(10,2)
);

insert into employees (name,department,salary) values
('Alice','HR',50000),
('Bob','IT',70000),
('Charlie','Finance',65000),
('David','IT',55000),
('Eva','HR',40000);

find employees eaerning more than the average salary

select avg(salary)
from employees;


select name, salary
from employees
where salary > 56000.00; 


-- SELECT name, salary
-- FROM employees
-- GROUP BY name, salary
-- HAVING salary > (SELECT AVG(salary) FROM employees);



combined: 
select name, salary
from employees
where salary > ( 
	select avg(salary)
    from employees
)

Main Types of Subqueries
1.Single-row subquery

SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

2.multi-row subquery
select name
from employees 
where salary >( select avg(salary) 
                 from employees);
                 
SELECT name, department
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    WHERE salary > 60000
);

SELECT name, salary
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department = 'HR'
);



DELIMITER $$
CREATE PROCEDURE GetHREmployees()
BEGIN
    SELECT * FROM Employees WHERE department = 'HR';
END $$
DELIMITER ;

call GetHREmployees();


DELIMITER $$
CREATE PROCEDURE GetDeptEmployees(IN dept_name varchar(50))
BEGIN
    SELECT * FROM Employees WHERE department = dept_name;
END $$
DELIMITER ;
call GetDeptEmployees('Finance');



create table bankaccounts(
	acc_id int primary key,
    name varchar(50),
    balance decimal(10,2)
);

insert into bankaccounts values
(1, 'John',1000),
(2, 'Mike', 500);

start transaction;
update bankaccounts
set balance = balance-200
where acc_id = 1;

update bankaccounts
set balance = balance + 200
where acc_id = 2;
commit;

select * from bankaccounts;

start transaction;
update bankaccounts
set balance = balance-100
where acc_id = 1;

update bankaccounts
set balance = balance + 100
where acc_id = 2;
rollback;

select * from bankaccounts;



Mysql view 

create view HighSalaryEmployees AS
select name, department, salary
from employees
where salary > 60000;

select * from HighSalaryEmployees;

--update
create or replace view HighSalaryEmployees AS
select name, department, salary
from employees
where salary > 55000;
select * from HighSalaryEmployees;
drop view HighSalaryEmployees;


create database shopdb;
use shopdb;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    city VARCHAR(100)
);

INSERT INTO customers (name, city) VALUES
('Alice','Mumbai'),
('Bob','Delhi'),
('Charlie','Mumbai'),
('David','Pune'),
('Eva','Delhi');


CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    total_amount DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders (customer_id,total_amount,order_date) VALUES
(1,1500,'2024-01-02'),
(2,300,'2024-01-05'),
(1,700,'2024-02-01'),
(3,1200,'2024-02-10'),
(2,450,'2024-03-02');
display customer name who placed more orders
select customers.name, orders.order_id, orders.total_amount
from customers
join orders on customers.customer_id = orders.customer_id
where orders.total_amount = (
    select max(total_amount)
    from orders
);

display customer name who placed more orders
from customers
where customer_id = (
	select customer_id
    from orders
    where total_amount = (
		select max(total_amount)
        from orders
    )
);
display customer name who placed no orders

select name
from customers
where customer_id not in (
    select customer_id
    from orders 
);
display customer name who placed atleast one order

select name
from customers
where customer_id in (
    select customer_id
    from orders 
);




