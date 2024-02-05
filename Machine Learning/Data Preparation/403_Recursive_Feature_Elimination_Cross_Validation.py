# -*- coding: utf-8 -*-
"""
@author: helen

Feature Selection - Recursive Feature Elimination with Cross Validation
"""
# Classification Template
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LinearRegression
import pandas as pd

my_df = pd.read_csv("feature_selection_sample_data.csv")

# split the output from the data

X = my_df.drop("output", axis=1)
y = my_df["output"]

regressor = LinearRegression()
feature_selector = RFECV(regressor, cv=5)

# Train model using 5 chunks
fit = feature_selector.fit(X, y)

# Once model trained we can find out what the optimal number of variables are,
# and which variables they are

optimal_feature_count = feature_selector.n_features_
print(f"The optimal number of features is: {optimal_feature_count}")

# create some dataframes so we can investigate
f_scores_df = pd.DataFrame(fit.get_feature_names_out())
input_variable_names = pd.DataFrame(X.columns)

X_2 = X.loc[:, feature_selector.get_support()]

plt.plot(range(1, len(fit.cv_results_["mean_test_score"]) + 1),
         fit.cv_results_["mean_test_score"], marker="o")
plt.ylabel = "Model Scores"
plt.xlabel = "Number of Features"
plt.title(
    f"Feature Selection using RFE \n Optimal number of features is {optimal_feature_count} (at score of : {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()
