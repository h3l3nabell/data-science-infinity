# -*- coding: utf-8 -*-
"""
@author: helen

Missing Values With Pandas
"""

# Import required packages
import numpy as np
import pandas as pd

from sklearn.impute import KNNImputer


my_df = pd.DataFrame({"A": [1, 2, 3, 4, 5],
                      "B": [1, 1, 3,  3, 4],
                      "C": [1, 2, 9, np.nan, 20]})

# Finding Missing Values with KNN Imputer
imputer = KNNImputer()
imputer = KNNImputer(n_neighbors=1)
imputer.fit_transform(my_df)

imputer = KNNImputer(n_neighbors=2)
imputer.fit_transform(my_df)

imputer = KNNImputer(n_neighbors=2, weights="distance")
imputer.fit_transform(my_df)
pd.DataFrame(imputer.fit_transform(my_df), columns=my_df.columns)
