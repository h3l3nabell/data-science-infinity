# -*- coding: utf-8 -*-
"""
@author: helen

PCA Advanced Template
"""
######################################
# import required packages
######################################
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

######################################
# read in sample data
######################################
data_for_model_0_loaded = pd.read_csv("data/sample_data_pca.csv")

# drop unnecessary columns
data_for_model_1_cd = data_for_model_0_loaded.drop(
    "user_id", axis=1)


# shuffle data
data_for_model_2_shuffled = shuffle(
    data_for_model_1_cd, random_state=42)

# class balance
data_for_model_2_shuffled["purchased_album"].value_counts(normalize=True)

######################################
# check for missing values
######################################
data_for_model_2_shuffled.isna().sum()
data_for_model_2_shuffled.isna().sum().sum()

data_for_model_3_mvr = data_for_model_2_shuffled.dropna(
    how="any")


######################################
# separate input and output data
######################################
X = data_for_model_3_mvr.drop(["purchased_album"], axis=1)
y = data_for_model_3_mvr["purchased_album"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

######################################
# Feature Scaling
######################################
scale_standard = StandardScaler()

X_train_scaled = scale_standard.fit_transform(x_train)
X_test_scaled = scale_standard.transform(x_test)
######################################
# Apply PCA
######################################
pca = PCA(n_components=None, random_state=42)

# fit the data
pca.fit(X_train_scaled)

# extract the explained variance across components
explained_variance = pca.explained_variance_ratio_
explained_variance_cumulative = pca.explained_variance_ratio_.cumsum()

######################################
# Plot the explained variance across components
######################################
num_vars = list(range(1, 101))
plt.figure(figsize=(15, 10))

# plot variance explained by each component
plt.subplot(2, 1, 1)
plt.bar(num_vars, explained_variance)
plt.title("Variance across Principal Components")
plt.xlabel("Number of Components")
plt.ylabel("% Variance")
plt.tight_layout()

# plot cumulative variance
plt.subplot(2, 1, 2)
plt.bar(num_vars, explained_variance_cumulative)
plt.title("Cumulative Variance across Principal Components")
plt.xlabel("Number of Components")
plt.ylabel("Cumulative % Variance")
plt.tight_layout()
plt.show()

######################################
# Apply PCA with number of components that explains 75%
######################################

pca = PCA(n_components=0.75, random_state=42)

# fit the data
x_train_pca = pca.fit_transform(X_train_scaled)
x_test_pca = pca.transform(X_test_scaled)

pca.n_components_

######################################
# Build Random Forest Classifier with this model
######################################
clf = RandomForestClassifier(random_state=42)
clf.fit(x_train_pca, y_train)


######################################
# Assess Model Accuracy
######################################

y_pred_class = clf.predict(x_test_pca)
accuracy_score(y_test, y_pred_class)
