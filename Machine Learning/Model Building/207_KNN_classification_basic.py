# -*- coding: utf-8 -*-
"""
@author: helen

KNN for Classification Basic
"""

# import required packages
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
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

# create classifier object
clf = KNeighborsClassifier()

# train model
clf.fit(x_train, y_train)

# test the classifier prediction with accuracy score
y_pred = clf.predict(x_test)
accuracy_score(y_test, y_pred)
