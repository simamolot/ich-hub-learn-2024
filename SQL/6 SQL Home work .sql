-- 1. Подключитесь к базе данных world
use world;

-- 2. Выведите список стран с языками, на которых в них говорят. 
select c.name as Country, cl.language
from country as c
join countrylanguage as cl 
on c.Code = cl.CountryCode;

-- 3. Выведите список городов с их населением и названием стран
select ci.name as City, ci.Population, co.name as Country
from city as ci
join country as co 
on ci.CountryCode = co.code;

-- 4. Выведите список городов в South Africa
select ci.name as City
from city as ci
join country as co 
on ci.CountryCode = co.Code
where co.name = 'South Africa';

select ci.name as city
from city as ci
join country as co 
on ci.countrycode = co.code
and co.name = 'South Africa';

-- 5. Выведите список стран с названиями столиц. Подсказка: 
-- в таблице country есть поле Capital, которое содержит номер города из таблицы City. 
select co.name as Country, ci.name as Capital
from country as co
join city as ci 
on co.Capital = ci.id;

-- 6. Измените запрос 4 таким образом, чтобы выводилось население в столице. 
select co.name as Country, ci.name as Capital, ci.Population as CapitalPopulation
from country as co
join city as ci 
on co.Capital = ci.id;

-- 7. Напишите запрос, который возвращает название столицы United States
select ci.name as Capital
from country as co
join city as ci 
on co.Capital = ci.id
where co.name = 'United States';

-- 8. Используя базу hr_data.sql, вывести имя, фамилию и город сотрудника.
select e.first_name, e.last_name, l.city
from hr.employees as e
join hr.departments as d 
on e.department_id = d.department_id
join hr.locations as l 
on d.location_id = l.location_id;

-- 9.  Используя базу hr_data.sql, вывести города и соответствующие городам страны.
select l.city, c.country_name
from hr.locations as l
join hr.countries as c 
on l.country_id = c.country_id;







