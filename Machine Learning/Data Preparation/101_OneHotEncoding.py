# -*- coding: utf-8 -*-
"""
@author: helen

One Hot Encoding - Dealing with Categorical Variables
This is where you make a new boolean column for each category
"""

# Import required packages
# import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder


X = pd.DataFrame({"input1": [1, 2, 3, 4, 5],
                  "input2": ["A", "A", "B",  "B", "C"],
                  "input3": ["X", "X", "X", "Y", "Y"]})

categorical_vars = ["input2", "input3"]

# Here sparse=False means we return an array rather than a  sparse object
# the drop = first will tell it to drop the first of the encoded values
# this avoids the dummy variable trap - and you dont lose any info for ML - the
# dropped value would have been 1 whenever the others were all zero.
one_hot_encoder = OneHotEncoder(sparse=False, drop="first")

encoder_vars_array = one_hot_encoder.fit_transform(X[categorical_vars])
encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

encoder_vars_df = pd.DataFrame(
    encoder_vars_array, columns=encoder_feature_names)

# the reset index ensures that no rows are not aligned.
X_HOT = pd.concat(
    [X.reset_index(drop=True), encoder_vars_df.reset_index(drop=True)], axis=1)

X_Clean = X_HOT.drop(categorical_vars, axis=1)
