# -*- coding: utf-8 -*-
"""
 Pandas - Renaming Columns
"""

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx",
                             sheet_name="transactions")
list(transactions)
transactions.rename(columns={"customer_id": "friend_id"}, inplace=True)

column_names = ['customer_id',
                'transaction_date',
                'basket_id',
                'product_group_id',
                'num_items',
                'sales_cost']

transactions.columns = column_names

list(transactions)

column_names = ['customer id',
                'transaction date',
                'basket id',
                'product group_id',
                'num_items',
                'sales_cost']

transactions.columns = transactions.columns.str.replace(" ", "_")
