# -*- coding: utf-8 -*-
"""
@author: helen

Regression Trees For  Regression Basic
"""

# import required packages
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeRegressor
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
regressor = DecisionTreeRegressor(min_samples_leaf=7)

# train model
regressor.fit(x_train, y_train)

# test the regressors prediction with r2 score
y_pred = regressor.predict(x_test)
r2_score(y_test, y_pred)

# A demonstration of overfitting
y_pred_train = regressor.predict(x_train)
r2_score(y_train, y_pred_train)

# plot decision tree
plt.figure(figsize=(25, 15))
tree = plot_tree(regressor,
                 feature_names=X.columns,
                 filled=True,
                 rounded=True,
                 fontsize=24)
