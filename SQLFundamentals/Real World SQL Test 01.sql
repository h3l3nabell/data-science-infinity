--SQL REAL WORLD QUESTIONS

-- Q1 : How many rows in the transactions table 
Select Count(*) from grocery_db.transactions;
-- 38506

-- Q2 : Return the customer id from the customer who lives farthest from the store.

Select customer_id
From grocery_db.customer_details
Where distance_from_store = (select distinct Max(distance_From_Store) from grocery_db.customer_details)
--limit 1
;

-- rank customers - dense rank?

-- Q3 : Return the number of unique customers in the customer_details table, split by gender
select gender, count(*) 
from grocery_db.customer_details
group by gender;

--F	485
--M	380
--NULL 5


-- Q4: What were the total sales for each product area name for July 2020?  Return these in order of highest to lowest sales.

select p.product_area_name, sum(t.sales_cost) as Total_Sales
From grocery_db.transactions t
inner join grocery_db.product_areas p on t.product_area_id = p.product_area_id
where t.transaction_date between '2020-07-01' and '2020-07-31'
group by p.product_area_name
order by Total_Sales desc;

-- Q5: Return a list of all customer_id's that do not have a loyalty score (ie. they are in the customer_details table, but not in the loyalty_scores table)

select distinct customer_id
from grocery_db.customer_details
where customer_id not in (select customer_id from grocery_db.loyalty_scores) 
order by 1

--- BONUS --- Customer Value = average purchase value X average number of purchases

select min(transaction_date), max(transaction_date)
from grocery_db.transactions
-- we have transaction data from 1/4/2020 to 30/9/2020

select *
from grocery_db.transactions
where transaction_date is null
or num_items is null
or sales_cost is null
or customer_id is null
limit 6
-- no null transaction dates or other data we're depending on...

-- customer value = average purchase value X average number of purchases
--with totals as (SELECT sum(num_items) as total_num_items, sum(sales_cost) as total_sales_cost from grocery_db.transactions)   

-- Who are our top 10 most valuable customers?
 
select customer_id
--, min(date_trunc('month',transaction_date)) as min_date
--, max(date_trunc('month',transaction_date)) as max_date
, sum(num_items) as total_num_items
, sum(sales_cost) as total_sales_cost
, sum(sales_cost) / sum(num_items) as average_purchase_value
, sum(sales_cost) / 6 as average_monthly_customer_value
from grocery_db.transactions
group by customer_id
order by average_monthly_customer_value desc
limit 10



-- churn?  Which customers have stopped spending  with us before the end of the period?
select customer_id, min(date_trunc('month',transaction_date)) as min_date, max(date_trunc('month',transaction_date)) as max_date,  sum(num_items) as num_items, sum(sales_cost) as sales_cost
from grocery_db.transactions
group by customer_id
having  max(date_trunc('month',transaction_date)) < '2020-09-01'
order by  max(date_trunc('month',transaction_date))
