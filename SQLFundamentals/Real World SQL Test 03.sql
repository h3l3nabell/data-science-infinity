--SQL REAL WORLD QUESTIONS

-- Q1 : Return a list of customers from the loyalty_scores table who have a customer_loyalty score of 0.77, 0.88 or 0.99

select *
from grocery_db.loyalty_scores 
where customer_loyalty_score in (0.77, 0.88, 0.99)
;


-- Q2 : Return the average customer loyalty score for customers split by gender
select CUST.gender, AVG(SCORES.customer_loyalty_score) as average_loyalty
from grocery_db.customer_details CUST 
inner join grocery_db.loyalty_scores SCORES on CUST.customer_id = SCORES.customer_id
group by CUST.gender
;

-- Q3 : return customer id, distance from store and a new column called distance category that tags customers who are less than mile from the store as "Walking Distance", 
--1 mile or more as "Driving Distance" and "Unknown" for those where we don't know how far away they are

Select customer_id
, distance_from_store
, CASE
  WHEN distance_from_store < 1 THEN 'WALKING DISTANCE'
  WHEN distance_from_store >= 1 THEN 'DRIVING DISTANCE'
  ELSE 'UNKNOWN'
  END AS distance_category
  
FROM grocery_db.customer_details
order by distance_from_store
;

-- Q4: For the 400 customers with a customer loyalty score, divide them up into 10 dectiles, and calculate the average distance from store for each dectile
WITH CUSTS AS
(
select  ntile(10) over (order by SCORES.customer_loyalty_score desc) as loyalty_dectile
 , distance_from_store
 
from grocery_db.customer_details CUST
inner join grocery_db.loyalty_scores SCORES on CUST.customer_id = SCORES.customer_id 
where credit_score is not null
)
SELECT CUSTS.loyalty_dectile, Avg(distance_from_store) as average_distance
FROM CUSTS
Group By CUSTS.loyalty_dectile
order by Custs.loyalty_dectile
;

-- Q5: Return data showing, for each product area name - the total sales, and the percentage of overall sales that each product area makes up.

create temp table overall_sales as select sum(sales_cost) as overall_total from grocery_db.transactions;
select * from overall_sales;
--drop table overall_sales;


WITH PRODUCTS AS
(
select product_area_name
, sum(sales_cost) as total_sales
from grocery_db.transactions t
inner join grocery_db.product_areas p on t.product_area_id = p.product_area_id
group by product_area_name
)
select PRODUCTS.product_area_name
, PRODUCTS.total_sales
--, overall_total
, (PRODUCTS.total_sales / overall_total) * 100 AS percentage_of_total
FROM PRODUCTS
Cross Join overall_sales AS OVERALL
;

WITH PRODUCTS AS
(
select product_area_name
, sum(sales_cost) as total_sales
from grocery_db.transactions t
inner join grocery_db.product_areas p on t.product_area_id = p.product_area_id
group by product_area_name
)
select PRODUCTS.product_area_name
, PRODUCTS.total_sales
, (PRODUCTS.total_sales / (select sum(sales_cost) from grocery_db.transactions)) * 100 AS percentage_of_total
FROM PRODUCTS
--Cross Join overall_sales AS OVERALL
;

