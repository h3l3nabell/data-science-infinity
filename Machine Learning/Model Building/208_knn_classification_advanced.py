# -*- coding: utf-8 -*-
"""
@author: helen

knn for classification ABC Grocery Task
"""
###############################################################
# import required packages
###############################################################
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.utils import shuffle
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.feature_selection import RFECV

###############################################################
# read in data
###############################################################
data_for_model_0_loaded = pd.read_pickle("data/abc_classification_modelling.p")

# drop unnecessary columns
data_for_model_1_cd = data_for_model_0_loaded.drop(
    "customer_id", axis=1)


# shuffle data
data_for_model_2_shuffled = shuffle(
    data_for_model_1_cd, random_state=42)


# class balance
data_for_model_2_shuffled["signup_flag"].value_counts(normalize=True)

###############################################################
# check for missing values
###############################################################

data_for_model_2_shuffled.isna().sum()
data_for_model_3_mvr = data_for_model_2_shuffled.dropna(
    how="any")

###############################################################
# deal with outliers
###############################################################

outlier_investigation = data_for_model_3_mvr.describe()

# from outliers in data prep
outlier_columns = ["distance_from_store",
                   "total_sales", "total_items"]

data_for_model_4_or = data_for_model_3_mvr

# remove outliers
for column in outlier_columns:
    lower_quartile = data_for_model_4_or[column].quantile(
        0.25)
    upper_quartile = data_for_model_4_or[column].quantile(
        0.75)
    interquartilerange = upper_quartile - lower_quartile
    iqr_extended = interquartilerange * 2
    min_border = lower_quartile - iqr_extended
    max_border = upper_quartile + iqr_extended
    print(f"lower quartile={lower_quartile} and min border={min_border}")
    print(f"upper quartile={upper_quartile} and max border={max_border}")
    outliers = data_for_model_4_or[(data_for_model_4_or[column] < min_border) | (
        data_for_model_4_or[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    data_for_model_4_or = data_for_model_4_or.drop(
        outliers)


# separate input and output data
X = data_for_model_4_or.drop(["signup_flag"], axis=1)
y = data_for_model_4_or["signup_flag"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

###############################################################
# deal with categorical variables
###############################################################

categorical_vars = ["gender"]

# Here sparse=False means we return an array rather than a  sparse object
# the drop = first will tell it to drop the first of the encoded values
# this avoids the dummy variable trap - and you dont lose any info for ML - the
# dropped value would have been 1 whenever the others were all zero.
one_hot_encoder = OneHotEncoder(sparse=False, drop="first")

x_train_encoded = one_hot_encoder.fit_transform(x_train[categorical_vars])
x_test_encoded = one_hot_encoder.transform(x_test[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

x_train_encoded = pd.DataFrame(
    x_train_encoded, columns=encoder_feature_names)

# the reset index ensures that no rows are not aligned.
x_train = pd.concat(
    [x_train.reset_index(drop=True), x_train_encoded.reset_index(drop=True)], axis=1)

x_train = x_train.drop(categorical_vars, axis=1)


x_test_encoded = pd.DataFrame(
    x_test_encoded, columns=encoder_feature_names)

# the reset index ensures that no rows are not aligned.
x_test = pd.concat(
    [x_test.reset_index(drop=True), x_test_encoded.reset_index(drop=True)], axis=1)

x_test = x_test.drop(categorical_vars, axis=1)

###############################################################
# Feature Scaling
###############################################################
scale_norm = MinMaxScaler()

x_train = pd.DataFrame(
    scale_norm.fit_transform(x_train), columns=x_train.columns)

x_test = pd.DataFrame(
    scale_norm.transform(x_test), columns=x_test.columns)

###############################################################
# Feature Selection
###############################################################

# we want to use RandomForestClassifier to find the important ones

clf = RandomForestClassifier(random_state=42)
feature_selector = RFECV(clf, cv=5)

# Train model using 5 chunks
fit = feature_selector.fit(x_train, y_train)

# Once model trained we can find out what the optimal number of variables are,
# and which variables they are

optimal_feature_count = feature_selector.n_features_
print(f"The optimal number of features is: {optimal_feature_count}")

# create some dataframes so we can investigate
# f_scores_df = pd.DataFrame(fit.get_feature_names_out())
# input_variable_names = pd.DataFrame(x_test.columns)

x_train = x_train.loc[:, feature_selector.get_support()]
x_test = x_test.loc[:, feature_selector.get_support()]

plt.plot(range(1, len(fit.cv_results_["mean_test_score"]) + 1),
         fit.cv_results_["mean_test_score"], marker="o")
plt.ylabel("Model Scores")
plt.xlabel("Number of Features")
plt.title(
    f"Feature Selection using RFE \n Optimal number of features is {optimal_feature_count} (at score of : {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()

###############################################################
# create classifier object
###############################################################
clf = KNeighborsClassifier()

# train model
clf.fit(x_train, y_train)

###############################################################
# Assess Model Accuracy
###############################################################

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

###############################################################
# Find the optimal value for k
###############################################################
k_list = list(range(2, 25))
accuracy_scores = []

for k in k_list:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    accuracy = f1_score(y_test, y_pred)
    accuracy_scores.append(accuracy)

max_accuracy = max(accuracy_scores)
max_accuracy_idx = accuracy_scores.index(max_accuracy)
optimal_k = k_list[max_accuracy_idx]

# plot max depth v accuracy
plt.plot(k_list, accuracy_scores)
plt.scatter(optimal_k, max_accuracy, marker="x", color="red")
plt.title(
    f"Accuracy (F1 Score) by K \n Optimal value for K: {optimal_k} - Accuracy: {round(max_accuracy, 4)}")
plt.xlabel("K")
plt.ylabel("Accuracy (F1 Score)")
plt.tight_layout()
plt.show()
