--SQL PORTFOLIO PROJECT 

select *
from grocery_db.transactions
limit 5
;

-- no null transaction dates or other data we're depending on...
select *
from grocery_db.transactions
where transaction_date is null
or num_items is null
or sales_cost is null
or customer_id is null
limit 6
;


-- look at our date range:

select max(transaction_date) as max_date
, min(transaction_date) as min_date
from grocery_db.transactions
;

-- Which customers made purchases in month 1?

select count(distinct customer_id)
from grocery_db.transactions
where transaction_date >= '2020-04-01'
and transaction_date <= '2020-04-30'
;

with ORIGINAL_MONTH AS
(
select distinct customer_id
from grocery_db.transactions
where transaction_date >= '2020-04-01'
and transaction_date <= '2020-04-30'
)
select count(distinct LATEST_MONTH.customer_id) 
from grocery_db.transactions LATEST_MONTH
inner join ORIGINAL_MONTH on ORIGINAL_MONTH.customer_id = LATEST_MONTH.customer_id
where LATEST_MONTH.transaction_date >= '2020-09-01'
and LATEST_MONTH.transaction_date <= '2020-09-30'
;

-- to do this all together we can do multiple sets
with
ORIGINAL_COUNT AS
(
select count(distinct customer_id) As TotalFirstMonth
from grocery_db.transactions
where transaction_date >= '2020-04-01'
and transaction_date <= '2020-04-30'
) 
, ORIGINAL_MONTH AS
(
select distinct customer_id
from grocery_db.transactions
where transaction_date >= '2020-04-01'
and transaction_date <= '2020-04-30'
)
, LATEST_MONTH AS 
(
select distinct LATEST_MONTH.customer_id
from grocery_db.transactions LATEST_MONTH
inner join ORIGINAL_MONTH on ORIGINAL_MONTH.customer_id = LATEST_MONTH.customer_id
where LATEST_MONTH.transaction_date >= '2020-09-01'
and LATEST_MONTH.transaction_date <= '2020-09-30'
)
select count(distinct LATEST_MONTH.customer_id) As Retained_Customers , Max(ORIGINAL_COUNT.TotalFirstMonth) As First_Month_Customers, (count(distinct LATEST_MONTH.customer_id) * 100 / Max(ORIGINAL_COUNT.TotalFirstMonth)) As Percent_Retention_Rate
from LATEST_MONTH 
CROSS JOIN ORIGINAL_COUNT



