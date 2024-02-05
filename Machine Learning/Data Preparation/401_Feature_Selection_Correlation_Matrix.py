# -*- coding: utf-8 -*-
"""
@author: helen

Feature Selection - Correlation Matrix
"""

import pandas as pd

my_df = pd.read_csv("feature_selection_sample_data.csv")

# Investigate correlation between variables and output and also with each other
# You dont want highly correlated variables in models like linear regression
# because it can violate the multi-colinearity assumption

correlation_matrix = my_df.corr()

correlation_matrix_spearman = my_df.corr(method="spearman")

correlation_matrix_kendall = my_df.corr(method="kendall")
