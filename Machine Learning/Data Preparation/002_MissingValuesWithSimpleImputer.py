# -*- coding: utf-8 -*-
"""
@author: helen

Missing Values With Pandas
"""

# Import required packages
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer


my_df = pd.DataFrame({"A": [1, 4, 7, 10, 13],
                      "B": [3, 6, 9,  np.nan, 15],
                      "C": [2, 5, np.nan, 11, np.nan]})

# Finding Missing Values with Simple Imputer
imputer = SimpleImputer()

# 2 step process - learn rules then apply them
imputer.fit(my_df)
imputer.transform(my_df)

my_df1 = imputer.transform(my_df)

# both steps in 1
imputer.fit_transform(my_df)

# Only use the above on training data.  You shouldnt fit on test data.

# to get a data frame

my_df2 = pd.DataFrame(imputer.fit_transform(my_df), columns=my_df.columns)

# if we only want to apply to specific columns, pass a list of them

imputer.fit_transform(my_df[["B", "C"]])

my_df["B"] = imputer.fit_transform(my_df[["B"]])
