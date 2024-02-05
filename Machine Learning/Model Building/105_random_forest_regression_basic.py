# -*- coding: utf-8 -*-
"""
@author: helen

Random Forest For Regression Basic
"""

# import required packages
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

# read in data
my_df = pd.read_csv("data/sample_data_regression.csv")

# separate input and output data
X = my_df.drop(["output"], axis=1)
y = my_df["output"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# create regression object
regressor = RandomForestRegressor(random_state=42, n_estimators=1000)

# train model
regressor.fit(x_train, y_train)

# test the regressors prediction with r2 score
y_pred = regressor.predict(x_test)
r2_score(y_test, y_pred)

# feature importance

feature_importances = regressor.feature_importances_
feature_importances_df = pd.DataFrame(feature_importances)
feature_names_df = pd.DataFrame(X.columns)

feature_importances_summary = pd.concat(
    [feature_names_df, feature_importances_df], axis=1)
feature_importances_summary.columns = ["input_variable", "feature_importance"]
feature_importances_summary.sort_values(by="feature_importance", inplace=True)

# plot a bar chart
plt.barh(feature_importances_summary["input_variable"],
         feature_importances_summary["feature_importance"])
plt.title(
    f"Feature Importance of Random Forest")
plt.xlabel("Feature Importance")
# plt.ylabel("input_variable")
plt.tight_layout()
plt.show()
