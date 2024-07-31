-- Task 1.
select * from hr.employees where job_id = "it_prog";
-- Task 2.
select * from hr.employees where job_id = "ap_vp";
-- Task 3.
select * from hr.employees where job_id = "IT_prog";
select * from hr.employees where job_id = "AP_VP";
-- Task 4.1 
select * from employees where salary between 10000 and 20000;
-- Task 4.2.
select hr.employees where department_di not in (60,30,100);
-- Task 4.3
select * from hr.employees where first_name like "%LL";
-- Task 4.4
select * from hr.employees where last_name like "%A";
-- Task 5.
select * from employees where salary >10000;
-- Task 6.
select * from employees where salary >10000 and last_name like "%L";

