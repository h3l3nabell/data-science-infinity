# -*- coding: utf-8 -*-
"""
@author: helen

Feature Scaling- to enhance the learning capabilities of the model
We force both the things we are measuring to be on the same scale.

2 common ways to do this:
    Standardisation
    Normalisation
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

X = pd.DataFrame({"Height": [1.98, 1.77, 1.76, 1.80, 1.64],
                  "Weight": [99, 81, 70, 86, 82]
                  })

# Standardisation method
scale_standard = StandardScaler()
scale_standard.fit_transform(X)

my_df_standardised = pd.DataFrame(
    scale_standard.fit_transform(X), columns=X.columns)

# Normalisation method
scale_norm = MinMaxScaler()
scale_norm.fit_transform(X)


my_df_normalised = pd.DataFrame(
    scale_norm.fit_transform(X), columns=X.columns)
