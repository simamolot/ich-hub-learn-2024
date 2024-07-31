use world;
-- 2.
(select name, population from city)
union
(select name, population from country);

-- 3.
-- Таблицы в базе данных "world" имеют ограничение уникальности для столбца Name в таблицах city и country, 
-- чтобы каждая запись имела уникальное значение имени города или страны.

use 310524ptm_serafima;

-- 4.
create table citizen (
    id int auto_increment primary key,
    social_security_number varchar(20),
    firstname varchar(50) not null,
    lastname varchar(50),
    email varchar(100)
);

-- 5. 
create table coworkers (
    id int auto_increment primary key,
    name varchar(100),
    department varchar(100)
);

-- 6.
insert into citizen (social_security_number, firstname, lastname, email) 
values ('123456789', 'johann', 'schmidt', 'johann.schmidt@example.com'),
('987654321', 'anna', 'müller', 'anna.müller@example.com'),
('555555555', 'maxim', 'ivanov', 'maxim.ivanov@example.com'),
('111111111', 'johann', '', 'johann.newman@example.com'),
('222222222', 'maria', '', 'maria.green@example.com');

-- 7.
alter table citizen
modify firstname varchar(50) not null,
modify lastname varchar(50) not null;

-- 8.
alter table citizen
add constraint uc_firstname_lastname unique (firstname, lastname);

-- 9.
drop table if exists citizen;

create table citizen (
    id int auto_increment primary key,
    social_security_number varchar(20),
    firstname varchar(50) not null,
    lastname varchar(50) not null,
    email varchar(100),
    constraint uc_firstname_lastname unique (firstname, lastname)
);

-- 10.

insert into citizen (social_security_number, firstname, lastname, email) 
values ('123456789', 'johann', 'schmidt', 'johann.schmidt@example.com'),
       ('987654321', 'anna', 'müller', 'anna.müller@example.com');

insert into citizen (social_security_number, firstname, lastname, email) 
values ('555555555', 'maxim', 'ivanov', 'maxim.ivanov@example.com'),  
       ('111111111', 'johann', '', 'johann.newman@example.com');  

select * from coworkers;


