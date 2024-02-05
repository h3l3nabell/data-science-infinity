# -*- coding: utf-8 -*-
"""
@author: helen

Grocery Case Study
"""
import pandas as pd
import pickle

loyalty_scores = pd.read_excel(
    "data/grocery_database.xlsx", sheet_name="loyalty_scores")

customer_details = pd.read_excel(
    "data/grocery_database.xlsx", sheet_name="customer_details")

transactions = pd.read_excel(
    "data/grocery_database.xlsx", sheet_name="transactions")


data_for_regression = pd.merge(
    customer_details, loyalty_scores, how="left", on="customer_id")

sales_summary = transactions.groupby("customer_id").agg({"sales_cost": "sum",
                                                         "num_items": "sum",
                                                         "transaction_id": "count",
                                                         "product_area_id": "nunique"
                                                         }).reset_index()

sales_summary.columns = ["customer_id", "total_sales_cost", "total_num_items",
                         "transaction_id_count", "unique_product_ids"]

sales_summary["average_basket_value"] = sales_summary["total_sales_cost"] / \
    sales_summary["transaction_id_count"]

data_for_regression = pd.merge(
    data_for_regression, sales_summary, how="inner", on="customer_id")

regression_modelling = data_for_regression.loc[data_for_regression["customer_loyalty_score"].notna(
)]

regression_scoring = data_for_regression.loc[data_for_regression["customer_loyalty_score"].isna(
)]

regression_scoring.drop(["customer_loyalty_score"], axis=1, inplace=True)

pickle.dump(regression_modelling, open("data/regression_modelling.p", "wb"))
pickle.dump(regression_scoring, open("data/regression_scoring.p", "wb"))
