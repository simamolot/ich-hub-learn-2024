-- Подключитесь к базе данных hr (которая находится на удаленном сервере). 
use hr;

-- Выведите количество сотрудников в базе
select count(*) as Count_of_employees
from employees;

-- Выведите количество департаментов (отделов) в базе
select count(*) as Conunt_of_departments
from departments;

-- Подключитесь к базе данных World (которая находится на удаленном сервере). 
use world;

-- Выведите среднее население в городах Индии (таблица City, код Индии - IND)
select avg(population) 
from city
where CountryCode = 'IND';

-- Выведите минимальное население в индийском городе и максимальное.
select min(population) 
from city
where CountryCode = 'IND';

select max(population) 
from city
where CountryCode = 'IND';

SET SQL_SAFE_UPDATES = 0;

-- Выведите самую большую площадь территории. 
select max(SurfaceArea)
from country;

-- Выведите среднюю продолжительность жизни по странам. 
select population, avg(LifeExpectancy) 
from country
group by population;

-- Найдите самый населенный город (подсказка: использовать подзапросы)
SELECT * from city;

select 
		name, population
FROM city
where population = 
(
select 
	max(population)
    from city
    )
;

select 
	name, 
    population
from 
	city
order by population DESC
limit 1
;

