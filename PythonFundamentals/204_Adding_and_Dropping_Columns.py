# -*- coding: utf-8 -*-
"""
 Pandas - Adding and dropping columns
"""

import pandas as pd
import numpy as np

transactions = pd.read_excel("grocery_database.xlsx",
                             sheet_name="transactions")

transactions["store_id"] = 1

transactions["profit"] = transactions["sales_cost"] * 0.2

transactions["sales_type"] = np.where(transactions["sales_cost"] > 20,
                                      "Large", "Small")

# list of conditions & outcomes
condition_rules = [transactions["sales_cost"] > 50,
                   transactions["sales_cost"] > 20,
                   transactions["sales_cost"] > 10]

outcomes = ["X-Large", "Large", "Medium"]
transactions["sales_type"] = np.select(condition_rules,
                                       outcomes, default="Small")
# axis = 1 means drop columns - to drop rows you would say axis = 0
new_df = transactions.drop(["sales_cost"], axis=1)
