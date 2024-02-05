# -*- coding: utf-8 -*-
"""
 Pandas - dealing with missing values
"""

import numpy as np
import pandas as pd


customer_details = pd.read_excel(
    "grocery_database.xlsx", sheet_name="customer_details")

# find nulls - gives true or false for every data item in dataframe
customer_details.isna()

# gives us how many nulls in each column
customer_details.isna().sum()

# or the opposite - not na - gives us how many not nulls in each column
customer_details.notna().sum()

# investigate a specific column - how many are missing?
customer_details["distance_from_store"].isna().sum()

# now we want to extract those rows, so ... kind of like a where clause in []
customer_details[customer_details["distance_from_store"].isna()]

# now we want to get only the rows without nulls
customer_details[customer_details["distance_from_store"].notna()]

# removes all rows where any value is missing
customer_details.dropna(how="any")

# removes all rows where all values are missing
customer_details.dropna(how="all")

customer_details.dropna(how="any", subset=["distance_from_store"])
customer_details.dropna(how="any", subset=["distance_from_store", "gender"])

# now instead of dropping missing values we want to substitute a value
my_df = pd.DataFrame({"A": [1, 2, 4, np.nan, 5, np.nan, 7],
                      "B": [4, np.nan, 7, np.nan, 1, np.nan, 2]})

# fill in missing values from column A (inplace = true)
my_df["A"].fillna(value=0)

mean_value = my_df["A"].mean()
my_df["A"].fillna(value=mean_value)

customer_details.isna().sum()
customer_details["gender"].fillna(value="U", inplace=True)
customer_details["gender"].value_counts()

# whole load of useful info, mean , std, min, max, 25/50/75%
customer_details["distance_from_store"].describe()

customer_details["distance_from_store"].fillna(
    value=customer_details["distance_from_store"].median(), inplace=True)
