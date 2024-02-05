
select * from grocery_db.customer_details;
select * from grocery_db.loyalty_scores;
-- Inner Join
select c.* , l.customer_loyalty_score
from grocery_db.customer_details c
inner join grocery_db.loyalty_scores l on c.customer_id = l.customer_id;
;
-- Left Join
select c.* , l.customer_loyalty_score
from grocery_db.customer_details c
left join grocery_db.loyalty_scores l on c.customer_id = l.customer_id;
;
-- Adding Other Logic

select c.* , l.customer_loyalty_score
from grocery_db.customer_details c
left join grocery_db.loyalty_scores l on c.customer_id = l.customer_id
where customer_loyalty_score > 0.5
;

-- Joining multiple tables

select t.* 
, l.customer_loyalty_score
, p.product_area_name
from grocery_db.transactions t
left join grocery_db.loyalty_scores l on t.customer_id = l.customer_id
inner join grocery_db.product_areas p on t.product_area_id = p.product_area_id
;

-- Other Join Types
create temp table table1 (
id char(1)
, t1_col1 int
, t1_col2 int
)
;

insert into table1 values ('A', 1, 1), ('B', 1, 1);

select * from table1;

--drop table table2;
create temp table table2 (
id char(1)
, t2_col1 int
, t2_col2 int
)
;

insert into table2 values ('A', 2, 2), ('C', 2, 2);

select * from table2;

-- outer join

select
 a.id as id_t1
 , a.t1_col1
 , a.t1_col2
 , b.id as id_t2
 , b.t2_col1
 , b.t2_col2
 
from
  table1 a
  full outer join table2 b on a.id = b.id
  ;
  

-- cross join

select
 a.id as id_t1
 , a.t1_col1
 , a.t1_col2
 , b.id as id_t2
 , b.t2_col1
 , b.t2_col2
 
from
  table1 a
  cross join table2 b 
  ;
  

-- Union (removes dupliclate rows) & Union All (doesn't)
select product_area_name from grocery_db.product_areas where product_area_id in (1, 2)
union
select product_area_name from grocery_db.product_areas where product_area_id in (1,2,3,4,5);


select 'T1', * from table1
union
select 'T2', * from table2
;

select product_area_name from grocery_db.product_areas where product_area_id in (1, 2)
union all
select product_area_name from grocery_db.product_areas where product_area_id in (1,2,3,4,5);



