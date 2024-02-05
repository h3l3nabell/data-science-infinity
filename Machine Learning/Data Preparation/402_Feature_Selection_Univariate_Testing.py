# -*- coding: utf-8 -*-
"""
@author: helen

Feature Selection - Univariate Testing
"""
# Regression Template
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression

my_df = pd.read_csv("feature_selection_sample_data.csv")

# separate input and output variables into separate objects
# X = input varables.  Y = output variables

X = my_df.drop(["output"], axis=1)
y = my_df["output"]

feature_selector = SelectKBest(f_regression, k="all")

fit = feature_selector.fit(X, y)

# A lower p value suggests a better confidence that the relationship is robust
# note scientific notation! we have very small values for input 1 & 2
# fit.pvalues_

# f scores - a higher value indicates a stronger relationship
# fit.scores_

# create some dataframes so we can investigate
p_values_df = pd.DataFrame(fit.pvalues_)
f_scores_df = pd.DataFrame(fit.scores_)
input_variable_names = pd.DataFrame(X.columns)

summary_stats = pd.concat(
    [input_variable_names, p_values_df, f_scores_df], axis=1)
# add the column headers
summary_stats.columns = ["input_variable", "p_value", "f_score"]
summary_stats.sort_values(by="p_value", inplace=True)

# select according to a threshold p value

p_value_threshold = 0.05
score_threshold = 5

selected_variables = summary_stats.loc[(
    summary_stats["f_score"] >= score_threshold)
    & (summary_stats["p_value"] <= p_value_threshold)]

selected_variables_list = selected_variables["input_variable"].tolist()

X_best_variables = X[selected_variables_list]

# now we know there are 2 good features! we could see what the original
# selectKBest would have done!  Returns an array
# however, in practice you will rarely know the number of features!
# Therefore will comment this out for our template and use the above!

# feature_selector = SelectKBest(f_regression, k=2)
# fit = feature_selector.fit(X, y)
# X_K_Best_Selected = feature_selector.transform(X)

# to find the columns that were selected
# features_selected = feature_selector.get_support()

# to get our results as a dataframe with columns!
# X_K_Best_Selected_DF = X.loc[:, features_selected]

# Classification Template:

p_values_df = pd.DataFrame(fit.pvalues_)
f_scores_df = pd.DataFrame(fit.scores_)
input_variable_names = pd.DataFrame(X.columns)

summary_stats = pd.concat(
    [input_variable_names, p_values_df, f_scores_df], axis=1)
# add the column headers
summary_stats.columns = ["input_variable", "p_value", "f_score"]
summary_stats.sort_values(by="p_value", inplace=True)

# select according to a threshold p value

p_value_threshold = 0.05
score_threshold = 5

selected_variables = summary_stats.loc[(
    summary_stats["f_score"] >= score_threshold)
    & (summary_stats["p_value"] <= p_value_threshold)]

selected_variables_list = selected_variables["input_variable"].tolist()

X_best_variables = X[selected_variables_list]
