-- 1.Подключиться к базе данных world
use world;

-- 2.Вывести население в каждой стране. Результат содержит два поля: CountryCode, 
-- sum(Population). Запрос по таблице city.
select CountryCode,sum(Population) as total_population
from city
group by CountryCode;

-- 3.Изменить запрос выше так, чтобы выводились только страны с населением более 3 млн человек.
select CountryCode,sum(Population) as population_more_then_3ml
from city
group by CountryCode
having sum(Population) > 3000000;

-- 4.Сколько всего записей в результате?
select count(*) as country_count
from (
    select CountryCode, sum(Population) as total_population
    from city
    group by CountryCode
    having sum(Population) > 3000000
) as population_count;

-- 5.Поменять запрос выше так, чтобы в результате вместо кода страны выводилось ее название. 
-- (Подсказка: нужен join таблиц city и country по полю CountryCode)
select c.Name as CountryName, sum(ci.Population) as total_population
from city ci
left join country c 
on ci.CountryCode = c.Code
group by c.Name
having sum(ci.Population) > 3000000;

-- 6.Вывести количество городов в каждой стране (CountryCode, amount of cities). 
-- (Подсказка: запрос по таблице city и группировка по CountryCode)
select CountryCode, count(*) as amount_of_cities
from city
group by CountryCode;

-- 7.Поменять запрос так, чтобы вместо кодов стран, было названия стран.
select C.Name as country_name, count(CI.id) as amount_of_cities
from city as CI
join country as C 
on CI.countrycode = C.code
group by C.Name;

-- 8.Поменять запрос так, чтобы выводилось среднее количество городов в стране. 
-- Подсказка: разделите задачу на несколько подзадач. Например, сначала вывести код 
-- страны и количество городов в каждой стране.  Затем сделать join получившегося результата 
-- с запросом, где высчитывается среднее от количества городов. Потом добавить 
-- join, который добавит имена стран, вместо кода.
 
select CountryCode, count(*) as amount_of_cities
from city
group by CountryCode; 

select floor(avg(cc.city_count)) as average_cities
from (
select CountryCode, count(Name) as city_count
from city
group by CountryCode
) as cc;