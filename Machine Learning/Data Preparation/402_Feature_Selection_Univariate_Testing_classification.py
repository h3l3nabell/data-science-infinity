# -*- coding: utf-8 -*-
"""
@author: helen

Feature Selection - Univariate Testing
"""
# Classification Template
import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2

my_df = pd.read_csv("feature_selection_sample_data.csv")

# separate input and output variables into separate objects
# X = input varables.  Y = output variables

X = my_df.drop(["output"], axis=1)
y = my_df["output"]

feature_selector = SelectKBest(chi2, k="all")

fit = feature_selector.fit(X, y)

# create some dataframes so we can investigate
p_values_df = pd.DataFrame(fit.pvalues_)
f_scores_df = pd.DataFrame(fit.scores_)
input_variable_names = pd.DataFrame(X.columns)

summary_stats = pd.concat(
    [input_variable_names, p_values_df, f_scores_df], axis=1)
# add the column headers
summary_stats.columns = ["input_variable", "p_value", "chi2_score"]
summary_stats.sort_values(by="p_value", inplace=True)

# select according to a threshold p value

p_value_threshold = 0.05
score_threshold = 5

selected_variables = summary_stats.loc[(
    summary_stats["chi2_score"] >= score_threshold)
    & (summary_stats["p_value"] <= p_value_threshold)]

selected_variables_list = selected_variables["input_variable"].tolist()

X_best_variables = X[selected_variables_list]
