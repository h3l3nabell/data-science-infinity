# -*- coding: utf-8 -*-
"""
@author: helen

Random Forest for Regresion Advanced Template
"""

# import required packages
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score
from sklearn.utils import shuffle
from sklearn.preprocessing import OneHotEncoder
from sklearn.inspection import permutation_importance

import pandas as pd
import pickle
import matplotlib.pyplot as plt

# read in data
data_for_model_0_loaded = pickle.load(
    open("data/regression_modelling.p", "rb"))

# drop unnecessary columns
data_for_model_1_cd = data_for_model_0_loaded.drop(
    "customer_id", axis=1)


# shuffle data
data_for_model_2_shuffled = shuffle(
    data_for_model_1_cd, random_state=42)

# check for missing values

data_for_model_2_shuffled.isna().sum()
data_for_model_3_mvr = data_for_model_2_shuffled.dropna(
    how="any")

# deal with outliers - we dont need to because dt doesnt care!


# separate input and output data
X = data_for_model_3_mvr.drop(["customer_loyalty_score"], axis=1)
y = data_for_model_3_mvr["customer_loyalty_score"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# deal with categorical variables - we need them numeric

categorical_vars = ["gender"]

# Here sparse=False means we return an array rather than a  sparse object
# the drop = first will tell it to drop the first of the encoded values
# this avoids the dummy variable trap - and you dont lose any info for ML - the
# dropped value would have been 1 whenever the others were all zero.
one_hot_encoder = OneHotEncoder(sparse=False, drop="first")

x_train_encoded = one_hot_encoder.fit_transform(x_train[categorical_vars])
x_test_encoded = one_hot_encoder.transform(x_test[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

# X-train apply encoded variable to dataframe
x_train_encoded = pd.DataFrame(
    x_train_encoded, columns=encoder_feature_names)

# the reset index ensures that no rows are not aligned.
x_train = pd.concat(
    [x_train.reset_index(drop=True), x_train_encoded.reset_index(drop=True)], axis=1)

x_train = x_train.drop(categorical_vars, axis=1)

# X-test apply encoded variable to dataframe
x_test_encoded = pd.DataFrame(
    x_test_encoded, columns=encoder_feature_names)

# the reset index ensures that no rows are not aligned.
x_test = pd.concat(
    [x_test.reset_index(drop=True), x_test_encoded.reset_index(drop=True)], axis=1)

x_test = x_test.drop(categorical_vars, axis=1)

# Feature Selection - not required for accuracy, but could be good for
# performance if you have a lot of variables


# create regression object
# regressor = RandomForestRegressor(random_state=42,  n_estimators=1000)
regressor = RandomForestRegressor(random_state=42)

# train model
regressor.fit(x_train, y_train)

# predict on the test set
y_pred = regressor.predict(x_test)

# calculate r-squared
r_squared = r2_score(y_test, y_pred)
print(r_squared)

# cross validation
cv = KFold(n_splits=4, shuffle=True, random_state=42)
cv_scores = cross_val_score(regressor, x_train, y_train, cv=cv, scoring="r2")
print(cv_scores.mean())

# caculate adjusted R-squared
num_data_points, num_input_vars = x_test.shape
adjusted_r_squared = 1 - \
    (1 - r_squared) * (num_data_points - 1) / \
    (num_data_points - num_input_vars - 1)
print(adjusted_r_squared)

# feature importance

feature_importances_df = pd.DataFrame(regressor.feature_importances_)
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

# Permutation Importance

result = permutation_importance(
    regressor, x_test, y_test, n_repeats=10, random_state=42)

permutation_importances_df = pd.DataFrame(result["importances_mean"])
permutation_names_df = pd.DataFrame(X.columns)

permutation_importances_summary = pd.concat(
    [permutation_names_df, permutation_importances_df], axis=1)
permutation_importances_summary.columns = [
    "input_variable", "permutation_importance"]
permutation_importances_summary.sort_values(
    by="permutation_importance", inplace=True)

# plot a bar chart
plt.barh(permutation_importances_summary["input_variable"],
         permutation_importances_summary["permutation_importance"])
plt.title(
    f"Permutation Importance of Random Forest")
plt.xlabel("Permutation Importance")
# plt.ylabel("input_variable")
plt.tight_layout()
plt.show()

# predictions under the hood

# look at the predicted loyalty score for the first customer
y_pred[0]
customer1_data = [x_test.iloc[0]]

predictions = []
tree_count = 0
for tree in regressor.estimators_:
    prediction = tree.predict(customer1_data)[0]
    predictions.append(prediction)
    tree_count += 1

# the average prediction is the same as the y_pred[0] we saw at the start
print(predictions)
ave_prediction = sum(predictions) / tree_count

# save objects for later use
pickle.dump(regressor, open("data/random_forest_regressor.p", "wb"))
pickle.dump(one_hot_encoder, open("data/random_forest_regressor_ohe.p", "wb"))
