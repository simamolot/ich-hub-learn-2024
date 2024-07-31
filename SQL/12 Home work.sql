-- Работаем с базой world:
use world;

-- 1. Вывести количество городов для каждой страны. Результат должен содержать CountryCode, 
-- CityCount (количество городов в стране). Поменяйте запрос с использованием джойнов так, 
-- чтобы выводилось название страны вместо CountryCode. 
select 
	Co.Name,count(Ci.CountryCode) 
    over(partition by CountryCode) as City_Count
from city as Ci
inner join country as Co
on Ci.CountryCode = Co.Code;
 
 select * from country;

-- 2. Используя оконные функции, вывести список стран с продолжительностью 
-- жизнью и средней продолжительностью жизни. 
select Name, 
	LifeExpectancy, 
	round(avg(LifeExpectancy) over(),2) as avg_Life_Expectancy
from country;

-- 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.
select 
	Name, LifeExpectancy,
    dense_rank() over (order by LifeExpectancy DESC) as rank_Life_Expectancy
from country;

-- 4. Используя ранжирующие функции, вывести третью страну с самой высокой 
-- продолжительностью жизни.
select *
from
(
select 
	Name, LifeExpectancy,
    dense_rank() over (order by LifeExpectancy DESC) as rank_Life_Expectancy
from country
) as t1
where rank_Life_Expectancy = 3;


