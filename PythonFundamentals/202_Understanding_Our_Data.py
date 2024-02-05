# -*- coding: utf-8 -*-
"""
 Pandas - Exploring & Understanding our Data using dataframe
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx",
                             sheet_name="transactions")

transactions.shape
transactions.head(20)
transactions.tail(10)
transactions.sample(frac=0.1)

# The first thing to do when you're looking at a new, big file
transactions.describe()
# The output shows us a count of records with non null values for each column
# We also have mean, min, max, and then 25%ile, 50%ile (median) and 25%ile

# have a  look at the first n rows with the largest values in columns, desc
transactions.nlargest(25, "sales_cost")

transactions.nsmallest(25, "sales_cost")

# get counts of unique values in each column
transactions.nunique()


customer_details = pd.read_excel("grocery_database.xlsx",
                                 sheet_name="customer_details")

# looking for nulls
customer_details.isna()

# there is also an isnull() function that does the same thing.

# now we can see how many rows with missing values we have!
customer_details.isna().sum()
