# -*- coding: utf-8 -*-
"""
@author: helen

Classification Trees Basic
"""

# import required packages
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# read in data
my_df = pd.read_csv("data/sample_data_classification.csv")

# separate input and output data
X = my_df.drop(["output"], axis=1)
y = my_df["output"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# create regression object
clf = DecisionTreeClassifier(random_state=42, min_samples_leaf=7)

# train model
clf.fit(x_train, y_train)

# test the regressors prediction with r2 score
y_pred = clf.predict(x_test)
accuracy_score(y_test, y_pred)

# A demonstration of overfitting
y_pred_train = clf.predict(x_train)
accuracy_score(y_train, y_pred_train)

# plot decision tree
plt.figure(figsize=(25, 15))
tree = plot_tree(clf,
                 feature_names=X.columns,
                 filled=True,
                 rounded=True,
                 fontsize=24)
