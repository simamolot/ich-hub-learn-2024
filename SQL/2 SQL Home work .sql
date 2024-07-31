-- Task 2,3,4
use hr;
select 
    case 
        when salary > 10000 THEN 1 
        else 0 
    end as SALARY_GROUP
from employees;

-- Task 5,6
select
    department_id,
    avg(salary) as average_salary
from employees
where department_id IN (60, 90, 100)
group by department_id;

-- Task 6.1
select
    avg(case
            when department_id = 60 OR department_id = 90 OR department_id = 100 
            then salary 
            else null
        end) as avg_dp60_90_100
from employees;

-- Task 7
select first_name, last_name,
    case
        when salary < 10000 then 'junior'
        when salary >= 10000 and salary < 15000 then 'mid'
        else 'senior'
    end as level
from employees;

-- Task 8
select * from jobs;
select 
    job_id,
    case 
        when max(salary) > 10000 then 'high_payer'
        else 'low_payer'
    end as payer_rank
from employees
group by job_id;

-- Task 9
select
    job_id,
    if(max(salary) > 10000, 'high_payer', 'low_payer') as payer_rank
from employees
group by job_id;

-- Task 10
select
    job_id,
    if(max(salary) > 10000, 'high_payer', 'low_payer') as payer_rank,
    max(salary) AS max_salary
from employees
group by job_id
order by max_salary DESC;





 
 
 
 
 
    