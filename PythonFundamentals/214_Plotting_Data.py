# -*- coding: utf-8 -*-
"""
 Pandas - dealing with duplicate data
"""

import pandas as pd

transactions = pd.read_excel(
    "grocery_database.xlsx", sheet_name="transactions")

customer_details = pd.read_excel(
    "grocery_database.xlsx", sheet_name="customer_details")

product_areas = pd.read_excel(
    "grocery_database.xlsx", sheet_name="product_areas")

customer_details.plot()  # tries to plot all numeric columns with line plot!

# line plots primarily used for sequential data

# make a more useful dataframe by aggregating transactions
daily_sales_summary = transactions.groupby(
    "transaction_date")[["sales_cost", "num_items"]].sum().reset_index()

daily_sales_summary["sales_cost"].plot()
# but y axis is just the index by default.  Specified column is the x.
daily_sales_summary.plot(x="transaction_date", y="sales_cost")

daily_sales_summary.plot(x="transaction_date", y="sales_cost", kind="line")

# good for investigating correlations
daily_sales_summary.plot(x="num_items", y="sales_cost", kind="scatter")

# box plot - middle line is median (50th percentile)
# the box is the upper and lower quartiles
# Extremity lines at the 5th and 95th percentile
# Visualise quickly the spread or distribution of the data
daily_sales_summary.plot(y="sales_cost", kind="box")

daily_sales_summary.plot(y="sales_cost", kind="hist")  # default bins = 10
daily_sales_summary.plot(y="sales_cost", kind="hist", bins=25)

product_areas.plot(kind="bar", y="profit_margin", x="product_area_name")
