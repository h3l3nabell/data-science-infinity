--select 1 as number;

select 
 * 
 , sum(sales_cost) over (partition by product_area_id) as transaction_total_sales
  , sales_cost * 100 / sum(sales_cost) over (partition by product_area_id) as transaction_sales_percent
from 
  grocery_db.transactions

--limit
--  3
  
--order by 
--   distance_from_store desc
;


select 
 * 
 , row_number() over (partition by customer_id order by transaction_date, transaction_id) as transaction_number
--  , sales_cost * 100 / sum(sales_cost) over (partition by product_area_id) as transaction_sales_percent
from 
  grocery_db.transactions
;
-- row number just numers in sequence.  Ties get a unique number
-- rank will give ties the same value, thin skip to the next value in terms of row number e.g.

--  time    rank
--  10s     1
--  10s     1
--  11s     3

-- dense_rank will do the same as rank but go to the next number in sequence after any ties

--  time    rank
--  10s     1
--  10s     1
--  11s     2

-- NTILE - for deciles / percentiles

select 
  customer_id
  , customer_loyalty_score
  , case
    when customer_loyalty_score > 0.66 then 'high loyal'
    when customer_loyalty_score > 0.33 then 'medium loyal' 
    else 'low loyal'
    end as loyalty_category
from 
  grocery_db.loyalty_scores
  ;
  
select 
  customer_id
  , customer_loyalty_score
  , ntile(3) over(order by customer_loyalty_score desc) as loyalty_category_3
  , ntile(10) over(order by customer_loyalty_score desc) as loyalty_category_10
from 
  grocery_db.loyalty_scores
  ;
