--SQL PORTFOLIO PROJECT 

select *
from grocery_db.transactions
limit 5
;

-- look at our date range:

select max(transaction_date) as max_date
, min(transaction_date) as min_date
from grocery_db.transactions
;

-- calculate how many purchases in the 6 months, which is the number of unique transactions for a customer.  We group by customer_id and transaction_id, and count the numer of days they shopped

select Customer_Id, Transaction_ID, Count( distinct transaction_date)
, sum(num_items) as num_items
, sum(sales_cost) as sales_cost
from grocery_db.transactions
where transaction_date >= '2020-04-01'
and transaction_date <= '2020-09-30'
Group By Customer_Id, Transaction_ID
;

-- Which customers had the most transactions in the 6 month period? 
with VISITS as
(
select Customer_Id, Transaction_ID, Count(Transaction_Date) AS Num_Visits
, sum(num_items) as num_items
, sum(sales_cost) as sales_cost
from grocery_db.transactions
where transaction_date >= '2020-04-01'
and transaction_date <= '2020-09-30'
Group By Customer_Id, Transaction_ID
)
, FREQUENCY as
(
Select VISITS.Customer_Id
, sum(Num_Visits) as Number_Of_Visits
, sum(num_items) as num_items
, sum(sales_cost) as sales_cost
From VISITS
Group By VISITS.Customer_Id
)
select FREQUENCY.Customer_Id
, ntile(10) over (order by FREQUENCY.Number_Of_Visits desc, sales_cost desc) as Frequency_Percentile
,Number_Of_Visits
, sales_cost
, num_items
FROM FREQUENCY
Order by Frequency_Percentile 
;

-- inspect our data by month
select Customer_Id
--, DATE_TRUNC('month',Transaction_date) as Transaction_Month
, To_Char(DATE_TRUNC('month',Transaction_date), 'Month') as Month
, Date_Part('Year',DATE_TRUNC('month',Transaction_date)) as Year
, count(*) as Transaction_Count
, sum(num_items) as num_items
, sum(sales_cost) as sales_cost
from grocery_db.transactions
group by Customer_Id, DATE_TRUNC('month',Transaction_date)
order by DATE_TRUNC('month',Transaction_date), Transaction_Count desc
;
