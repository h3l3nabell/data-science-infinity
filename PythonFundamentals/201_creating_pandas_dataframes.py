# -*- coding: utf-8 -*-
"""
Pandas - creating dataframes
"""

import pandas as pd

# Create an empty dataframe
my_df = pd.DataFrame()

# Create with a column - Name, list of values
my_df = pd.DataFrame({"Name": ["Tom", "Dick", "Harry"]})


# To create a multi-column dataframe, there must be the same number of
# row entries for each column.
my_df = pd.DataFrame({"Name": ["Tom", "Dick", "Harry"],
                      "ID": [101, 102, 103]})


# Creating Dataframes from a list
my_list = [["Tom", 101], ["Dick", 102], ["Harry", 103]]
my_df = pd.DataFrame(my_list, columns=["Name", "ID"])

# Importing from an external file - csv
my_data = pd.read_csv("TomDickHarry.csv")

transactions = pd.read_excel("grocery_database.xlsx",
                             sheet_name="transactions")
