--SQL REAL WORLD QUESTIONS

-- Q1 : How many unbique transactions are there in the transactions table 
Select count(distinct transaction_id) from grocery_db.transactions;
--18160

Select distinct transaction_id from  grocery_db.transactions;

-- Q2 : How many customers were in each mailer_type category for the delivery club campaign?
select mailer_type, count(*)
from grocery_db.campaign_data
where campaign_name =  'delivery_club'	
group by mailer_type
;

-- Q3 : Return a list of customers who spent more than $500 and had 5 or more unique transactions in the month of August 2020
select customer_id, count(distinct transaction_id) as total_txns, sum(sales_cost) as total_spend 
from grocery_db.transactions
where transaction_date between '2020-08-01' and '2020-08-31'
group by customer_id
having sum(sales_cost) > 500 and count(distinct transaction_id) > 4
order by total_txns desc
;

-- Q4: Return a list of duplicate credit scores that exist in the customer_details table

select credit_score, count(*)
from grocery_db.customer_details
group by credit_score
having count(*) > 1
;

-- Q5: Return the customer_id(s) for the customer(s) who has/have the 2nd highest credit score. Make sure your code would work for the Nth highest credit score as well


SELECT * 
FROM
grocery_db.customer_details CUST
Inner Join
(
select  distinct credit_score 
, dense_rank() over (order by credit_score desc)
from grocery_db.customer_details
where credit_score is not null
order by credit_score desc
) SCORES
ON Scores.Credit_Score = CUST.Credit_Score
WHERE SCORES.dense_rank = 4
--and X = 2
order by CUST.credit_score desc
;

WITH SCORES AS 
(
  SELECT
    customer_id,
    credit_score, 
    dense_rank() over (order by credit_score desc) as score_rank
    
  FROM
    grocery_db.customer_details
    
  WHERE 
    credit_score is not null
)
SELECT customer_id, score_Rank
FROM SCORES
WHERE score_rank = 44
;


-- Q6: I made this up -  Return the customer_id(s) for the customer(s) who have a credit score in the top 25%. 
SELECT Cust.*, Scores.Score 
FROM
grocery_db.customer_details CUST
Inner Join
(
select  distinct credit_score 
, ntile(4) over (order by credit_score desc) As Score
from grocery_db.customer_details
where credit_score is not null
order by credit_score desc
) SCORES
ON Scores.Credit_Score = CUST.Credit_Score
WHERE SCORES.Score = 3
--and X = 2
order by CUST.credit_score desc
;

WITH SCORES AS 
(
  SELECT
    customer_id,
    credit_score, 
    ntile(4) over (order by credit_score desc) as score
    
  FROM
    grocery_db.customer_details
    
  WHERE 
    credit_score is not null
)
SELECT customer_id, score
FROM SCORES
WHERE score = 4
;

