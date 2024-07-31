-- 1.Вывести текущую дату и время
SELECT DATE_FORMAT(NOW(), '%Y_%m_%d | %H - %i - %S') as Year_and_hour;

-- 2.Вывести текущий год и месяц
SELECT DATE_FORMAT(NOW(), "%Y_%m");

-- 3.Вывести текущее время
SELECT DATE_FORMAT(NOW(), '%H:%i:%s');

-- 4.Вывести название текущего дня недели
SELECT DATE_FORMAT(NOW(), '%W') as current_day_of_week;

-- 5.Вывести номер текущего месяца
SELECT DATE_FORMAT(NOW(), '%m') as current_month_of_week;

-- 6.Вывести номер дня в дате “2020-03-18”
SELECT DAY('2020-03-18') as day_number;

-- 7.Подключиться к базе данных shop (которая находится на удаленном сервере).
use shop;

-- 8.Определить какие из покупок были совершены апреле (4-й месяц)
SELECT ORDER_ID, ODATE as Year_date, 
MONTHNAME(ODATE) as month_name
FROM ORDERS
WHERE MONTH(ODATE) = 4;

-- 9.Определить количество покупок в 2022-м году
select count(ORDER_ID) as Orders, 
ODATE as Orders_year
from ORDERS
where YEAR(ODATE) = 2022;

-- 10.Определить, сколько покупок было совершено в каждый день. Отсортировать 
-- строки в порядке возрастания количества покупок. Вывести два поля - дату и количество покупок
SELECT ODATE as Date_, COUNT(ORDER_ID) as Number_of_orders
FROM ORDERS
GROUP BY ODATE
ORDER BY Number_of_Orders;

-- 11.Определить среднюю стоимость покупок в апреле
select avg(AMT) as Average_Orders, ODATE as Apri_ldate
from ORDERS
where MONTHNAME(ODATE) = 'April';





