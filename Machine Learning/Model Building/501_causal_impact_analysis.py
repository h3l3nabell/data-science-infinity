# -*- coding: utf-8 -*-
"""
@author: helen

Causal Impact Analysis - Advanced Template
"""
######################################
# import required packages
######################################
import pandas as pd
from causalimpact import CausalImpact


######################################
# import & create data
######################################
transactions_0_loaded = pd.read_excel(
    "data/grocery_database.xlsx", sheet_name="transactions")

campaign_data_0_loaded = pd.read_excel(
    "data/grocery_database.xlsx", sheet_name="campaign_data")

# aggregate transaction data to customer level
customer_daily_sales = transactions_0_loaded.groupby(
    ["customer_id", "transaction_date"])["sales_cost"].sum().reset_index()


# merge on the signup flag from the campaign_data table

customer_daily_sales_merged = pd.merge(
    customer_daily_sales, campaign_data_0_loaded, how="inner", on="customer_id")

# pivot the data to aggregate daily sales by signup group
causal_impact_df = customer_daily_sales_merged.pivot_table(index="transaction_date",
                                                           columns="signup_flag",
                                                           values="sales_cost",
                                                           aggfunc="mean"
                                                           )

# provide a frequency for the time series date values to make it daily
causal_impact_df.index.freq = "D"

# for causal impact, we need the impacted group to be the first column so flip!
causal_impact_flipped_df = causal_impact_df[[1, 0]]

# rename columns to something more meaningful
causal_impact_flipped_df.columns = ["member", "non_member"]

######################################
# apply causal impact
######################################

# include start and end dates for pre and post periods
pre_period = ["2020-04-01", "2020-06-30"]
post_period = ["2020-07-01", "2020-09-30"]

ci = CausalImpact(causal_impact_flipped_df, pre_period, post_period)

######################################
# plot the causal impact
######################################
ci.plot()

######################################
# Extract summary statistics and report
######################################
print(ci.summary())

print(ci.summary(output="report"))
