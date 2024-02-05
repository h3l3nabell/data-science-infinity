# -*- coding: utf-8 -*-
"""
@author: helen

Missing Values With Pandas
"""

# Import required packages
import numpy as np
import pandas as pd

my_df = pd.DataFrame({"A": [1, 2, 4, np.nan, 5, np.nan, 7],
                      "B": [4, np.nan, 7, np.nan, 1, np.nan, 2]})

# Finding Missing Values with Pandas

# returns true for null, false otherwise
my_df.isna()

# returns a count of the trues in each column
my_df.isna().sum()


# dropping missing values with pandas * recommended approach if possible

my_df.dropna()
my_df.dropna(how="any")
my_df.dropna(how="all")

my_df.dropna(how="any", subset=["A"])

my_df.dropna(how="any", inplace=True)

# filling missing values with pandas

my_df = pd.DataFrame({"A": [1, 2, 4, np.nan, 5, np.nan, 7],
                      "B": [4, np.nan, 7, np.nan, 1, np.nan, 2]})

my_df.fillna(value=100)

mean_value = my_df["A"].mean()
my_df["A"].fillna(value=mean_value)

my_df.fillna(value=my_df.mean(), inplace=True)
