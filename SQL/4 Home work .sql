use 310524ptm_serafima;
-- 1.Вывести все заказы, отсортированные по убыванию по стоимости
select * from Orders 
order by price DESC;

-- 2.Вывести всех заказчиков, у которых почта зарегистриварована на gmail.com
select Customer_id, first_name, last_name
from Customers
where e_mail like '%@gmail.com';

-- 3.Вывести заказы, добавив дополнительный вычисляемый столбец status, 
-- который вычисляется по стоимости заказа и имеет три значения: low, middle, high. 
select *, 
case when price < 60 then 'Low'
when price between 60 and 90 then 'Mid'
else 'High' 
 end as Status 
 from Orders ;
 
 -- 4.Pейтинг
 alter table Customers 
 add column rating integer default 0;
 
-- 4.Вывести заказчиков по убыванию рейтинга. 
select * from Customers
order by rating DESC;  
 
 -- 5.Вывести всех заказчиков из города на ваш выбор. 
select * from Customers
where city like "Dnipro";

-- Запрос, который вернет самый часто продаваемый товар:
select item_id, count(item_id) as count 
from Orders 
group by item_id 
order by count DESC 
limit 1;

-- Вывести список заказов с максимальной скидкой:
 select * 
from Orders 
where (price - discounter_price) = (
    select max(price - discounter_price) 
    from Orders
);

-- 8.Ответ на вопрос: как вы определите скидку?
-- Скидка определяется как разница между нормальной ценой (price) и скидочной ценой (discounter_price). 

-- 9.Ответ на вопрос: может ли это быть разница между нормальной ценой и скидочной ценой?
-- Да, скидка может быть разницей между нормальной ценой и скидочной ценой.

-- 10.Запрос, который выведет все заказы с дополнительным столбцом процент скидки, 
-- который содержит разницу в процентах между нормальной и скидочной ценой:
select *, 
    ((price - discounter_price) / price * 100) as discounter_percentage
from Orders;


