--SQL PORTFOLIO PROJECT

-- no null transaction dates or other data we're depending on...
select *
from grocery_db.transactions
where transaction_date is null
or num_items is null
or sales_cost is null
or customer_id is null
limit 6

-- look at our sales totals for the 6 months
select
  sum(sales_cost) as total_sales_value
,  sum(num_items) as total_num_items
,  avg(sales_cost) as average_transaction_value
from grocery_db.transactions
;

select *
from grocery_db.customer_details;

-- Who are our top 10 most valuable customers?
select customer_id
, sum(num_items) as total_num_items
, sum(sales_cost) as total_sales_cost
, sum(sales_cost) / sum(num_items) as average_item_value
, avg(sales_cost) as average_purchase_value
, sum(sales_cost) / 6 as average_monthly_customer_value
--, sum(sum(sales_cost)) over () as grand_total_Sales
from grocery_db.transactions
group by customer_id
order by total_sales_cost desc
limit 10

-- Q1 - Verify the validity of the pareto principal - that 80% of profits come from 20% of customers - for our data.  
-- Split our customers into quintiles of total sales value from the 6 months transaction data we have - our top 20% will be quintile 1
select customer_id
, sum(num_items) as total_num_items
, sum(sales_cost) as total_sales_value
, ntile(5) over (order by  sum(sales_cost) desc) As Customer_Value_Quintile
, sum(sum(sales_cost)) over () as grand_total_sales
from grocery_db.transactions
group by customer_id


-- run a query over this selection and group by the quintile, to see the total sales value for each customer value quintile
With CUST_VALUE as 
(
select customer_id
, sum(num_items) as total_num_items
, sum(sales_cost) as total_sales_value
, ntile(5) over (order by  sum(sales_cost) desc) As Customer_Value_Quintile
, sum(sum(sales_cost)) over () as grand_total_sales
from grocery_db.transactions
group by customer_id
)
SELECT Customer_Value_Quintile
,  sum(total_num_items) as total_num_items
,  sum(total_sales_value) as total_sales_value
,  (sum(total_sales_value) * 100) / max(grand_total_sales) as percentage_total_sales
FROM CUST_VALUE
GROUP BY Customer_Value_Quintile
ORDER BY Customer_Value_Quintile
;

-- so we see from our grocery db data, that pareto's principal is false, we have just under 50% of sales from our top 20% of customers.


-- Q2 We want to look at the cost of supply, so now we ideally want to optimise for customers who make fewer, larger purchases, thereby reducing packing and delivery costs.

  




