# -*- coding: utf-8 -*-
"""
@author: helen

Linear Regression Basic
"""

# import required packages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import pandas as pd

# read in data
my_df = pd.read_csv("data\sample_data_regression.csv")

# separate input and output data
X = my_df.drop(["output"], axis=1)
y = my_df["output"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# create regression object
regressor = LinearRegression()

# train model
regressor.fit(x_train, y_train)

# test the regressors prediction with r2 score
y_pred = regressor.predict(x_test)
r2_score(y_test, y_pred)
