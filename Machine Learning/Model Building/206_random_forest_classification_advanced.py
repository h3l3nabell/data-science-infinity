# -*- coding: utf-8 -*-
"""
@author: helen

Random Forest for Classification - Advanced Template
"""

# import required packages
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.utils import shuffle
from sklearn.preprocessing import OneHotEncoder
from sklearn.inspection import permutation_importance

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np

# read in data
data_for_model_0_loaded = pd.read_pickle("data/abc_classification_modelling.p")

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

# class balance
data_for_model_3_mvr["signup_flag"].value_counts(normalize=True)

# deal with outliers - we dont need to because dt doesnt care!


# separate input and output data
X = data_for_model_3_mvr.drop(["signup_flag"], axis=1)
y = data_for_model_3_mvr["signup_flag"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)


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
clf = c(random_state=42, n_estimators=500, max_features=5)

# train model
clf.fit(x_train, y_train)

# predict on the test set
y_pred_class = clf.predict(x_test)

# predict the probability that each datapoint will fall into either class
y_pred_prob = clf.predict_proba(x_test)[:, 1]

# confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred_class)

plt.style.available
plt.style.use("seaborn-v0_8-poster")
plt.matshow(conf_matrix, cmap="coolwarm")
plt.gca().xaxis.tick_bottom()
plt.title("Confusion Matrix")
plt.ylabel("Actual Class")
plt.xlabel("Predicted Class")

# center the numbers in the matrix
for (i, j), corr_value in np.ndenumerate(conf_matrix):
    plt.text(j, i, corr_value, ha="center", va="center", fontsize=20)
plt.show()

# Accuracy - the number of correct classification out of all attempts
accuracy_score(y_test, y_pred_class)

# Precision - of all obs prdicted +ve how many were actually +ve
precision_score(y_test, y_pred_class)

# Recall - of all +ve obs how many did we predict as +ve
recall_score(y_test, y_pred_class)

# f1 - harmonic mean of precision and recall
f1_score(y_test, y_pred_class)

# feature importance

feature_importances_df = pd.DataFrame(clf.feature_importances_)
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
    clf, x_test, y_test, n_repeats=10, random_state=42)

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
