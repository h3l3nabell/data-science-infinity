# -*- coding: utf-8 -*-
"""
 Pandas - Map, Replace, ApplyMap
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx",
                             sheet_name="transactions")

# ILOC - index locate
# transactions.iloc[row_indexes, column_indexes]

transactions.iloc[0]  # returns the first row of df

transactions.iloc[0: 4]  # slicing rows 0 to 4

transactions.iloc[[0, 30, 51]]   # list of specific items

# limit columns as well
transactions.iloc[0: 4, [0, 3, -1]]

transactions.iloc[:, [0, 3, -1]]

# LOC - locate
# transactions.loc[row_labels, column_labels]

transactions.loc[0]  # returns the first row of df - row labels are indexes
transactions.set_index("customer_id", inplace=True)
transactions.loc[642]  # returns ALL rows for customer 642
transactions.reset_index(inplace=True)

# to get column names
list(transactions)
transactions.loc[0:10, "customer_id"]
transactions.loc[0:10, ["customer_id", "product_area_id", "sales_cost"]]
transactions.loc[0:10, ["customer_id", "sales_cost", "product_area_id"]]

# Conditional Logic

transactions.loc[transactions["customer_id"] == 642]
transactions.loc[transactions["customer_id"] == 642,
                 ["customer_id", "product_area_id", "sales_cost"]]

transactions.loc[(transactions["customer_id"] == 642)
                 & (transactions["num_items"] > 5)]

transactions.loc[(transactions["customer_id"] == 642)
                 | (transactions["num_items"] > 5)]

transactions.loc[transactions["customer_id"].isin([642, 700])]
transactions.loc[~transactions["customer_id"].isin([642, 700])]
