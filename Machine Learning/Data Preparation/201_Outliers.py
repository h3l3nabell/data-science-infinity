# -*- coding: utf-8 -*-
"""
@author: helen

Outliers should only be removed when absolutely necessary, as in
they are having a detrimental effect on your models predictions.

Boxplot Approach
"""

import pandas as pd

X = pd.DataFrame({"input1": [15, 41, 44, 47, 50, 53, 56, 59, 99],
                  "input2": [29, 41, 44, 47, 50, 53, 56, 59, 66]
                  })

X.plot(kind="box", vert=False)

outlier_columns = ["input1", "input2"]

for column in outlier_columns:
    lower_quartile = X[column].quantile(0.25)
    upper_quartile = X[column].quantile(0.75)
    interquartilerange = upper_quartile - lower_quartile
    iqr_extended = interquartilerange * 1.5
    min_border = lower_quartile - iqr_extended
    max_border = upper_quartile + iqr_extended
    print(f"lower quartile={lower_quartile} and min border={min_border}")
    print(f"upper quartile={upper_quartile} and max border={max_border}")

    outliers = X[(X[column] < min_border) | (X[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    X = X.drop(outliers)

# Standard Deviation Approach
X = pd.DataFrame({"input1": [15, 41, 44, 47, 50, 53, 56, 59, 99],
                  "input2": [29, 41, 44, 47, 50, 53, 56, 59, 66]
                  })

for column in outlier_columns:
    mean = X[column].mean()
    std_dev = X[column].std()
    min_border = mean - std_dev * 3
    max_border = mean + std_dev * 3

    outliers = X[(X[column] < min_border) | (X[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    X.drop(outliers, inplace=True)
