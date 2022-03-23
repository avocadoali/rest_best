# Database Scripts

## Enter postgresql shell

heroku login 
heroku pg:psql -a rest-best

## Drop table

DROP TABLE IF EXISTS restbesttables;


## Create Tables
CREATE TABLE IF NOT EXISTS restbestmenu(
ID          serial PRIMARY KEY,
name        varchar(40) NOT NULL,
type        varchar(15) NOT NULL CHECK (type IN('Starters', 'Main Dishes', 'Drinks', 'Side Dishes')), 
price       float NOT NULL, 
details     varchar(300) 
);

CREATE TABLE IF NOT EXISTS restbesttables(
ID          serial PRIMARY KEY,
TABLE_ID    integer NOT NULL,
ITEM_ID     integer NOT NULL,
FOREIGN KEY (ITEM_ID) REFERENCES restbestmenu(ID)
);


## Insert Row in a table restbesttables
INSERT INTO restbesttables (table_id, item_id)
VALUES ( 6969, 10);

INSERT INTO restbesttables (table_id, item_id)
VALUES ( 6969, 420)
RETURNING *;



## Insert Row in a table restbestmenu
DROP TABLE IF EXISTS restbestmenu;

CREATE TABLE IF NOT EXISTS restbestmenu(
ID          serial PRIMARY KEY,
name        varchar(40) NOT NULL,
type        varchar(15) NOT NULL CHECK (type IN( 'Main Dishes', 'Drinks', 'Side Dishes')), 
price       float NOT NULL, 
details     varchar(300) 
);

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Hamburger', 'Main Dishes', 6.00, '180g Patty, housemade burger sauce, salad, tomatoes, pickled cucumber, caramilized onions')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Chesseburger', 'Main Dishes', 6.69, '180g Patty, cheddar cheese, housemade burger sauce, salad, tomatoes, pickled cucumber, caramilized onions')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Bacon Cheesebuger', 'Main Dishes', 7.10, '180g Patty, bacon, cheddar cheese, housemade burger sauce, salad, tomatoes, pickled cucumber, caramilized onions')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Double Cheeseburger', 'Main Dishes', 7.50, '2x 180g Patty, , cheddar cheese, housemade burger sauce, salad, tomatoes, pickled cucumber, caramilized onions')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Water', 'Drinks', 3.50 , '5l Ensinger Sport')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Augustiner Helles', 'Drinks', 4.20 , '')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'French Fries', 'Side Dishes', 3.90 , 'Housemade crispy frenchfries')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Chicken Wings', 'Side Dishes', 6.20 , 'Housemade crispy chicken wings with sweet honey mustard sauce')
RETURNING *;

INSERT INTO restbestmenu (name, type, price, details)
VALUES ( 'Ceasar Salad', 'Side Dishes', 4.50, 'Fresh ceasar salad with housemade ceasar dressing')
RETURNING *;






## Select from table

SELECT * FROM restbestmenu;


## Select all Order from one Table
with get_all as (
    SELECT rm.id as id, rm.name, rm.type,rm.price
    FROM restbesttables rt, restbestmenu rm 
    where rt.table_id = 123
    and rm.id = rt.item_id
), get_anz as (
    SELECT rm.id iddd, count(*) cnt
    FROM restbesttables rt, restbestmenu rm 
    where rt.table_id = 123
    and rm.id = rt.item_id
    group by rm.id
)
select distinct * 
from get_all a, get_anz b 
where a.id = b.iddd;

## Select all Order from one Table with chrono
with get_all as (
    SELECT rm.id as id, rm.name, rm.type,rm.price, rt.id as chrono
    FROM restbesttables rt, restbestmenu rm
    where rt.table_id = 123
    and rm.id = rt.item_id
), get_anz as (
    SELECT rm.id iddd, count(*) cnt
    FROM restbesttables rt, restbestmenu rm
    where rt.table_id = 123
    and rm.id = rt.item_id
    group by rm.id
)
select distinct(id), name, type, price, iddd, cnt
from get_all a, get_anz b
where a.id = b.iddd;

## Delete n entries in tables

DELETE FROM restbesttables
WHERE id  IN (
    SELECT id 
    FROM restbesttables rt
    WHERE rt.table_id = 55555
    AND rt.item_id = 1
    limit 2
    )

## Select all orders from all tables
SELECT rt.table_id, rt.id as order_nr,  rm.id as food_id, rm.name, rm.type,rm.price
FROM restbesttables rt, restbestmenu rm 
where rm.id = rt.item_id
order by table_id, order_nr;

## Get distinct tables
select distinct(table_id)
from restbesttables


## Rename Columns

ALTER TABLE restbestmenu 
RENAME COLUMN name TO nameeeeee;

## Change Column Type 

ALTER TABLE restbestmenu
ALTER name varchar(15) not null (type IN('Starters', 'Main Dishes', 'Drinks', 'Side Dishes'));

ALTER TABLE restbestmenu
ALTER type varchar(15) not null (type IN('Starters', 'Main Dishes', 'Drinks', 'Side Dishes'));
## Update Column 
UPDATE restbestmenu 
SET details = '0.5l Ensinger Sport'
WHERE name = 'Water';



# TODO's

Benachrichtungsfunktion 
    Hilfe
    Bezahlen
    Nachrichtschicken

Loginpage Benutzer - Passwort

Karte selber anlegen
