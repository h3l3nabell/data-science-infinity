# -*- coding: utf-8 -*-
"""
 Pandas - Accessing Columns in a dataframe
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx",
                             sheet_name="transactions")


"""
 equivalent to
 select customer_id, sales_cost
 from transactions
 """

new_df_bad_example = transactions.customer_id
# all sorts of problems if the column name is a reserved word or var name

my_var = "customer_id"

# fails with attribute error:
new_df_bad_example.my_var

new_df_good = transactions["customer_id"]
transactions[my_var]  # works! but its a series, not a dataframe

# now its a dataframe bc we passed a col list
new_df = transactions[[my_var, "sales_cost"]]
new_df.head(20)
