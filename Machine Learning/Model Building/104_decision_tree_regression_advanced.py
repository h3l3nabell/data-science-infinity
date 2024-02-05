# -*- coding: utf-8 -*-
"""
@author: helen

Regression Trees Advanced Template
"""

# import required packages
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import r2_score
from sklearn.utils import shuffle
from sklearn.preprocessing import OneHotEncoder

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
regressor = DecisionTreeRegressor(random_state=42, max_depth=4)

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

# overfitting demo
y_pred_train = regressor.predict(x_train)
r2_score(y_train, y_pred_train)

# finding the best max depth
max_depth_list = list(range(1, 9))
accuracy_scores = []

for depth in max_depth_list:
    regressor = DecisionTreeRegressor(max_depth=depth, random_state=42)
    regressor.fit(x_train, y_train)
    y_pred = regressor.predict(x_test)
    accuracy = r2_score(y_test, y_pred)
    accuracy_scores.append(accuracy)

max_accuracy = max(accuracy_scores)
max_accuracy_idx = accuracy_scores.index(max_accuracy)
optimal_depth = max_depth_list[max_accuracy_idx]

# plot max depth v accuracy
plt.plot(max_depth_list, accuracy_scores)
plt.scatter(optimal_depth, max_accuracy, marker="x", color="red")
plt.title(
    f"Accuracy by Max Depth \n Optimal Tree Depth: {optimal_depth} - Accuracy: {round(max_accuracy, 4)}")
plt.xlabel("Max Depth of Decision Tree")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.show()

# plot the model

plt.figure(figsize=(25, 15))
tree = plot_tree(regressor,
                 feature_names=X.columns,
                 filled=True,
                 rounded=True,
                 fontsize=16)
