# -*- coding: utf-8 -*-
"""
 Pandas - Map, Replace, ApplyMap
"""

import numpy as np
import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx",
                                 sheet_name="customer_details")
product_areas = pd.read_excel("grocery_database.xlsx",
                              sheet_name="product_areas")


# Sorting
customer_details.sort_values(by="distance_from_store", inplace=True)

customer_details.sort_values(by="distance_from_store",
                             inplace=True,
                             ascending=False)

customer_details.sort_values(by=["distance_from_store", "credit_score"],
                             inplace=True,
                             ascending=False,
                             na_position="first")


# Ranking
x = pd.DataFrame({"column1": [1, 1, 1, 2, 3, 4, 5, np.nan, 6, 8]})
x["column1"].rank()
x["column1_rank"] = x["column1"].rank()
x["average_rank"] = x["column1"].rank(method="average")
x["min_rank"] = x["column1"].rank(method="min")
x["max_rank"] = x["column1"].rank(method="max")
x["first_rank"] = x["column1"].rank(method="first")
x["dense_rank"] = x["column1"].rank(method="dense")

x["dense_rank_na_top"] = x["column1"].rank(method="dense", na_option="top")
x["dense_rank_na_bottom"] = x["column1"].rank(
    method="dense", na_option="bottom")
