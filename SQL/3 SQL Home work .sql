use 310524ptm_serafima;

create table weather (
    city varchar(50),
    forecast_date date,
    temperature integer
);

insert into weather (city, forecast_date, temperature)
values ('Berlin', '2023-08-29', 30),
       ('Paris', '2023-06-15', 28),
       ('Rome', '2023-07-22', 32),
       ('New York', '2023-05-10', 25);

select * from weather;

update weather 
set temperature = 26 
where city = 'Berlin' AND temperature = 30;
set SQL_SAFE_UPDATES = 0;

update weather 
set city = 'Paris' 
where temperature > 25;

alter table weather 
add column min_temp integer;

update weather 
set min_temp = 0;

select * from weather;

